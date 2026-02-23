def bai1_predict():
    x = float(input("Nhập x: "))
    w = float(input("Nhập w: "))
    b = float(input("Nhập b: "))
    y = w * x + b
    print("Giá trị dự đoán y =", y)
def bai2_word_frequency():
    sentence = input("Nhập câu: ")
    sentence = sentence.lower()
    for ch in ".,!?":
        sentence = sentence.replace(ch, "")
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    print("Tần suất từ:", freq)
# Đếm số từ
def bai3_word_count():
    sentence = input("Nhập câu: ")
    sentence = sentence.lower()
    for ch in ".,!?":
        sentence = sentence.replace(ch, "")
    words = sentence.split()
    print("Số từ trong câu:", len(words))
def bai4_bag_of_words():
    sentence = input("Nhập câu: ")
    vocab = input("Nhập vocab (cách nhau bằng dấu phẩy): ").split(",")
    sentence = sentence.lower()
    vocab = [v.strip().lower() for v in vocab]
    for ch in ".,!?":
        sentence = sentence.replace(ch, "")
    words = sentence.split()
    vector = []
    for v in vocab:
        vector.append(words.count(v))
    print("Vector Bag of Words:", vector)
def main():
    print("1. Bài 1 - Dự đoán tuyến tính")
    print("2. Bài 2 - Word Frequency")
    print("3. Bài 3 - Word Count")
    print("4. Bài 4 - Bag of Words")
    choice = int(input("Chọn bài (1-4): "))
    if choice == 1:
        bai1_predict()
    elif choice == 2:
        bai2_word_frequency()
    elif choice == 3:
        bai3_word_count()
    elif choice == 4:
        bai4_bag_of_words()
    else:
        print("Lựa chọn không hợp lệ!")
main()
