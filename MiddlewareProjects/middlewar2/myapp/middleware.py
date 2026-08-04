class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print('Init Method Executed')
        self.get_response = get_response
        
    def __call__(self,request):
        print("Preprocessing the request")
        response = self.get_response(request)
        print("Processing the response")
        return response
    
    
        
        
    
        
