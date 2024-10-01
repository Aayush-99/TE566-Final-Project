from wtforms import Form, StringField, SelectField, validators

# Common validator for required fields
required = [validators.input_required()]

# Employee Form
class EmployeeForm(Form):
    firstname = StringField('First Name', validators=required)
    lastname = StringField('Last Name', validators=required)
    address1 = StringField('Address 1', validators=required)
    address2 = StringField('Address 2', validators=[validators.optional()])
    city = StringField('City', validators=required)
    state = StringField('State', validators=required)
    zipcode = StringField('Zip Code', validators=required)
    ssn = StringField('Social Security Number (numbers only)', validators=required)
    witholdings = StringField('Witholdings', validators=required)
    salary = StringField('Salary (Dollars)', validators=required)

# Customer Form
class CustomerForm(Form):
    companyname = StringField('Company Name', validators=required)
    firstname = StringField('First Name', validators=required)
    lastname = StringField('Last Name', validators=required)
    address1 = StringField('Address 1', validators=required)
    address2 = StringField('Address 2', validators=[validators.optional()])
    city = StringField('City', validators=required)
    state = StringField('State', validators=required)
    zipcode = StringField('Zip Code', validators=required)
    price = StringField('Price (Dollars)', validators=required)

# Vendor Form
class VendorForm(Form):
    companyname = StringField('Company Name', validators=required)
    part = StringField('Part', validators=required)
    price_per_unit = StringField('Price/Unit (Dollars)', validators=required)
    address1 = StringField('Address 1', validators=required)
    address2 = StringField('Address 2', validators=[validators.optional()])
    city = StringField('City', validators=required)
    state = StringField('State', validators=required)
    zipcode = StringField('Zip Code', validators=required)

# Employee Payment Form
class EmployeePaymentForm(Form):
    employee = SelectField('Employee')

# Purchase Order Form
class POForm(Form):
    part = SelectField('Part')
    quantity = StringField('Quantity', validators=required)

# Invoice Form
class InvoiceForm(Form):
    customer = SelectField('Customer')
    number_to_invoice = StringField('Number of Units to Invoice', validators=required)

# Build Inventory Form
class BuildInventoryForm(Form):
    quantity = StringField('Quantity', validators=required)