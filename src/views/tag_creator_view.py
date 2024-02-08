from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController
class TagCreatorView:
    '''
    responsabilidade para interagir com http
    '''
    def validate_and_create(self, http_request: HttpRequest ) -> HttpResponse :
        tag_creator_controller = TagCreatorController()
        body = http_request.body
        product_code = body ["product_code"]
        #Logicas de regra de negocio
        formatted_response = tag_creator_controller.create_tag(product_code)
        #retorno http
        return HttpResponse(status_code=200, body=formatted_response)
        