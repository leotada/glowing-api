# glowing-api

# How to run without docker

Using Python 3.11:

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python app.py

# How to get account balance
```
curl --location 'http://127.0.0.1:5000/bank_account/1'
```

The number is the ID of bank account.

# How to execute transactions
```
curl --location --request PUT 'http://127.0.0.1:5000/bank_account' \
--header 'Content-Type: application/json' \
--data '{
    "from": 1,
    "to": 2,
    "value": 35.11
}'
```
The number is the ID of bank account.
