def incremente(x):
    return x + 1

def higher_order_func(x, func):
    return x + func(x)

result = higher_order_func(5, incremente)
print("func: ", result)

# higher_order_func mediantes lambdas
incremente_v1 = lambda x: x + 1

higher_order_func_Ve = lambda x, func: x + func(x)

result_lambda = higher_order_func_Ve(4, incremente_v1)

result_lambda1 = higher_order_func_Ve(4, lambda x: x * 2)
result_lambda2 = higher_order_func_Ve(4, lambda x: x - 2)
print(result_lambda1)
print(result_lambda2)