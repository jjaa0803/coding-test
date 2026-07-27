"""
문제: 모음사전 (프로그래머스 Lv2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/84512
유형: 완전탐색(재귀) / 소요:

약속: dfs(s)는 아무것도 반환하지 않는다. s로 시작하는 5글자 이하 단어를
      사전순으로 전부 result에 넣는다.
말단: len(s) == 5 이면 return. 값 없이 그냥 멈추고 더 안 내려간다.
갈래: 'A','E','I','O','U' 다섯 개. 거를 조건 없음(같은 글자 여러 번 써도 됨).
연산: 없음. 합칠 반환값이 없다. result.append 가 일의 전부.
답:   dfs("") 를 다 돌린 뒤 result.index(word) + 1. index()는 0부터 세니까 +1.

배운 점
1. 재귀에 두 종류가 있다. 타겟넘버·피로도는 답이 아래에서 위로 올라오는 종류(return 있음).
   모음사전은 내려가면서 그때그때 일을 하는 종류(return 없음).
   새 문제를 만나면 어느 쪽인지부터 정할 것. 이번엔 피로도 틀을 그대로 가져와서 막혔다.
2. 만드는 순서가 곧 사전순이다. A→E→I→O→U 순으로 돌면서 만들자마자 append 하면
   result = ['A','AA','AAA','AAAA','AAAAA','AAAAE',...] 순서가 나온다.
3. dfs(s+i) 는 완전히 끝나야 for 문이 다음 i 로 넘어간다.
   그래서 "AAAA"는 4번째인데 "AAAE"는 10번째다. 사이에 AAAAA~AAAAU 다섯 개가 들어간다.
4. 재귀는 머리로 끝까지 따라가는 게 아니다. dfs("") 밑에 단어가 3905개다.
   한 층만 읽고, dfs(s+i) 안은 약속을 믿고 안 본다. 약속을 쓰는 이유가 이것이다.
5. 전수 나열이 낭비 아닌지 의심했는데, 3905개는 0.5ms다.
   완전탐색 판단은 감이 아니라 개수를 세서 1억과 비교하는 것.
"""
def solution(word):
    result = []
    def dfs(s):
        if len(s) == 5:
            return
            
        for i in ['A','E','I','O','U']:
            result.append(s+i)
            dfs(s+i)
            
    
    answer = dfs("")
    
    return result.index(word)+1