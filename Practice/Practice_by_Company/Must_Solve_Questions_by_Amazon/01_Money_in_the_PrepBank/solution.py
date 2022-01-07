def solve(N):
    a_week = 28
    incr_for_week = 7
    numb_of_full_weeks = (N - (N % 7)) // 7
    full_weeks = a_week * numb_of_full_weeks
    numb_of_rest_days = N - numb_of_full_weeks * 7
    base_rest_of_days = sum(range(0, numb_of_rest_days + 1))
    incr_full_weeks = sum(range(0, numb_of_full_weeks)) * 7
    incr_base_of_days = numb_of_rest_days * numb_of_full_weeks
    result = full_weeks + incr_full_weeks + base_rest_of_days + incr_base_of_days
    # print("N =", N)
    # print("Numb of full weeks =", numb_of_full_weeks)
    # print("Full weeks =", full_weeks)
    # print("Numb of rest days =", numb_of_rest_days)
    # print("Base rest of days =", base_rest_of_days)
    # print("Incr full weeks =", incr_full_weeks)
    # print("Incr base of days =", incr_base_of_days)
    # print("Result = ", result)
    print(result)

def main():
    T = int(input())
    # T = 1
    for i in range(T):
        N = int(input())
        # N = 10
        solve(N)

main()
