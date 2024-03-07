import time


def calc(n):
    if n % 2 == 0:
        n = int(n / 2)
        return n
    else:
        n = int(3 * n + 1)
        return n


def update_sequence_dict(seq_dict, current_number):
    while current_number not in seq_dict:
        next_number = calc(current_number)
        seq_dict[current_number] = next_number
        current_number = next_number


sequence_dict = {}

start = time.time()
for i in range(1, 10001):
    update_sequence_dict(sequence_dict, i)

end = time.time()

print(sequence_dict)
print({"Time taken": end - start})
