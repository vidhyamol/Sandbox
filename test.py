from bottle import route,run,template,get,post,put,delete,request
pat_dic={}
#code for post
@post('/patient')
def add_data():
	id=request.POST['id']
	name=request.POST['name']
	gender=request.POST['gender']
	info_dic={'name':name,'gender':gender}
	pat_dic[id]=info_dic
	return pat_dic
@get('/patient/<id>')
def get_data(id):
	return pat_dic[id]
	
@put('/patient/<id>')
def modify(id):
	if id in pat_dic.keys():
		pat_dic[id].update(name = request.POST['name'],gender = request.POST['gender'])
		return"successfully updated"
	else:
		return"Error in id"
	
@delete('/patient/del/<id>')
def remove(id):
	
	del(pat_dic[id])
	return pat_dic
run(host='localhost',port=8080)

			
