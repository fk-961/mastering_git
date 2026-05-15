# Python practical tips

## List comprehension
`[i for i in l if i%2 == 0]` returns the even elements in a list `l`.

`[
    [i,j,k] for i in range(x) for j in range(y) for k in range(z)
]` returns list of permutations

## List functions
`set()` returns an unordered list of unique values. Applying the set functions return an arbitrary order everytime.

`list.sort()` modifies the list by sorting its elemts.

`sorted(list)` return a sorted version of the argument. It has a reverse parameter `reverse` for the sorting order.

Other useful functions:

- `l.insert(index, element)`: straightforward.
- `l.remove(element)`: removes first occurence of element.
- `l.pop()`: removes last element.

**Note:** 
- When using `set()` on a dictionary it returns a set of the keys.
- When doing for loops, it is good practice to do it on a set if we have huge list.

