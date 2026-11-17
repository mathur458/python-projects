"""Product Inventory Management System.

Provides price calculation, discount calculation and stock availability
checks with input validation, exception handling and logging.
"""

import logging
from numbers import Real

LOG_FILE = "application.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

logger = logging.getLogger("inventory")
logger.setLevel(logging.DEBUG)

if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
    _file_handler = logging.FileHandler(LOG_FILE)
    _file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(_file_handler)


def _validate_number(value, name):
    """Ensure value is a real number (not bool) and not negative."""
    if isinstance(value, bool) or not isinstance(value, Real):
        logger.error("%s must be a number, got %r", name, value)
        raise TypeError(f"{name} must be a number")
    if value < 0:
        logger.error("%s cannot be negative, got %s", name, value)
        raise ValueError(f"{name} cannot be negative")


def _validate_quantity(value, name):
    """Ensure value is a whole number (not bool) and not negative."""
    if isinstance(value, bool) or not isinstance(value, int):
        logger.error("%s must be an integer, got %r", name, value)
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        logger.error("%s cannot be negative, got %s", name, value)
        raise ValueError(f"{name} cannot be negative")


def calculate_total_price(price, quantity):
    """Return the total price for `quantity` units at `price` each."""
    logger.debug("Calculating total price: price=%s, quantity=%s", price, quantity)
    _validate_number(price, "Price")
    _validate_quantity(quantity, "Quantity")

    if quantity == 0:
        logger.warning("Quantity is zero; total price will be 0")

    total = round(price * quantity, 2)
    logger.info("Total price calculated: %s", total)
    return total


def apply_discount(total, discount_percent):
    """Return the amount payable after applying `discount_percent` to `total`."""
    logger.debug("Applying discount: total=%s, discount=%s%%", total, discount_percent)
    _validate_number(total, "Total")
    _validate_number(discount_percent, "Discount percent")

    if discount_percent > 100:
        logger.error("Discount percent must be 0-100, got %s", discount_percent)
        raise ValueError("Discount percent must be between 0 and 100")

    if discount_percent == 0:
        logger.warning("Discount is 0%; no discount applied")

    discounted = round(total - (total * discount_percent / 100), 2)
    logger.info("Discount applied: %s -> %s", total, discounted)
    return discounted


def check_stock(available_stock, requested_quantity):
    """Return True if `requested_quantity` can be fulfilled, else False."""
    logger.debug(
        "Checking stock: available=%s, requested=%s",
        available_stock,
        requested_quantity,
    )
    _validate_quantity(available_stock, "Available stock")
    _validate_quantity(requested_quantity, "Requested quantity")

    if requested_quantity == 0:
        logger.error("Requested quantity must be at least 1")
        raise ValueError("Requested quantity must be at least 1")

    if requested_quantity > available_stock:
        logger.warning(
            "Insufficient stock: requested %s, only %s available",
            requested_quantity,
            available_stock,
        )
        return False

    logger.info("Stock available for requested quantity %s", requested_quantity)
    return True


def process_order(product_name, price, quantity, available_stock, discount_percent=0):
    """Run a full product check and return a result dictionary.

    Exceptions from the helper functions are caught here so one bad order
    does not crash the application. Returns None if the order is invalid.
    """
    logger.info("Product check started: %s", product_name)
    try:
        if not check_stock(available_stock, quantity):
            return {"product": product_name, "status": "out of stock", "total": 0}
        total = calculate_total_price(price, quantity)
        payable = apply_discount(total, discount_percent)
    except (TypeError, ValueError) as error:
        logger.error("Order for %s failed: %s", product_name, error)
        print(f"Error processing {product_name}: {error}")
        return None

    logger.info("Order for %s processed successfully: %s", product_name, payable)
    return {"product": product_name, "status": "in stock", "total": payable}


def main():
    """Demonstrate the inventory functions with sample products."""
    samples = [
        ("Laptop", 55000, 2, 5, 10),
        ("Mouse", 500, 10, 4, 0),
        ("Keyboard", 1500, -1, 20, 5),
        ("Monitor", 12000, 1, 3, 150),
    ]
    for name, price, quantity, stock, discount in samples:
        result = process_order(name, price, quantity, stock, discount)
        print(result)


if __name__ == "__main__":
    main()
