import math


def tinh_S(n):
    # Khởi tạo giá trị ban đầu là căn bậc hai của n
    S = math.sqrt(n)

    # Lần lượt lồng căn từ (n-1) về 1
    for i in range(n - 1, 0, -1):
        S = math.sqrt(i + S)

    return S


# Kiểm tra hàm với giá trị n = 5
n = 5
print(f"S({n}) =", tinh_S(n))