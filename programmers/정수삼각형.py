def solution(triangle):
    fore = triangle[0]
    for i in range(1, len(triangle)):
        curr = triangle[i]

        max_sum = []
        for j in range(len(curr)):
            if not j:
                sum = fore[j] + curr[j]
                max_sum.append(sum)
            elif j == len(curr) - 1:
                sum = fore[j - 1] + curr[j]
                max_sum.append(sum)
            else:
                sum = max(
                    fore[j - 1] + curr[j],
                    fore[j] + curr[j]
                )
                max_sum.append(sum)
        fore = max_sum
    answer=max(fore)
    return answer
