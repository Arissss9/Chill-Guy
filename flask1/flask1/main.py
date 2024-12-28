from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    # <a> anchor tag with its attribute
    return "<h1>Hello, World!</h1><br><p>Nice to see you</p><p>please check</p><a href='/random_fact'>View a random fact!</a><br><a href='/modern_fact'>View a modern fact!</a><br><a href='/coin'>Coin Flip!</a><br><a href='/password'>Password!</a><br><a href='/image'>Image!</a>"
    
# 2nd page
@app.route("/random_fact")

def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    # formatted string
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'
# 2nd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')#folder templates
# 2nd page
@app.route("/coin")
def kedua_c():
    koin = random.randint(1,2)
    # formatted string
    if koin == 1:
        return "It's Head"
    elif koin == 2:
        return "It's Tail"
#password
@app.route("/password")
def ketiga_c():
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(10):
        password += random.choice(elements)

    return password
#image
@app.route("/image")
def keempat_c():
    jpg_name = random.choice(os.listdir("img"))
    with open(f'img/{jpg_name}', 'r') as f:
        image = f.read()
        return f'{image}'


app.run(debug=True)