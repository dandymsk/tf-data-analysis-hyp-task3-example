import pandas as pd
import numpy as np


chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.06
    t_stat, p_value = ttest_ind(x, y)
    if p_value <= alpha:
        return True
    else:
        return False
