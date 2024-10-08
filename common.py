import datetime

class model():
    def __init__(self):
        self.employees_data = []
        self.customers_data = []
        self.vendors_data = []
        self.payroll_data = payroll()
        self.invoice_history = invoices()
        self.purchase_order_history = purchase_orders()
        self.sale_price_per_unit = 4000.00  # Fixed per the example problem
        self.date = current_date()

        self.income_data = income_statement(sales=500000,
                                            cogs=300000,
                                            payroll=20000,
                                            payroll_withholding=5000,
                                            bills=15000,
                                            other_income=10000,
                                            income_taxes=25000)
        self.balance_sheet_data = balance_sheet(cash=2000000,
                                                ar=150000,
                                                inventory_data=inventory(1000),
                                                lands_buildings=1750000,
                                                equipment=50000,
                                                furniture_fixtures=25000,
                                                ap=50000,
                                                notes_payable=100000,
                                                accruals=20000,
                                                mortgage=1500000)
        self.employees_data.append(
            employee('Emily', 'Anderson', '742 Evergreen Terrace', 'Apt 5B', 'Springfield', 'IL', '62704', '123-45-6781', '2', '85000'))
        self.employees_data.append(
            employee('Michael', 'Johnson', '58 Kings Road', 'Suite 12', 'Madison', 'WI', '53703', '234-56-7892', '1', '92000'))
        self.employees_data.append(
            employee('Sophia', 'Brown', '1600 Pennsylvania Ave NW', '', 'Washington', 'DC', '20500', '345-67-8903', '3', '115000'))
        self.employees_data.append(
            employee('David', 'Garcia', '1234 Elm Street', 'Apt 302', 'Austin', 'TX', '78701', '456-78-9014', '1', '78000'))
        self.employees_data.append(
            employee('Olivia', 'Martinez', '789 Maple Avenue', 'Apt 22A', 'San Francisco', 'CA', '94102', '567-89-0125', '0', '120000'))
        self.employees_data.append(
            employee('James', 'Lee', '456 Oak Street', 'Apt 6', 'Portland', 'OR', '97205', '678-90-1236', '2', '68000'))
        self.employees_data.append(
            employee('Ava', 'Wilson', '951 Pine Lane', '', 'Chicago', 'IL', '60605', '789-01-2347', '1', '98000'))
        
        self.customers_data.append(customer('Microcenter', 'Smith', 'John', '123 Technology Blvd', 'Suite 200', 'Columbus', 'OH', '43215', '2500.00'))
        self.customers_data.append(customer('Best Buy', 'Johnson', 'Emily', '7601 Penn Ave S', '', 'Richfield', 'MN', '55423', '3000.00'))
        self.customers_data.append(customer('Newegg', 'Lee', 'Kevin', '17708 Rowland St', '', 'City of Industry', 'CA', '91748', '3500.00'))
        self.customers_data.append(customer('Amazon', 'Brown', 'Olivia', '410 Terry Ave N', '', 'Seattle', 'WA', '98109', '5000.00'))
        self.customers_data.append(customer('Walmart', 'Davis', 'James', '702 SW 8th St', '', 'Bentonville', 'AR', '72716', '4500.00'))
        self.customers_data.append(customer('Target', 'Martinez', 'Sophia', '1000 Nicollet Mall', '', 'Minneapolis', 'MN', '55403', '4000.00'))
        self.customers_data.append(customer('Computer World', 'Garcia', 'David', '789 IT Park Ave', '', 'San Jose', 'CA', '95110', '2200.00'))
        self.customers_data.append(customer('Rakuten', 'Wilson', 'Ava', '215 2nd St', 'Suite 400', 'San Francisco', 'CA', '94105', '2800.00'))
        self.customers_data.append(customer('BestPCNow', 'Clark', 'Michael', '456 PC Lane', 'Apt 12B', 'Austin', 'TX', '78701', '2700.00'))
        
        self.vendors_data.append(vendor('AMD Inc.', 'CPU', '320.00', '1 AMD Place', '', 'Santa Clara', 'CA', '95054'))
        self.vendors_data.append(vendor('AsusTek Computer Inc.', 'Motherboard', '140.00', '15 Li-Te Road', 'Beitou District', 'Taipei', '', '112'))
        self.vendors_data.append(vendor('Corsair Components', 'RAM', '85.00', '47100 Bayside Pkwy', '', 'Fremont', 'CA', '94538'))
        self.vendors_data.append(vendor('NVIDIA Corporation', 'GPU', '700.00', '2788 San Tomas Expy', '', 'Santa Clara', 'CA', '95051'))
        self.vendors_data.append(vendor('Samsung Electronics', 'SSD', '110.00', '129 Samsung-ro', 'Yeongtong-gu', 'Suwon-si', 'Gyeonggi-do', '16677'))
        self.vendors_data.append(vendor('Fractal Design', 'PC Case', '89.99', 'Fractal Design USA', '2400 North Commerce Pkwy', 'Weston', 'FL', '33326'))
        self.vendors_data.append(vendor('Noctua', 'CPU Cooler', '60.00', 'Kundenservice Noctua', 'Kottingbrunn', '', 'Austria', '2542'))
        self.vendors_data.append(vendor('Seasonic Electronics', 'Power Supply', '120.00', '14F, No.136, Sec.3, Ren Ai Rd.', '', 'Taipei', '', '106'))
        self.vendors_data.append(vendor('BoxCo Packaging', 'Shipping Box', '2.50', '300 Packaging Dr.', '', 'Atlanta', 'GA', '30301'))
        self.vendors_data.append(vendor('Tech Labor Inc.', 'Labor', '50.00', '600 Industry Way', '', 'Chicago', 'IL', '60616'))
        self.vendors_data.append(vendor('FoamWorks', 'Packaging Foam', '1.25', '220 Foam Ave', '', 'Dallas', 'TX', '75201'))
        self.vendors_data.append(vendor('Cable Solutions', 'Cables', '0.50', '440 Cable St', '', 'San Jose', 'CA', '95112'))
        self.vendors_data.append(vendor('Cooling Fans Co.', 'Cooling Fans', '12.99', '678 Fan Drive', '', 'Portland', 'OR', '97205'))

    def reinitialize(self):
        self.__init__()

