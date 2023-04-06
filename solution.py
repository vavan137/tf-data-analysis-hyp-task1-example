import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 5463739632 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p = 0.09
    cr = norm.ppf(p)
    t_sh = (x_success+y_success)/(x_cnt+y_cnt)
    result = False
    if (y_success/y_cnt - x_success/x_cnt) / np.sqrt( t_sh*(1-t_sh)/x_cnt + t_sh*(1-t_sh)/y_cnt) < cr:
      result = True
    return result # Ваш ответ, True или False
