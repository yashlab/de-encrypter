from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        key = request.form['Secret Key']
        value = request.form['Target Value']
        convert = request.form['TYPE']
        print(convert)
        out = masterf(key,value,convert)
        return render_template('output.html',value=out)
    else:
        pass
        
    return render_template('index.html')

def masterf(key,value,type):
    vp = []
    for i,j in zip(range(10),[key[i] for i in range(10)]):
        vp.append(str(i)+j)
    
    out=""
    
    if type=='C':    
        for i in range(len(value)):
            try:
                out+=vp[int(value[i])][-1]
            except:
                out+=value[i]
    
    elif type=='D':
        if len(set(key)) == 10:
            rev_dict = {}
            for i in vp:
                rev_dict.update({i[-1]:i[0]})
            for i in range(len(value)):
                try:
                    out= out + rev_dict[value[i].upper()]
                except:
                    out+=value[i]
        else:
            out = "PLEASE ENTER ONE-TO-ONE SECRET KEY"
    
    return out

if __name__=="__main__":
    app.run(debug=True)