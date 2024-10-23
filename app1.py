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

    st.write("### Select your items and quantities")
    
    selected_items = {}
    for item in menu.keys():
        quantity = st.number_input(f"Quantity of {item}", min_value=0, value=0, step=1)
        if quantity > 0:
            selected_items[item] = quantity

    # Calculate the total bill
    total_bill = sum(menu[item] * quantity for item, quantity in selected_items.items())

    # Discount section
    discount_percent = st.number_input("Enter discount percentage (0-100):", min_value=0, max_value=100, value=0)
    discount_amount = (discount_percent / 100) * total_bill
    final_total = total_bill - discount_amount

    st.write("### Your Selection")
    for item, quantity in selected_items.items():
        st.write(f"- {item}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}")
    
    st.write(f"### Subtotal: ${total_bill:.2f}")
    st.write(f"### Discount: -${discount_amount:.2f} ({discount_percent}%)")
    st.write(f"### Final Total: ${final_total:.2f}")

if __name__ == "__main__":
    main()
