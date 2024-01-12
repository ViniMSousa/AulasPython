usuarios = {}

usuarios = {
    "chaves" : ["Chaves do 8", "24/12/2017", "Recepc_01"],
    "quico" : ["Quico das Flores", "20/12/2017", "Raiox_03"]
}
print(usuarios)

usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]

print(usuarios)

print("###---###")
print(usuarios.get("quico"))