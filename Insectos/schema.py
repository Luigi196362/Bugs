import graphene
from graphene_django import DjangoObjectType
from Insectos.models import Insecto, Vote
from graphql import GraphQLError
from django.db.models import Q
from users.schema import UserType


from .models import Insecto


class InsectoType(DjangoObjectType):
    class Meta:
        model = Insecto

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    Insectos = graphene.List(InsectoType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_Insectos(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(nombre__icontains=search) |
                Q(color__icontains=search)
            )
            return Insecto.objects.filter(filter)
        
        return Insecto.objects.all()
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

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
    posted_by = graphene.Field(UserType)
    

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
        
        user = info.context.user or None

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
            posted_by=user
            
            )
        Insectos.save()

        return CreateInsecto(
            id=Insectos.id,
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
            posted_by=Insectos.posted_by
        )

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    insecto = graphene.Field(InsectoType)

    class Arguments:
        insecto_id = graphene.Int()

    def mutate(self, info, insecto_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Debes iniciar sesión para votar.')

        insecto = Insecto.objects.filter(id=insecto_id).first()
        if not insecto:
            raise GraphQLError('Insecto no válido.')

        Vote.objects.create(
            user=user,
            insecto=insecto
        )

        return CreateVote(user=user, insecto=insecto)

#4
class Mutation(graphene.ObjectType):
    create_Insectos = CreateInsecto.Field()
    create_link = CreateInsecto.Field()
    create_vote = CreateVote.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)