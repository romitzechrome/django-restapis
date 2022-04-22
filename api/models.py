from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class EmployeeMaster(models.Model):

    emp_id = models.AutoField(db_column="emp_id", primary_key=True, null=False)
    employee_first_name = models.CharField(db_column="employee_first_name", max_length=255, default="", null=False)
    employee_last_name = models.CharField(db_column="employee_last_name", max_length=255, default="", null=False)
    employee_surname = models.CharField(db_column="employee_surname", max_length=255, default="", null=False)
    employee_salary = models.CharField(db_column="employee_salary", max_length=255, null=False)
    dob = models.CharField(db_column="dob", max_length=255, null=False)
    gender = models.CharField(db_column="gender" ,max_length=255, null=False)

    def __str__(self):
        return '{} {}'.format(self.employee_first_name, self.employee_last_name)

    def __as_dict__(self):
        return {
            "employee_first_name": self.employee_first_name,
            "employee_last_name": self.employee_last_name,
            "employee_surname": self.employee_surname,
            "employee_salary": self.employee_salary,
            "dob": self.dob,
            "gender": self.gender,
        }

    class Meta:
        db_table = "employee_master"



