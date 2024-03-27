from flask import Flask, render_template, url_for, redirect, request 
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clothing_store.db"
app.config['SECRET_KEY'] = 'thisisasecretekey'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

class RegisterForm(FlaskForm): 
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder" : "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder" : "Username"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_name = User.query.filter_by(
            username=username.data).first() 
    
        if existing_user_name: 
            raise ValidationError(
                "That username already exists.Please choose the different one"
            )

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder" : "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder" : "Username"})
    submit = SubmitField("Login")

class Clothes(db.Model):
    clothes_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_id = db.Column(db.BigInteger, nullable=False)
    clothes_nm = db.Column(db.String(100), nullable=False)
    category_nm = db.Column(db.String(40), nullable=False)
    color_nm = db.Column(db.String(40))
    price_amt = db.Column(db.Integer, nullable=False)
    sex_nm = db.Column(db.String(50))

class ClothesForm(FlaskForm):
    brand_id = IntegerField('Brand ID', validators=[InputRequired()])
    clothes_nm = StringField('Clothing Name', validators=[InputRequired()])
    category_nm = StringField('Category', validators=[InputRequired()])
    color_nm = StringField('Color')
    price_amt = IntegerField('Price', validators=[InputRequired()])
    sex_nm = SelectField('Sex', choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')])

@app.route('/hello/add_clothing', methods=['GET', 'POST'])
def add_clothing():
    form = ClothesForm()
    if form.validate_on_submit():
        new_clothing = Clothes(
            brand_id=form.brand_id.data,
            clothes_nm=form.clothes_nm.data,
            category_nm=form.category_nm.data,
            color_nm=form.color_nm.data,
            price_amt=form.price_amt.data,
            sex_nm=form.sex_nm.data
        )
        db.session.add(new_clothing)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard or any other page
    return render_template('add_clothing.html', form=form)  

class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.clothes_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    # Define relationships
    user = db.relationship('User', backref=db.backref('cart_items', lazy=True))
    clothes = db.relationship('Clothes', backref=db.backref('cart_items', lazy=True))


# Routes
@app.route('/')
def index():
    signed_in = current_user.is_authenticated
    id = current_user.id if signed_in else None
    username = current_user.username if signed_in else None
    return render_template('index.html', signed_in=signed_in, username=username, id=id)

    
@app.route('/shop')
def shop():
    signed_in = current_user.is_authenticated
    username = current_user.username if signed_in else None
    clothes = Clothes.query.all()
    return render_template('shop.html', clothing_items=clothes, signed_in=signed_in, username=username)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html',form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html',username=current_user.username, id=current_user.id)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# @app.route('/admin', methods=['GET', 'POST'])
# @login_required
@app.route('/hello')
def admin():
    id = current_user.id
    if id == 1:
        return render_template("admin.html")
    else:
        return "<h1>you are not admin, please comeback!!!</h1>"

@app.route('/hello/admin_dashboard')
def admin_dashboard():
    # Retrieve all clothing items from the database
    clothing_items = Clothes.query.all()
    return render_template('admin_dashboard.html', clothing_items=clothing_items)

@app.route('/add_to_cart/<int:clothes_id>', methods=['POST'])
@login_required  # Assuming you have login_required decorator for authentication
def add_to_cart(clothes_id):
    user = current_user  
    existing_item = CartItem.query.filter_by(user_id=user.id, clothes_id=clothes_id).first()

    if existing_item:
        existing_item.quantity += 1
    else:
        new_item = CartItem(user_id=user.id, clothes_id=clothes_id, quantity=1)
        db.session.add(new_item)

    db.session.commit()

    return redirect(url_for('shop'))

@app.route('/cart')
@login_required
def cart():
    # Retrieve cart items associated with the current user
    cart_items = current_user.cart_items
    return render_template('cart.html', cart_items=cart_items)

@app.route('/update_cart', methods=['POST'])
@login_required
def update_cart():
    if request.method == 'POST':
        # Get the quantities from the form submission
        quantities = {}
        for key, value in request.form.items():
            if key.startswith('quantity_'):
                item_id = int(key.split('_')[1])
                quantities[item_id] = int(value)

        # Update the quantities in the database
        for cart_item in current_user.cart_items:
            if cart_item.id in quantities:
                cart_item.quantity = quantities[cart_item.id]

        db.session.commit()

    # Redirect back to the user profile page after updating the cart
    return redirect(url_for('cart'))


app.app_context().push()
if __name__ == '__main__':
    app.run(debug=True)
