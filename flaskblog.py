from flask import Flask, render_template, url_for , flash , redirect
from forms import RegistrationForm , LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2f0dbb41f8a1da366e2a4b748a0d174'


posts = [
    {
        'author': 'Rishabh Raj Sharma',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 18 , 2020'
    },
    {
        'author': 'Rishabh Raj Sharma',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 18 , 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
            flash(f'Account Created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
    return render_template('register.html',title="Registration" , form= form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "qwertyhjkl":
            flash('You have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect credentials','danger')
    return render_template('login.html',title="Login" , form= form)



if __name__ == '__main__':
    app.run(debug=True)