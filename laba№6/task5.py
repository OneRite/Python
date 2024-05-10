import numpy as np

def log_density_multivariate_normal(X, m, C):
    D = len(m)
    # Нормализация данных
    X_norm = X - m
    # Нахождение определителя матрицы ковариаций
    det_cov = np.linalg.det(C)
    # Нахождение обратной матрицы ковариаций
    inv_cov = np.linalg.inv(C)
    # Вычисление квадратичной формы
    quadratic_form = np.sum(np.dot(X_norm, inv_cov) * X_norm, axis=1)
    # Вычисление логарифма плотности вероятности
    log_density = -0.5 * (quadratic_form + np.log(det_cov) + D * np.log(2 * np.pi))
    return log_density

# Пример использования функции
X = np.array([[1, 2], [3, 4], [5, 6]])
m = np.array([0, 0])
C = np.array([[1, 0.5], [0.5, 1]])
log_density = log_density_multivariate_normal(X, m, C)
print("Логарифм плотности многомерного нормального распределения:", log_density)
