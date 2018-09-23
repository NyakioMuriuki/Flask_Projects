from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    #To get the args passed in our html form
        # The 3 conditions to check (start as False)
    has_upper = False
    has_lower = False
    has_num = False
    name = request.args.get('name')

    has_lower = any(letter.islower() for letter in name)
    has_upper = any(letter.isupper() for letter in name)
    has_num = name[-1].isdigit()
    # Check if all are True.
    report = has_upper and has_lower and has_num

    return render_template('report.html', name = name,has_upper = has_upper,has_lower = has_lower, has_num = has_num,report = report)




if __name__=='__main__':
    app.run(debug=True)