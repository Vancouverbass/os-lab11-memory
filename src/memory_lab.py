import os
import time

size_mb = 100 
print("PID:", os.getpid(), flush=True)
print(f"Выделяю {size_mb} МиБ...", flush=True)
data = bytearray(size_mb * 1024 * 1024)

for i in range(0, len(data), 4096):
 data[i] = 1
print("Память заполнена", flush=True)
time.sleep(5)
print("Программа завершилась успешно", flush=True)