from django.urls import path
from .views import panel,displayForm,insertData,deleteData,editData,updateData,showData,panel2

urlpatterns = [
    path('panel',panel,name="panel"),
    path('panel2',panel2,name="panel2"),
    path('displayForm',displayForm,name="displayForm"),
    path('insertData',insertData,name="insertData"),
    path('deleteData/<int:id>',deleteData,name="deleteData"),
    path('editData/<int:id>',editData,name="editData"),
    path('updateData/<int:id>',updateData,name="updateData"),
    path('showData/<int:id>',showData,name="showData"),
    # path('my-model/', MyModelMonthArchiveView.as_view(), name='panel'),
]