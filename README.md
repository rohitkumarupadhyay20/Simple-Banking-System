SIMPLE BANKING SYSTEM

Python Programming Project – PS No. 12

Course: BCA – AI & ML
Institution: Rungta International Skills University
Developed by: Rohit Kumar Upadhyay

---

1. Project Overview

The Simple Banking System is a menu-driven Python application that performs basic banking operations. It allows users to create accounts, deposit money, withdraw money, transfer funds, and check account balances.

Account information is stored permanently in a text file named "bank.txt" using JSON format.

2. Project Objectives

- Understand Python functions and loops.
- Apply conditional statements.
- Implement file handling.
- Develop a simple banking application.
- Maintain minimum balance requirements.
- Store and retrieve account information.

3. Features

1. Create a new bank account.
2. Generate unique account numbers.
3. Deposit money.
4. Withdraw money.
5. Transfer money between accounts.
6. Check account balance.
7. Store account details in a file.
8. Validate transactions.

4. Software Requirements

- Python 3.x
- Visual Studio Code or any Python IDE
- Windows operating system
- Built-in Python modules: "json" and "os"

5. Banking Rules

- Account numbers start from 1001.
- Minimum account balance must be ₹500.
- Deposit amount must be positive.
- Withdrawal amount must be positive.
- Sender and receiver accounts must exist for transfers.
- A transaction cannot reduce the balance below ₹500.

6. Project Files

File Name| Description
"one.py"| Main Python program
"bank.txt"| Stores account information
"README.md"| Project documentation

7. How to Execute the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Keep "one.py" and "bank.txt" in the same folder.
4. Open the project folder in VS Code.
5. Open the terminal.
6. Run the following command:

python one.py

7. Select an option from the displayed menu.

8. Input and Output Details

Inputs:

- Menu selection
- Account holder name
- Account number
- Deposit amount
- Withdrawal amount
- Transfer amount
- Receiver account number

Outputs:

- Account creation confirmation
- Transaction success or failure messages
- Account balance details
- Error messages for invalid operations

9. Testing

The project includes four test cases:

Test Case 1: Account Creation

- Create an account for Anil.
- Opening deposit: ₹2000.
- Expected account number: 1001.
- Expected balance: ₹2000.

Test Case 2: Withdrawal

- Initial balance: ₹2000.
- Withdraw: ₹1500.
- Expected remaining balance: ₹500.

Test Case 3: Invalid Transfer

- Transfer ₹100 to account number 9999.
- Expected result: Transfer cancelled because the account does not exist.

Test Case 4: Successful Transfer

- Account 1001 balance: ₹2000.
- Account 1002 balance: ₹3000.
- Transfer ₹1000 from account 1002 to account 1001.
- Expected account 1001 balance: ₹3000.
- Expected account 1002 balance: ₹2000.

Each test case should be executed separately using the appropriate initial account data.

10. Python Concepts Used

- Variables and data types
- Functions
- Loops
- Conditional statements
- Dictionaries
- File handling
- JSON data storage
- Exception handling

11. Conclusion

The Simple Banking System demonstrates the practical implementation of Python programming concepts. It provides basic banking operations while maintaining account records using file handling.

This project helped develop an understanding of functions, loops, conditions, data structures, and file operations in Python.

---

Project: Simple Banking System
Project Number: PS No. 12
Language: Python 3
