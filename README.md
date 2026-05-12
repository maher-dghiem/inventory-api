Inventory API:
A clean and scalable Inventory Management API built with Django REST Framework.
It manages categories, suppliers, products, and stock movements, with full support for filtering, ordering, and search.

-----------

Features:
Category management (CRUD)

Supplier management (CRUD)

Product management with category & supplier relations

Stock movement tracking (IN / OUT)

Automatic quantity updates

Filtering, ordering, and search

-----------
Permissions:
Authenticated staff users can create and modify data

Unauthenticated and not staff users have read‑only access

-----------

Main Endpoints:
/categories/

/suppliers/

/products/

/movements/

Supports:
?search= • ?ordering= • ?category_id=
