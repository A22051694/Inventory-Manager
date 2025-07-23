# Inventory-Manager
Inventory Manager with REST API — manage product stock and track customer orders using Django backend and HTML/Tailwind frontend with secure login.


---

## 📦 Product Fields

| Field Name         | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `name`             | Name of the product (e.g., "Laptop", "Book")             |
| `description`      | Optional short text about the product                    |
| `price`            | Price (as a decimal or float)                            |
| `stock_quantity`   | Current available units in stock                         |
| `created_at`       | Timestamp when product was added                         |
| `updated_at`       | Timestamp when product was last updated                  |
| `is_active`        | Boolean to soft-delete or hide product (optional)        |
| `owner` (optional) | User who added the product (for user-specific inventory) |

---

## 📦 Order Fields

| Field Name      | Description                                                     |
| --------------- | --------------------------------------------------------------- |
| `product`       | Link to the product being ordered                               |
| `quantity`      | How many units of the product ordered                           |
| `customer_name` | Name of the person placing the order                            |
| `status`        | Current order status (e.g., "Pending", "Delivered", "Canceled") |
| `created_at`    | Timestamp when the order was placed                             |
| `updated_at`    | Timestamp when the order was last modified                      |
| `placed_by`     | User who placed the order (if using Django auth)                |

---

## ✅ Optional Future Plana (Admin/User Role-Based Logic)

* Plan Use `request.user.is_staff` to allow admin-only edits/cancellations.
* Plan to Add soft-delete (`is_canceled`) or a delivery flag (`is_delivered`) if needed.


