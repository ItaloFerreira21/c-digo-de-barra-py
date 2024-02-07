from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
class TagCreatorView:
    '''
    responsabilidade para interagir com http
    '''
    def validade_and_creat(self, http_request: HttpRequest ) -> HttpResponse :
        #body = http_request.body
        #product_code = body ["product_code"]
        #Logicas de regra de negocio
        print("estou na minha viwe")
        print(http_request)
        #retorno http
        return HttpResponse(status_code=200, body={"helow": "word"})
        