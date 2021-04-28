from bottle import run, route, get, template, post, static_file, request
import petl as etl
import csv
import cgi, cgitb


#this is based on API called REST
@route('/')
def server_static(filepath="index.html"):
    return template(filepath, root='./public/')

@route('/createfile')
def server_static(filepath="createfile.html"):
    return template(filepath, root='./public/')

@post('/doform')
def process():
    File = request.forms.get('File')
    Name = request.forms.get('Name')+".csv"
    Headings = request.forms.getall('headings')
    with open(Name, 'w') as file:
        writer=csv.writer(file)
        writer.writerow(Headings)
    
    return "Your File {0} is already create in local folder.".format(Name)

@route('/importfile')
def server_static(filepath="importfile.html"):
    return template(filepath, root='./public/')

@post('/doimport')
def upload(filepath="modifyfile.html"):
    uploadfile = request.files.get('uploadfile')
    fname = uploadfile.filename
    uploadfile = uploadfile.file.readlines()
    list=[]
    for line in uploadfile:
        x = str(line)
        x = x.replace("b'", "")
        x = x.replace(" ", "_")
        list.append(x.split(","))
    print(list)
    page = template(filepath, {"th":list, "fname":fname} )
    return page

@post('/redoform')
def process():
    filename = request.forms.get('filename')
    filename = filename.replace("-"," ")
    nheadings = request.forms.getall('nheadings')
    print(filename, nheadings)
    with open(filename, 'w') as file:
        writer=csv.writer(file)
        writer.writerow(nheadings)

    return "Your File {0} is already create in local folder.".format(filename)


run(host='localhost', reloader=True, port=8080, debug=True)
