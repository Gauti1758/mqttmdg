import mysql.connector
import json
from flask import make_response, request

class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tigersingh",
            database="flask_tutorial")

            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Some error")    

    #Get all details of user Model       
    def user_getall_model(self):
        try:
            self.cur.execute("SELECT * FROM users")
            result=self.cur.fetchall()
            if len(result)>0 :
                res = make_response({"payload":result},200)
                res.headers['Access-Control-Allow-Origin']='*'
                return res
                # return json.dumps(result)
            else:
                return make_response({"message":"No data found"},204)
        except:
            return make_response({"message":"Get error in Table or Queary"},204)
        # finally:
        #     self.cur.close()
        #     self.con.close()

    #Get by id user model
    def user_getById_model(self,id):
        try:
            self.cur.execute(f"SELECT * FROM users WHERE id={id}")
            result = self.cur.fetchone()
            if result is not None:
                res = make_response({"payload": result}, 200)
                res.headers['Access-Control-Allow-Origin'] = '*'
                return res
            else:
                return make_response({"message": "No data found"}, 204)
        except:
            return make_response({"message": "Error in Table or Query"}, 204)

    #Post Api of user model
    def user_postone_model(self,data):
        # self.cur.execute(f"insert into users(name,email,phone,role,password) values('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        # return make_response({"message":"User created successfuly"},201)

        #For Retrieve JSON data from the request
        json_data = request.get_json()  
        self.cur.execute(f"INSERT INTO users (name, email, phone, role, password) VALUES ('{json_data['name']}', '{json_data['email']}', '{json_data['phone']}', '{json_data['role']}', '{json_data['password']}')")
        return make_response({"message": "User created successfully"}, 201)
    
    #update api of user model
    def user_update_model(self,data):
        data=request.get_json()
        self.cur.execute(f"update users set name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' where id= {data['id']} ")
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfuly"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
        
    #delete api of user model
    def user_delete_model(self,id):
        self.cur.execute(f'delete from users where id={id}')
        if self.cur.rowcount>0:
            return make_response({"message":"User deleted successfuly"},200)
        else:
            return make_response({"message":"Nothing to delete"},202)
        
    #update specific row
    def user_patch_model(self,data,id):
        data=request.get_json()
        qry="update users set "
        for key in data:
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" where id={id}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfuly"},201)
        else:
            return make_response({"message":"Nothing to update"},202)
        # print(qry)
        # return "patch data from user model"

    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        try:
            if limit != 0:
                start=(limit * page) - page
                qry=f"select * from users LIMIT {start},{page}"
                self.cur.execute(qry)
                result=self.cur.fetchall()
                if len(result) > 0:
                    res=make_response({"payload":result,"limit":limit,"page_no":page},200)
                    return res
                else:
                    return make_response({"message":"No Data Foune"},204)
        except:
            return make_response({"message":"limit can't be 0"},500)