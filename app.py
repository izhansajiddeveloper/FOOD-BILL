import streamlit as st

# Define the menu items and their prices
menu = {
    "Burger": 5.0,
    "Pizza": 8.0,
    "Pasta": 7.0,
    "Salad": 4.5,
    "Soda": 1.5,
}

def main():
    st.title("Food Bill Calculator")

    st.write("### Menu")
    for item, price in menu.items():
        st.write(f"{item}: ${price:.2f}")

    st.write("### Select your items")
    
    # Create a checkbox for each menu item
    selected_items = []
    for item in menu.keys():
        if st.checkbox(item):
            selected_items.append(item)

    # Calculate the total bill
    total_bill = sum(menu[item] for item in selected_items)
    
    st.write("### Your Selection")
    for item in selected_items:
        st.write(f"- {item}: ${menu[item]:.2f}")
    
    st.write(f"### Total Bill: ${total_bill:.2f}")

if __name__ == "__main__":
    main()
