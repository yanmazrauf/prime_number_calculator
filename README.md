#Calculate Prime Numbers in a Range

This program is a simple Prime Number Calculator built using Python’s Tkinter library for GUI. It allows users to input a range by specifying a lower and upper limit and calculates the prime numbers within that range using the Sieve of Eratosthenes algorithm, which is an efficient method for finding prime numbers.

The algorithm starts by creating a boolean list, where all numbers are initially marked as prime (True). However, 0 and 1 are immediately set to False since they are not prime numbers. Then, it begins with the smallest prime number, 2, and marks all of its multiples as non-prime. This process continues for the next prime number and repeats until all non-prime numbers in the range have been identified. After this step, the function extracts all numbers that remain marked as prime and returns them as a list.

![Sieve of Eratosthenes](https://mathbitsnotebook.com/JuniorMath/Factoring/sievepic.jpg)

##How It Works

![image](https://github.com/user-attachments/assets/f1eb1c4a-5951-4a7d-8634-bb50ccfc5ddb)

When the user clicks the "Calculate" button, the program retrieves the input values, runs the prime number calculation, and then displays the total number of prime numbers found along with the first ten prime numbers from the range.

![image](https://github.com/user-attachments/assets/93e06155-afbd-4945-b63e-e00b735e7a7e)


