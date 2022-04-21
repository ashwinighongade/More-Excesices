import json

a={
    "users": [{
            "firstName": "vidur",
            "lastName": "singla",
            "details": {
                "age": 21,
                "mobileNo": 1234567890,
                "City": "Delhi"
            }
        },
        {
            "firstName": "rishabh",
            "lastName": "verma",
            "details": {
                "age": 22,
                "mobileNo": 12345678320,
                "City": "Chandigarh"
            }
        },
        {
            "firstName": "abhishek",
            "lastName": "gupta",
            "details": {
                "age": 25,
                "mobileNo": 12332567890,
                "City": "Gurgaon"
            }
        }
    ]
}



out_file= open("users.json","w")
json.dump(a,out_file,indent=4)
out_file.close()

with open('users.json') as f:    
    data = json.load(f)

users = data['users']
for i in data:
    # print(i)
    for j in users:
        print("user full name is"+ j["firstName"]+ " "+j["lastName"])
        print("user mobile number is",j["details"]["mobileNo"])
        print("user age is",j["details"]["age"])
        print("user city is",j["details"]["City"])
        
