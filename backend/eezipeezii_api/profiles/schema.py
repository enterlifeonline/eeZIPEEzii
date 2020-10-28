import graphene
from graphene_django import DjangoObjectType

from .models import Profile
from .models import Education
from .models import Experience


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class EducationType(DjangoObjectType):
    class Meta:
        model = Education


class ExperienceType(DjangoObjectType):
    class Meta:
        model = Experience


class Query(graphene.ObjectType):
    Profiles = graphene.List(ProfileType)

    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()


class CreateProfile(graphene.Mutation):
    user = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()
    address_line_one = graphene.String()
    address_line_two = graphene.String()
    city = graphene.String()
    state = graphene.String()
    postal_code = graphene.Int()
    phone_country_code = graphene.String()
    phone_extension = graphene.String()
    phone_number = graphene.Int()
    hear_about_us = graphene.String()
    previously_employed_by_company = graphene.Boolean()

    class Arguments:
        user = graphene.ID()
        first_name = graphene.String()
        last_name = graphene.String()
        address_line_one = graphene.String()
        address_line_two = graphene.String()
        city = graphene.String()
        state = graphene.String()
        postal_code = graphene.Int()
        phone_country_code = graphene.String()
        phone_extension = graphene.String()
        phone_number = graphene.Int()
        hear_about_us = graphene.String()
        previously_employed_by_company = graphene.Boolean()

    def mutate(self, user, first_name, last_name, address_line_one, address_line_two, city, state, postal_code, phone_country_code, phone_extension, phone_number, hear_about_us, previously_employed):
        profile = Profile(
            user=user, first_name=first_name, last_name=last_name, address_line_one=address_line_one, address_line_two=address_line_two, city=city, state=state, postal_code=postal_code, phone_country_code=phone_country_code, phone_extension=phone_extension, phone_number=phone_number, hear_about_us=hear_about_us, previously_employed=previously_employed)
        profile.save()

        return CreateProfile(
            user=profile.user,
            first_name=profile.first_name,
            last_name=profile.last_name,
            address_line_one=profile.address_line_one,
            address_line_two=profile.address_line_two,
            city=profile.city,
            state=profile.state,
            postal_code=profile.postal_code,
            phone_country_code=profile.phone_country_code,
            phone_extension=profile.phone_extension,
            phone_number=profile.phone_number,
            hear_about_us=profile.hear_about_us,
            previously_employed_by_company=profile.previously_employed_by_company,
        )


class CreateExperience(graphene.Mutation):
    profile = graphene.ID()
    title = graphene.String()
    company = graphene.String()
    location = graphene.String()
    start_date = graphene.DateTime()
    end_date = graphene.DateTime()
    current_job = graphene.Boolean()
    role_description = graphene.String()

    class Arguments:
        profile = graphene.ID()
        title = graphene.String()
        company = graphene.String()
        location = graphene.String()
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()
        current_job = graphene.Boolean()
        role_description = graphene.String()

    def mutate(self, profile, title, company, location, start_date, end_date, current_job, role_description):
        experience = Experience(
            profile=profile, title=title, company=company, location=location, start_date=start_date, end_date=end_date, current_job=current_job, role_description=role_description)
        experience.save()

        return CreateExperience(
            profile=experience.profile,
            title=experience.title,
            company=experience.company,
            location=experience.location,
            start_date=experience.start_date,
            end_date=experience.end_date,
            current_job=experience.current_job,
            role_description=experience.role_description,
        )


class CreateEducation(graphene.Mutation):
    profile = graphene.ID()
    university = graphene.String()
    degree = graphene.String()
    start_date = graphene.DateTime()
    end_date = graphene.DateTime()
    major = graphene.String()
    GPA = graphene.Float()

    class Arguments:
        profile = graphene.ID()
        university = graphene.String()
        degree = graphene.String()
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()
        major = graphene.String()
        GPA = graphene.Float()

    def mutate(self, profile, university, degree, start_date, end_date, major, GPA):
        education = Education(
            profile=profile, university=university, degree=degree, start_date=start_date, end_date=end_date, major=major, GPA=GPA)
        education.save()

        return CreateEducation(
            profile=education.profile,
            university=education.university,
            degree=education.degree,
            start_date=education.start_date,
            end_date=education.end_date,
            major=education.major,
            GPA=education.GPA,
        )


class Mutation(graphene.ObjectType):
    create_profile = CreateProfile.Field()
    create_experience = CreateExperience.Field()
    create_education = CreateEducation.Field()
