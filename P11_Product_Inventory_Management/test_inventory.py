import pytest

from inventory import (
    apply_discount,
    calculate_total_price,
    check_stock,
    process_order,
)


# --- calculate_total_price ---
def test_total_price_valid():
    assert calculate_total_price(250.50, 4) == 1002.0


def test_total_price_zero_quantity_boundary():
    assert calculate_total_price(100, 0) == 0


def test_total_price_negative_price_rejected():
    with pytest.raises(ValueError):
        calculate_total_price(-10, 2)


def test_total_price_negative_quantity_rejected():
    with pytest.raises(ValueError):
        calculate_total_price(10, -2)


def test_total_price_wrong_types_rejected():
    with pytest.raises(TypeError):
        calculate_total_price("abc", 2)
    with pytest.raises(TypeError):
        calculate_total_price(10, 2.5)


# --- apply_discount ---
def test_discount_valid():
    assert apply_discount(1000, 10) == 900


def test_discount_boundaries():
    assert apply_discount(500, 0) == 500
    assert apply_discount(500, 100) == 0


@pytest.mark.parametrize("percent", [-5, 100.1, 150])
def test_discount_out_of_range_rejected(percent):
    with pytest.raises(ValueError):
        apply_discount(1000, percent)


def test_discount_negative_total_rejected():
    with pytest.raises(ValueError):
        apply_discount(-1000, 10)


# --- check_stock ---
def test_stock_sufficient():
    assert check_stock(10, 5) is True


def test_stock_exact_boundary():
    assert check_stock(5, 5) is True


def test_stock_insufficient():
    assert check_stock(3, 5) is False


def test_stock_zero_requested_rejected():
    with pytest.raises(ValueError):
        check_stock(10, 0)


def test_stock_negative_values_rejected():
    with pytest.raises(ValueError):
        check_stock(10, -1)
    with pytest.raises(ValueError):
        check_stock(-10, 1)


def test_stock_non_integer_rejected():
    with pytest.raises(TypeError):
        check_stock(10, "five")


# --- process_order (exception handling + logging) ---
def test_process_order_success():
    result = process_order("Laptop", 1000, 2, 5, 10)
    assert result == {"product": "Laptop", "status": "in stock", "total": 1800.0}


def test_process_order_out_of_stock():
    result = process_order("Mouse", 500, 10, 4)
    assert result["status"] == "out of stock"


def test_process_order_invalid_input_returns_none():
    assert process_order("Keyboard", 1500, 2, 20, 150) is None


# --- logging ---
def test_warning_logged_when_stock_insufficient(caplog):
    with caplog.at_level("WARNING", logger="inventory"):
        check_stock(1, 5)
    assert "Insufficient stock" in caplog.text


def test_error_logged_for_invalid_input(caplog):
    with caplog.at_level("ERROR", logger="inventory"), pytest.raises(ValueError):
        calculate_total_price(-1, 1)
    assert "cannot be negative" in caplog.text
