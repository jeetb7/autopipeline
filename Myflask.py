from flask import Flask,jsonify, make_response, request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'




orders={
    "order1":{
        "size":"small",
        "toppins":"cheese",
        "crust":"thin"
    }
}

@app.route("/orders")
def get_order():
    response=make_response(jsonify(orders),200)
    return response


@app.route("/orders/<orderID>")
def get_order_details(orderID):
    if orderID in orders:
        response=make_response(jsonify(orders[orderID]),200)
        return response
    return "Order  not found"

@app.route("/orders/<orderID>/<items>")
def get_item_details(orderID,items):
    item=orders[orderID].get(items)
    if item:
        response=make_response(jsonify(item),200)
        return response
    
    return "Order  not found"


@app.route("/orders/<orderID>",methods=["POST"])
def post_order_details(orderID):
    req=request.get_json()
    if orderID in orders:
        response=make_response(jsonify({"error:Order ID already exists"}),200)
        return response
    orders.update({orderID:req})
    response=make_response(jsonify({"messege":"New order created"}),200)
    return response




if __name__=="__main__":
    app.run(host='0.0.0.0', port=4500)
            