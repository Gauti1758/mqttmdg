from flask import request
from app import app
from model.user_model import user_model

obj = user_model()
@app.route("/user/getall")
def getall():
    return obj.user_getall_model()

@app.route("/user/getById/<int:id>")
def getById(id):
    return obj.user_getById_model(id)

@app.route("/user/postone",methods=['POST'])
def postone():
    return obj.user_postone_model(request.get_json())
    # return obj.user_postone_model(request.form)

@app.route("/user/update",methods=['PUT'])
def update():
    # return obj.user_update_model(request.form)
    return obj.user_update_model(request.get_json())

@app.route("/user/delete/<id>",methods=['DELETE'])
def delete(id):
    return obj.user_delete_model(id)

@app.route("/user/patch/<id>",methods=['PATCH'])
def patch(id):
    return obj.user_patch_model(request.get_json(),id)

@app.route("/user/getall/limit/<limit>/page/<page>",methods=['GET'])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)