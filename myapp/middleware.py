# creating middlewares

# as a class
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # one time configuration and initialization
        
    def __call__(self, request):
        # code to be executed for each request before
        # the view (and later middleware) are called.
        
        print("before response")
        response = self.get_response(request)
        print("After response")
        
        # code to be executed for each request before
        # the view (and later middleware) are called.
        
        return response
    
    
#  as a function 
def  simple_middleware(get_response):
    # one time configuration and initialization
    
    def middleware(request):
        # code to be executed for each request before
        # the view (and later middleware) are called.
        print("before response")
        response = get_response(request)
        print("After response")
        # code to be executed for each request before
        # the view (and later middleware) are called.
        
        return response
    
    return middleware