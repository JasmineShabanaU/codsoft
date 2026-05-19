contacts = {}


def add_contact():
    """Add a new contact."""
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()

    if name in contacts:
        print("⚠️ Contact already exists!")
        return

    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    address = input("Enter Address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print(f"✅ Contact '{name}' added successfully!")


def view_contacts():
    """Display all contacts."""
    print("\n--- Contact List ---")

    if not contacts:
        print("📂 No contacts found.")
        return

    print(f"{'Name':<20}{'Phone Number':<15}")
    print("-" * 35)

    for name, details in contacts.items():
        print(f"{name:<20}{details['phone']:<15}")


def search_contact():
    """Search contact by name or phone number."""
    print("\n--- Search Contact ---")
    search = input("Enter Name or Phone Number: ").strip().lower()

    found = False

    for name, details in contacts.items():
        if search == name.lower() or search == details["phone"]:
            print("\n📇 Contact Found:")
            print(f"Name    : {name}")
            print(f"Phone   : {details['phone']}")
            print(f"Email   : {details['email']}")
            print(f"Address : {details['address']}")
            found = True
            break

    if not found:
        print("❌ Contact not found.")


def update_contact():
    """Update existing contact."""
    print("\n--- Update Contact ---")
    name = input("Enter the contact name to update: ").strip()

    if name not in contacts:
        print("❌ Contact not found.")
        return

    print("Leave field blank to keep current value.")

    phone = input(f"New Phone ({contacts[name]['phone']}): ").strip()
    email = input(f"New Email ({contacts[name]['email']}): ").strip()
    address = input(f"New Address ({contacts[name]['address']}): ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address

    print(f"✅ Contact '{name}' updated successfully!")


def delete_contact():
    """Delete a contact."""
    print("\n--- Delete Contact ---")
    name = input("Enter the contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found.")


def show_menu():
    """Display main menu."""
    print("\n" + "=" * 40)
    print("📞 CONTACT BOOK APPLICATION")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=" * 40)


def main():
    """Main program loop."""
    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n👋 Thank you for using Contact Book!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
