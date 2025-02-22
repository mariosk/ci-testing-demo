# pylint: disable=import-error

""" Unit Test Cases """
from typing import Any
from typing import SupportsFloat

import pytest
from fastvector.vector import Vector2D


V1 = Vector2D(0, 0)
V2 = Vector2D(-1, 1)
V3 = Vector2D(2.5, -2.5)


####################
#       INIT       #
####################


@pytest.mark.parametrize(
    ("x_axis", "y_axis"),
    (
        (-1, None),
        (1, None),
        (None, 1),
        (None, -1),
    ),
)
def test_init_raises(x_axis: SupportsFloat, y_axis: SupportsFloat) -> None:
    """Test init raises."""
    with pytest.raises(TypeError):
        _ = Vector2D(x_axis, y_axis)


@pytest.mark.parametrize(
    ("x_axis", "y_axis", "exp"),
    (
        (-1, 1, Vector2D(-1, 1)),
        (1, -1, Vector2D(1, -1)),
        (1, 1, Vector2D(1, 1)),
    ),
)
def test_from_values(
    x_axis: SupportsFloat, y_axis: SupportsFloat, exp: Vector2D
) -> None:
    """Test from values."""
    assert exp == Vector2D(x_axis, y_axis)


####################
#     STRINGS      #
####################


def test_repr(capture_stdout: dict) -> None:
    """Test repr."""
    print(repr(Vector2D(1.0, 2.0)))
    assert capture_stdout["stdout"] == "vector.Vector2D(1.0, 2.0)\n"


def test_str(capture_stdout: dict) -> None:
    """Test str."""
    print(str(Vector2D(1.0, 2.0)))
    assert capture_stdout["stdout"] == "(1.0, 2.0)\n"


####################
#   COMPUTATIONS   #
####################


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, Vector2D(-1, 1)),
        (V1, V3, Vector2D(2.5, -2.5)),
        (V3, V2, Vector2D(1.5, -1.5)),
    ),
)
def test_add(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    """Test add."""
    assert lhs + rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, Vector2D(1, -1)),
        (V1, V3, Vector2D(-2.5, 2.5)),
        (V3, V2, Vector2D(3.5, -3.5)),
    ),
)
def test_sub(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    """Test sub."""
    assert lhs - rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    ),
)
def test_mul_vec(lhs: Vector2D, rhs: Vector2D, exp_res: float) -> None:
    """Test mul vec."""
    assert lhs * rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, 2.0, Vector2D(0.0, 0.0)),
        (V2, 2.0, Vector2D(-2.0, 2.0)),
        (V3, 2.0, Vector2D(5.0, -5.0)),
    ),
)
def test_mul_float(lhs: Vector2D, rhs: float, exp_res: Vector2D) -> None:
    """Test mul float."""
    assert lhs * rhs == exp_res


@pytest.mark.parametrize(
    ("rhs", "lhs"),
    (
        (Vector2D(1, 1), None),
        (Vector2D(1, 1), "1"),
    ),
)
def test_mul_raises(rhs: Vector2D, lhs: Any) -> None:
    """Test mul raises."""
    with pytest.raises(TypeError):
        rhs * lhs  # pylint: disable=pointless-statement


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, 2.0, Vector2D(0.0, 0.0)),
        (V2, 2.0, Vector2D(-0.5, 0.5)),
        (V3, 2.0, Vector2D(1.25, -1.25)),
    ),
)
def test_div(lhs: Vector2D, rhs: float, exp_res: Vector2D) -> None:
    """Test div."""
    assert lhs / rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs"), ((Vector2D(0.0, 0.0), Vector2D(0.0, 0.0)),)
)
def test_div_raises(lhs: Vector2D, rhs: float) -> None:
    """Test div raises."""
    with pytest.raises(TypeError):
        lhs / rhs  # pylint: disable=pointless-statement


@pytest.mark.parametrize(
    ("rhs", "lhs"),
    (
        (Vector2D(1, 1), (0, 1)),
        (Vector2D(1, 1), [1, 0]),
    ),
)
def test_operators_raises(rhs: Vector2D, lhs: Vector2D) -> None:
    """Test operators raises."""
    with pytest.raises(TypeError):
        rhs < lhs  # pylint: disable=pointless-statement
    with pytest.raises(TypeError):
        rhs + lhs  # pylint: disable=pointless-statement
    with pytest.raises(TypeError):
        rhs - lhs  # pylint: disable=pointless-statement


@pytest.mark.parametrize(
    ("rhs", "lhs"),
    (
        (Vector2D(0, 0), 0),
        (Vector2D(0, 1), 1),
        (Vector2D(1, 0), 1),
    ),
)
def test_abs(rhs: Vector2D, lhs: SupportsFloat) -> None:
    """Test abs."""
    assert abs(rhs) == lhs


####################
#   COMPARISONS    #
####################


@pytest.mark.parametrize(
    ("lhs", "rhs"),
    (
        (Vector2D(1, 1), (1, 1)),
        (Vector2D(1, 1), [1, 1]),
    ),
)
def test_equality_other_class(lhs: Vector2D, rhs: object) -> None:
    """Test equality."""
    assert lhs != rhs


@pytest.mark.parametrize(
    ("lhs", "rhs"),
    (
        (Vector2D(1, 1), Vector2D(0, 1)),
        (Vector2D(1, 1), Vector2D(1, 0)),
    ),
)
def test_less_than(lhs: Vector2D, rhs: Vector2D) -> None:
    """Test less than."""
    assert rhs < lhs


###################
#   CODEIUM.AI    #
###################


# Divide a vector by a scalar of 0, and verify that a ValueError is raised.
def test_divide_by_scalar_of_0() -> None:
    """Test division by 0."""
    vector = Vector2D(3, 4)
    scalar = 0
    with pytest.raises(ValueError):
        division = vector / scalar
        assert division != 0
