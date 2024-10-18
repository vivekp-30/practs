## Q. Create a JSON file and persist it in any database.

1. Create and Save the JSON file to your system.

2. Use the `mongoimport` tool to import the JSON data into a MongoDB database to persist.

---

### Step1: Create a sample JSON file like this (use different data):
users.json
```json
[
  {
    "username": "john_doe",
    "password": "hashed_password_123",
    "email": "john@example.com",
    "isAdmin": false
  },
  {
    "username": "jane_smith",
    "password": "hashed_password_456",
    "email": "jane@example.com",
    "isAdmin": true
  },
  {
    "username": "michael_brown",
    "password": "hashed_password_789",
    "email": "michael@example.com",
    "isAdmin": false
  }
]
```

### Step2: Persist the JSON file in MongoDB

#### 1. **Install MongoDB Tools (if not installed)**
You need MongoDB tools to import data from the JSON file to MongoDB. Download and install them from:

[MongoDB Tools Download](https://www.mongodb.com/try/download/database-tools)

#### 2. **Use the `mongoimport` command**
Once you have the MongoDB tools set up, use the following command to import the JSON file into MongoDB:

```bash
mongoimport --db UserDB --collection users --file path/to/users.json --jsonArray
```

**Explanation:**
- `UserDB`: The database where the data will be imported.
- `users`: The collection where the data will be stored.
- `path/to/users.json`: The location of your JSON file.
- `--jsonArray`: Specifies that the file contains an array of documents.


### Step3: Verify the Data in MongoDB

After importing, you can verify that the data has been inserted into your MongoDB collection:

1. Open your MongoDB shell or a GUI tool like **MongoDB Compass**.
2. Switch to the database you used in the `mongoimport` command (e.g., `UserDB`).
3. Query the `users` collection to verify the inserted documents:

   ```javascript
   db.users.find().pretty()
   ```

You should see all the documents from the users.json file stored in the `users` collection in the MongoDB which will persist this JSON data.
