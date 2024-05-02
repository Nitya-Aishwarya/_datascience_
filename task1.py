def main():
    # Creating a list with different variable name and values
    custom_list = [100, 200, 300, 400, 500]
    print("List:", custom_list)

    # Adding an element to the list
    custom_list.append(600)
    print("List after adding element:", custom_list)

    # Removing an element from the list
    custom_list.remove(300)
    print("List after removing element:", custom_list)

    # Modifying an element in the list
    custom_list[2] = 1000
    print("List after modifying element:", custom_list)

    # Creating a dictionary with different variable name and values
    custom_dict = {'apple': 10, 'banana': 20, 'orange': 30}
    print("\nDictionary:", custom_dict)

    # Adding a key-value pair to the dictionary
    custom_dict['grape'] = 40
    print("Dictionary after adding key-value pair:", custom_dict)

    # Removing a key-value pair from the dictionary
    del custom_dict['banana']
    print("Dictionary after removing key-value pair:", custom_dict)

    # Modifying a value in the dictionary
    custom_dict['orange'] = 100
    print("Dictionary after modifying value:", custom_dict)

    # Creating a set with different variable name and values
    custom_set = {110, 220, 330, 440, 550}
    print("\nSet:", custom_set)

    # Adding an element to the set
    custom_set.add(660)
    print("Set after adding element:", custom_set)

    # Removing an element from the set
    custom_set.remove(330)
    print("Set after removing element:", custom_set)

    # Trying to modify an element in the set (Sets are immutable, so no modification operation exists)
    # custom_set[2] = 1000  # This line would raise an error

if __name__ == "__main__":
    main()
