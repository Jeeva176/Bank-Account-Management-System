# Bank-Account-Management-System 🏦
Bank Account Management System A Python-based Object-Oriented Programming (OOP) project that simulates a banking system. It includes features like account creation, deposits, withdrawals, transfers, and interest-based accounts with proper exception handling.

## Overview
This is a Python-based Object-Oriented Banking System that supports:
- Account creation 🆕
- Deposits and withdrawals 💰
- Fund transfers between accounts 🔄
- Interest-based accounts with reward features 🎁
- Exception handling for low balances ❌

## Features
✔️ **BankAccount Class** – Basic account functions  
✔️ **InterestRewardAccount Class** – Deposits with 5% interest  
✔️ **SavingAcct Class** – Includes withdrawal fees  
✔️ **Exception Handling** – Prevents overdrafts  

Concepts & Tools Used in Your Bank Account System

1. Object-Oriented Programming (OOP)
Classes & Objects → BankAccount, InterestRewardAccount, SavingAcct
Inheritance → InterestRewardAccount and SavingAcct inherit from BankAccount
Encapsulation → Storing account balance and name inside the class
Method Overriding → deposit and withdraw methods are overridden in child classes

3. Exception Handling
Custom Exceptions → BalanceException to handle low balance situations
Try-Except Blocks → Handling withdrawal and transfer failures gracefully
