This README file refers to banking.py app. Please ignore api.py - I used it to follow along a tutorial from https://flask-restful.readthedocs.io/en/latest/quickstart.html

Objective: create a TABLE that keeps track of funds moving between wallets.

in the ledger, we want to know:
1. wallet_id
2. balance

resources we need:
- show a wallet balance & ids
    GET /balances/name
    
    Response example(200):
        {
            "name": string,
            "balance": integer
        }

- show balance of all wallets
    GET /balances

    Response example(200):
    [
        {
            "wallet id": string,
            "balance": integer
        },
        ...
    ]

- update balances whenever there's a change (transaction)
    POST /transaction

    -H: authorisation

    -d:{sender: wallet id, 
        receiver: wallet id,
        amount: integer}
    
    Request example:
    post('http://localhost:5000/transaction',
        data={
            "sender":"Alexey",
            "receiver":"Dima",
            "amount":25
            }
        ).json()

    Response example(200):
    {
        'sender': 'Alexey',
        'receiver': 'Dima',
        'amount': 25,
        'message': 'Alexey sent $25 to Dima'
        }
    