def alphabeta(depth, node, isMax, values, alpha, beta):
    if depth == max_depth:
        return values[node]

    if isMax:
        best = -1000
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:   
                break
        return best
    else:
        best = 1000
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:   
                break
        return best

max_depth = int(input("Enter tree depth (e.g., 3): "))

leaf_nodes = 2 ** max_depth
values = []

print("Enter values for leaf nodes:")
for i in range(leaf_nodes):
    values.append(int(input(f"Value {i}: ")))

result = alphabeta(0, 0, True, values, -1000, 1000)
print("\nOptimal value:", result)
