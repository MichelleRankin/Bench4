from django.test import TestCase
from app import models
# Create your tests here.

class TestJob(TestCase):
    def test_can_create_job(self):
        job = models.create_jobs(
            "Manager",
            "Work hard to guide workers",
            "CSpire",
            "We're a tech company run on hard work and determination.",
            "Previous, experience",
            "Oxford, Ms",
            30000,
            60000,
        )
        self.assertEqual(job.id, 1)
        self.assertEqual(job.role_name, "Manager")
        self.assertEqual(job.role_description, "Work hard to guide workers")
        self.assertEqual(job.company_name, "CSpire")
        self.assertEqual(job.company_description, "We're a tech company run on hard work and determination.")
        self.assertEqual(job.role_requirements, "Previous, experience")
        self.assertEqual(job.location, "Oxford, Ms")
        self.assertEqual(job.minimum_salary, 30000)
        self.assertEqual(job.maximum_salary, 60000)

    def test_can_view_all_jobs(self):
        jobs_list= [ 
            {
                "role_name": "Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 30000,
                "maximum_salary": 60000,
                },

            {
                "role_name": "Assistant Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 20000,
                "maximum_salary": 50000,
                },

            {
                "role_name": "Worker",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 10000,
                "maximum_salary": 40000,
                },
        ]

        for job_list in jobs_list:
            models.create_jobs(
                job_list["role_name"],
                job_list["role_description"],
                job_list["company_name"],
                job_list["company_description"],
                job_list["role_requirement"],
                job_list["location"],
                job_list["minimum_salary"],
                job_list["maximum_salary"],

            )

        jobs = models.all_jobs()
        self.assertEqual(len(jobs), len(jobs_list))


        jobs_list = sorted(jobs_list, key=lambda c: c["role_name"])
        jobs = sorted(jobs, key=lambda c: c.role_name)

        for data, job in zip(jobs_list, jobs):
            self.assertEqual(data["role_name"], job.role_name)
            self.assertEqual(data["role_description"], job.role_description )
            self.assertEqual(data["company_name"],job.company_name)
            self.assertEqual(data["company_description"], job.company_description)
            self.assertEqual(data["role_requirement"], job.role_requirements)
            self.assertEqual(data["location"], job.location)
            self.assertEqual(data["minimum_salary"], job.minimum_salary)
            self.assertEqual(data["maximum_salary"], job.maximum_salary)





    def test_can_search_by_jobs(self):
        jobs_list= [ 
            {
                "role_name": "Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 30000,
                "maximum_salary": 60000,
                },

            {
                "role_name": "Assistant Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 20000,
                "maximum_salary": 50000,
                },

            {
                "role_name": "Worker",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 10000,
                "maximum_salary": 40000,
                },
        ]

        for job_list in jobs_list:
            models.create_jobs(
                job_list["role_name"],
                job_list["role_description"],
                job_list["company_name"],
                job_list["company_description"],
                job_list["role_requirement"],
                job_list["location"],
                job_list["minimum_salary"],
                job_list["maximum_salary"],

            )



        jobs = models.all_jobs()
        self.assertEqual(len(jobs), len(jobs_list))


        jobs_list = sorted(jobs_list, key=lambda c: c["role_name"])
        jobs = sorted(jobs, key=lambda c: c.role_name)

        for data, job in zip(jobs_list, jobs):
            self.assertEqual(data["role_name"], job.role_name)
            self.assertEqual(data["role_description"], job.role_description )
            self.assertEqual(data["company_name"],job.company_name)
            self.assertEqual(data["company_description"], job.company_description)
            self.assertEqual(data["role_requirement"], job.role_requirements)
            self.assertEqual(data["location"], job.location)
            self.assertEqual(data["minimum_salary"], job.minimum_salary)
            self.assertEqual(data["maximum_salary"], job.maximum_salary)


        self.assertIsNone(models.find_jobs_by_name("aousnth"))

        Job = models.find_jobs_by_name("Manager")

        self.assertIsNotNone(job)
        self.assertEqual(job.company_name, "CSpire")


    def test_can_view_location(self):
        jobs_list= [ 
            {
                "role_name": "Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 30000,
                "maximum_salary": 60000,
                },

            {
                "role_name": "Assistant Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 20000,
                "maximum_salary": 50000,
                },

            {
                "role_name": "Worker",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 10000,
                "maximum_salary": 40000,
                },
        ]

        for job_list in jobs_list:
            models.create_jobs(
                job_list["role_name"],
                job_list["role_description"],
                job_list["company_name"],
                job_list["company_description"],
                job_list["role_requirement"],
                job_list["location"],
                job_list["minimum_salary"],
                job_list["maximum_salary"],

        )



        jobs = models.all_jobs()
        self.assertEqual(len(jobs), len(jobs_list))


        jobs_list = sorted(jobs_list, key=lambda c: c["role_name"])
        jobs = sorted(jobs, key=lambda c: c.role_name)

        for data, job in zip(jobs_list, jobs):
            self.assertEqual(data["role_name"], job.role_name)
            self.assertEqual(data["role_description"], job.role_description )
            self.assertEqual(data["company_name"],job.company_name)
            self.assertEqual(data["company_description"], job.company_description)
            self.assertEqual(data["role_requirement"], job.role_requirements)
            self.assertEqual(data["location"], job.location)
            self.assertEqual(data["minimum_salary"], job.minimum_salary)
            self.assertEqual(data["maximum_salary"], job.maximum_salary)

        self.assertEqual(len(models.job_locations(job.location)), 3)



    def test_can_update(self):
        jobs_list= [ 
            {
                "role_name": "Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 30000,
                "maximum_salary": 60000,
                },

            {
                "role_name": "Assistant Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 20000,
                "maximum_salary": 50000,
                },

            {
                "role_name": "Worker",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 10000,
                "maximum_salary": 40000,
                },
        ]

        for job_list in jobs_list:
            models.create_jobs(
                job_list["role_name"],
                job_list["role_description"],
                job_list["company_name"],
                job_list["company_description"],
                job_list["role_requirement"],
                job_list["location"],
                job_list["minimum_salary"],
                job_list["maximum_salary"],

        )



        jobs = models.all_jobs()
        self.assertEqual(len(jobs), len(jobs_list))


        jobs_list = sorted(jobs_list, key=lambda c: c["role_name"])
        jobs = sorted(jobs, key=lambda c: c.role_name)

        for data, job in zip(jobs_list, jobs):
            self.assertEqual(data["role_name"], job.role_name)
            self.assertEqual(data["role_description"], job.role_description )
            self.assertEqual(data["company_name"],job.company_name)
            self.assertEqual(data["company_description"], job.company_description)
            self.assertEqual(data["role_requirement"], job.role_requirements)
            self.assertEqual(data["location"], job.location)
            self.assertEqual(data["minimum_salary"], job.minimum_salary)
            self.assertEqual(data["maximum_salary"], job.maximum_salary)


        models.update_job("Manager", "Water Valley")

        self.assertEqual(
            models.find_jobs_by_name("Manager").location, "Water Valley"
        )



