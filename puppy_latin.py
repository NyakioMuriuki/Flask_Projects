"""
#####################RULES####################
If a puppy name does not end in a y add a y to the end of the name eg Rufus --> Rufusy
If the puppy name ends in a y add an iful at the end and remove the y at the end eg: Sparky --> Sparkiful

"""

from flask import Flask
app = Flask(__name__)

#Welcome page
@app.route('/')
def index():
    return '<h1> Jambo, welcome to the puppy latin convertor, please go to /puppy_latin/name to see you puppy\'s latin name</h1>'

#Page Two - using dynamic routing so as to allow the user to enter their puppy's name


@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    name = name.lower()
    if name[-1] == 'y':
        #remove the y and replace it with iful
        name = list(name)
        name[-1] = 'iful'
        name = ''.join(name)

    else:
        name = name + 's'
        
    return 'Your puppy\'s latin name is {}'.format(name)


if __name__ == '__main__':
    app.run(debug=True)