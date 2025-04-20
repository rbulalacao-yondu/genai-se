def get_item(arr, index):
    return arr[index]

def main():
    items = ["apple", "banana", "cherry"]
    # Valid access:
    print("Third fruit is:", get_item(items, 2))
    # Invalid access — this will raise IndexError
    print("Fifth fruit is:", get_item(items, 4))

if __name__ == "__main__":
    main()