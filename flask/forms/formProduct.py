from wwtforms import From, StringField, IntegerField, DecimalField, SelectField, SubmitField, HiddenField,

class formProduct():
    id = HiddenField("id")
    id_category = SelectField("Catégorie", validate_choice=False)
    name = StringField("Nom", [validators.Length(
        min=1, max=2
    )])
