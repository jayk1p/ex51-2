import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')


class Index(object):
    def GET(self):
        return render.hello_form()
        # This asks for the "hello_form.html"

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)

        return render.index(greeting = greeting)
        # This asks for the "index.html"

if __name__ == "__main__":
    app.run()
