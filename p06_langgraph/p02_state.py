# Import NotRequired to mark fields that are populated later.
from typing_extensions import TypedDict, NotRequired

class EmployeeState(TypedDict):

    employee_name: str
    department: str
    experience: int
    salary: float

    validation_status: NotRequired[str]
    annual_salary: NotRequired[float]
    employee_summary: NotRequired[str]
    final_output: NotRequired[str]
