import os
import streamlit as st

FILE_NAME = "expenses.txt"


def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    category, amount = line.split(",")
                    expenses.append((category, float(amount)))
    return expenses


def save_all(expenses):
    with open(FILE_NAME, "w") as f:
        for category, amount in expenses:
            f.write(category + "," + str(amount) + "\n")


st.title("Expense Tracker")

expenses = load_expenses()

st.subheader("Add expense")
with st.form("add_form", clear_on_submit=True):
    category = st.text_input("Category (food, travel, etc.)")
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    submitted = st.form_submit_button("Add")

if submitted:
    category = category.replace(",", " ").strip()
    if category == "":
        st.error("Please enter a category.")
    else:
        expenses.append((category, amount))
        save_all(expenses)
        st.rerun()

st.subheader("Your expenses")
if len(expenses) > 0:
    rows = []
    total = 0
    number = 1
    for category, amount in expenses:
        rows.append({"No.": number, "Category": category, "Amount": amount})
        total = total + amount
        number = number + 1
    st.table(rows)
    st.write("Total:", total)

    st.subheader("Delete expense")
    delete_number = st.number_input(
        "Enter the number to delete", min_value=1, max_value=len(expenses), step=1
    )
    if st.button("Delete"):
        expenses.pop(int(delete_number) - 1)
        save_all(expenses)
        st.rerun()
else:
    st.info("No expenses yet.")