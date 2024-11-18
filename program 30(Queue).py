from collections import deque
bank = deque(["anis", "rahim", "karim"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
if not bank :
    print("no person left")

