# CodeAlpha_Stock-Portfolio-Tracker

# Stock Portfolio Tracker (Indian MNCs) 📈

This project was developed as part of the **CodeAlpha Python Programming Internship (Task 2)**.

It is a simple console-based Python application that calculates the total investment value of a stock portfolio based on predefined stock prices of top Indian Multinational Companies (MNCs) in **Indian Rupees (₹)**.

---

## 📌 Project Overview & Objectives

- **Defined Stock Market Data:** Uses a dictionary containing top Indian MNC benchmark stocks and their prices per share in INR (₹).
- **Dynamic User Inputs:** Allows users to input multiple stock symbols and quantities until they type `done`.
- **Input Validation:** Ensures only valid stock symbols and positive whole numbers for share quantities are accepted.
- **Investment Calculation:** Automatically computes the subtotal for each stock (`price × quantity`) and the cumulative total investment in Rupees.
- **File Handling (Optional):** Prompts the user with an option to export and save their portfolio summary to a `portfolio_summary.txt` file.

---

## 🏢 Available Indian MNC Stocks

| Stock Symbol | Company Name | Price per Share (₹) |
| :--- | :--- | :--- |
| **TCS** | Tata Consultancy Services | ₹3,920 |
| **INFY** | Infosys Ltd. | ₹1,850 |
| **RELIANCE** | Reliance Industries | ₹2,950 |
| **HCLTECH** | HCL Technologies | ₹1,720 |
| **WIPRO** | Wipro Ltd. | ₹540 |
| **TATAMOTORS**| Tata Motors | ₹940 |
| **TECHM** | Tech Mahindra | ₹1,580 |
| **LT** | Larsen & Toubro | ₹3,560 |

---

## 🔑 Key Concepts Used

- **Dictionary:** Fast lookup for stock prices and storing user holdings.
- **While Loops & Conditionals:** Drives the interactive menu and input loops.
- **Input / Output:** Formatted console prompts and summary display.
- **Basic Arithmetic:** Multiplying share prices by quantities and calculating total sums.
- **File Handling:** Writing the final investment breakdown to a text file using `open()`.

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have **Python 3.x** installed on your system.

### Running the Script
1. Clone this repository or download the files:
   ```bash
   git clone https://github.com/saidinesh8631/CodeAlpha_Stock-Portfolio-Tracker.git
   cd CodeAlpha_Stock_Portfolio_Tracker
   ```

2. Run the script:
   ```bash
   python Stock_Portfolio_Tracker.py
   ```

---

## 💻 Sample Program Output

```text
Welcome to the Indian Stock Portfolio Tracker!

Available Indian MNC stocks and prices (per share in INR):
  TCS: ₹3,920
  INFY: ₹1,850
  RELIANCE: ₹2,950
  HCLTECH: ₹1,720
  WIPRO: ₹540
  TATAMOTORS: ₹940
  TECHM: ₹1,580
  LT: ₹3,560

Enter stock symbol and quantity. Type 'done' as symbol to finish.

Stock symbol: TCS
Quantity of TCS: 2
Added 2 share(s) of TCS.

Stock symbol: INFY
Quantity of INFY: 5
Added 5 share(s) of INFY.

Stock symbol: done

Portfolio Summary
=============================================
TCS: 2 shares x ₹3,920 = ₹7,840
INFY: 5 shares x ₹1,850 = ₹9,250
=============================================
Total Investment: ₹17,090

Save summary to a file? (y/n): y

Portfolio summary saved to 'portfolio_summary.txt'.
```

### Generated `portfolio_summary.txt`
```text
Stock Portfolio Summary (Indian MNCs)
=============================================
TCS: 2 shares x ₹3,920 = ₹7,840
INFY: 5 shares x ₹1,850 = ₹9,250
=============================================
Total Investment: ₹17,090
```

---

## 👤 Author
- **Intern:** Python Programming Intern at CodeAlpha
- **Task:** Task 2 - Stock Portfolio Tracker
