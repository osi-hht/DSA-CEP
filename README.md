# DSA-CEP
LRU Cache Implementation in Python
Project Overview
This project implements an LRU (Least Recently Used) Cache using Doubly Linked List and HashMap in Python. The LRU Cache is designed to efficiently manage memory by storing a limited number of items and discarding the least recently used items when the cache reaches capacity.

Features
Implements an O(1) time complexity for get() and put() operations.
Uses a doubly linked list for quick removal and insertion.
Stores key-node mappings in a dictionary (hashmap) for fast lookups.
Provides a miss rate calculator to analyze cache performance.
How It Works
The LRU cache follows these principles:

When a key is accessed (get()), it is moved to the most recently used position.
When a new key-value pair is added (put()), it is inserted at the most recently used position.
If the cache exceeds its capacity, the least recently used element (LRU) is removed.
Performance Analysis
The LRU cache is tested with:

Sequential inserts: Filling the cache with numbers from 0 to 49.
Odd-numbered key lookups: Checking how often keys are hit or missed.
Prime number inserts: Filling the cache with prime numbers between 0 to 100.
The final miss rate is calculated to evaluate the cache efficiency.

Usage
Run the script in Python.
Modify cache capacity to experiment with different values.
Analyze cache performance based on access patterns.
Why LRU?
LRU is widely used in:

Operating System Page Replacement Policies
Database Query Caching
Web Browser Caching
CPU Cache Management

Contributors
Osama Humayun
Mashaal Ali, Anas Yazdani
License
This project is open-source and available under the MIT License.
