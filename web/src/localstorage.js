import * as blueslip from "./blueslip";

const ls = {
    // check if the datestamp is from before now and if so return true.
    isExpired(stamp) {
        return new Date(stamp) < new Date();
    },

    // return the localStorage key that is bound to a version of a key.
    formGetter(version, name) {
        return "ls__" + version + "__" + name;
    },

    // create a formData object to put in the data, a signature that it was
    // created with this library, and when it expires (if ever).
    formData(data, expires) {
        return {
            data,
            __valid: true,
            expires: Date.now() + expires,
        };
    },

    getData(version, name) {
        const key = this.formGetter(version, name);
        let data;
        try {
            const raw_data = localStorage.getItem(key);
            data = JSON.parse(raw_data);
        } catch {
            // data stays undefined
        }
        if (
            data &&
            data.__valid &&
            // JSON forms of data with `Infinity` turns into `null`,
            // so if null then it hasn't expired since nothing was specified.
            (!ls.isExpired(data.expires) || data.expires === null)
        ) {
            return data;
        }

        return undefined;
    },

    // set the wrapped version of the data into localStorage.
    setData(version, name, data, expires) {
        const key = this.formGetter(version, name);
        const val = this.formData(data, expires);

        localStorage.setItem(key, JSON.stringify(val));
    },

    // remove the key from localStorage and from memory.
    removeData(version, name) {
        const key = this.formGetter(version, name);

        localStorage.removeItem(key);
    },

    // Remove keys which (1) map to a value that satisfies a
    // property tested by `condition_checker` and (2) which match
    // the pattern given by `name`.
    removeDataRegexWithCondition(version, regex, condition_checker) {
        const key_regex = new RegExp(this.formGetter(version, regex));
        let keys = [];
        try {
            keys = Object.keys(localStorage);
        } catch {
            // Do nothing if we fail to fetch the local storage
        }

        keys = keys.filter((key) => key_regex.test(key));

        for (const key of keys) {
            let value;
            let value_set = false;
            try {
                value = localStorage.getItem(key);
                value_set = true;
            } catch {
                // Do nothing if the fetch fails
            }
            if (value_set && condition_checker(value)) {
                try {
                    localStorage.removeItem(key);
                } catch {
                    // Do nothing if deletion fails
                }
            }
        }
    },

    // migrate from an older version of a data src to a newer one with a
    // specified callback function.
    migrate(name, v1, v2, callback) {
        const old = this.getData(v1, name);
        this.removeData(v1, name);

        if (old && old.__valid) {
            const data = callback(old.data);
            this.setData(v2, name, data, Number.POSITIVE_INFINITY);

            return data;
        }

        return undefined;
    },
};

// return a new function instance that has instance-scoped variables.
export const localstorage = function () {
    const _data = {
        VERSION: 1,
        expires: Number.POSITIVE_INFINITY,
        expiresIsGlobal: false,
    };

    const prototype = {
        // `expires` should be a Number that represents the number of ms from
        // now that this should expire in.
        // this allows for it to either be set only once or permanently.
        setExpiry(expires, isGlobal) {
            _data.expires = expires;
            _data.expiresIsGlobal = isGlobal || false;

            return this;
        },

        get(name) {
            const data = ls.getData(_data.VERSION, name);

            if (data) {
                return data.data;
            }

            return undefined;
        },

        set(name, data) {
            if (_data.VERSION !== undefined) {
                ls.setData(_data.VERSION, name, data, _data.expires);

                // if the expires attribute was not set as a global, then
                // make sure to return it back to Infinity to not impose
                // constraints on the next key.
                if (!_data.expiresIsGlobal) {
                    _data.expires = Number.POSITIVE_INFINITY;
                }

                return true;
            }

            return false;
        },

        // remove a key with a given version.
        remove(name) {
            ls.removeData(_data.VERSION, name);
        },

        // Remove keys which (1) map to a value that satisfies a
        // property tested by `condition_checker` AND (2) which
        // match the pattern given by `name`.
        removeDataRegexWithCondition(name, condition_checker) {
            ls.removeDataRegexWithCondition(_data.VERSION, name, condition_checker);
        },

        migrate(name, v1, v2, callback) {
            return ls.migrate(name, v1, v2, callback);
        },
    };

    // set a new master version for the LocalStorage instance.
    Object.defineProperty(prototype, "version", {
        get() {
            return _data.VERSION;
        },
        set(version) {
            _data.VERSION = version;
        },
    });

    return prototype;
};

let warned_of_localstorage = false;

localstorage.supported = function supports_localstorage() {
    try {
        return window.localStorage !== undefined && window.localStorage !== null;
    } catch {
        if (!warned_of_localstorage) {
            blueslip.error(
                "Client browser does not support local storage, will lose socket message on reload",
            );
            warned_of_localstorage = true;
        }
        return false;
    }
};
