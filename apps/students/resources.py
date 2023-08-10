from import_export import resources
from .models import Student

class ResultResorses(resources.ModelResource):
    class Meta:
        model = Student
        # fields = ('current_status','registration_number','surname','firstname','other_name','gender','date_of_birth', 'date_of_admission','parent_mobile_number','address','others')
        # export_order = ('current_status','registration_number','surname','firstname')


