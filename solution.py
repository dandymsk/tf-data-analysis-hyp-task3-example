import pandas as pd
import numpy as np
from scipy.stats import permutation_test

chat_id = 841977 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.06
    obs_diff = abs(np.mean(x) - np.mean(y))
    # Проведение перестановочного теста
    n_permutations = 1000
    perm_diffs = []
    for i in range(n_permutations):
        combined = np.concatenate([x, y])
        perm = np.random.permutation(combined)
        perm_x = perm[:len(x)]
        perm_y = perm[len(x):]
        perm_diff = np.mean(perm_x) - np.mean(perm_y)
        perm_diffs.append(perm_diff)

# Вычисление p-value
    p_value = np.sum(np.abs(perm_diffs) >= np.abs(obs_diff)) / n_permutations

# Вывод результата
        
    if p_value <= alpha:
        return True
    else:
        return False
