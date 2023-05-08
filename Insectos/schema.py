import graphene
from graphene_django import DjangoObjectType

from .models import Insecto


class InsectoType(DjangoObjectType):
    class Meta:
        model = Insecto


class Query(graphene.ObjectType):
    Insectos = graphene.List(InsectoType)

    def resolve_Insectos(self, info, **kwargs):
        return Insecto.objects.all()
    
    

    # ...code
#1
class CreateInsecto(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    nomcientifico = graphene.String()
    clase= graphene.String()
    orden=graphene.String()
    familia=graphene.String()
    habitat=graphene.String()
    dieta=graphene.String()
    longitud=graphene.String()
    color=graphene.String()
    numalas=graphene.String()
    

    #2
    class Arguments:
        nombre = graphene.String()
        nomcientifico = graphene.String()
        clase= graphene.String()
        orden=graphene.String()
        familia=graphene.String()
        habitat=graphene.String()
        dieta=graphene.String()
        longitud=graphene.String()
        color=graphene.String()
        numalas=graphene.String()
        
    #3
    def mutate(self, info , nombre, nomcientifico, clase, orden, familia, habitat, dieta, longitud, color, numalas):
        Insectos = Insecto(
            nombre=nombre, 
            nomcientifico=nomcientifico, 
            clase=clase, 
            orden=orden, 
            familia=familia, 
            habitat=habitat, 
            dieta=dieta, 
            longitud=longitud, 
            color=color, 
            numalas=numalas,
            
            )
        Insectos.save()

        return CreateInsecto(
            id=Insecto.id,
            nombre=Insectos.nombre,
            nomcientifico=Insectos.nomcientifico,
            clase=Insectos.clase,
            orden=Insectos.orden,
            familia=Insectos.familia,
            habitat=Insectos.habitat,
            dieta=Insectos.dieta,
            longitud=Insectos.longitud,
            color=Insectos.color,
            numalas=Insectos.numalas,
            

        )


#4
class Mutation(graphene.ObjectType):
    create_Insectos = CreateInsecto.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)