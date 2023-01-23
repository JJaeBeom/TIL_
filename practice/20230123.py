# 5-2 달력 문제
# 입력 예시
# 2015
# 8
# 31

# # 출력 예시 
# # 경고 월요일입니다.
# # {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
# import calendar
# year = int(input('연도를 입력해주세요. : '))
# #윤년 x
# #calendar.isleap(year) year가 윤년이면 True를, 그렇지 않으면 False를 반환합니다.
# while calendar.isleap(year): #윤년이라면 
#     print('윤년은 불가능합니다. 다시 입력해주세요.')
#     year = int(input('연도를 입력해주세요. : ')) #다시 입력 받기.
# print(calendar.calendar(year)) #해당 연도 달력 출력.
# month = int(input('월을 입력해주세요. : '))
# day = int(input('일을 입력해주세요. : '))
# weekday_num = calendar.weekday(year, month, day)
# # 월요일 = 경고메시지. 월 : 0 ~ 일 : 6
# if weekday_num == 0 :
#     print('경고! 월요일입니다.')
# #dictionary에 정리해서 출력
# week_dict = {0: "월요일", 1: "화요일", 2: "수요일",
#              3: "목요일", 4: "금요일", 5: '토요일', 6: '일요일'}

# date_dict = {"년": year, "월": month,
#              "일": day, "요일": week_dict[weekday_num]}
# print(date_dict)
######################################
# 6-4 애너그램
words = ['eat','tea','tan','ate','nat','bat', 'haha', 'aahh']
def group_anagrams(words):
    word_dict = {}
    for word in words:
        sub_dict = {}
        for char in word:
            if char in sub_dict:
                sub_dict[char] += 1
            else:
                sub_dict[char] = 1
        word_dict[word] = sub_dict

    anagram = []
    for word in words:
        for ana_list in anagram:
            ana_word = ana_list[0]
            if word_dict[word] == word_dict[ana_word]:
                ana_list.append(word)
                break
        else:
            anagram.append([word])
    return anagram        


print(group_anagrams(words))


words = ['eat','tea','tan','ate','nat','bat', 'haha', 'aahh']

def group_anagrams(words):
    word_dict = {} # 단어를 수집할 딕셔너리 생성
    for word in words:    # 넘겨받은 모든 단어들을 순회
        sub_dict = {} # 현재 조사할 word의 정보를 저장할 dict 생성
        for char in word:# 각 단어를 알파벳 기준으로 순회
            if char in sub_dict: # 만약 순회중인 알파벳이 현재 단어 정보 dict에 이미 있다면
                sub_dict[char] += 1 # 해당 알파벳의 개수를 1 증가
            else:
                # 아니면, sub_dictt에 해당 알파벳을 키로 하는 새로운 값 1 할당
                sub_dict[char] = 1
        # word에 대한 조사가 끝나면 단어 수집할 dict에
        # word를 키로하는 단어 정보 dict : sub_dict을 할당
        word_dict[word] = sub_dict

    anagram = []  # 애너그램이 형성되는 단어들끼리 그룹핑할 리스트 생성
    # 다시 모든 단어들을 순회
    # word_dict의 key로 사용할 예정
    for word in words:
        # anagram 리스트 안에서 또다른 리스트를 만들어 그룹필 할 예정이므로
        # anagram이 가진 모든 리스트 항목을 순회한다
        # 단, 최초 순회시에는 anagram 리스트가 비어있으므로
        # 반복문 내부 코드가 실행되지 않고,
        # break된적 없으므로 for else문이 실행,
        # 최초 순회하는 word를 삽입한다.
        for ana_list in anagram:
            # anagram의 요소들 중 하나인 ana_list에는 
            # word가 1개 이상 포함되어 있으므로 0번째 조회가능
            # 아나그램을 형성할 수 있는 대표 단어를 찾아 할당한다.
            ana_word = ana_list[0]
            # 대표단어 ana_word와 현재 순회중인 단어 word가 
            # 동일한 단어 정보(sub_dict)를 가지고 있다면, 둘은 아나그램이 형성가능하다.
            if word_dict[word] == word_dict[ana_word]:
                # 따라서 현재 순회중인 리스트에 
                # 현재 순회중인 단어를 삽입하고
                # break -> 그래야 for else문이 실행되지 않아, 새로운 그룹이 만들어지지 않는다.
                ana_list.append(word)
                break
        else:
            # word를 anagram에 삽입할 때, 그룹을 만들어야 하므로
            # 단어를 그대로 삽입하는 것이 아닌,
            # 리스트 형태로 삽입한다.
            anagram.append([word])
    return anagram        


print(group_anagrams(words))

