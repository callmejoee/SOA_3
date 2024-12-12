class Language:
    def __init__(self, language_name, score_out_of_100):
        self.language_name = language_name
        self.score_out_of_100 = score_out_of_100

class Employee:
    def __init__(self, first_name, last_name, employee_id, designation, known_languages):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.designation = designation
        self.known_languages = known_languages

    def to_dict(self):
        return {
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "EmployeeID": self.employee_id,
            "Designation": self.designation,
            "KnownLanguages": [
                {"LanguageName": lang.language_name, "ScoreOutof100": lang.score_out_of_100}
                for lang in self.known_languages
            ]
        }

    @classmethod
    def from_dict(cls, data):
        known_languages = [Language(lang['LanguageName'], lang['ScoreOutof100']) for lang in data['KnownLanguages']]
        return cls(data['FirstName'], data['LastName'], data['EmployeeID'], data['Designation'], known_languages)
