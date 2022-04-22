import re
from .models import User, EmployeeMaster
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# import datetime
# from datetime import datetime
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


# user register serializer for with validation
class UserRegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message="A user with that email address already exists.")])
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message="A user with that username already exists.")])
    
    def password_validator(values):
        pattern = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        test_string = values
        result = re.match(pattern, test_string)
        if not result:
            raise serializers.ValidationError(
                "Please enter Minimum eight characters,at least one letter,one number and one special character")

    password = serializers.CharField(write_only=True, validators=[password_validator])
    first_name = serializers.CharField(allow_null=False)
    last_name = serializers.CharField(allow_null=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        username = validated_data['username']
        password = validated_data['password']
        user.set_password(password)
        user.is_active = True
        user.save()
        return user


# employee serializer for the validate employe data with validators 
class EmployeeMasterializer(serializers.ModelSerializer):

    # checking salary is valid or not 
    def salary_validator(values):
        salary = str(values).count(".")
        try:
            if int(salary) == 1:
                salary = float(values)
            elif int(salary) == 0:
                salary = int(values)
            else:
                raise serializers.ValidationError("Please enter valide salary")
        except:
            raise serializers.ValidationError("Please enter valide salary")
        
    def gender_validator(values):
        if values == "Male" or values == "Female":
            values = values
        else:
            raise serializers.ValidationError(
                "Please enter valide gender details (Male or Female)")

    # checking date format only accept d/m/y format
    def date_validator(values):
        date_string = values
        date_format = "%d/%m/%Y"
        try:
            datetime.strptime(date_string, date_format)
        except ValueError:
            raise serializers.ValidationError(
                "Please enter date in (Date/Month/Year) formate")

    employee_salary = serializers.CharField(validators=[salary_validator])
    employee_first_name = serializers.CharField(allow_null=False)
    employee_last_name = serializers.CharField(allow_null=False)
    employee_surname = serializers.CharField(allow_null=False)
    dob = serializers.CharField(validators=[date_validator], allow_null=False)
    gender = serializers.CharField(
        validators=[gender_validator], allow_null=False)

    class Meta:
        model = EmployeeMaster
        fields = '__all__'

    def create(self, validated_data):
        employee = EmployeeMaster.objects.create(**validated_data)
        employee_first_name = validated_data['employee_first_name']
        employee_last_name = validated_data['employee_last_name']
        employee_surname = validated_data['employee_surname']
        dob = validated_data['dob']
        gender = validated_data['employee_salary']
        employee_salary = validated_data['employee_salary']

        employee.save()
        return employee
