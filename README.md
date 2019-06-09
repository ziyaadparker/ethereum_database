# Ethereum Web Database

Use the csv file generated from https://github.com/ziyaadparker/eth-secure.git
The csv file will now contain possible ethereum private and public keys.

Follow below code to import the data into the database.

```bash
git clone https://github.com/ziyaadparker/ethereum_database.git
cd ethereum_database
python import_csv_data.py
```
You will now have imported the csv file with private and public ethereum keys.

Now run the code to display the date in the web interface.

```bash
python manage.py runserver
```

Feel free to fork and contribute. 
