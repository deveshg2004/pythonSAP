from pydantic import BaseModel
from pydantic import Field

class EmployeeProfile(BaseModel):

    name: str = Field(
        description="Full name of the employee"
    )

    department: str = Field(
        description="Department in which the employee works"
    )

    experience_years: int = Field(
        description="Total years of professional experience"
    )

    skills: list[str] = Field(
        description="List of technical skills possessed by the employee"
    )