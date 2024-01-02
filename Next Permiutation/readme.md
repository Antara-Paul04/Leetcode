# Next Permutation

## Problem Statement

Given a list of integers, implement the "next permutation" algorithm, which rearranges the numbers into the lexicographically next greater permutation of numbers. If no such permutation exists, reverse the list.

## Brute Force Algorithm

- Generate all possible permutations of the given list.
- Perform a linear search to find the next permutation.
- Identify the index of the next permutation.
- **Time Complexity:** O(n! * n)

## Better Algorithm (using C++ STL)

- Utilize the built-in C++ STL library to generate the solution efficiently.

## Optimal Algorithm

### Observation:

- Consecutive elements often have a longer common prefix in their permutations.
- Find the breakpoint index `i` where `a[i] < a[i+1]`.

### Next Greater Number:

- Find the smallest number greater than `a[i]` in the remaining numbers.
- Swap `a[i]` with the found number.

### Sorted Order:

- Arrange the remaining numbers in sorted order.
- If the remaining numbers are already in descending order, reverse them.

### Example:

- Original List: [2, 1, 5, 4, 3, 0, 0]
- Breakpoint: i=1 (a[1] < a[2])
- Next Greater: 3 (smallest among numbers greater than 1)
- Swap: [2, 3, 5, 4, 1, 0, 0]
- Arrange Remaining: [2, 3, 0, 0, 1, 4, 5]
- Result: [2, 3, 0, 0, 1, 4, 5]


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
