from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

'''flask_form = FlaskForm
string_field = StringField
submit_field = SubmitField'''

'''def init_app(app):
    FlaskForm.init_app(app)
    StringField.init_app(app)
    SubmitField.init_app(app)

    #initalisig all three might be bad practice!!'''


'''It is not necessary to define a custom instance of an extension in every application, but it can be useful in some cases.

If an extension requires configuration parameters that are specific to a particular application, it can be beneficial to create a custom instance of the extension and pass those parameters to it during initialization. This allows you to configure the extension differently for different applications.

On the other hand, some extensions do not require any application-specific configuration and can be used with the default instance provided by the extension itself. In such cases, creating a custom instance is not necessary.

In general, it is up to the developer to decide whether a custom instance of an extension is necessary for their specific use case.'''