from flask import Flask, request, render_template_string
import wikipedia


wikipedia.set_lang("en")

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"<h2>Hello {name}</h2>" if name else "<h2>Hello</h2>"


def celsius_to_fahrenheit(c):
    return c * 9.0 / 5.0 + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        c = float(celsius)
        f = celsius_to_fahrenheit(c)
        return f"<h2>{c}° Celsius is equal to {f:.2f}° Fahrenheit</h2>"
    except ValueError:
        return "<p style='color:red;'>Invalid input. Please enter a valid number.</p>"


@app.route('/wiki', methods=['GET', 'POST'])
def wiki_search():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            return render_template_string(FORM_HTML, error="Please enter a title.", request=request)

        try:
            page = wikipedia.page(title, auto_suggest=False)
            return render_template_string(RESULT_HTML,
                                          title=page.title,
                                          summary=page.summary,
                                          url=page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            return render_template_string(AMBIGUOUS_HTML,
                                          suggestions=e.options,
                                          request=request)
        except wikipedia.exceptions.PageError:
            return render_template_string(FORM_HTML,
                                          error="Page not found. Try a different title.",
                                          request=request)
        except Exception as ex:
            return render_template_string(FORM_HTML,
                                          error=f"An unexpected error occurred: {str(ex)}",
                                          request=request)

    return render_template_string(FORM_HTML, request=request)


# HTML 代码模板
FORM_HTML = '''
    <h2>Wikipedia Page Search</h2>
    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
    <form method="post">
        Wikipedia Page Title: <input type="text" name="title" value="{{ request.form.title }}">
        <input type="submit" value="Search">
    </form>
'''

RESULT_HTML = '''
    <h1>{{ title }}</h1>
    <p>{{ summary }}</p>
    <a href="{{ url }}" target="_blank">Read more on Wikipedia</a><br><br>
    <a href="/wiki">Search another</a>
'''

AMBIGUOUS_HTML = '''
    <h2>Ambiguous title, please be more specific.</h2>
    <ul>
    {% for item in suggestions %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
    <a href="/wiki">Back to search</a>
'''

if __name__ == '__main__':
    app.run(debug=True)
