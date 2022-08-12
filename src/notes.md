```python
results = list(
    collection.aggregate([
        {
            "$group": {
                "_id": {"cuisine": "$metadata.cuisine"},
                "count": {"$sum": 1},
                "average": {"$avg": "$rating"}
            }
        }
    ])
)
```

Modify Incoming Doc Data
```python
results = list(
    collection.aggregate([
        {"$project": {
            "date": {
                "$dateToString": {"format": "%Y-%m", "date": "$timestamp"}
            },
        }}
    ])
)
```

Time Series Grouping

```python
results = list(
    collection.aggregate([
        {
            "$project": {
                "date": {
                    "$dateToString": {"format": "%Y-%m", "date": "$timestamp"}
                },
                "cuisine": "$metadata.cuisine",
                "rating": "$rating",
            }
        },
        {
            "$group": {
                "_id": {
                    "cuisine": "$cuisine",
                    "date": "$date",
                },
                "average": {"$avg": "$rating"}
            }
        },
        {"$addFields": {"cuisine": "$_id.cuisine" }},
        {"$addFields": {"date": "$_id.date" }}
    ])
)
```



Match & Sort Filter
```python
import datetime

results = list(
    collection.aggregate([
        {
            "$match": {
                "timestamp": {"$gte": datetime.datetime.now() - datetime.timedelta(days=50, "$lte"  datetime.datetime.now() - datetime.timedelta(days=10}
            }
        }, 
        {
            "$project": {
                "date": {
                    "$dateToString": {"format": "%Y-%m", "date": "$timestamp"}
                },
                "cuisine": "$metadata.cuisine",
                "rating": "$rating",
            }
        },
        {
            "$group": {
                "_id": {
                    "cuisine": "$cuisine",
                    "date": "$date",
                },
                "average": {"$avg": "$rating"}
            }
        },
        {"$addFields": {"cuisine": "$_id.cuisine" }},
        {"$addFields": {"date": "$_id.date" }},
        {"$sort": {"date": 1 }}
    ])
)
```


PyMongo -> Pandas DataFrame

```python
import pandas as pd

dataset = list(
    collection.aggregate([ 
        {
            "$project": {
                "date": {
                    "$dateToString": {"format": "%Y-%m", "date": "$timestamp"}
                },
                "cuisine": "$metadata.cuisine",
                "rating": "$rating",
            }
        },
        {
            "$group": {
                "_id": {
                    "cuisine": "$cuisine",
                    "date": "$date",
                },
                "average": {"$avg": "$rating"}
            }
        },
        {"$addFields": {"cuisine": "$_id.cuisine" }},
        {"$addFields": {"date": "$_id.date" }},
        {"$sort": {"date": 1 }}
    ])
)


df = pd.DataFrame(dataset)
df['date'] = pd.to_datetime(df['date'])
df = df[['date', 'cuisine', 'average']]
df.set_index('date', inplace=True)
```