import json
with open ("database.json", "w") as file:
	json.dump("data", file)
	file.write("[]")
	file.close()
print("t\ne\ns\nt")
