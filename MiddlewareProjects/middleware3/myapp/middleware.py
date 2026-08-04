from django.http import HttpResponse
class AppMaintainenceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        response = self.get_response(request)
        return HttpResponse("<h1 style='text-align:center;color:red'>App Under Maintainence Try After 2 days</h1>")
    
    