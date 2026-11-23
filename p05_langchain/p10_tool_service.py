# Import the tool decorator from LangChain.
from langchain_core.tools import tool


# Create a tool to calculate annual salary.
@tool
def calculate_salary(monthly_salary: float) -> float:
    """Calculate annual salary using the monthly salary."""
    annual_salary = monthly_salary * 12
    return annual_salary


# Create a tool to calculate an employee bonus.
@tool
def calculate_bonus(monthly_salary: float, bonus_percentage: float) -> float:
    """Calculate employee bonus using monthly salary and bonus percentage."""
    annual_salary = monthly_salary * 12
    bonus = annual_salary * bonus_percentage / 100
    return bonus


# Create a tool to retrieve an employee's leave balance.
@tool
def get_leave_balance(employee_id: str) -> str:
    """Get the available leave balance for an employee using employee ID."""
    leave_records = {
        "EMP101": 12,
        "EMP102": 8,
        "EMP103": 15
    }

    # Search for the employee ID.
    if employee_id in leave_records:

        return f"{leave_records[employee_id]} leave days available."

    return "Employee ID not found."


# Create a tool to retrieve employee details.
@tool
def get_employee_details(employee_id: str) -> str:
    """Retrieve employee name and department using employee ID."""

    # Create sample employee records.
    employees = {
        "EMP101": {
            "name": "Arun",
            "department": "Python Development"
        },
        "EMP102": {
            "name": "Priya",
            "department": "Human Resources"
        },
        "EMP103": {
            "name": "Kumar",
            "department": "Data Science"
        }
    }

    # Check whether the employee ID exists.
    if employee_id in employees:

        # Retrieve the employee record.
        employee = employees[employee_id]

        # Return employee information.
        return (
            f"Name: {employee['name']}, "
            f"Department: {employee['department']}"
        )

    # Return a message if the employee does not exist.
    return "Employee ID not found."



# Create a list containing all available tools.
employee_tools = [
    calculate_salary,
    calculate_bonus,
    get_leave_balance,
    get_employee_details
]