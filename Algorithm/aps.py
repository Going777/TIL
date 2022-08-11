import sys

sys.stdin = open('input.txt', 'r')



# 구간합
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     lst = [0] + list(map(int, input().split()))
#     sum_k = [0] * (N-M+1)
#
#     for i in range(1, N+1): # 입력받은 배열로 누적합 계산
#         lst[i] += lst[i-1]
#
#     i = M
#     j = 0
#     while i < N+1:
#         sum_k[j] = lst[i] - lst[j]
#         i += 1
#         j += 1
#
#     mx, mn = sum_k[0], sum_k[0]
#     for sm in sum_k:
#         if mx < sm:
#             mx = sm
#         elif mn > sm:
#             mn = sm
#
#     print(f"#{test_case} {mx-mn}")

# 정렬
# def bubble_sort(arr, N):
#     for i in range(N - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     s_arr = bubble_sort(arr, N)
#
#     print(f"#{test_case} {' '.join(map(str, s_arr))}")

# 숫자 카드
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     counts = [0] * 10 # 0~9까지 원소별 카운트 저장할 배열
#     for num in input():
#         counts[int(num)] += 1
#
#     mx_cnt = counts[0] # 가장 큰 카운트 값 초기화
#     mx_num = counts.index(mx_cnt) # 가장 큰 카운트에 해당하는 숫자 초기화
#     for i in range(10):
#         if mx_cnt <= counts[i]: # 카드 장수가 같을 경우, 더 큰 숫자를 저장해야하므로, 등호 포함 필수
#             mx_cnt = counts[i]
#             mx_num = i
#
#     print(f"#{test_case} {mx_num} {mx_cnt}")

# 전기 버스
# T = int(input())
# for test_case in range(1, T+1):
#     K, N, M = map(int, input().split())
#     station = [0] + list(map(int, input().split())) + [N] # '출발위치 + 충전소위치 + 종점위치'담은 배열
#     cnt = 0 # 충전소 들리는 횟수
#
#     i = 0 # 현재 위치
#     while i < N-K:
#         for k in range(K, -1, -1): # 최소 충전 횟수를 구해야하므로 K값의 뒤에서부터 탐색
#             if k == 0: # 충전소에 도착할 수 없는 경우 -> 종료 -> 0 출력
#                 cnt = 0
#                 i += N # 강제종료를 위해 N을 더해줌
#                 break
#             if (i+k) in station: # 현재 위치에서 k만큼 이동했을 때 충전소가 있다면
#                 i += k # 현재 위치를 해당 충전소 위치로 변경
#                 cnt += 1
#                 break
#
#     print(f"#{test_case} {cnt}")

# 간단한 소인수분해
# T = int(input())
# for t in range(1, T+1):
#     num = int(input())
#     div = [2, 3, 5, 7, 11] # 약수 배열
#     result = []
#
#     for d in div:
#         cnt = 0
#         while (num % d == 0): # 해당 약수로 나누어떨어지면 계속 반복
#             cnt += 1 # 카운트 +1
#             num //= d # 타겟값인 num은 약수로 나눠줌
#         result.append(cnt)
#
#     print(f"#{t}", *result)

# 현주의 상자 바꾸기
# T = int(input())
# for t in range(1, T+1):
#     N, Q = map(int, input().split())
#     box = [0] * N # 초기 상태 박스(모두 0)
#     for i in range(1, Q+1): # Q회 반복
#         L, R = map(int, input().split())
#         box[L-1:R] = [i] * (R-L+1)
#
#     print(f"#{t}", *box)

# 삼성시의 버스 노선
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     counts = [0] * 5000 # 정류장별 노선 개수 저장 배열
#     result = [] # 최종 결과 저장 배열 (P의 개수만큼 해당 정류장 번호의 노선 개수 저장)
#
#     # start 번호부터 end 번호까지 정류장에 노선 개수 1씩 증가
#     for _ in range(N):
#         start, end = map(int, input().split())
#         counts[start-1: end]  = list(map(lambda x: x+1, counts[start-1: end]))
#
#     P = int(input())
#     # 각 정류장 번호에 해당하는 노선 개수 result에 추가
#     for j in range(1, P+1):
#         result.append(counts[j-1])
#
#     print(f"#{t}", *result)

