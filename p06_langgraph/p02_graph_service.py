from langgraph.graph import StateGraph, START, END

from p02_state import EmployeeState


class EmployeeGraphService:

    def __init__(self):

        self.graph_builder = StateGraph(EmployeeState)

        self.graph_builder.add_node( "validate_employee", self.validate_employee )
        self.graph_builder.add_node( "calculate_salary",  self.calculate_salary  )
        self.graph_builder.add_node( "generate_summary", self.generate_summary )
        self.graph_builder.add_node( "prepare_output",  self.prepare_output )


        self.graph_builder.add_edge( START, "validate_employee")
        self.graph_builder.add_edge( "validate_employee", "calculate_salary")
        self.graph_builder.add_edge( "calculate_salary", "generate_summary")
        self.graph_builder.add_edge( "generate_summary", "prepare_output" )
        self.graph_builder.add_edge( "prepare_output", END )

        self.graph = self.graph_builder.compile()



    # Node 1: Validate employee information.
    def validate_employee(self, state: EmployeeState):

        print("\n[Node 1] Validating employee information...")

        employee_name = state["employee_name"]
        department = state["department"]
        experience = state["experience"]
        salary = state["salary"]

        # Check whether the employee information is valid.
        if (
            employee_name.strip() and department.strip()
            and experience >= 0 and salary >= 0
        ):
            validation_status = "Valid employee information"

        else:
            validation_status = "Invalid employee information"


        print("[Node 1] Validation:", validation_status)

        return { "validation_status": validation_status }


    # Node 2: Calculate annual salary.
    def calculate_salary(self, state: EmployeeState):

        print("\n[Node 2] Calculating annual salary...")

        monthly_salary = state["salary"]
        annual_salary = monthly_salary * 12

        print("[Node 2] Annual salary:", annual_salary)

        return { "annual_salary": annual_salary }



    # Node 3: Generate an employee summary.
    def generate_summary(self, state: EmployeeState):

        print("\n[Node 3] Generating employee summary...")

        employee_name = state["employee_name"]
        department = state["department"]
        experience = state["experience"]
        annual_salary = state["annual_salary"]
        validation_status = state["validation_status"]

        # Generate a summary using the available state information.
        employee_summary = (
            f"Employee {employee_name} works in {department} "
            f"with {experience} years of experience. "
            f"Annual salary is Rs. {annual_salary:,.2f}. "
            f"Validation: {validation_status}."
        )

        print("[Node 3] Employee summary generated.")

        return {  "employee_summary": employee_summary  }



    # Node 4: Prepare the final application output.
    def prepare_output(self, state: EmployeeState):

        print("\n[Node 4] Preparing final output...")

        employee_summary = state["employee_summary"]

        final_output = (
            "EMPLOYEE INFORMATION REPORT\n"
            "---------------------------\n"
            f"{employee_summary}"
        )

        print("[Node 4] Final output prepared.")

        return { "final_output": final_output  }



    # Define a method to execute the employee graph.
    def run_graph(self, employee_data: EmployeeState):

        print("\nStarting employee processing graph...")

        result = self.graph.invoke(employee_data)

        return result
