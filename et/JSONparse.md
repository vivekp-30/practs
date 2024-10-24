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

### Step 3: Steps for Running

1. Create a new folder in VS Code and create empty `.json` and `.js` files.
2. Copy the code into the files.
3. Install the Code Runner extension from the Extensions Tab in VS Code.
4. Make sure the file name of json file matches the file name passed in `fs.readfile()` in `.js` file.
5. Right Click on the js File and click Run Code.

### Expected Output

When you run the code, you should see an output similar to this:

```
Username: john_doe, Email: john.doe@example.com, Is Admin: false
Username: jane_smith, Email: jane.smith@example.com, Is Admin: true
Username: alice_jones, Email: alice.jones@example.com, Is Admin: false
```
