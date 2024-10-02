# Business Management System

This Python Flask-based Business Management System offers a comprehensive suite of tools for managing employees, customers, and vendors. It features a robust backend capable of handling payroll processing, inventory management, financial statement generation, and maintaining a history of invoices and purchase orders.

## Features

- **Employee Management**: Add, view, and pay employees.
- **Customer Management**: Add and view customers, and create invoices.
- **Vendor Management**: Add and view vendors, and create purchase orders.
- **Financial Reports**: Generate balance sheets and income statements.
- **Payroll System**: Manage payroll events including automatic tax calculation.
- **Inventory Control**: Manage parts and complete units with functionality to build or purchase inventory.
- **Date Management**: Simulate time progression for financial operations.

## Tech Stack

- **Python**: Flask framework for the backend.
- **HTML/CSS**: For frontend display.
- **Jinja2**: Template engine for rendering HTML dynamically.

## Installation

1. **Clone the repository**
```bash
git clone https://your-repository-url.git
cd your-project-directory
```

2. **Set up a virtual environment (Optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install required packages:**
```bash
pip install flask
```

4. **Environment Variables:**
Create a .env file in the project root directory and add the following:
```
SECRET_KEY=your_secret_key
```

5. **Start the application:**
```bash
python app.py
```

## Usage

- **Home Page**: Access the main page at `http://localhost/`.
- **Navigate using the links to access different functionalities:**
  - `/employees` - Manage employees
  - `/customers` - Manage customers
  - `/vendors` - Manage vendors
  - `/payroll` - Access payroll data
  - `/inventory` - Manage inventory
  - `/balance-sheet` - View the balance sheet
  - `/income-statement` - View the income statement

## Contributing

Feel free to fork the repository and submit pull requests. Before submitting a new pull request, please discuss the change you wish to make via an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries, please open an issue on GitHub.

Make sure to replace placeholders like https://your-repository-url.git and your_secret_key with actual data relevant to your project. This README is designed to give a clear overview of your application’s functionality and provide all the necessary instructions for other developers to get started quickly.
