from rest_framework.schemas import ManualSchema
from rest_framework.compat import coreapi, coreschema


class AccountsSchema(ManualSchema):
    def __init__(self):
        """
        Parameters:

        * `fields`: list of `coreapi.Field` instances.
        * `description`: String description for view. Optional.
        """
        fields = [
            coreapi.Field(
                name="card_number",
                required=False,
                location="form",
                schema=coreschema.String(title="Card number", description="Enter a card number")
            )
        ]
        encoding = "application/json"
        super(ManualSchema, self).__init__()
        assert all(isinstance(f, coreapi.Field) for f in fields), "`fields` must be a list of coreapi.Field instances"
        self._fields = fields
        self._description = "Find an account by card number"
        self._encoding = encoding
