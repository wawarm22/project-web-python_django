import calendar
import datetime
import django_filters
from django import forms
from blog.models import Post

class MonthFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value:
            month_num = list(calendar.month_name).index(value.title())
            qs = qs.filter(**{
                f'{self.field_name}__month': month_num
            })
        return qs   

class DataFilter(django_filters.FilterSet):
    MONTH_CHOICES = [(calendar.month_name[i], calendar.month_name[i]) for i in range(0, 13)]
    date = MonthFilter(widget=forms.Select(choices=MONTH_CHOICES))

    class Meta:
        model = Post
        fields = ['date', 'district', 'subdictrict', 'gender', 'filed', 'ageRange']


# class MonthFilter(django_filters.Filter):
#     def filter(self, qs, value):
#         if value:
#             year = datetime.date.today().year
#             month_num = list(calendar.month_name).index(value.title())
#             qs = qs.filter(**{
#                 f'{self.field_name}__year': year,
#                 f'{self.field_name}__month': month_num
#             })
#         return qs

# class DataFilter(django_filters.FilterSet):
#     MONTH_CHOICES = [(calendar.month_name[i], calendar.month_abbr[i]) for i in range(0, 13)]
#     month = MonthFilter(field_name='date', widget=forms.Select(choices=MONTH_CHOICES))

#     class Meta:
#         model = Post
#         fields = ['month','district', 'subdictrict', 'gender', 'filed', 'ageRange']





    			
		
    			
	
	
		