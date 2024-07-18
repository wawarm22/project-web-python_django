from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from blog import models
from category.models import District,Subdictrict,Gender,Living_Con,Career,Level_of_Education,Filed,AgeRange
from django.core.files.storage import FileSystemStorage
from blog.models import Post
from .filter import DataFilter
from django.db.models.functions import ExtractMonth  
from django.db.models import Count
import calendar

def get_monthly_count(qs):
    monthly_count = (
        qs.annotate(month=ExtractMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    return monthly_count

def age_count_monthly(qs, age_range):
    return (
        qs.filter(ageRange=age_range)
        .annotate(month=ExtractMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

def filed_count_monthly(qs, filed_value):
    return (
        qs.filter(filed=filed_value)
        .annotate(month=ExtractMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    
def panel(request):
    datas = Post.objects.all()        
    dataCount = datas.count()        
    myFilterCount1 = Post.objects.filter(filed = 1)
    myFilterCount2 = Post.objects.filter(filed = 2)
    ageCounts1 = Post.objects.filter(ageRange = 1)
    ageCounts2 = Post.objects.filter(ageRange = 2) 
    ageCounts3 = Post.objects.filter(ageRange = 3)          
    districts = District.objects.all()
    subdictricts = Subdictrict.objects.all()
    genders = Gender.objects.all()
    livings = Living_Con.objects.all()
    levels = Level_of_Education.objects.all() 
    careers = Career.objects.all()
    fileds = Filed.objects.all()
    ageRanges = AgeRange.objects.all()          
    myFilter = DataFilter(request.GET, queryset=datas)    
    datas = myFilter.qs              
    myFilterCount1 = DataFilter(request.GET, queryset=myFilterCount1)
    filedCount1 = myFilterCount1.qs.count()
    myFilterCount2 = DataFilter(request.GET, queryset=myFilterCount2)
    filedCount2 = myFilterCount2.qs.count()
    ageCounts1 = DataFilter(request.GET, queryset=ageCounts1)
    ageCount1 = ageCounts1.qs.count()
    ageCounts2 = DataFilter(request.GET, queryset=ageCounts2)
    ageCount2 = ageCounts2.qs.count()
    ageCounts3 = DataFilter(request.GET, queryset=ageCounts3)
    ageCount3 = ageCounts3.qs.count()       
    return render(request,"backend/index.html",
                  {'myFilter':myFilter,'levels':levels,'careers':careers,
                    'datas':datas,'dataCount':dataCount,'districts':districts,
                    'subdictricts':subdictricts,'genders':genders,'livings':livings,
                    'fileds':fileds,'filedCount1':filedCount1,'filedCount2':filedCount2,
                    'ageRanges':ageRanges,'ageCount1':ageCount1,'ageCount2':ageCount2
                    ,'ageCount3':ageCount3}) 
    

def panel2(request):
    datas = Post.objects.all()        
    dataCount = datas.count()    
    districts = District.objects.all()
    subdictricts = Subdictrict.objects.all()
    genders = Gender.objects.all()
    livings = Living_Con.objects.all()
    levels = Level_of_Education.objects.all() 
    careers = Career.objects.all()
    fileds = Filed.objects.all()
    ageRanges = AgeRange.objects.all()
    
    monthly_count = get_monthly_count(datas)
    filed_count1 = filed_count_monthly(datas, 1)
    filed_count2 = filed_count_monthly(datas, 2)
    age_count1 = age_count_monthly(datas, 1)
    age_count2 = age_count_monthly(datas, 2)
    age_count3 = age_count_monthly(datas, 3)
    month_names = list(calendar.month_name)[1:]
    count_data = [0] * 12
    filed_count_data1 = [0] * 12
    filed_count_data2 = [0] * 12
    age_count_data1 = [0] * 12
    age_count_data2 = [0] * 12
    age_count_data3 = [0] * 12
    for item in monthly_count:
        count_data[item['month']-1] = item['count']
    for item in filed_count1:
        filed_count_data1[item['month']-1] = item['count']
    for item in filed_count2:
        filed_count_data2[item['month']-1] = item['count']
    for item in age_count1:
        age_count_data1[item['month']-1] = item['count']
    for item in age_count2:
        age_count_data2[item['month']-1] = item['count']
    for item in age_count3:
        age_count_data3[item['month']-1] = item['count']

    myFilter = DataFilter(request.GET, queryset=datas)
    datas = myFilter.qs
    myFilterCount1 = DataFilter(request.GET, queryset=Post.objects.filter(filed=1))
    filedCount1 = myFilterCount1.qs.count()
    myFilterCount2 = DataFilter(request.GET, queryset=Post.objects.filter(filed=2))
    filedCount2 = myFilterCount2.qs.count()
    ageCounts1 = DataFilter(request.GET, queryset=Post.objects.filter(ageRange=1))
    ageCount1 = ageCounts1.qs.count()
    ageCounts2 = DataFilter(request.GET, queryset=Post.objects.filter(ageRange=2))
    ageCount2 = ageCounts2.qs.count()
    ageCounts3 = DataFilter(request.GET, queryset=Post.objects.filter(ageRange=3))
    ageCount3 = ageCounts3.qs.count()    
        
    return render(request,"backend/secondform.html",{'myFilter':myFilter,'levels':levels,'careers':careers,
                                              'datas':datas,'dataCount':dataCount,'districts':districts,
                                              'subdictricts':subdictricts,'genders':genders,'livings':livings,
                                              'fileds':fileds,'filedCount1':filedCount1,'filedCount2':filedCount2,
                                              'ageRanges':ageRanges,'ageCount1':ageCount1,'ageCount2':ageCount2
                                              ,'ageCount3':ageCount3,
                                              'month_names': month_names,'count_data': count_data,
                                              'filed_count_data1': filed_count_data1,
                                              'filed_count_data2': filed_count_data2,
                                              'age_count_data1': age_count_data1,
                                              'age_count_data2': age_count_data2,
                                              'age_count_data3': age_count_data3,})
  
    
def displayForm(request):    
    datas = Post.objects.all()
    dataCount = datas.count()    
    districts = District.objects.all()
    subdictricts = Subdictrict.objects.all()
    genders = Gender.objects.all()
    livings = Living_Con.objects.all()
    levels = Level_of_Education.objects.all() 
    careers = Career.objects.all()
    fileds = Filed.objects.all()
    ageRanges = AgeRange.objects.all()              
    return render(request,"backend/addform.html",{'levels':levels,'careers':careers,'datas':datas,
                                               'dataCount':dataCount,'districts':districts,
                                               'subdictricts':subdictricts,'genders':genders,
                                               'livings':livings,'fileds':fileds,'ageRanges':ageRanges})

def insertData(request):
    try:
        if request.method == "POST":            
            #รับค่าจากฟอร์ม
            name = request.POST["name"]           
            nationalID = request.POST["nationalID"]
            address = request.POST["address"]
            district = request.POST["district"]
            subdictrict = request.POST["subdictrict"]
            gender = request.POST["gender"]
            age = request.POST["age"]
            phonenumber = request.POST["phonenumber"]
            email = request.POST["email"]
            living = request.POST["living"]   
            level = request.POST["level"] 
            career = request.POST["career"]
            filed = request.POST["filed"]
            ageRange = request.POST["ageRange"]                                           
               
            #บันทึกข้อมูลบทความ
            datas = Post(name = name,district_id=district,subdictrict_id=subdictrict,
                         gender_id=gender,nationalID=nationalID,address=address,age=age,
                         phonenumber = phonenumber,email = email,living_id = living,level_id = level,
                         career_id = career,filed_id = filed,ageRange_id = ageRange)
            datas.save()
            messages.info(request,"บันทึกข้อมูลเรียบร้อย")
            return redirect("displayForm")
        else:
            messages.info(request,"บันทึกไม่สำเร็จ")
            return redirect("displayForm")
    except:
        return redirect("displayForm")    
    
def deleteData(request,id):
    
    try:        
        datas = Post.objects.get(id=id)
        fs = FileSystemStorage()        
        #ลบข้อมูลจากฐานข้อมูล
        datas.delete()
        return redirect('panel')
    except:
        return redirect('panel')
    
def editData(request,id):
    #ข้อมูลพื้นฐาน    
    datas = Post.objects.all()
    dataCount = datas.count()    
    districts = District.objects.all()
    subdictricts = Subdictrict.objects.all()
    genders = Gender.objects.all()
    livings = Living_Con.objects.all()
    levels = Level_of_Education.objects.all()
    careers = Career.objects.all()
    fileds = Filed.objects.all()
    ageRanges = AgeRange.objects.all()        
    dataEdit = Post.objects.get(id=id)
    return render(request,"backend/editform.html",{'livings':livings,"dataEdit":dataEdit,'dataCount':dataCount,
                                                'districts':districts,'subdictricts':subdictricts,
                                                'genders':genders,'levels':levels,'careers':careers,
                                                'fileds':fileds,'ageRanges':ageRanges})

def updateData(request,id):
    try:
        if request.method == "POST":
            #ดึงข้อมูลบทความที่ต้องการแก้ไขมาใช้งาน
            datas = Post.objects.get(id=id)
            #รับค่าจากฟอร์ม
            name = request.POST["name"]            
            nationalID = request.POST["nationalID"]
            address = request.POST["address"]
            district = request.POST["district"]
            subdictrict = request.POST["subdictrict"]
            gender = request.POST["gender"]
            age = request.POST["age"]
            phonenumber = request.POST["phonenumber"]
            email = request.POST["email"]
            living = request.POST["living"]
            level = request.POST["level"]
            career = request.POST["career"]
            filed = request.POST["filed"]
            ageRange = request.POST["ageRange"] 
             

            #อัพเดตข้อมูล
            datas.name = name            
            datas.nationalID = nationalID
            datas.address = address
            datas.district_id = district
            datas.subdictrict_id = subdictrict
            datas.gender_id = gender
            datas.age = age
            datas.phonenumber = phonenumber
            datas.email = email
            datas.living_id = living
            datas.level_id = level
            datas.career_id = career
            datas.filed_id = filed
            datas.ageRange_id = ageRange
                       
            datas.save()            
            return redirect("panel")
    
    except :
        return redirect("panel")
    
def showData(request,id):    
    datas = Post.objects.all()
    dataCount = datas.count()    
    districts = District.objects.all()
    subdictricts = Subdictrict.objects.all()
    genders = Gender.objects.all()
    livings = Living_Con.objects.all()
    levels = Level_of_Education.objects.all()
    careers = Career.objects.all()
    fileds = Filed.objects.all()
    ageRanges = AgeRange.objects.all()      
    dataShow = Post.objects.get(id=id)
    return render(request,"backend/dataform.html",{'livings':livings,"dataShow":dataShow,'dataCount':dataCount,
                                                'districts':districts,'subdictricts':subdictricts,
                                                'genders':genders,'levels':levels,'careers':careers,
                                                'fileds':fileds,'ageRanges':ageRanges})    
