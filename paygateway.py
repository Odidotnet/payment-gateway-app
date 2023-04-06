import tkinter as tk
from tkinter  import messagebox

# from PIL import Image,ImageTk



    # perform payment processing logic here
    # (e.g., validate card details, charge the card, etc.)

    # Display payment confirmation


    # create main window
root = tk.Tk()
root.title("Payment Interface")

# Load and display images
# image = Image.open("drift.jpg")  # Replace #image.jpg with another image entirely
# photo = ImageTk.PhotoImage(image)
# image_Label = tk.Label(root, image=photo)
# image_Label
# image_Label.pack()

def process_payment():
    card_number = card_number_entry.get()
    card_expiry = card_expiry_entry.get()
    card_cvv = card_cvv_entry.get()
    card_name = card_name_entry.get()
    amount = amount_entry.get()
    messagebox.showinfo("payment configuration", f"Payment of ${amount} processed successfully")

# create card number label and entry
card_number_label = tk.Label(root, text="Card Number:")
card_number_label.pack()
card_number_entry = tk.Entry(root)
card_number_entry.pack()

# create card expiry label and entry
card_expiry_label = tk.Label(root, text="Card Expiry:")
card_expiry_label.pack ()
card_expiry_entry = tk.Entry(root)
card_expiry_entry.pack()


# create card CVV label and entry
card_cvv_label = tk.Label(root, text="Card CVV:")
card_cvv_label.pack()
card_cvv_entry = tk.Entry(root, show="*")
card_cvv_entry.pack()

# create card name label and entry
card_name_label = tk.Label(root, text="Cardholder Name:")
card_name_label.pack()
card_name_entry = tk.Entry(root)
card_name_entry.pack()

# create amount label and entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# create process payment button
process_button = tk.Button(root, text="Process Payment", command=process_payment)
process_button.pack(pady=10)

# start the main loop
root.mainloop()