import webapp2
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        rotate_form = """
        <center><form action="/rotate" method="post">
            <label>
                Rotate by:
                <input type="number" name="rotate-by" value="0"/>
            </label><br><br>
            <textarea name="text-to-rotate" style="height: 100px; width: 400px;"></textarea><br>
            <input type="submit"/>
        </form></center>
        """

        response = page_header + rotate_form + page_footer
        self.response.write(response)

class Rotate(webapp2.RequestHandler):
    def post(self):
        text_to_rotate = self.request.get("text-to-rotate")
        rotate_by = self.request.get("rotate-by")
        rotated_text = encrypt(text_to_rotate, int(rotate_by))

        ans_form = """
        <center><form action="/rotate" method="post">
            <label>
                Rotate by:
                <input type="number" name="rotate-by" value="0"/>
            </label><br><br>
            <textarea name="text-to-rotate" style="height: 100px; width: 400px;">{0!s}</textarea><br>
            <input type="submit"/>
        </form></center>
        """.format(rotated_text)

        response = page_header + ans_form + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rotate', Rotate)
], debug=True)
