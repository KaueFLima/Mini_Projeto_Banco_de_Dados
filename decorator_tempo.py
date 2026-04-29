import time
import logging
from functools import wraps

logging.basicConfig(
    filename='lgpd_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def medir_tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        duracao = fim - inicio
        msg = f"Função '{func.__name__}' executada em {duracao:.6f} segundos."
        print(msg)
        logging.info(msg)
        return resultado
    return wrapper
