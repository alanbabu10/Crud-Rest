from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list(request):

    # GET METHOD
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # POST METHOD
    elif request.method == 'POST':

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


# GET SINGLE + UPDATE + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):

    try:
        student = Student.objects.get(id=pk)

    except Student.DoesNotExist:
        return Response(
            {"error": "Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET SINGLE DATA
    if request.method == 'GET':

        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # UPDATE DATA
    elif request.method == 'PUT':

        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    # DELETE DATA
    # elif request.method == 'DELETE':

    #     student.delete()

    #     return Response(
    #         {"message": "Deleted successfully"},
    #         status=status.HTTP_204_NO_CONTENT
    #     )
    