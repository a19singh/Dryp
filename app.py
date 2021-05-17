from flask import Flask, request, render_template
import calculator

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def cal():

    out = 0 

    try : 
        if request.method == 'POST': #request method checking 

            # fetching operand values
            a = int(request.form.get('ValueA')) 
            b = int(request.form.get('ValueB'))

            # fetching operation to be performed
            op = request.form.get('operator')

            # calling of the function to perform operation as per user requirement
            if op == 'addition':
                out = calculator.addition(a,b)
            elif op == 'subtraction':
                out = calculator.subtraction(a,b)
            elif op == 'multiplication':
                out = calculator.multiplication(a,b)
            else:
                out = calculator.division(a,b)

            return render_template('index.html', output = out)
        
        return render_template('index.html', output = out)

    #catching the raised exception if any, except ValueError     
    except Exception as e:
        print('Error: ',e)


if __name__=="__main__":
    app.run(debug=True)


