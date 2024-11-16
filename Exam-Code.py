def display_menu():
    print("\n--- Data Management Menu ---")
    print("1. Add Single Data")
    print("2. Add Multiple Data")
    print("3. Display Data")
    print("4. Delete Data")
    print("5. Update Data")
    print("6. Reverse Data")
    print("7. Exit")
    print("-----------------------------")

def main():
    data_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            item = input("Enter data to add: ")
            data_list.append(item)
            print(f"'{item}' has been added.")
        
        elif choice == '2':
            items = input("Enter data to add separated by commas: ")
            data_list.extend(items.split(','))
            print(f"{len(items.split(','))} items have been added.")

        elif choice == '3':
            print("Current Data:")
            for idx, item in enumerate(data_list, start=1):
                print(f"{idx}. {item}")

        elif choice == '4':
            item = input("Enter data to delete: ")
            if item in data_list:
                data_list.remove(item)
                print(f"'{item}' has been deleted.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == '5':
            idx = int(input("Enter the index of data to update (1 to {}): ".format(len(data_list))))
            if 1 <= idx <= len(data_list):
                new_item = input("Enter new data: ")
                data_list[idx - 1] = new_item
                print(f"Data at index {idx} has been updated to '{new_item}'.")
            else:
                print("Invalid index.")

        elif choice == '6':
            data_list.reverse()
            print("Data has been reversed.")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()