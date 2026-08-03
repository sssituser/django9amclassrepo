from django.http import HttpResponse
class ExecutionFlowMiddleware(object):
    
    def __init__(self,get_response):
        print('init method executed')
        self.get_response=get_response
    
    
    def __call__(self,request):
        print("Preprocessing the request")
        response = self.get_response(request)
        print("PostProccessing the request")
        return   response
    
    
    def process_exception(self,request,exception):
        #return HttpResponse('<h1 style="color:red">Currently we are facing technicl  issuess,try after some time</h1>')
        return HttpResponse(f"Raised Exception is  :{exception}")