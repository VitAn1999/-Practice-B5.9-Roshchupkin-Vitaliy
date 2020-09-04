# импротируем библиотеку time
import time

class Stopwatch:
"""Класс секундомер. В качестве аргумента принимает количество
проверок и оборачивает функцию, после чего возвращает
время выполнения оборачиваемой функции"""
    def __init__(self, num_runs=10):
        self.num_runs = num_runs
        
    # функция-декоратор
    def __call__(self, func):
        def wrap():
            avg_time = 0
            for i in range(self.num_runs):
                start = time.time()
                func()
                end = time.time()
                avg_time += (end - start)
            avg_time /= self.num_runs
            print(f'Выполнение заняло {avg_time} секунд')
        return wrap
    
    # контекстный менеджер 
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        avg_time = (self.end - self.start)
        print(f'Выполнение заняло {avg_time} секунд')
    

@Stopwatch(10)
def new_func():
    for j in range(1000000):
        pass

with Stopwatch() as sw:
    new_func()
