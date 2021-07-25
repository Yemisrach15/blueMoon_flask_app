from appFolder import db, api
import app


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    #post = db.relationship('Plant', backref='posted plant', lazy=True)
    #getUser = db.relationship('UserPlant', backref='get user', lazy=True)

    # def __repr__(self):
    #     return f"(username = {username}, password = {password})"


class Plant(db.Model):
    __tablename__ = "plant"
    plant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    use = db.Column(db.String(), nullable=False)
    imagePath = db.Column(db.String(100), nullable=False)
    approved = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)#db.ForeignKey('user.user_id'), 
    #getPlant = db.relationship('UserPlant', backref='get plant', lazy=True)

    # def __repr__(self):
    #     return f"(username = {username}, password = {password})"


class UserPlant(db.Model):
    __tablename__ = "user_plant"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plant_id = db.Column(db.Integer, nullable=False)#db.ForeignKey('plant.plant_id'), 
    user_id = db.Column(db.Integer, nullable=False)#db.ForeignKey('user.user_id'), 
    delivered = db.Column(db.Boolean, default=False)

    #ingredRecip = db.relationship('RecipeIngredientTable', backref='ingredRecipe', lazy=True)


# db.create_all()
