# eperate script with functions to import from other scripts or notebooks

def compute_the_mean(numbers):
    return sum(numbers) / len(numbers)


# if run in terminal then print
print(__name__)
if __name__ == "__main__":
    output = compute_the_mean([2, 3, 4, 5])
    print(output)