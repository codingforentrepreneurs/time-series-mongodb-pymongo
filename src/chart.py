# blank on purpose - check `final` branch
import datetime
import pathlib
import sys

import pandas as pd
import db_client


def output_chart(days_ago=1600, days_end=0):
    client = db_client.get_db_client()
    db = client.business
    collection = db.rating_over_time
    delta = datetime.datetime.now() - datetime.timedelta(days=days_ago)
    match_filter_dict =  {"$gte":delta}
    if isinstance(days_end, int):
        delta2 = datetime.datetime.now() - datetime.timedelta(days=days_end)
        match_filter_dict =  {**match_filter_dict, "$lte":delta2}
    dataset = list(
        collection.aggregate([ 
            {
                "$match": {
                    "timestamp": match_filter_dict
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
    df = pd.DataFrame(dataset)
    df = df[["average", "cuisine", "date"]]
    df['date'] = pd.to_datetime(df['date'])
    df.set_index("date", inplace=True)
    group_data = df.groupby("cuisine")['average']
    group_plot = group_data.plot(legend=True, figsize=(15, 5)) #matplotlib
    base_dir = pathlib.Path(__file__).parent.parent
    output_dir = base_dir / "plots" / "cuisines"
    output_dir.mkdir(exist_ok=True, parents=True)
    now = datetime.datetime.now()
    now_as_str = f"{int(now.timestamp())}"
    out_file = str(output_dir / f"{now_as_str}-{delta}.png")
    # df.to_csv(out_file.replace('.png', '.csv'))
    fig = group_plot[0].get_figure()
    fig.savefig(out_file)

if __name__ == "__main__":
    days_ago = 150
    try:
        days_ago = int(sys.argv[1])
    except:
        pass
    output_chart(days_ago=days_ago)