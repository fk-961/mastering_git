# Python practical tips

## List comprehension
`[i for i in l if i%2 == 0]` returns the even elements in a list `l`.

`[
    [i,j,k] for i in range(x) for j in range(y) for k in range(z)
]` returns list of permutations

## sets and sorts
`set()` returns an unordered list of unique values.

`list.sort()` modifies the list by sorting its elemts.

`sorted(list)` return a sorted version of the argument. It has a reverse parameter `reverse` for the sorting order.

**Note:** 
- When using `set()` on a dictionary it returns a set of the keys.
- When doing for loops, it is good practice to do it on a set if we have huge list.

