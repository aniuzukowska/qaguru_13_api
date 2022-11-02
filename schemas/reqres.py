from voluptuous import Schema, PREVENT_EXTRA, All, Length, Any

SchemaListUsersData = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

SchemaListUsersSupport = Schema(
    {
        "url": str,
        "text": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

SchemaListUsers = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([SchemaListUsersData], Length(min=1)),
        "support": SchemaListUsersSupport
    },
    required=True,
    extra=PREVENT_EXTRA
)

SchemaCreateUser = Schema(
    {
        "name": str,
        "job": Any(str, None),
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA
)

SchemaUpdateUser = Schema(
    {
        "name": str,
        "job": Any(str, None),
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

SchemaLoginUnsuccessful = Schema(
    {
        "error": str
    },
    required=True,
    extra=PREVENT_EXTRA
)
