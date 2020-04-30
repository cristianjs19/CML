from rest_framework import viewsets, mixins
from .serializers import BookSerializer, BookImageSerializer, LendingAgreementSerializer, LendingRequestSerializer
from accounts.models import User
from books.models import Book, LendingAgreement, LendingRequest

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class LendingAgreementViewSet(viewsets.ModelViewSet):
	queryset = LendingAgreement.objects.all()
	serializer_class = LendingAgreementSerializer

class LendingRequestViewSet(viewsets.ModelViewSet):
	queryset = LendingRequest.objects.all()
	serializer_class = LendingRequestSerializer	

# 	def get_queryset(self):
#         program = int(self.kwargs.get('pk_program',  0))
#         if program:
#             enrollment_program = EnrollmentProgram.objects.filter(
#                 program__pk=program)
#         else:
#             enrollment_program = EnrollmentProgram.objects.filter(student=self.request.user)
#         return enrollment_program

# class EnrollmentProgramByCourseView(viewsets.ModelViewSet):
#     serializer_class = EnrollmentProgramSerializer
#     http_method_names = ["get"]
#     filter_backends = (DjangoFilterBackend,)
#     filter_class = EnrollmentProgramFilter

#     def get_queryset(self):
#         student = self.kwargs.get("pk_student", None)
#         enroll_student = EnrollmentProgram.objects.filter(student=student)
#         return enroll_student


