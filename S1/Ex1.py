import random
import string
import numpy as np
import pandas as pd
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else 'Division by zero error'
    else:
        return 'Invalid operation'
    
def remove_duplicates(lst):
    return list(set(lst))

data = {
    'name': 'Praneeth',
    'age': 21,
    'city': 'Hyderabad',
    'job': 'Student',
    'college': 'vnr vjiet'
}


matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

sum_matrix = matrix1 + matrix2
product_matrix = np.dot(matrix1, matrix2)


def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.head()

import string

def most_common_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip(string.punctuation)
        word_count[word] = word_count.get(word, 0) + 1
    return max(word_count, key=word_count.get) if word_count else None


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

