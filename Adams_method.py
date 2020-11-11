from csv_converter import csv_e, csv_s

def Adams(answer, func, x0, h):
    """
    Adams method 

    :param answer: analytical y
    :param func: f'(x,y)
    :param x0: float
    :param h: float
    :return: max_error = abs(y_ans - y_i)
    """

    x_0, x_1, x_2, x_3 = x0, x0 + h, x0 + 2 * h, x0 + 3 * h
    x_1 = float('{:.3f}'.format(x_1))
    x_2 = float('{:.3f}'.format(x_2))
    x_3 = float('{:.3f}'.format(x_3))
    steps = int(1 // h + 2)

    y_0, y_1, y_2, y_3 = csv_e(f"Runge_Kutta_method h={h}.csv") 
    y0, y1, y2, y3 = answer(x_0), answer(x_1), answer(x_2), answer(x_3)
    max_error = max(abs(y0 - y_0), abs(y1 - y_1), abs(y2 - y_2), abs(y3 - y_3))
    
    outputs = [['i', 'x_i', 'y*_i', 'y_i', '|y*_i-y_i|'],
               [0, x_0, y0, y_0, abs(y0-y_0)],
               [1, x_1, y1, y_1, abs(y1-y_1)],
               [2, x_2, y2, y_2, abs(y2-y_2)],
               [3, x_3, y3, y_3, abs(y3-y_3)]]
    
    for i in range(4, steps):
        y = y_3 + h * (55 * func(x_3, y_3) - 59 * func(x_2, y_2) + 37 * func(x_1, y_1) - 9 * func(x_0, y_0)) / 24

        x_0, x_1, x_2 = x_1, x_2, x_3
        x_3 += h
        x_3 = float('{:.3f}'.format(x_3))
        y_ans = answer(x_3)

        y_0, y_1, y_2 = y_1, y_2, y_3
        y_3 = y

        outputs.append([i, x_3, y_ans, y, abs(y_ans - y)])
        if max_error <= abs(y_ans - y):
            max_error = abs(y_ans - y)
        
    csv_s(outputs, f'Adams_method h={h}.csv')
    return max_error