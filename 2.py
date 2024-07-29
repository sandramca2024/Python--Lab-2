from set_operations import (
    add_element, remove_element, union_intersection, difference,
    is_subset, set_length, symmetric_difference, power_set, unique_subsets
)

def print_menu():
    print("\nSet Operations Menu:")
    print("1. Add element to set")
    print("2. Remove element from set")
    print("3. Union and Intersection of two sets")
    print("4. Difference between two sets")
    print("5. Check if set is a subset of another set")
    print("6. Find length of a set")
    print("7. Compute symmetric difference of two sets")
    print("8. Compute power set of a set")
    print("9. Get unique subsets of a set")
    print("0. Exit")

def main():
   
    set1 = set()
    set2 = set()
    
    while True:
        print_menu()
        choice = input("Enter your choice (0-9): ")
        
        if choice == '0':
            break
        
        if choice == '1':
            element = int(input("Enter element to add: "))
            add_element(set1, element)
            print(f"Set1 after adding {element}: {set1}")

        elif choice == '2':
            element = int(input("Enter element to remove: "))
            remove_element(set1, element)
            print(f"Set1 after removing {element}: {set1}")

        elif choice == '3':
            set2 = set(map(int, input("Enter elements for Set2 (comma-separated): ").split(',')))
            union, intersection = union_intersection(set1, set2)
            print(f"Union of Set1 and Set2: {union}")
            print(f"Intersection of Set1 and Set2: {intersection}")

        elif choice == '4':
            set2 = set(map(int, input("Enter elements for Set2 (comma-separated): ").split(',')))
            diff = difference(set1, set2)
            print(f"Difference (Set1 - Set2): {diff}")

        elif choice == '5':
            set2 = set(map(int, input("Enter elements for Set2 (comma-separated): ").split(',')))
            print(f"Is Set1 a subset of Set2? {is_subset(set1, set2)}")

        elif choice == '6':
            print(f"Length of Set1: {set_length(set1)}")

        elif choice == '7':
            set2 = set(map(int, input("Enter elements for Set2 (comma-separated): ").split(',')))
            sym_diff = symmetric_difference(set1, set2)
            print(f"Symmetric Difference of Set1 and Set2: {sym_diff}")

        elif choice == '8':
            print(f"Power Set of Set1: {power_set(set1)}")

        elif choice == '9':
            print(f"Unique Subsets of Set1: {unique_subsets(set1)}")

        else:
            print("Invalid choice. Please enter a number between 0 and 9.")

if __name__ == "__main__":
    main()
