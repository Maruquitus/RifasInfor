from flask import Flask, redirect, url_for, request
import planilha
app = Flask(__name__)

@app.route('/postRequest',methods = ['POST', 'GET'])
def postRequest():
   if request.method == 'POST':
      print("Atualizando...")
      planilha.updateTask()
      return "Successo!"
   else:
      return "Não autorizado"

if __name__ == '__main__':
   app.run()