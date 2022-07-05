# waitress-serve --listen=*:8000 app:app
from api import API
from middleware import Middleware

app = API()


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)


app.add_middleware(SimpleCustomMiddleware)


def custom_exception_handler(request, response, exception_cls):
    response.body = app.template("internal_error.html", context={"error": exception_cls}).encode()


app.add_exception_handler(custom_exception_handler)


# @app.route("/home")
# def exception_throwing_handler(request, response):
#     raise AssertionError("This handler should not be used")


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = str(req.body)


@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template("index.html", context={"name": "Alcazar", "title": "Best Framework"}).encode()
