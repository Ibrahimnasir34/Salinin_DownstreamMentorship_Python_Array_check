def process_list(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError("Input list length must be a multiple of 10")

    output_list = [num for idx, num in enumerate(input_list, start=1) if idx % 2 != 0 or idx % 3 != 0]
    return output_list



if __name__ == "__main__":
    try:
        input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
        result = process_list(input_list)
        print("Processed list:", result)
    except ValueError as e:
        print("Error:", e)
