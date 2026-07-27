"""
문제: 피로도 (프로그래머스 Lv2)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
유형: 완전탐색(백트래킹) / 소요: (직접 적어)
약속: dfs(s) = 피로도 s와 지금 visited 상태에서, 앞으로 돌 수 있는 던전의 최대 개수
말단: 갈 수 있는 던전이 없으면 0 — return 0 대신 best=0 초기값이 그 역할
갈래: 남은 던전 중 입장 가능한 것만 / 갈래 값 = 1 + dfs(돌고 난 피로도), 끝나면 visited 원상복구
연산: max (타겟넘버의 더하기와 다름 — 세계의 개수가 아니라 최고 기록을 고르는 문제라서)
배운 점: 약속은 문제가 최종적으로 묻는 값의 단위에서 역산한다.
"""

"""재구현 이력
2026.07.24 최초 — 뼈대와 빈칸을 받아서 통과
2026.07.27 2회차 백지 — 실패. 다음 다섯 군데가 틀림
  1. visited를 dfs 안에서 생성 → 호출마다 새 판이 생김. 자리는 solution 안, dfs 밖
  2. dfs(s)를 부르기만 하고 반환값을 안 씀 → cand = dfs(...) + 1 로 받아야 함
  3. best를 dfs 밖에 둠 → 자리는 dfs 첫 줄. 호출마다 새로 0
  4. 뺄 값을 dungeons[i][0](필요)로 씀 → dungeons[i][1](소모)
  5. 갈래를 "이 던전을 돌지 말지" 2개로 봄 → "남은 것 중 어느 것을 고를지" n개
  6. 약속 문장에 s를 안 씀 → dfs(6)과 dfs(3)이 왜 다른지 설명이 안 됨
"""

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n

    def dfs(s):
        # 약속: 피로도 s, 지금 visited 상태에서 앞으로 돌 수 있는 최대 던전 개수
        best = 0
        for x in range(n):
            if visited[x]:
                continue          # 이미 돈 던전은 갈래가 아님
            if s < dungeons[x][0]:
                continue          # 입장 불가 조건 
            visited[x] = True
            cand = dfs(s-dungeons[x][1])+1          # 이 갈래의 값: "던전 1개 + 그 뒤로의 최대"
            visited[x] = False    # 이 세계 탐험 끝, 다른 갈래를 위해 원상복구
            best = max(best,cand)          # 합치기 — 네가 말한 max, best와 cand로
        return best

    return dfs(k)             # 시작 상태: 아직 아무 데도 안 갔을 때의 피로도
