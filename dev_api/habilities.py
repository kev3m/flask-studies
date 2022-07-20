from ast import Delete
from flask import Flask, request
from flask_restful import Resource
import json

habilities_List = ['Python','Java','Flask', 'PHP','Go','C','C++','C#']

class Habilities(Resource):
    def get(self):
        return habilities_List

    #Insere uma nova habilidade
    def post(self):
        new_hability = json.loads(request.data)
        habilities_List.append(new_hability)
        return habilities_List

class HabilitiesList_manipulation(Resource):
    
    #Altera o nome da habilidade na posição indicada(id)
    def put(self,id):
        new_hability = json.loads(request.data)
        habilities_List[id] = new_hability
        return habilities_List
    
    #Remove a habilidade na posição indicada
    def delete(self,id):
        habilities_List.pop(id)
        return habilities_List
