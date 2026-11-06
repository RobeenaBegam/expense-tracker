# Expense Tracker

A simple expense tracker written in Python, with a command-line version and a Streamlit web page.

## Features

- Add an expense
- View all expenses with a numbered list and total
- Delete an expense
- Saves data to a text file (expenses.txt)
- Web page version built with Streamlit (add form, table, total and delete)

## How to run the command-line version

1. Install Python 3
2. Run: `python main.py`

## How to run the web page (Streamlit)

1. Install Streamlit: `python -m pip install streamlit`
2. Run: `python -m streamlit run app.py`
3. If the browser does not open by itself, go to http://localhost:8501

Both versions save to the same expenses.txt file, so the data is shared.
