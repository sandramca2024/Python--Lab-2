from dictionary_operations import (
    merging_Dict, common_keys, invert_dict, common_key_value_pairs
)

def input_dictionary():
    print("Enter dictionary items (key=value), one per line. Enter 'done' to finish.")
    dictionary = {}
    while True:
        entry = input("Enter key=value: ")
        if entry.lower() == 'done':
            break
        try:
            key, value = entry.split('=')
            dictionary[key.strip()] = value.strip()
        except ValueError:
            print("Invalid format. Please enter in key=value format.")
    return dictionary

def print_menu():
    print("\nDictionary Operations Menu:")
    print("1. Merge dictionaries")
    print("2. Find common keys in dictionaries")
    print("3. Invert a dictionary")
    print("4. Find common key-value pairs in dictionaries")
    print("0. Exit")

def main():
    dictionaries = []
    
    while True:
        print_menu()
        choice = input("Enter your choice (0-4): ")
        
        if choice == '0':
            break
        
        if choice == '1':
            print("Enter dictionaries to merge:")
            while True:
                dictionaries.append(input_dictionary())
                more = input("Add another dictionary? (yes/no): ")
                if more.lower() != 'yes':
                    break
            merged = merging_Dict(*dictionaries)
            print("Merged Dictionary:", merged)
            dictionaries.clear()  

        elif choice == '2':
            print("Enter dictionaries to find common keys:")
            while True:
                dictionaries.append(input_dictionary())
                more = input("Add another dictionary? (yes/no): ")
                if more.lower() != 'yes':
                    break
            common = common_keys(*dictionaries)
            print("Common Keys:", common)
            dictionaries.clear()  

        elif choice == '3':
            dictionary = input_dictionary()
            inverted = invert_dict(dictionary)
            print("Inverted Dictionary:", inverted)

        elif choice == '4':
            print("Enter dictionaries to find common key-value pairs:")
            while True:
                dictionaries.append(input_dictionary())
                more = input("Add another dictionary? (yes/no): ")
                if more.lower() != 'yes':
                    break
            common_pairs = common_key_value_pairs(*dictionaries)
            print("Common Key-Value Pairs:", common_pairs)
            dictionaries.clear() 

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
