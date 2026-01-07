# Arrays

<code>
    Its a continuous fixed type block of memory of different data types which is stored in the RAM and can be defined by its index position. And the values are fetched in constant time (O(1)). Use it when you care about order and/or allow duplicates.
</code>

## Its Operations:
1. Accessing: O(1)
2. Insertion: best case - O(1) :: worst case(due to having to shift elements from thier nodes, and having to create spaces) - O(n)
3. Deletion: best case - O(1) :: worst case(due to having to shift elements from thier nodes after deleting an element) - O(n)
4. Searching: O(n) - to search array with random values, O(log n) - to search array with sorted values
5. Traversing: O(n) - due to having to iterate over every element in the array
6. Updating: O(1) - done instantly by fetching the element to update

## Benefits
1. Random access: O(1)
2. Cache friendly: O(n)
3. Ease of sorting
4. Supports implementation of other data structures

## Limitations
1. Fixed Size
2. Inefficient for frequent modifications

## Use Cases
1. Implementation of other data structures
2. Caching e.g memoization
3. Tracks visited nodes
4. Mathematical calculations
5. Coding patterns e.g pointers, sliding window
6. Storing a sequence of numbers or letters.
7. Sorting, reversing, or doing arithmetic on elements.

## Dictionary/Hash Map
1. Use it when you want to map keys to values, and you need fast lookup.
2. Great when you need to count occurrences or remember last positions.
3. Lookup, insert, and update are usually O(1).

## Set
1. Use a set when you only care about uniqueness and fast membership check.
2. Elements are unordered, cannot repeat.
3. Lookup, insert, remove are usually O(1).
