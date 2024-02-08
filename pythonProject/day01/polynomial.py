def print_poly(t_x, f_x) -> str:
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        term = t_x[i]
        coefficient = f_x[i]
        if coefficient >= 0 and i!=0 :
            poly_expression += "+"
        poly_expression += f"{coefficient}x^{term} "

    return poly_expression
def calculation_poly(x_value, t_x, f_x) -> int:
    return_value = 0

    for i in range(len(fx)):
        term = t_x[i]
        coefficient = f_x[i]
        return_value += coefficient * pow(x_value, term)
        term -= 1
    return return_value

tx = [10, 2, 0]
fx = [7, 3, 4]

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(print_poly(tx,fx))
    print(calculation_poly(int(input("input x : ")), tx, fx))


