from flask_sqlalchemy import SQLAlchemy
from flask import url_for
# step-1: ORM
db = SQLAlchemy()

# step-2: create Model
class Product(db.Model):
    # Schema: static attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    img = db.Column(db.String) # name_of_image

    def __init__(self, name, description, img):
        # attributes of instance of the class / object
        self.name = name
        self.description = description
        self.img = img
    
    def __str__(self):
        return "Product"
    # step-3: # acess to db
    # classmethod

    @property
    def get_obj_img_url(self):
        return url_for('products.static', filename=f'{self.img}')
    
    @property
    def get_route_of_obj(self):
        return url_for('products.show_product', id=self.id)
    
    @classmethod
    def show_all_products(cls):
        return cls.query.all()
    
    @classmethod
    def add_project_obj(cls, data):
        # create object for db
        p_name = data['p_name']
        img_file = data['img_file']
        desc = data['desc']
        try:
            added_prod = cls(p_name, desc, img_file)
            db.session.add(added_prod)
            db.session.commit()
            return "OK"
        except:
            return "Error"
    
    @classmethod
    def get_one_obj(cls, id):
        try:
            return cls.query.get(id)
        except:
            return "Error"