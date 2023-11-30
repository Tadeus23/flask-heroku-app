
class CVData:
    def __init__(self):
        self.data = {
            "personal_info": {
                "name": "Catalin-Gabriel Popescu",
                "job": "Software Developer",
                "email": "popescu351@gmail.com",
                "phone": "+40751540992",
            },
            "experience_data": [
                {"title": "Software Developer", "company": "IPTE Germany GmbH Factory automation", "year": 2018},
                {"title": "Junior Software Developer", "company": "IPTE Sibiu Factory automation", "year": 2016},
                {"title": "System Engineer", "company": "Atexis SRL Iasi Systems solution", "year": 2015},
            ],
            "education_data": [
                {"degree": "Master of Engineering", "major": "Environmental monitoring computer systems", "year_start": 2015, "year_end": 2017},
                {"degree": "Bachelor of Engineering", "major": "Engineering in instrumentation and data acquisition", "year_start": 2011, "year_end": 2015},
            ],
            "skills_data": [
                {"skill": "IEC 61131-3", "years_exp": ">5 years"},
                {"skill": "C#", "years_exp": "2 years"},
                {"skill": "Python", "years_exp": "1.5 years"},
            ],
            "certifications_data": [
                {"name": "AWS Cloud Practitioner CLF-02", "institute": "Amazon Web Services", "period": "November 2023"},
                {"name": "Python Development Industry", "institute": "Brainnest Solutions","period": "Jan-March 2023"},
                {"name": "Microsoft .NET: C# training", "institute": "Strongbytes Iasi","period": "May-June 2016"},
            ]
        }