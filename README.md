# django-restapis
create virtual environment

python3 -m venv env
for windows : => env\Scripts\activate
for ubuntu :  => source env/bin/activate

=> pip freeze > requirements.txt

install all dependency from req.txt file.-
=> pip install -r requirements.txt

for the start our api 

=> python manage.py runserver

Apis:

* for user login
Api = http://127.0.0.1:8000/register/    
method = Post
Request:-
{
    "username":"admin2",
    "first_name":"admin_fname",
    "last_name":"admin_lname",
    "email":"admin12345@gmail.com",
    "password":"admin@1234"
}
-----------------------------------------------------------------------------

* for user registration
Api= http://127.0.0.1:8000/login/
Method = Post
Request:-
{
    "email":"admin123@gmail.com",
    "password":"Admin@1234"
}
------------------------------------------------------------------------------
-------------------------------------------------------------------------------

================================================================================
NOTE: Jwt token required in authorization 
================================================================================

* for add employee data 
Api = http://127.0.0.1:8000/employee/
Method = Post

Request:-
{
    "employee_first_name":"emp_2",
    "employee_last_name":"emp_22",
    "employee_surname":"emp_emp2",
    "employee_salary":"123.1",
    "dob":"11/05/2021",
    "gender":"Female"
}
-----------------------------------------------------------------------------

* for get employee perticuler 
Api = http://127.0.0.1:8000/employee/1/
Note:- hear 1 is employee id 
method = GET
----------------------------------------------------------------------------

* for get employee all data
Api = http://127.0.0.1:8000/employee/
method = GET
--------------------------------------------------------------------------

* for update employee data
Api = http://127.0.0.1:8000/employee/1/
NOTE = heare 1 is emp id 
Method = PUT
request:-
{
    "employee_first_name":"emp_16",
    "employee_last_name":"emp_22",
    "employee_surname":"emp_emp2",
    "employee_salary":"123.1",
    "dob":"11/05/2021",
    "gender":"male"
}
---------------------------------------------------------------------------------

for the dlete employee data
Api = http://127.0.0.1:8000/employee/1/
hear 1 is employe id 
Method = DELETE
------------------------------------------------------------------------------






