from flask import Flask, request
from flask_restful import Resource, Api

app = Flask (__name__) ## instance of this API through Flask class, __name__ becomes main
api = Api(app) ## put instance of Flask class into API class 

table={"Alexey":100,"Dima":50}

class Balance(Resource): 
    '''this resource shows balance of a specific account''' 
    def get(self,name):
        return {
                "name": name,
                "balance": table[name]
                }

class Ledger(Resource):
    '''this resource shows balances for all accounts''' 
    def get(self):
        return [{"name":key,"balance":value} for key,value in table.items()]
    
class Transaction(Resource):
    '''this resource allows for sendig money between accounts''' 
    def post(self):
        sender = request.form['sender']
        receiver = request.form['receiver']
        amount = int(request.form['amount'])
   
        table[sender]=table[sender]-amount
        table[receiver]=table[receiver]+amount

        return {
            "sender":sender,
            "receiver":receiver,
            "amount":amount,
            "message":sender+" sent $"+str(amount)+" to "+receiver
            }

api.add_resource(Balance,'/balances/<string:name>')
api.add_resource(Ledger,'/balances')
api.add_resource(Transaction,'/transaction')

if __name__ == '__main__': #when you import the app,__name__ = name of the app e.g. "api" in this case;
    
    app.run(debug=True) #each time you run the app, the __name__ automatically turns into __main__