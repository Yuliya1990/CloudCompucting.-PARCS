import random

def generate_random_integers(num_integers):
    random_integers = [random.randint(0, 999) for _ in range(num_integers)]
    return random_integers

def write_to_file(filename, numbers):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(str(number) + '\n')

if __name__ == "__main__":
    num_integers = 1000000
    random_integers = generate_random_integers(num_integers)
    write_to_file("random_integers.txt", random_integers)
    print("Random integers have been written to 'random_integers.txt'.")