# Flatten
# T = 10
# for test_case in range(1, T + 1):
#     dump_cnt = int(input())
#     boxes = list(map(int, input().split()))
#     result = 0
#
#     cnt = 0
#     while cnt <= dump_cnt:
#         max_h_i, min_h_i = 0, 0
#         for idx in range(len(boxes)):  # 리스트 내 최댓값, 최솟값 인덱스 찾기
#             if boxes[max_h_i] < boxes[idx]:
#                 max_h_i = idx
#             elif boxes[min_h_i] > boxes[idx]:
#                 min_h_i = idx
#
#         cnt += 1
#         result = boxes[max_h_i] - boxes[min_h_i]
#
#         if result <= 1:  # 빠른 종료조건(dump 카운트 내에 평탄화 완료된 경우)
#             break
#
#         # 최대 높이 박스를 최소 높이 위치로 이동
#         boxes[min_h_i] += 1
#         boxes[max_h_i] -= 1
#
#     print(f"#{test_case} {result}")

# 쉬운 거스름돈
# T = int(input())
# for t in range(1, T+1):
#     m = int(input())
#     m_u = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
#     result = []
#
#     for u in m_u:
#         result.append(m // u)
#         m %= u
#
#     print(f"#{t}")
#     print(*result)

# 델타 검색
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     for i in range(N):
#         for j in range(N):
#             for k in ((-1,0),(1,0),(-1,0),(0,1)): # 상하좌우 4방향 탐색
#                 ni, nj = i + k, j + k
#                 if (0 <= ni < N) and (0 <= nj < N):
#                     ori = arr[i][j]
#                     new = arr[ni][nj]
#                     abs_r = ori-new if ori > new else new-ori # 내장함수 쓰지 않고 절댓값 구하기
#                     ans += abs_r
#     print(f"#{t} {ans}")

# 부분집합
# def my_sum(arr):
#     ans = 0
#     for a in arr:
#         ans += a
#     return ans
#
# T = int(input())
# for t in range(1, T+1):
#     is_exist = 0
#     arr = list(map(int, input().split()))
#     n = len(arr)
#     p = []
#
#     for i in range(1, 1 << n): # 공집합 제외
#         for j in range(n):
#             if i & (1 << j):
#                 p.append(arr[j])
#         if my_sum(p) == 0:
#             is_exist = 1
#             break
#         p = []
#
#     print(f"#{t} {is_exist}")

# 연속한 1의 개수
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input()))
#     max_cnt = 0
#     cnt = 0
#     for i in range(N):
#         if arr[i] == 1:
#             cnt += 1
#             if max_cnt < cnt:
#                 max_cnt = cnt
#         else:
#             cnt = 0
#
#     print(f"#{t} {max_cnt}")

# 고대 유적
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     m_cnt = 0
#
#     for i in range(N):
#         tmp = 0
#         for j in range(M):
#             if arr[i][j] == 1:
#                 tmp += 1
#                 if m_cnt < tmp:
#                     m_cnt = tmp
#             else:
#                 tmp = 0
#
#     for j in range(M):
#         tmp = 0
#         for i in range(N):
#             if arr[i][j] == 1:
#                 tmp += 1
#                 if m_cnt < tmp:
#                     m_cnt = tmp
#             else:
#                 tmp = 0
#
#     print(f"#{t} {m_cnt}")

# 달팽이 숫자
# # 방향 -> 우하좌상
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]
#
#     num = 1 # 배열에 기록할 숫자
#     i, j = 0, -1 # 초기 위치
#     d = 0 # 방향 초기화(우측 이동)
#     while num <= N**2:
#         # 다음번 예상 위치
#         ni = i + di[d]
#         nj = j + dj[d]
#
#         # 조건 탐색
#         if (0 <= ni < N) and (0 <= nj < N) and (arr[ni][nj] == 0): # 예상 위치가 범위내이 있으면서 해당 자리가 비어있는 경우
#             arr[ni][nj] = num  # 해당 자리에 숫자 기록
#             num += 1
#             i, j = ni, nj # 현재 위치 갱신
#         else: # 기록 X , 방향 전환
#             d = (d + 1) % 4
#
#     print(f"#{t}")
#     [print(*row) for row in arr]