def test_delete(self):        
        jobs_list= [ 
            {
                "role_name": "Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 30000,
                "maximum_salary": 60000,
                },

            {
                "role_name": "Assistant Manager",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 20000,
                "maximum_salary": 50000,
                },

            {
                "role_name": "Worker",
                "role_description": "Work hard to guide workers",
                "company_name": "CSpire",
                "company_description": "We're a tech company run on hard work and determination.",
                "role_requirement":"Previous, experience",
                "location":"Oxford, Ms",
                "minimum_salary": 10000,
                "maximum_salary": 40000,
                },
        ]

        for job_list in jobs_list:
            models.create_jobs(
                job_list["role_name"],
                job_list["role_description"],
                job_list["company_name"],
                job_list["company_description"],
                job_list["role_requirement"],
                job_list["location"],
                job_list["minimum_salary"],
                job_list["maximum_salary"],

        )



        jobs = models.all_jobs()
        self.assertEqual(len(jobs), len(jobs_list))


        jobs_list = sorted(jobs_list, key=lambda c: c["role_name"])
        jobs = sorted(jobs, key=lambda c: c.role_name)


        for data, job in zip(jobs_list, jobs):
            self.assertEqual(data["role_name"], job.role_name)
            self.assertEqual(data["role_description"], job.role_description )
            self.assertEqual(data["company_name"],job.company_name)
            self.assertEqual(data["company_description"], job.company_description)
            self.assertEqual(data["role_requirement"], job.role_requirements)
            self.assertEqual(data["location"], job.location)
            self.assertEqual(data["minimum_salary"], job.minimum_salary)
            self.assertEqual(data["maximum_salary"], job.maximum_salary)

        models.delete_Job("Worker")

        self.assertEqual(len(models.all_jobs()), 2)