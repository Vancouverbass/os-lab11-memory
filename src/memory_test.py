import os
import time
import gc

print("PID:", os.getpid(), flush=True)
data = []
for i in range(5):
 block = bytearray(10 * 1024 * 1024)
 for j in range(0, len(block), 4096):
        block[j] = 1
 data.append(block)
 print(f"Выделено {(i + 1) * 10} МиБ", flush=True)
 time.sleep(5)
print("Ожидание 20 секунд...", flush=True)
time.sleep(20)
print("Освобождение памяти...", flush=True)
data.clear()
gc.collect()
print("После очистки:", flush=True)
time.sleep(20)