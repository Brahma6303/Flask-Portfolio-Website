from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/contact')
# def contact():
#     # if request.method == 'POST':
#     #     name = request.form['name']
#     #     print(name)
#     #     email=request.form['email']
#     #     subject=request.form['subject']
#     #     message = request.form['message']
#     #     return f"Thanks {name}-{email}-{subject}-{message}, your message has been received!"
#     return render_template('contact.html')
@app.route('/contact', methods=['GET', 'POST']) 
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message = request.form['message']
        return f" <h1><strong>Thanks ,<span style='color:green;'>{name}</strong>, <b>your message has been received!</b></h1>"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)