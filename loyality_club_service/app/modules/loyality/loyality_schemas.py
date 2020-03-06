import marshmallow as ma

class NewEntrySchema():
    user_id = ma.fields.String()
    entry_type = ma.fields.String()
    value = ma.fields.Decimal()

class EntrySchema():
    user_id = ma.fields.String()
    entry_type = ma.fields.String()
    date = ma.fields.DateTime()
    value = ma.fields.Decimal()