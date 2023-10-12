import random

hiragana = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"]
katakana = ["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", "サ", "シ", "ス", "セ", "ソ", "タ", "チ", "ツ", "テ", "ト", "ナ", "ニ", "ヌ", "ネ", "ノ", "ハ", "ヒ", "フ", "ヘ", "ホ", "マ", "ミ", "ム", "メ", "モ", "ヤ", "ユ", "ヨ", "ラ", "リ", "ル", "レ", "ロ", "ワ", "ヲ", "ン"]

kr = ["아", "이", "우", "에", "오", "카", "키", "쿠", "케", "코", "사", "시", "스", "세", "소", "타", "치", "츠", "테", "토", "나", "니", "누", "네", "노", "하", "히", "후", "헤", "호", "마", "미", "무", "메", "모", "야", "유", "요", "라", "리", "루", "레", "로", "와", "오", "응"]
en = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so", "ta", "chi", "tsu", "te", "to", "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"]

ques_list = [] # 문제 리스트
answ_list = [] # 정답 리스트
num_list = [] # 숫자 리스트

cnt = 0 # 반복문 카운트
num = 0 # 문제 개수

jp_type = "" # 문제 타입

answer = "" # 사용자 입력값
crct = 0 # 정답 개수
retry = "" # 재시작 여부

def generate_question(number):
    temp1 = list(range(0, len(hiragana)))
    random.shuffle(temp1)
    temp2 = list(range(0, len(katakana)))
    random.shuffle(temp2)
    num_list = temp1 + temp2
    del num_list[number:]

    for cnt in range(0, number):
        if jp_type == "1":
            ques_list.append(hiragana[num_list[cnt]])
            answ_list.append(kr[num_list[cnt]])
        elif jp_type == "2":
            ques_list.append(katakana[num_list[cnt]])
            answ_list.append(kr[num_list[cnt]])
        elif jp_type == "3":
            if num_list[cnt] % 2 == 0:
                ques_list.append(hiragana[num_list[cnt]])
                answ_list.append(kr[num_list[cnt]])
            else:
                ques_list.append(katakana[num_list[cnt]])
                answ_list.append(kr[num_list[cnt]])

print("일본어 읽기 연습 프로그램입니다.\n히라가나 또는 가타카나의 발음을 맞춰보세요!")

while True:
    jp_type = str(input("\n히라가나만(1), 가타카나만(2), 섞어서(3) 중 하나를 선택하세요 (1/2/3) : "))
    num = int(input("몇 개의 글자를 연습하실건가요? (1~96): "))
    generate_question(num) # 문제와 답 생성
    for cnt in range(0, num):
        answer = str(input("\n" + str(cnt+1) + "번째 문제 - " + ques_list[cnt] + "는 무슨 발음일까요? : "))
        if answer == answ_list[cnt]:
            print("⭕정답입니다⭕")
            crct += 1
        else:
            print("❌오답입니다❌\n정답은 " + answ_list[cnt] + "입니다.")
    print("\n총 " + str(num) + "개 중 " + str(crct) + "개를 맞추셨습니다.")

    retry = str(input("\n다시 하시겠습니까? (y/n) : "))
    if retry == "y":
        ques_list.clear()
        answ_list.clear()
        num_list.clear()
        crct = 0 # 초기화
        continue
    elif retry == "n":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        break