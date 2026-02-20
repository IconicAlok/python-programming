def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")

display_invoice("AlokKuri", 40.02, "01/01")
display_invoice("JoeSchmo", 100.01, "01/02")
display_invoice("JohnSmith", 505.98, "05/02")