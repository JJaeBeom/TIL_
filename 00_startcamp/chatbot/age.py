# ctrl + / = 현재 포커싱 되어있는 줄을 주석 처리/ 주석 해제
# student = {'홍진환': 50, '김성현': 0, '홍진환':30}

student = {
    '강남구': '비싸다', 
    '종로구': [1, 2, 3], 
    '서대문구': {
        '김구현': 13, 
        'viktor': ['여기도', 'dict의', 'value이다.']
        }
    }

menu = [['아침', '점심', '저녁'], {'강남구': 50, '서대문구': 47}]

print(student)
print(menu)
print(menu[0][1])
print(menu[1]['서대문구'])
print(student['서대문구']['viktor'][1])