class current_date():
    def __init__(self):
        self._date = datetime.date.today()
        self.months_advanced = 0

    def advance_a_month(self):
        self.months_advanced += 1
        # Settle payables and receivables
        model_instance = model()  # Assuming you have an instance to access
        self.settle_payables_and_receivables(model_instance)

    def settle_payables_and_receivables(self, model_instance):
        current_date = self.date
        # Settle Accounts Payable
        for po in model_instance.purchase_order_history.po_events:
            if not po.settled and po.due_date <= current_date:
                model_instance.balance_sheet_data.ap -= po.total
                model_instance.balance_sheet_data.cash -= po.total
                po.settled = True

        # Settle Accounts Receivable
        for invoice in model_instance.invoice_history.invoice_events:
            if not invoice.settled and invoice.due_date <= current_date:
                model_instance.balance_sheet_data.ar -= invoice.total
                model_instance.balance_sheet_data.cash += invoice.total
                invoice.settled = True

    @property
    def date(self):
        delta = datetime.timedelta(self.months_advanced * 365 / 12)
        return (datetime.date.today() + delta).isoformat()

class employee():
    def __init__(self, firstname, lastname, address1, address2,
                 city, state, zipcode, ssn, witholdings, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.ssn = ssn
        self.witholdings = int(witholdings)
        self.salary = float(salary)

class customer():
    def __init__(self, companyname, firstname, lastname, address1, address2,
                 city, state, zipcode, price):
        self.companyname = companyname
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.price = float(price)

class vendor():
    def __init__(self, companyname, part, price_per_unit, address1, address2, city,
                 state, zipcode):
        self.companyname = companyname
        self.part = part
        self.price_per_unit = float(price_per_unit)
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode

class payroll():
    def __init__(self, todal_dispursement=0, total_witholdings=0):
        self.payroll_events = []
        self.total_dispursement = todal_dispursement
        self.total_witholdings = total_witholdings

    def add_payroll_event(self, event):
        self.payroll_events.append(event)
        self.total_dispursement += event.dispursement
        self.total_witholdings += event.witholdings
        return self.total_dispursement + self.total_witholdings

class payroll_event():
    def __init__(self, employee, date_paid, bounce=0):
        self.lastname = employee.lastname
        self.date_paid = date_paid
        self.bounce = bounce
        self.salary = employee.salary/12.0
        self.federal_tax = 1559.45 + (self.salary - 7850) * 0.28
        self.state_tax = self.salary * 0.0495
        self.social_sec_tax = self.salary * 0.062
        self.medicare_tax = self.salary * 0.0145
        self.dispursement = self.salary - self.witholdings

    @property
    def witholdings(self):
        return self.federal_tax + self.state_tax + self.social_sec_tax + self.medicare_tax

class part():
    def __init__(self, price_per_unit, quantity, bom_qty):
        self.price_per_unit = float(price_per_unit)
        self.quantity = int(quantity)
        self.bom_qty = int(bom_qty)

    @property
    def value(self):
        return self.price_per_unit * self.quantity

    @property
    def re_order(self):
        if self.quantity < 100:
            return 'X'
        return ''

class inventory():
    def __init__(self, complete_units):
        self.parts = {}
        self.parts['CPU'] = part('200.00', '142', 1)
        self.parts['Motherboard'] = part('100.00', '59', 1)
        self.parts['GPU'] = part('400.00', '32', 1)
        self.parts['RAM'] = part('25.00', '245', 2)
        self.parts['SSD'] = part('85.00', '42', 2)
        self.parts['Case'] = part('43.99', '531', 1)
        self.parts['CPU Cooler'] = part('15.00', '600', 1)
        self.parts['Power Supply'] = part('73.45', '234', 1)
        self.parts['Box'] = part('1.85', '1100', 1)
        self.parts['Foam'] = part('0.58', '4231', 3)
        self.parts['Labor'] = part('45.00', '50000', 1)
        self.parts['Cables'] = part('0.13', '100000', 5)
        self.parts['Fans'] = part('2.49', '4233', 3)
        self.complete_units = complete_units
        
    def units_possible_to_build(self):
        units_possible = [p.quantity / p.bom_qty for name, p in self.parts.items()]
        if units_possible:
            return min(units_possible)
        else:
            return 0

    def purchase_part(self, part_name, additional_qty):
        self.parts[part_name].quantity += additional_qty

    def purchase_complete_unit(self, qty):
        self.complete_units -= qty
        
    def build_complete_unit(self, qty):
        units_to_build = min(self.units_possible_to_build(), qty)
        for name, p in self.parts.items():
            self.parts[name].quantity -= units_to_build * p.bom_qty
        self.complete_units += units_to_build

    @property
    def cog_per_unit(self):
        count = 0
        for name, p in self.parts.items():
            count += p.price_per_unit * p.bom_qty
        return count

    @property
    def total(self):
        count = 0
        for name, p in self.parts.items():
            count += p.value
        return count

    @property
    def complete_units_to_build(self):
        return self.units_possible_to_build()

    @property
    def complete_units_cost(self):
        return self.complete_units * self.cog_per_unit

class purchase_orders():
    def __init__(self):
        self.po_events = []
        self.po_number = 1

    def create_po(self, supplier, part, quantity, price_per_unit, total, date_paid):
        new_po = purchase_order(self.po_number, supplier, part, quantity, price_per_unit, total, date_paid)
        self.po_events.append(new_po)
        self.po_number += 1
        # Initial impact on AP
        model_instance = model()  # Assuming you have an instance to access
        model_instance.balance_sheet_data.ap += total

class purchase_order():
    def __init__(self, number, supplier, part, quantity, price_per_unit, total, date_paid):
        self.number = number
        self.supplier = supplier
        self.part = part
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total = total

        # Convert date_paid from string to datetime.date if it's a string
        if isinstance(date_paid, str):
            date_paid = datetime.datetime.strptime(date_paid, "%Y-%m-%d").date()

        # Calculate the due date
        self.date_paid = date_paid
        self.due_date = (date_paid + datetime.timedelta(days=30)).isoformat()  # 30-day payable term
        self.settled = False

class invoices():
    def __init__(self):
        self.invoice_events = []
        self.invoice_number = 1001

    def create_invoice(self, customer, quantity, price_per_unit, total, date_paid):
        new_invoice = invoice(self.invoice_number, customer, quantity, price_per_unit, total, date_paid)
        self.invoice_events.append(new_invoice)
        self.invoice_number += 1
        # Initial impact on AR
        model_instance = model()  # Assuming you have an instance to access
        model_instance.balance_sheet_data.ar += total

class invoice():
    def __init__(self, number, customer, quantity, price_per_unit, total, date_paid):
        self.number = number
        self.customer = customer
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total = total

        # Convert date_paid from string to datetime.date if it's a string
        if isinstance(date_paid, str):
            date_paid = datetime.datetime.strptime(date_paid, "%Y-%m-%d").date()

        # Calculate the due date
        self.date_paid = date_paid
        self.due_date = (date_paid + datetime.timedelta(days=30)).isoformat()  # 30-day receivable term
        self.settled = False

class income_statement():
    def __init__(self, sales, cogs, payroll, payroll_withholding, bills,
                 other_income, income_taxes):
        self.sales = sales
        self.cogs = cogs
        self.payroll = payroll
        self.payroll_withholding = payroll_withholding
        self.bills = bills
        self.expense_accounts = monthly_expenses(maintenance=1250*2,
                                                 cleaning=416.67*2,
                                                 water=416.67*2,
                                                 sewage=833.33*2,
                                                 electricity=1250*2,
                                                 travel=833.33*2,
                                                 donuts=416.67*2,
                                                 gas=1250*2,
                                                 internet=833.33*2,
                                                 phone=833.33*2)
        self.other_income = other_income
        self.income_taxes = income_taxes

    @property
    def annual_expenses(self):
        return self.expense_accounts.total_expenses * 12

    @property
    def gross_profit(self):
        return self.sales - self.cogs

    @property
    def expenses(self):
        return self.payroll + self.bills + self.annual_expenses

    @property
    def operating_income(self):
        return self.gross_profit - self.expenses

    @property
    def net_income(self):
        return self.operating_income - self.income_taxes + self.other_income

class balance_sheet():
    def __init__(self, cash, ar, inventory_data, lands_buildings, equipment, furniture_fixtures,
                 ap, notes_payable, accruals, mortgage):
        self.cash = cash
        self.ar = ar
        self.lands_buildings = lands_buildings
        self.equipment = equipment
        self.furniture_fixtures = furniture_fixtures
        self.ap = ap
        self.notes_payable = notes_payable
        self.accruals = accruals
        self.mortgage = mortgage
        self.inventory_data = inventory_data

    @property
    def total_current_assets(self):
        return self.cash + self.ar + self.inventory_data.total

    @property
    def total_fixed_assets(self):
        return self.lands_buildings + self.equipment + self.furniture_fixtures

    @property
    def total_assets(self):
        return self.total_current_assets + self.total_fixed_assets

    @property
    def total_current_liabilities(self):
        return self.ap + self.notes_payable + self.accruals

    @property
    def total_long_term_debt(self):
        return self.mortgage

    @property
    def total_liabilities(self):
        return self.total_current_liabilities + self.total_long_term_debt

    @property
    def net_worth(self):
        return self.total_assets - self.total_liabilities

class monthly_expenses():
    def __init__(self, maintenance, cleaning, water, sewage, electricity, travel, donuts, gas, internet, phone):
        self.maintenance = maintenance
        self.cleaning = cleaning
        self.water = water
        self.sewage = sewage
        self.electricity = electricity
        self.travel = travel
        self.donuts = donuts
        self.gas = gas
        self.internet = internet
        self.phone = phone
        self.total_expenses = self.total_monthly_expenses

    @property
    def total_monthly_expenses(self):
        return self.maintenance + self.cleaning + self.water + self.sewage + self.electricity + self.travel + self.donuts + self.gas + self.internet + self.phone