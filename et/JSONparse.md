## Q. Create a JSON file and parse it.

### Step 1: Create a JSON File

Example:
**`users.json`** (use different file and data)
```json
[
  {
    "username": "john_doe",
    "password": "securepassword123",
    "email": "john.doe@example.com",
    "isAdmin": false
  },
  {
    "username": "jane_smith",
    "password": "mypassword456",
    "email": "jane.smith@example.com",
    "isAdmin": true
  },
  {
    "username": "alice_jones",
    "password": "password789",
    "email": "alice.jones@example.com",
    "isAdmin": false
  }
]
```

### Step 2: Parse the JSON File

You can use Node.js to read and parse this JSON file. Here’s a simple example of how to do that (use different data):

**`parseJSON.js`**
```javascript
const fs = require('fs');

//Read the JSON file
fs.readFile('users.json', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  //Parse the JSON data
  try {
    const users = JSON.parse(data);

    // Example: Accessing individual user properties
    users.forEach(user => {
      console.log(`Username: ${user.username}, Email: ${user.email}, Is Admin: ${user.isAdmin}`);
    });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
```

### Step 3: Run the Code

1. Save the JSON content into a file.
2. Save the JavaScript code into a file named `parseJSON.js`.
3. Make sure you have Node.js installed on your machine.
4. Open a terminal and navigate to the directory containing both the files.
5. Run the script with the following command:

```bash
node parseJSON.js
```

### Expected Output

When you run the code, you should see an output similar to this:

```
Username: john_doe, Email: john.doe@example.com, Is Admin: false
Username: jane_smith, Email: jane.smith@example.com, Is Admin: true
Username: alice_jones, Email: alice.jones@example.com, Is Admin: false
```
