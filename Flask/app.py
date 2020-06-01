import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#On créer l'API Flask 
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#On lui donne une adresse pour l'entrée de la requête
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

#On itère dans les valeurs passé au formulaire
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

#On effectue la prédiction sur les données du formulaire
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

#On affiche le résutat et la template
    return render_template('index.html', prediction_text='Les ventes du trimestre seront de € {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    
#On renvoie la prédiction au format JSON
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
