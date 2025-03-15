def solution(x):
    if x == 0:
        return True
    
    if x < 0:
        return False
    
    # Check if x ends with 0 (except 0 itself)
    if x % 10 == 0 and x != 0:
        return False

    reverse = 0
    original = x
    while x > 0:
        last = x % 10
        reverse = reverse * 10 + last
        x = x // 10

    return reverse == original

# For testing locally
if __name__ == "__main__":
    test_cases = [121, -121, 10, 12321, 0]
    for tc in test_cases:
        print(f"{tc}: {solution(tc)}")
