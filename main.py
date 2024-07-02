import tornado.web, tornado.ioloop, json


class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits, indent=4))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added"}))


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid int.")


class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, student_name, course_id):
        self.write(f"Welcome {student_name} the course you are viewing is {course_id}")


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", mainRequestHandler),
            (r"/list", listRequestHandler),
            (r"/isEven", queryParamRequestHandler),
            (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        ]
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
