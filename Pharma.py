import hashlib
import time

# Class representing a Drug in the supply chain
class Drug:
    def __init__(self, name, manufacturer, status):
        self.name = name
        self.manufacturer = manufacturer
        self.timestamp = time.time()
        self.status = status

    def __str__(self):
        return f"Drug Name: {self.name}, Manufacturer: {self.manufacturer}, Status: {self.status}, Timestamp: {self.timestamp}"

# Class representing a Transaction in the supply chain
class Transaction:
    def __init__(self, drug, prev_hash=""):
        self.drug = drug
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.drug.name}{self.drug.manufacturer}{self.drug.status}{self.timestamp}{self.prev_hash}"
        return hashlib.sha256(data.encode()).hexdigest()

    def __str__(self):
        return f"Transaction: {self.hash}, Previous Hash: {self.prev_hash}, Drug: {self.drug}"

# Class representing the Pharma Supply Chain
class PharmaSupplyChain:
    def __init__(self):
        self.chain = []

    # Method to add a new drug to the supply chain
    def add_drug(self, drug):
        prev_hash = self.chain[-1].hash if self.chain else ""
        new_transaction = Transaction(drug, prev_hash)
        self.chain.append(new_transaction)
        print(f"Drug added: {drug}")
        print(f"Transaction hash: {new_transaction.hash}")

    # Method to update the status of a drug in the supply chain
    def update_drug_status(self, drug_name, new_status):
        for transaction in self.chain:
            if transaction.drug.name == drug_name:
                transaction.drug.status = new_status
                transaction.hash = transaction.calculate_hash()
                print(f"Drug status updated: {transaction.drug}")
                return
        print("Drug not found")

    # Method to retrieve information about a drug
    def get_drug_info(self, drug_name):
        for transaction in self.chain:
            if transaction.drug.name == drug_name:
                print(transaction.drug)
                return
        print("Drug not found")

    # Method to validate the integrity of the supply chain
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_transaction = self.chain[i]
            prev_transaction = self.chain[i - 1]
            if current_transaction.prev_hash != prev_transaction.hash:
                print("Chain is invalid!")
                return False
            if current_transaction.hash != current_transaction.calculate_hash():
                print("Current transaction hash is invalid!")
                return False
        print("Chain is valid")
        return True

# Function to display the menu and get user input
def display_menu():
    print("\nPharma Supply Chain System")
    print("1. Add a new drug")
    print("2. Update drug status")
    print("3. Retrieve drug information")
    print("4. Validate the supply chain")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

# Main logic to simulate the Pharma Supply Chain with user input
def main():
    supply_chain = PharmaSupplyChain()

    while True:
        choice = display_menu()

        if choice == '1':
            name = input("Enter the drug name: ")
            manufacturer = input("Enter the manufacturer: ")
            status = input("Enter the status (e.g., Produced, Shipped, In Transit): ")
            drug = Drug(name, manufacturer, status)
            supply_chain.add_drug(drug)

        elif choice == '2':
            drug_name = input("Enter the drug name to update: ")
            new_status = input("Enter the new status (e.g., Shipped, Delivered): ")
            supply_chain.update_drug_status(drug_name, new_status)

        elif choice == '3':
            drug_name = input("Enter the drug name to retrieve information: ")
            supply_chain.get_drug_info(drug_name)

        elif choice == '4':
            supply_chain.validate_chain()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
