"use strict";

const {strict: assert} = require("assert");

const {zrequire} = require("./lib/namespace");
const {run_test} = require("./lib/test");

const colorspace = zrequire("colorspace");

run_test("sRGB_to_linear", () => {
    let srgb_color = 0.0042;
    let expected_value = 0.0042 / 255 / 12.92;
    let actual_value = colorspace.sRGB_to_linear(srgb_color);
    assert.equal(actual_value, expected_value);

    srgb_color = 255;
    expected_value = 1;
    actual_value = colorspace.sRGB_to_linear(srgb_color);
    assert.equal(actual_value, expected_value);
});

run_test("rgb_luminance", () => {
    const channel = [1, 1, 1];
    const expected_value = 1;
    const actual_value = colorspace.rgb_luminance(channel);
    assert.equal(actual_value, expected_value);
});

run_test("luminance_to_lightness", () => {
    let luminance = 0;
    let expected_value = (116 * 4) / 29 - 16;
    let actual_value = colorspace.luminance_to_lightness(luminance);
    assert.equal(actual_value, expected_value);

    luminance = 1;
    expected_value = 100;
    actual_value = colorspace.luminance_to_lightness(luminance);
    assert.equal(actual_value, expected_value);
});
