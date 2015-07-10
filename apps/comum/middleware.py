# coding=utf-8


class LogMiddleware(object):
    def process_request(self, request):
        print(request.user)
        print(request.path)
        print(request.META['REMOTE_ADDR'])
        print(request.META['HTTP_USER_AGENT'])

    # def process_view(self, request, view, view_args, view_kwargs):
    #     print(view)
    #
    # def process_response(self, request, response):
    #     print(response)
    #     return response
