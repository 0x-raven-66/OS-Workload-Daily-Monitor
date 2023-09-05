import psutil
from datetime import datetime
import time
from mail_sender import sendEmail

def writeDateTime():
    now = datetime.now().time().strftime("%H:%M:%S")
    date = datetime.now().strftime("%Y-%m-%d")
    text = f"date:{date}\ntime:{now}\n"
    with open('log_file.txt', 'w') as f:
        f.write(text)

def writeDisksUsage():
    partitions = psutil.disk_partitions()
    partitions_usage,partitions_names,total,used,free,percent = [],[],[],[],[],[]

    for i in range(0, len(partitions)):
        partitions_names.append(partitions[i][0])
        partitions_usage.append(psutil.disk_usage(partitions[i][0]))
        # devided on 1073741824 to convert from byte to gigabyte
        total.append(round(partitions_usage[i][0]/1073741824,2))
        used.append(round(partitions_usage[i][1]/1073741824,2))
        free.append(round(partitions_usage[i][2]/1073741824,2))
        percent.append(partitions_usage[i][3])

    for i in range(0,len(partitions_names)):
        text = f"partition '{partitions_names[i]}': Total={total[i]} GB, Used={used[i]} GB, Free={free[i]} GB, Percantage={percent[i]}%\n"
        with open('log_file.txt', 'a') as f:
            f.write(text)

def writeRamUsage():
    ram = psutil.virtual_memory()
    total = round(ram[0]/1073741824, 2)
    used = round(ram[3]/1073741824, 2)
    free = round(ram[4]/1073741824, 2)
    percent = ram[2]
    text = f"RAM : Total={total} GB, Used={used} GB, Free={free} GB, Percantage={percent}%\n"
    with open('log_file.txt', 'a') as f:
        f.write(text)

def writeNetworkUsage():
    # devided on 1048576 to convert byts to megabytes
    recv = round(psutil.net_io_counters()[1]/1048576,2)
    send = round(psutil.net_io_counters()[0]/1048576,2)
    text = f"Network Usage: Send={send} MB, Recive={recv} MB\n"
    with open('log_file.txt', 'a') as f:
        f.write(text)

def writeCpuUsage():
    text = f"CPU Usage:{psutil.cpu_percent(1)}%\n"
    with open('log_file.txt', 'a') as f:
        f.write(text)

if __name__ == '__main__':
    while True:
        writeDateTime()
        writeCpuUsage()
        writeRamUsage()
        writeDisksUsage()
        writeNetworkUsage()
        sendEmail()
        # wiat for 12 hours to repeat
        time.sleep(12*3600)
