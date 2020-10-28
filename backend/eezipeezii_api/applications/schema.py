import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Application
from jobs.schema import JobType
from users.schema import UserType
from jobs.models import Job
from django.contrib.auth import get_user_model


class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application


class Query(graphene.ObjectType):
    applications = graphene.List(ApplicationType)

    def resolve_applications(self, info, **kwargs):
        return Application.objects.all()


class CreateApplication(graphene.Mutation):
    job = graphene.Field(JobType)
    user = graphene.Field(UserType)
    status = graphene.String()
    description = graphene.String()

    class Arguments:
        job_id = graphene.ID()
        # user attribute will be filled in the mutation
        # user = graphene.ID()
        status = graphene.String()
        description = graphene.String()

    def mutate(self, info, job_id, status, description):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Must be logged in to apply to jobs')

        job = Job.objects.filter(id=job_id).first()
        if not job:
            raise Exception('Job does not exist')

        Application.objects.create(
            job=job, user=user, status=status, description=description)

        return CreateApplication(
            job=job,
            user=user,
            status=status,
            description=description,)


class Mutation(graphene.ObjectType):
    create_application = CreateApplication.Field()
