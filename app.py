from flask import Flask, request, render_template_string

app = Flask(__name__)

def details(name, age, sex):
    return f"Name: {name}, Age: {age}, Sex: {sex}"

# Route to show a form
@app.route('/')
def index():
    return '''
        <form action="/submit" method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            Sex: <input type="text" name="sex"><br>
            <input type="submit" value="Submit">
        </form>
    '''

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    sex = request.form['sex']
    result = details(name, age, sex)
    return render_template_string("<h2>{{ result }}</h2>", result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


