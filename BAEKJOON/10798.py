# T = int(input())
# for tc in range(1, T+1):
word = [list(map(str, input())) for _ in range(5)]
max_len = 0
for i in word:
    if len(i) > max_len:
        max_len = len(i)
for i in word: #공백 맞춰주기
    if len(i) < max_len:
        while len(i) < max_len:
            i.append('')
word_1 = list(zip(*word)) # 전치
word_2 = '' #출력준비
for i in range(len(word_1)):
    for j in range(len(word_1[0])):
        if word_1[i][j] != '':
            word_2 += (word_1[i][j])
print(f'{word_2}')
