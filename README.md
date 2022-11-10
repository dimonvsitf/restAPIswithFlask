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


    Response example:
    