dog = dict()
dog = {"name": "Asier", "color": "Whitereed": "pug", "legs": 4, "age": 17}
student_dictionary = {
    "first_name": "Asier",
    "last_name": "Martin",
    "gender": "M",
    "age": 17,
    "marital_status": "unmarried",
    "skills": ["procrastinating"],
    "country": "spain",
    "city": "jerez",
    "address": "la granjat",
}
print(len(student_dictionary))
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))
student_dictionary["skills"].append("Sleeping")
list_keys = list(student_dictionary.keys())
list_values = list(student_dictionary.values())
list_of_tuples = [(k, v) for k, v in student_dictionary.items()]
student_dictionary.pop("marital_status")
del dog