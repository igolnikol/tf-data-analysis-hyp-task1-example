import pandas as pd
import numpy as np
import math
import scipy.stats as stats
from scipy.stats import norm


chat_id = 263819966 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    px = x_success / x_cnt
    py = y_success / y_cnt  
    p_combined = (x_success + y_success) / (x_cnt + y_cnt) 
    difference = px - py
    
    z_value = difference / math.sqrt(p_combined * (1 - p_combined) * (1/x_cnt + 1/y_cnt))
    distr = stats.norm(0, 1)
    
    p_value = (1 - distr.cdf(abs(z_value))) * 2
    
    return p_value < alpha # Ваш ответ, True или False
