from flask import Flask, request, jsonify
from data_preparation import data_cleaning_preparation

app = Flask(__name__)




df = data_cleaning_preparation()
def Calculate_average_salary_per_department():
    """ Calculate the average salary per department.
    
    input:
    output: 
    """
    average = df.groupby('Department')['Salary'].mean()
    return average

    
@app.route('/highest_paid_employees/<int:k>')
def find_top_highest_paid_employees(k):
    """ Findthe top 3 highest paid employees.
    
    input:
    output: 
    """
    top_highest_k_paid_employees = df.sort_values(by='Salary', ascending=False).head(k)
    
    return jsonify(top_highest_k_paid_employees.to_json())
    
@app.route('/number_employees_in_department/<department>')
def get_number_employees_per_department(department):
    """Determine the number of employees in each department
    
    input:
    output: 
    """
    employees_per_department = df.groupby('Department')[['ID']].count().rename(columns = {'ID':'Number of Employees'})
    
    return jsonify(employees_per_department.loc[department, :].to_json())



if __name__ == "__main__": 
    app.run(debug=True) 