Given an array, the task is to divide it into two arrays A1 and A2 such that the absolute difference between their sums is minimum.

Input:
an array A with n integers

Output:
the minimum (absolute) difference between the sums of 2 arrays consisting of all the elements from the input array

Constraints:
- `1<=n<=50`
- `1<=A[I]<=50`

The original task is wrong as it describes an array as input and 2 sets as output.
The array A is not restricted to distinct values.

Example: `[1,4,5,5,10]`
- The best array-solution is:
`[1,10]` and `[4,5,5]` -> difference: 3
- But the best set solution is:
`{1,4,5,5}` and `{10}` = `{1,4,5}` and `{10}` -> difference: 0

The unit tests on the website expect an array solution. So this task expects one.