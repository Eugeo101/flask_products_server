from app.products import product_routes
from app.models import Product
from flask import render_template, request, redirect, url_for, flash
from app.auth import auth_routes 

@product_routes.route("/all")
def show_all_products():
    products = Product.show_all_products()
    return render_template("products.html", products=products)

@product_routes.route("/add", methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET':
        return render_template("add_page.html")
    else: # POST
        p_name = request.form.get('p_name')
        img_file = request.form.get('img_file')
        desc = request.form.get('desc')
        # <=== validate data ===>
        data = {'p_name':p_name, 'img_file':img_file, 'desc':desc}
        res_db = Product.add_project_obj(data)
        if res_db == "OK":
            return redirect(url_for("products.show_all_products"))
        else: # Error
            flash("Error While Adding item in database", 'error')
            return render_template("add_page.html")
        
@product_routes.route("/product/<int:id>")
def show_product(id):
    found_product = Product.get_one_obj(id)
    if found_product != None: # nag7
        return render_template("product.html", product=found_product)
    else:
        return redirect(url_for("products.get_worng_info"))
    
@product_routes.route("error")
def get_worng_info():
    return render_template("error.html")