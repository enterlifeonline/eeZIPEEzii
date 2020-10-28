import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from .models import Job


class JobType(DjangoObjectType):
    class Meta:
        model = Job


class Query(graphene.ObjectType):
    jobs = graphene.List(JobType, search=graphene.String())

    def resolve_jobs(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search) |
                Q(title__icontains=search)
            )
            return Job.objects.filter(filter)
        return Job.objects.all()


class CreateJob(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        job = Job(url=url, description=description)
        job.save()

        return CreateJob(
            id=job.id,
            url=job.url,
            description=job.description,
        )


class Mutation(graphene.ObjectType):
    create_job = CreateJob.Field()
