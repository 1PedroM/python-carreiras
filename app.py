from logging import debug
from flask import Flask, render_template, flash, redirect, url_for, jsonify


app = Flask(__name__)

VAGAS =[
   {
     "id": 1,
     "nome": "Analista de Sistemas",
     "localidade": "Niteroi, RJ",
     "salario": "R$ 4000"
   },
   {
       "id": 2,
       "nome": "Analista de dados",
       "localidade": "Rio de Janeiro, RJ",
       "salario": "R$ 5000"
  },
  {
     "id": 1,
     "nome": "Cientista de dados",
     "localidade": "São Gonçalo, RJ",
     "salario": "R$ 8000"
   }
]


@app.route('/')
def inicio():
  return render_template("inicio.html", vagas=VAGAS)


@app.route('/api/vagas')
def api_vagas():
  return jsonify(VAGAS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  