# Sum
# T = 10
# for _ in range(2):
#     N = int(input())
#     arr = [list(map(int, input().split())) * 100 for _ in range(100)]
#     m_sum = 0
#
#     tmp3, tmp4 = 0, 0
#     for i in range(100):
#         tmp, tmp2 = 0, 0
#         tmp3 += arr[i][i] # 우측하단 대각선 합
#         tmp4 += arr[i][100-i-1] # 좌측하단 대각선 합
#         for j in range(100):
#             tmp += arr[i][j] # 행 합
#             tmp2 += arr[j][i] # 열 합
#
#         for t_sum in [tmp, tmp2, tmp3, tmp4]: # 가장 큰 값 찾기
#             if t_sum > m_sum:
#                 m_sum = t_sum
#
#     print(f"#{N} {m_sum}")

# 최대 성적표 만들기
# def select_sort(arr, N, K): # 내림차순 반환 (선택정렬)
#     for i in range(K): # K번 반복하면 K번째까지의 최대값을 앞쪽부터 찾을 수 있다
#         m_idx = i
#         for j in range(i+1, N):
#             if arr[m_idx] < arr[j]:
#                 m_idx = j
#         arr[m_idx], arr[i] = arr[i], arr[m_idx]
#     return arr
#
# T = int(input())
# for t in range(1, T+1):
#     N, K = map(int, input().split())
#     scores = list(map(int, input().split()))
#     s_scores = select_sort(scores, N, K)
#     k_sum = sum(s_scores[:K])
#     print(f"#{t} {k_sum}")

# 1789, 수들의 합
# S = int(input())
# n = 0
# m_sum = 0
# while m_sum < S:
#     n += 1
#     m_sum += n
# if S < m_sum:
#     n -= 1
# print(n)

# 색칠하기
# def make_arr(arr, s_i, s_j, e_i, e_j):
#     for i in range(s_i, e_i+1):
#         for j in range(s_j, e_j+1):
#             arr[i][j] = 1
#     return arr
#
# T = int(input())
# for t in range(1, T+1):
#     arr1 = [[0]*10 for _ in range(10)] # c=1일 때 채울 배열
#     arr2 = [[0]*10 for _ in range(10)] # c=2일 때 채울 배열
#     N = int(input())
#     cnt = 0 # 겹치는 박스 개수
#
#     for _ in range(N):
#         s_i, s_j, e_i, e_j, c = map(int, input().split())
#         if c == 1:
#             arr1 = make_arr(arr1, s_i, s_j, e_i, e_j)
#         else:
#             arr2 = make_arr(arr2, s_i, s_j, e_i, e_j)
#
#     # 배열의 모든 원소를 순회하면서, arr1 arr2의 원소값이 모두 1인 경우 cnt+=1
#     for i in range(10):
#         for j in range(10):
#             if arr1[i][j] == arr2[i][j] == 1:
#                 cnt += 1
#     print(f"#{t} {cnt}")

# 부분집합의 합
# def my_sum(lst):
#     ans = 0
#     for s in lst:
#         ans += s
#     return ans
#
# T = int(input())
# for t in range(1, T+1):
#     A = list(range(1, 13)) # 1~12
#     M = len(A) # A의 원소 개수(12)
#     N, K = map(int, input().split()) # 원소 개수, 원소 N개의 합
#     cnt = 0
#
#     for i in range(1, 1<<M): #
#         p = []
#         for j in range(M):
#             if i & (1<<j):
#                 p.append(A[j])
#         print(i, p)
#         if len(p) == N and my_sum(p) == K:
#             cnt += 1
#
#     print(f"#{t} {cnt}")

# 이진탐색
# def calc_cnt(P, t):
#     book = list(range(1, P+1))
#     l, r = 0, P-1 # 초기 위치
#     cnt = 0
#
#     while l < r:
#         m = (l + r) // 2 # 중간값 계산
#         cnt += 1
#         if book[m] == t: # 타겟값을 찾은 경우
#             return cnt
#         elif book[m] < t: # 중간값보다 타겟이 크다면 우측에서 탐색
#             l = m # left를 중간값으로 갱신
#         else: # 중간값보다 타겟이 작다면 좌측에서 탐색
#             r = m # right를 중간값으로 갱신
#     return 0 # 타겟값을 찾지 못한 경우
#
# T = int(input())
# for t in range(1, T+1):
#     P, A, B = map(int, input().split())

#     cnt_A = calc_cnt(P, A)
#     cnt_B = calc_cnt(P, B)
#
#     result = "A" if cnt_A < cnt_B else "B" if cnt_A > cnt_B else 0
#     print(f"#{t} {result}")

