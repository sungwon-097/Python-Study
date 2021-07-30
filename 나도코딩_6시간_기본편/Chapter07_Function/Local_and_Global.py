gun=10

def checkpoint(soldiers):
    global gun #global을 사용하지 않았을 경우 checkpoint에서만 사용 가능한 local variable
    gun= gun - soldiers
    print(f"[함수 내]남은 총 : {gun}")

print(f"전체 총 : {gun}")
checkpoint(2)
print(f"남은 총 : {gun}")

def checkpoint_ret(gun, soldiers):
    gun=gun-soldiers
    print(f"함수 내 : 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
gun=checkpoint_ret(gun, 2)
print(f"남은 총 : {gun}")