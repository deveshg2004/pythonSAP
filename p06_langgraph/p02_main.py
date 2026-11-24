from p02_graph_service import EmployeeGraphService

def main():

    employee_name = input("\nEnter employee name: ")
    department = input("Enter department: ")
    experience = int(input("Enter years of experience: "))
    salary = float(input("Enter monthly salary: "))

    # Prepare the initial graph state.
    employee_data = {
        "employee_name": employee_name,
        "department": department,
        "experience": experience,
        "salary": salary
    }

    # Create an instance of the employee graph service.
    employee_service = EmployeeGraphService()

    # Execute the LangGraph application.
    result = employee_service.run_graph(employee_data)

    print("Validation Status :", result["validation_status"])
    print("Annual Salary     :", result["annual_salary"])

    print("\n" + result["employee_summary"])
    print("\n" + result["final_output"])
    print("\nGraph execution completed successfully.")


if __name__ == "__main__":
    main()
