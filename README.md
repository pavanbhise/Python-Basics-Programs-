import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Certificate:
    def __init__(self, student_name, gender, dbo, course, year):
        self.student_name = student_name
        self.gender = gender
        self.dbo = dbo
        self.course = course
        self.year = year

    def bonafide(self):
        pronoun = 'He' if self.gender.lower() == 'male' else 'She'
        possessive_pronoun = 'his' if self.gender.lower() == 'male' else 'her'

        return f"""
        Date: {current_time}
        **********************************
        *        BONAFIDE CERTIFICATE        *
        **********************************
        This is to certify that Mr./Ms. {self.student_name} is a bonafide student of this college studying in B.Tech {self.year} Electronic Engineering ({self.course}) during the academic year 2024-2025.
        {possessive_pronoun} date of birth as per college register is {self.dbo}.  
        {pronoun} conduct and progress is satisfactory to the best of my knowledge.
        {pronoun} bears a good moral character.

        ____________________________
        Signature of the Principal
        """


S1 = Certificate('Pavan', 'male', '17/02/2004', 'VLSI', 'Second Year')

print(S1.bonafide())
