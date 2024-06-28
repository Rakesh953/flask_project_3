from flask import Flask, render_template

FAI = Flask(__name__)

@FAI.route('/rakesh')
def rakesh():
    return 'You are here'

@FAI.route('/first_view')
def first_view():
    return render_template('first_view.html', name='Rajesh', age=23)
    

FAI.run(debug=True, host='192.168.43.28', port=5000)

