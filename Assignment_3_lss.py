if __name__ == '__main__':
	A = list(map(int,input("Enter First Array separated by space ").strip().split()))
	B = list(map(int,input("Enter Second Array separated by space ").strip().split()))
	n = len(A)
	m = len(B)
	dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
	for i in range(n - 1, -1, -1):
		for j in range(m - 1, -1, -1):
			if A[i] == B[j]:
				dp[j][i] = dp[j + 1][i + 1] + 1
	max_m = 0
	max_e = 0
	idx = 0
	for i in dp:
		for j in i:
			max_m = max(max_m, j)
			if max_m > max_e:
				idx = j-1
				max_e = max_m
	ans = [] 
	while max_m > 0:
		ans.append(B[idx])
		idx = idx+1
		max_m = max_m-1
	print(ans)