

1. Sum, Min, Max, and Avg in Aggregation Queries:

You can use the aggregation pipeline in MongoDB to calculate these values across a set of documents. Here’s an example for each operation:
```javascript 
db.collection.aggregate([
  {
    $group: {
      _id: "$category",  // Grouping by a field (e.g., "category")
      total: { $sum: "$amount" },  // Sum of the "amount" field
      minAmount: { $min: "$amount" },  // Minimum value in "amount" field
      maxAmount: { $max: "$amount" },  // Maximum value in "amount" field
      avgAmount: { $avg: "$amount" },  // Average of the "amount" field
    }
  }
])
```

In this example:

$sum adds up all values in the amount field.

$min finds the smallest value in the amount field.

$max finds the largest value in the amount field.

$avg calculates the average value for the amount field.


2. Using $push and $addToSet in Aggregation:

$push: Adds values to an array for each document in a group. It allows duplicates.

$addToSet: Adds unique values to an array. It automatically removes duplicates.


Here’s an example:

```javascript
db.collection.aggregate([
  {
    $group: {
      _id: "$category",
      allItems: { $push: "$item" },  // Push all values of "item" into an array (with duplicates)
      uniqueItems: { $addToSet: "$item" }  // Push unique values of "item" into an array
    }
  }
])
```
$push will gather all item values into the allItems array, including duplicates.

$addToSet will gather only distinct item values into the uniqueItems array.


Let me know if you need further clarification or more examples!

