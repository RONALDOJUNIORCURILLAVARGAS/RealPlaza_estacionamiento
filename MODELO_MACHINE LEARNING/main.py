from pyexpat import model
from typing import Optional

from fastapi import FastAPI
from house_class import House
import pickle

app = FastAPI()

@app.on_event("autos")
def load_model():
    global model
    model=pickle.load(open("modelo_autos_ES1.pkl","rb"))

@app.get("/")
def index():
    return {
        "msg": "ML de autos",
        "autor":"ronaldo",
        "email":"hola@gmail.com",
        "org":"RON",
        'api-documentation':"ruraipa.com/docs"
    }


@app.get("/predict")
def read_item(data:House):
    received=data.dict()
    house_attr=[[
        received['Hora_reserva'],
        received['Hora_estacionamiento_Num'],
        received['Hora_retiro_Num'],
        received['TiempoDemorado'].
        received['Dniauto'],
        received['estacionamiento']
    ]]
    hora_reserva=model.predict(house_attr).totlist()[0]
    return {'data': received, "hora_reserva":hora_reserva}

