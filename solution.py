from scipy.stats import mannwhitneyu
import pandas as pd
import numpy as np

chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.06
    stat, p = mannwhitneyu(x, y, alternative='two-sided')
    if p <= alpha:
        return True
    else:
        return False
