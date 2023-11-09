## Fixed bugs
- When writing the code I was trying to pass a variable into a method unsuccessfully. The problem was that I did not define the relevant variable, which was the outcome of another method, in the global space but only within that previous method. Solved by assigning the outcome of the previous method to a variable in the global space. 


## Credits
- On how to use the round() function: https://www.geeksforgeeks.org/round-function-python/