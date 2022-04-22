from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeMaster
from .serializers import EmployeeMasterializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class EmployeeList(APIView):
    
    # for jwt token authentication and only login user can use the functionality
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    
    # get the all employee data
    def get(self, request, format=None):
        try:
            employee = EmployeeMaster.objects.all().order_by('emp_id')
            serializer = EmployeeMasterializer(employee, many=True)
            return Response(serializer.data)
        except Exception as ex:
            json_response = {"status":status.HTTP_400_BAD_REQUEST,"message": "Employee data not get successfully...","response":ex}
            return Response(json_response)  
            
    # add employee data 
    def post(self, request, format=None):   
        try:
            serializer = EmployeeMasterializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                json_response = {"status":status.HTTP_201_CREATED,
                            "response": serializer.data, "message": "Employee data add successfully..."}
                return Response(json_response)
            json_response = {"status":status.HTTP_400_BAD_REQUEST,
                            "response": serializer.errors, "message": "Employee data not add successfully..."}
            return Response(json_response)
        
        except Exception as ex:
            json_response = {"status":status.HTTP_400_BAD_REQUEST,
                            "response":ex, "message": "Register not successfully..."}
            return Response(json_response)


class EmployeeDetail(APIView):
    
    # for jwt token authentication and only login user can use the functionality
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, )
    
    # get the perticuler employee data 
    def get(self,request,pk,format=None):
        try:
            employee = EmployeeMaster.objects.filter(pk=pk)
            if len(employee) != 0 :
                serializer = EmployeeMasterializer(employee[0])
                return Response(serializer.data)
            else:
                json_response = {"status":status.HTTP_400_BAD_REQUEST, "message": "Employee data  not get successfully..."}
                return Response(json_response)
            
        except Exception as ex :
            json_response = {"status":status.HTTP_400_BAD_REQUEST,"response":ex, "message": "Employee data  not get successfully..."}
            return Response(json_response)

    # update employee data
    def put(self, request, pk, format=None):
        try:
            employee = EmployeeMaster.objects.filter(pk=pk)
            if len(employee) != 0 :
                serializer = EmployeeMasterializer(employee[0], data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    json_response = {"status":status.HTTP_200_OK,"message": "Employee data update successfully..."}
                    return Response(json_response)
                else:
                    json_response = {"status":status.HTTP_400_BAD_REQUEST,"response":serializer.errors,"message": "Employee data not update successfully..."}
                    return Response(json_response)
                    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else :
                json_response = {"status":status.HTTP_400_BAD_REQUEST, "message": "Employee data  not not found check emp_id..."}
                return Response(json_response)
                
        except Exception as ex :
            json_response = {"status":status.HTTP_400_BAD_REQUEST,"response":ex, "message": "Employee data  not update successfully..."}
            return Response(json_response)
        
    # delete perticuler employee      
    def delete(self, request, pk, format=None):
        try:
            employee = EmployeeMaster.objects.filter(pk=pk)
            if len(employee) != 0 :
                employee.delete()
                json_response = {"status":status.HTTP_200_OK,"message": "Employee data delete successfully..."}
                return Response(json_response)
            else :
                json_response = {"status":status.HTTP_400_BAD_REQUEST,"message": "Employee not exist..."}
            return Response(json_response)
                
        except Exception as ex:
            json_response = {"status":status.HTTP_400_BAD_REQUEST,"message": "Employee data not delete successfully...","response":ex}
            return Response(json_response)    
    