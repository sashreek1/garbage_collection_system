from flask import Flask
from flask import render_template
from flask import request
from sendmsg import get_data

app = Flask(__name__)



def main(area):
        rows = get_data()
        for i in rows:
                if i[0] == area:
                        percentage = round((i[4]/i[3])*100,1)
	return percentage

@app.route('/',methods=['POST', 'GET'])
def index():
	if request.method=='GET':
		area=request.args.get('area_name', '')
	elif request.method=='POST':
		area=request.form['area_name']

	percent = main(area)
	return render_template('index.html')

@app.route('/submited',methods=['POST', 'GET'])
def result():
	if request.method=='GET':
		area=request.args.get('area_name', '')
	elif request.method=='POST':
		area=request.form['area_name']

	percent = main(area)
	return render_template('result.html', area=area, percent=percent)


if __name__ == '__main__':
	app.run()
