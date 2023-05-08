from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from Insectos.schema import schema
from Insectos.models import Insecto

Insectos_QUERY = '''
 {Insectos{ 
    id
    nombre
    nomcientifico 
    clase 
    orden 
    familia 
    habitat 
    dieta 
    longitud 
    color 
    numalas
    descripcion}}
'''
CREATE_Insectos_MUTATION = '''
mutation createInsectosMutation($nombre: String, $nomcientifico: String, $clase: String, $orden: String, $familia: String, $habitat: String, $dieta: String, $longitud: String, $color: String, $numalas: String, $descripcion: String){
 createInsectos(nombre: $nombre, nomcientifico: $nomcientifico, clase: $clase, orden: $orden, familia: $familia, habitat: $habitat, dieta: $dieta, longitud: $longitud, color: $color, numalas: $numalas, descripcion: $descripcion){
  nombre
  nomcientifico
  clase
  orden
  familia
  habitat
  dieta
  longitud
  color
  numalas
  descripcion
 }
}
'''

class InsectoTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.Insecto1 = mixer.blend(Insecto)
        self.Insecto2 = mixer.blend(Insecto)

    def test_Insectos_query(self):
        response = self.query(
            Insectos_QUERY,
        )


        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query Insectos results")
        print (content)
        assert len(content['data']['Insectos']) == 2

    def test_createInsectos_mutation(self):

        response = self.query(
            CREATE_Insectos_MUTATION,
            variables={'nombre': "a", 'nomcientifico': "a", 'clase': "a", 'orden': "a", 
                       'familia': "a", 'habitat': "a", 
                       'dieta': "a", 
                       'longitud': "a", 'color': "a", 
                       'numalas': "a",'descripcion': "a"}
        )
        print('mutation')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createInsectos": {"nombre": "a", 'nomcientifico': "a", 'clase': "a", 
                                                 'orden': "a", 'familia': "a", 
                                                 'habitat': "a", 
                                                 'dieta': "a", 
                                                 'longitud': "a", 'color': "a", 
                                                 'numalas': "a",'numalas': "a"}}, content['data'])