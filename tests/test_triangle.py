# src/test_triangle.py
"""Unit test suite for the triangle module.

Includes tests for:
- is_triangle(a, b, c) - checking if three sides can form a triangle,
- triangle_area(a, b, c) - computing area using Heron's formula,
- triangle_perimeter(a, b, c) - computing perimeter of a triangle,
- handling of invalid inputs (zero, negative, NaN, inf, strings),
- integration with pytest-html for enhanced HTML reports.
"""

import pytest
from pytest_html import extras as html_extras
import triangle as t


# -------------------------------------------------------------------------------------
# TRIANGLE VALIDITY TESTS
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (2, 3, 4, True),
        (5.1, 5.1, 5.1, True),
        (-1, 1, 1, False),
        (1, 1, 0, False),
        (-1, -1, -1, False),
        (0, 0, 0, False),
        ("a", 2, 3, False),
        (1, 2, float("inf"), False),
        (float("nan"), 10, 10, False),
        (1e6, 1e7, 1e8, False),
    ],
    ids=[
        "valid scalene", "equilateral", "negative side", "one zero",
        "all negative", "all zero", "string input",
        "infinite side", "NaN input", "too large sides",
    ]
)
def test_is_triangle(a, b, c, expected, record_property, extras):
    """Tests is_triangle() for valid, invalid, and edge case inputs."""

    result = t.is_triangle(a, b, c)
    record_property("a", a)
    record_property("b", b)
    record_property("c", c)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(
    f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
    f"<b>Sides ({a}, {b}, {c}) {'form' if result else 'do not form'} a triangle.</b><br>"
    f"Result: {result}<br>"
    f"Expected: {expected}</div>"
    ))

    assert result == expected


# -------------------------------------------------------------------------------------
# TRIANGLE AREA TESTS
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 3, 3, 3.89711),
        (5.1, 5.1, 5.1, 11.26266),
        (10, 1, 1, 0),
        (0, 0, 0, 0),
        (-1, 1, 0, 0),
        ("a", 2, 3, 0),
        (1, 2, float("inf"), 0),
        (float("nan"), 10, 10, 0),
        (1e6, 1e7, 1e8, 0),
    ],
)
def test_triangle_area(a, b, c, expected, record_property, extras):
    """Tests triangle_area() for valid and invalid triangles using Heron's formula."""

    result = round(t.triangle_area(a, b, c), 5)
    record_property("a", a)
    record_property("b", b)
    record_property("c", c)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(
    f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
    f"<b>Sides ({a}, {b}, {c}) give the area {result}.</b><br>"
    f"Result: {result}<br>"
    f"Expected: {expected}</div>"
    ))

    assert result == pytest.approx(expected)


# -------------------------------------------------------------------------------------
# TRIANGLE PERIMETER TESTS
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 3, 3, 9),
        (3.1, 4.1, 5.1, 12.3),
        (10, 1, 1, 0),
        (0, 0, 0, 0),
        (-1, 1, 0, 0),
        ("a", 2, 3, 0),
        (1, 2, float("inf"), 0),
        (float("nan"), 10, 10, 0),
        (1e6, 1e7, 1e8, 0),
    ],
)
def test_triangle_perimeter(a, b, c, expected, record_property, extras):
    """Tests triangle_perimeter() for valid and invalid triangles."""

    result = t.triangle_perimeter(a, b, c)
    record_property("a", a)
    record_property("b", b)
    record_property("c", c)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(
    f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
    f"<b>Sides ({a}, {b}, {c}) {f'give {result} perimeter.' if result != 0 else 'do not form a triangle.'} </b><br>"
    f"Result: {result}<br>"
    f"Expected: {expected}</div>"
    ))

    assert result == pytest.approx(expected)
