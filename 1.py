import module_ListFunction as mlf

def print_menu():
    print("\nMenu:")
    print("1. Find maximum value")
    print("2. Find minimum value")
    print("3. Calculate sum")
    print("4. Compute average")
    print("5. Find median")
    print("6. Exit")

def get_list_input():
    user_input = input("Enter numbers separated by spaces: ")
    return [int(x) for x in user_input.split()]

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting the program.")
            break

        if choice in ['1', '2', '3', '4', '5']:
            lst = get_list_input()
            
            try:
                if choice == '1':
                    print("Maximum value:", mlf.find_max(lst))
                elif choice == '2':
                    print("Minimum value:", mlf.find_min(lst))
                elif choice == '3':
                    print("Sum of elements:", mlf.calculate_sum(lst))
                elif choice == '4':
                    print("Average of elements:", mlf.compute_average(lst))
                elif choice == '5':
                    print("Median of elements:", mlf.find_median(lst))
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
