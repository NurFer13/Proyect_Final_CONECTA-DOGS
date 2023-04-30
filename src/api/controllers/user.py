from api.models import db, User

# import requests
# import json 


def create_user(body):

    try:

        claves_user = body.keys()

        if not "email" in claves_user or not "password" in claves_user or not "name" in claves_user or not "lastName" in claves_user or not "address" in claves_user or not "province" in claves_user or not "postalCode" in claves_user or not "phone" in claves_user or not "country" in claves_user or not "birthdate" in claves_user:
            return {"code": 400, "msg": "Missing data in the forms"}

        # Crear un nuevo usuario en la base de datos
        new_user = User(
            email = body["email"],
            password = body["password"], 
            name = body["name"], 
            lastName = body["lastName"], 
            address = body["address"], 
            province = body["province"], 
            postalCode = int(body["postalCode"]), 
            phone = int(body["phone"]),
            country = body["country"], 
            birthdate = body["birthdate"],
            is_active = True)

        db.session.add(new_user)
        id_user = new_user.id
        
        db.session.commit()

        return {"code": 200, "msg": "All ok", "id": id_user}          #ID para rutas

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}


def get_users():

    try:

    
        # Obtener usuarios de la base de datos
        query = db.select(User).order_by(User.id)
        users = db.session.execute(query).scalars()
        
        # print(users)

        user_list = [user.serialize() for user in users]

        return {"code": 200, "msg": "All ok", "users": user_list}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}


    # users = db.session.execute(db.select(User.email).order_by(User.id)).scalars()
    # users = db.session.execute(db.select([User.name, User.email]).order_by(User.id)).scalars()

    # all_users = User.query.all()
    # # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
    # user_serialized = list(map(lambda user: user.serialize(), all_users))
    # response = {
    #     "result": {
    #         "planets": planet_serialized,
    #         "user": user_serialized
    #     }
    # }
    # return response, 200


def get_user(id):

    try:
    
        # Obtener usuario de la base de datos
        user = db.get_or_404(User, id)
        # user = db.session.execute(db.select(User).filter_by(id)).scalars().one()
        
        return {"code": 200, "msg": "All ok", "user": user.serialize()}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}


def update_user(body, id):

    try:
    
        # Obtener usuario de la base de datos           # NO SE PUEDE PASAR NI ACTUALIZAR UN EMAIL, PORQUE SI MANDAS EL MISMO, COMO ES UNICO DA ERROR
        user = db.get_or_404(User, id)

        user.password = body["password"]
        user.name = body["name"]
        user.lastName = body["lastName"]
        user.address = body["address"]
        user.province = body["province"]
        user.postalCode = int(body["postalCode"])
        user.phone = int(body["phone"])
        user.country = body["country"]
        user.birthdate = body["birthdate"]
        user.aboutMe = body["aboutMe"]
        user.is_active = True

        # if body["userPhoto"]:
        #     cloudinary.uploader.upload(user.name + ".mp4", 
        #         folder = body["userPhoto"],                 # "myfolder/mysubfolder/" 
        #         public_id = user.name,            # "my_dog"
        #         overwrite = True, 
        #         notification_url = "http://res.cloudinary.com/drlf5uatk", 
        #         resource_type = "photo")
        #     res = requests.get('https://api.cloudinary.com/v1_1/drlf5uatk')
        #     response = json.loads(res.text)
        #     user.photo = response

        db.session.commit()

        return {"code": 200, "msg": "User update ok", "user": user.serialize()}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}


def delete_user(id):

    try:
    
        # Obtener usuarios de la base de datos
        user = db.get_or_404(User, id)

        db.session.delete(user)
        db.session.commit()

        # query = db.select(User).order_by(User.id)                 # SI DESPUES NECESITA UNA LISTA COMPLETA ACTUALIZADA
        # users = db.session.execute(query).scalars()


        return {"code": 200, "msg": "Delete user ok"}

    except Exception as error:
        print(error)
        return {"code": 500, "msg": "Error in server, something was wrong"}







# selected_member = [member for member in users if member["id"] == id]
# try:       
#         new_member = {     
#         "id": member.get("id",self._generateId()),
#         "first_name": member["first_name"],
#         "last_name": self.last_name,
#         "age": member["age"],
#         "lucky_numbers": member["lucky_numbers"]
#         }

#         self._members.append(new_member)

#         return {"code": 200, "mensaje": "Todo ha ido bien", "members": self._members}

#     except:
#         return {"code": 500}  