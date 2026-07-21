capitals = {
    "France": {"city": "Paris", "greeting": "Bonjour"},
    "Spain": {"city": "Madrid", "greeting": "Hola"},
    "Germany": {"city": "Berlin", "greeting": "Hallo"},
    "Italy": {"city": "Rome", "greeting": "Ciao"},
}

for capital in capitals:
    print(f"The capital of {capital} is {capitals[capital]['city']}.")
    print(f"Greeting in {capital}: {capitals[capital]['greeting']}")

capitals["Japan"] = {"city": "Tokyo", "greeting": "Konnichiwa"}
capitals.pop("Germany")
capitals.update({"Italy": {"city": "Turin", "greeting": "Ciao"}, "Portugal": {"city": "Porto", "greeting": "Olá"}})
capitals.setdefault("Brazil", {"city": "Brasilia", "greeting": "Olá"})
print(capitals)
print(capitals.items())
for key, value in capitals.items():
    for sub_key, sub_value in value.items():
        print(f"{key} {sub_key}: {sub_value}")
        print(f"{key = }, {sub_key = }, {sub_value = }")