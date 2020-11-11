from csv_converter import csv_s

def Runge_Kutta(answer, func, x0, y0, h):
    """
    Runge-Kutta method

    :param answer: analytical y
    :param func: f'(x,y)
    :param x0: float
    :param y0: float
    :param h: float
    :return: max_error = abs(y_ans - y_i)
    
    """
    outputs = [['i', 'x_i', 'y*_i', 'y_i', '|y*_i-y_i|']]
    steps = int(1 // h + 2)
    x_i, y_i = x0, y0
    y_ans = y0
    max_error = 0

    for i in range(steps):
        k1 = func(x_i, y_i)
        k2 = func(x_i + h * 0.5, y_i + h * k1 * 0.5)
        k3 = func(x_i + h * 0.5, y_i + h * k2 * 0.5)
        k4 = func(x_i + h, y_i + h * k3)
        y_next = y_i + h * (k1 + 2 * (k2 + k3) + k4) / 6

        outputs.append([i, x_i, y_ans, y_i, abs(y_ans-y_i)])

        if max_error <= abs(y_ans - y_i):
            max_error = abs(y_ans - y_i)
        
        y_i = y_next
        x_i += h
        x_i = float('{:.3f}'.format(x_i))
        y_ans = answer(x_i)

    csv_s(outputs, f'Runge_Kutta_method h={h}.csv')
    return max_error