# 특별한 정렬
# def selection_sort(arr, N):
#     for i in range(N-1):
#         max_i = i
#         for j in range(i+1, N):
#             if arr[max_i] < arr[j]:
#                 max_i = j
#         arr[max_i], arr[i] = arr[i], arr[max_i]
#     return arr
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     s_arr = selection_sort(arr, N) # 입력받은 배열 내림차순 정렬
#     result = []
#     for i in range(N//2): # 양 끝단에서부터 안쪽으로 원소 2개씩 result에 append
#         result.extend([s_arr[i], s_arr[N-i-1]])
#     if N % 2: # 배열의 길이가 홀수라면, 중앙의 원소는 포함되지 못함 >> 따로 append 필요
#         result.append(s_arr[N//2])
#     print(f"#{t}", *result[:10]) # 10개까지만 출력

# 파리 퇴치
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     s_max = 0
#
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             tmp = 0
#             for k in range(i, i + M):
#                 for l in range(j, j + M):
#                     tmp += arr[k][l]
#             s_max = tmp if s_max < tmp else s_max
#
#     print(f"#{t} {s_max}")

# 어디에 단어가 들어갈 수 있을까
# T = int(input())
# for t in range(1, T+1):
#     N, K = map(int, input().split()) # 크기 / 단어 길이
#     arr = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)] # 0으로 행렬 둘러쌈
#     cnt = 0
#
#     for _ in range(2): # 원래 행렬 & 전치 행렬 행 탐색
#         for i in range(N+2): # 원래 행렬에서 앞,뒤로 2개씩 늘었기 때문에 N+1까지 탐색해야 함
#             tmp = 0 # 1의 누적합 저장 변수
#             for j in range(N+2):
#                 if arr[i][j] == 1: # 해당 원소값이 1인 경우
#                     tmp += 1
#                 else: # 해당 원소값이 0인 경우
#                     if tmp == K: # 지금까지 누적된 tmp값이 K와 같다면 cnt += 1
#                         cnt += 1
#                     tmp = 0 # tmp 초기화
#         arr = list(map(list, zip(*arr))) # 행렬 전치하여 열에도 같은 작업 반복
#
#     print(f"#{t} {cnt}")

# 이진 탐색2
# T = int(input())
# for t in range(1, T+1):
#     N, D = map(int, input().split())
#     arr = list(map(int, input().split()))
#     l, r = 1, N
#     ans = 0
#
#     while l <= r:
#         m = (l + r) // 2
#         if arr[m-1] == D:
#             ans = m
#             break
#         elif arr[m-1] < D:
#             l = m + 1
#         else:
#             r = m - 1
#
#     print(f"#{t} {ans}")

# ladder1
# T = 10
# dj = [-1, 1] # 좌우
# for _ in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     r_arr = [row for row in arr[::-1]] # 배열을 상하반전시킴
#
#     # 시작 위치 설정
#     i = 0
#     for idx in range(100):
#         if r_arr[0][idx] == 2: # r_arr의 첫번째 배열에서 2가 나오는 인덱스가 시작 열의 인덱스
#             j = idx
#
#     while i < 100:
#         r_arr[i][j] = 3 # 방문했음을 3으로 표시
#         for k in range(2): # 좌우 이동
#             nj = j + dj[k] # 예상 위치
#             if (0 <= nj < 100) and (r_arr[i][nj] == 1): # 좌우로 움직일 수 있는 경우
#                 j = nj # 현재 열 위치 갱신
#                 break
#         if j != nj: # 좌우로 움직일 수 없을 경우, 아래로 이동
#             i += 1
#     print(f"#{N} {j}")

# 스도쿠 검증
def is_sdoku(arr, N):
    for _ in range(2): # 행/열 두 번 탐색
        for i in range(0, N, 1):
            counts = [0] * N # 0~9까지 카운트 저장
            for j in range(N):
                if counts[arr[i][j]-1] != 0: # 이전에 카운트된 숫자가 있다면
                    return 0 # 중복이 있는 것 -> 스도쿠X(0)
                else:
                    counts[arr[i][j]-1] = 1 # 해당 원소에 카운트 + 1
        arr = list(map(list, zip(*arr))) # 행렬 전치 > 열방향을 행으로 바꿔 탐색

    for k in range(0, N, 3):
        for i in range(k, k+3):
            for j in range(k, k+3):
                arr[i][j]
    return 1 # 모든 조건을 통과한 경우 -> 스도쿠O(1)

T = int(input())
for t in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)] # 9 X 9 스도쿠 배열
    result = is_sdoku(arr, N)
    print(f"#{t} {result}")
