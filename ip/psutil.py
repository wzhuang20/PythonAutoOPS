import psutil

mem = psutil.virtual_memory()
mem.total,mem.used

print mem

cpu = psutil.cpu_times()
print cpu