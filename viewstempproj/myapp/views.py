from django.shortcuts import render

# Create your views here.

def home(request):
    emplist =[
        {
            "eid":111,
            "ename":"kiran",
            "esal":40000
        },
        {
            "eid":112,
            "ename":"Raj",
            "esal":50000
        },
        {
            "eid":113,
            "ename":"Ravi",
            "esal":70000
        },
    ]
    return render(request,'myapp/home.html',{"employees":emplist})

def getstudents(request):
    stulist =[
        {
            "stuid":10,
            "stuname":"Raj",
            "stumarks":500,
            "imgurl" :"https://wallpaperaccess.com/full/3710582.jpg"
        },
        {
            "stuid":11,
            "stuname":"Sindhuja",
            "stumarks":600,
            "imgurl":"https://1.bp.blogspot.com/-vdbJAGhILhc/T5KDtEUCEjI/AAAAAAAAKD4/FfVQyNKhjhk/s1600/prabhas+Rebel+-+MastiMusiQ+(4).jpg"
        },
        {
            "stuid":13,
            "stuname":"Pooja",
            "stumarks":550,
            "imgurl":"https://i.indiglamour.com/photogallery/telugu/actress/2021/TL_Act_101821-01/Pooja-Hegde/normal/Pooja-Hegde_1656606171.jpg"
        },
        {
            "stuid":14,
            "stuname":"MrunalThakur",
            "stumarks":500,
            "imgurl":"https://www.gethucinema.com/wp-content/uploads/2022/01/MrunalThakur-386-819x1024.jpg"
        },
        {
            "stuid":15,
            "stuname":"Rashmika",
            "stumarks":560,
            "imgurl":"https://wallpaperaccess.com/full/3710582.jpg",
        },
    ]
    return render(request,'myapp/students.html',{"students":stulist}) 