import tkinter as tk
from tkinter import messagebox

# Simulated user data
users = {
    'user1': {'pin': '1234', 'balance': 1000},
    # Add more users as needed
}

# Simulate fingerprint authentication (always returns True for simplicity)
def authenticate_fingerprint():
    return True

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        
        self.current_user = None
        
        self.create_initial_screen()
    
    def create_initial_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Fingerprint ATM", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.root, text="Scan Fingerprint", command=self.scan_fingerprint).pack(pady=10)
        tk.Button(self.root, text="Enter PIN", command=self.login_screen).pack(pady=10)
    
    def scan_fingerprint(self):
        if authenticate_fingerprint():
            messagebox.showinfo("Success", "Fingerprint Authentication Successful")
            self.current_user = 'user1'  # Assuming the fingerprint belongs to 'user1'
            self.main_screen()
        else:
            messagebox.showerror("Error", "Fingerprint Authentication Failed")

    def login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Enter PIN", font=("Arial", 18)).pack(pady=10)
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=10)
        
        tk.Button(self.root, text="Login", command=self.check_pin).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_initial_screen).pack(pady=10)
    
    def check_pin(self):
        pin = self.pin_entry.get()
        for user, details in users.items():
            if details['pin'] == pin:
                self.current_user = user
                self.main_screen()
                return
        messagebox.showerror("Error", "Invalid PIN")
    
    def main_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Welcome to ATM", font=("Arial", 24)).pack(pady=20)
        
        tk.Button(self.root, text="View Balance", command=self.view_balance).pack(pady=10)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_screen).pack(pady=10)
        tk.Button(self.root, text="Deposit", command=self.deposit_screen).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)
    
    def view_balance(self):
        balance = users[self.current_user]['balance']
        messagebox.showinfo("Balance", f"Your balance is: ${balance}")
    
    def withdraw_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Enter Amount", font=("Arial", 18)).pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=10)
        
        tk.Button(self.root, text="Withdraw", command=self.withdraw).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.main_screen).pack(pady=10)
    
    def withdraw(self):
        amount = int(self.amount_entry.get())
        if amount <= users[self.current_user]['balance']:
            users[self.current_user]['balance'] -= amount
            messagebox.showinfo("Success", "Withdrawal successful")
            self.main_screen()
        else:
            messagebox.showerror("Error", "Insufficient balance")
    
    def deposit_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Enter Amount to Deposit", font=("Arial", 18)).pack(pady=10)
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack(pady=10)
        
        tk.Button(self.root, text="Deposit", command=self.deposit).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.main_screen).pack(pady=10)
    
    def deposit(self):
        amount = int(self.deposit_entry.get())
        if amount > 0:
            users[self.current_user]['balance'] += amount
            messagebox.showinfo("Success", "Deposit successful")
            self.main_screen()
        else:
            messagebox.showerror("Error", "Invalid amount")
    
    def logout(self):
        self.current_user = None
        self.create_initial_screen()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATM(root)
    root.geometry("400x300")
    root.mainloop()
