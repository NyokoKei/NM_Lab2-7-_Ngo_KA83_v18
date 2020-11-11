from Adams_method import Adams
from Runge_Kutta_method import Runge_Kutta

def answer(x):
    """
    Solution of the Cauchy problem at point x
    
    :param x: float
    :return: y
    """
    return x ** 2
    

def func(x, y):
    """
    1st order differential equation
    :param x: float
    :param y: float
    :return: f'(x, y)
    """
    return 1 - (1 - 2 * x) * y / x ** 2


if __name__ == "__main__":
    H = [0.1, 0.05, 0.025]

    for h in H:
        RK = Runge_Kutta(answer, func, 1, 1, h)
        A = Adams(answer, func, 1, h)
        
        print('Max error for h =', h, ':\n\tRunge_Kutta: ', RK, '\n\tAdams: ', A)
    
