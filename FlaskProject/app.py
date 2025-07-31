from flask import Flask, render_template, request, redirect, url_for
import wikipedia

app = Flask(__name__)
wikipedia.set_lang("en")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        title = request.form.get('title', '').strip()
        if not title:
            return redirect(url_for('index'))

        try:
            page = wikipedia.page(title, auto_suggest=False)
            summary = page.summary
            return render_template('result.html', title=page.title, summary=summary, url=page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            return render_template('disambiguation.html', title=title, suggestions=e.options)
        except wikipedia.exceptions.PageError:
            error = f'No page found for the title "{title}". Please try another keyword.'
            return render_template('error.html', error=error)
        except Exception as ex:
            error = f"An unexpected error occurred: {ex}"
            return render_template('error.html', error=error)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
