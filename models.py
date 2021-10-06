from django.db import models

# Create your models here.
class Job(models.Model):
    role_name = models.CharField(max_length=300)
    role_description = models.CharField(max_length=3000)
    company_name = models.CharField(max_length=300)
    company_description = models.CharField(max_length=30000)
    role_requirements = models.CharField(max_length=3000)
    location = models.CharField(max_length=300)
    minimum_salary = models.IntegerField()
    maximum_salary = models.IntegerField()


def create_jobs(role_name, role_description, company_name, company_description, role_requirements, location, minimum_salary, maximum_salary):
    new_job= Job(role_name=role_name, role_description=role_description, company_name=company_name, company_description=company_description, role_requirements=role_requirements, location=location, minimum_salary=minimum_salary, maximum_salary=maximum_salary)
    new_job.save()
    return new_job
    

def all_jobs():
    return Job.objects.all()

def job_locations(location):
    return Job.objects.filter(location=location)

def find_jobs_by_name(role_name):
    try:
        return Job.objects.get(role_name=role_name)
    except Job.DoesNotExist:
        return None

def goal_salary(minimum_salary, maximum_salary):
    return Job.objects.filter(minimum_salary=minimum_salary, maximum_salary=maximum_salary)


def delete_Job(role_name):
    Job = find_jobs_by_name(role_name)
    Job.delete()


def update_job(role_name, location):
    Job.objects.filter(role_name=role_name).update(location=location)