#### Pandas basics
---
This is a handy guide for the pandas library. For more in depth information, check online documentation.
## DataFrame and Series
```
pd.DataFrame(

    {
        'column A' : [1,2,3,4],
        'column b' : ['a','b','c','d']
    },

    index = ["row "+str(i+1) for i in range(4)]
)
```
If we want to create a dataset like the one above, we need to pass these arguments. The length of lists and indexes must be the same to fill all the values.
Every column is of type `pd.Series`.

`replace` is a method that can be used on both DataFrames and Series to replace something.

## Accessing and Indexing
To access elements in the dataset, there are a lot of ways to do it. The most used are `pd.DataFrame.iloc` and `pd.DataFrame.loc`. We can however treat the dataset as a dictionary and perform operations such as these `pd.DataFrame['column A'][2]` which is straightforward to what it does.
- `pd.DataFrame.iloc` is an index-way of accessing data. So we pass iloc[index,column] and we can do slicing operations. The arguments here are always numeric.
- `pd.DataFrame.loc` is a broader way of accessing data. We can pass names, conditions and more stuff.
  
**Note:** A difference between the two is that `iloc` doesnt include the last term entered (like for loops) while `loc` includes it.

## Summary functions and maps
Useful methods to describe and get an idea of what our data looks like are `pd.DataFrame.describe` and `pd.DataFrame.info`. The aggregate functions can also be handy like `max`, `min`, `count` and `mean`.

**Map** is a really useful way to manipulate data. It can be used on the DataFrame or Series.
- `data.map(lambda x: str(x)+"!")` adds `!` to the end of every element in the data. However it does not modify the original dataset.
- `data.column1.map(lambda x: str(x)+"!")` adds `!` to column1 of the data and returns a Series.

**Apply** is more general than **Map** since we can pass a more general functino as argument. We need to specify in the arguments the axis on which we want to apply the function. Below is a very general example of how apply can be used:
```
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

## Grouping and Sorting
Often we want to group by our data based on certain columns and do something with the result. Maybe we want to group by region and sum the population or do a whole other functions on the result.

The usual syntax is like this:
```
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```
What we are doing here is grouping by country and province and getting the best ranked element there. The result is a multi-index DataFrame. If we wanna keep using it we can use `pd.DataFrame.reset_index()` so we go back to numeric indexes with the first two columns being country and province.

`sort_values` is another method we can use on the result to, well, sort the values. `asceding` is an optional boolean argument we can pass to specify the order.