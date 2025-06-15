def is_palindrome(s):
    print(f"Original: {s}")
    s = ''.join(filter(str.isalnum, s)).lower()
    print(f"Processed: {s}")
    result = s == s[::-1]
    print(f"Is palindrome? {result}")
    return result

def test_cases():
    cases = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?"
    ]
    for case in cases:
        is_palindrome(case)

if __name__ == "__main__":
    test_cases()