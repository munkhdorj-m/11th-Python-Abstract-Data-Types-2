# Abstract Data Types 1

Abstract Data Types PDF:

https://drive.google.com/file/d/1jXGQdSvuUYjGXl-PUuHMUzKWEBGQoARL/view?usp=sharing


---

## Exercise 1

**Problem:**
 
Decimal to Binary (Using a Stack)   
Implement a `Stack` class and use it to convert a decimal number to binary.   
Methods:   
- `push(item)`   
- `pop()`    
- `is_empty()`   
- `decimal_to_binary(n)`   
    
Example:

    Input:
       print(decimal_to_binary(13))
    Output:
       1101
       
Explanation:
Stack stores remainders → popped in reverse order → binary.
---

## Exercise 2

**Problem:**

Bank Queue Simulation (Using a Queue)    
Simulate customers waiting in line at the bank.   
Methods:   
- `enqueue(item)`
- `dequeue()`
- `is_empty()`
- `bank_simulation(customers)`
  
Example:

    Input: 
       customers = ["Alice", "Bob", "Charlie"]
       print(bank_simulation(customers))
      
    Output:
       Serving: Alice
       Serving: Bob
       Serving: Charlie

---

