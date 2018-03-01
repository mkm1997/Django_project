class BookMiddleware(object):
    def process_request(self):
        print("middleware executed")