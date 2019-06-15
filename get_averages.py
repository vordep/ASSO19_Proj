import csv


def get_averages(csv):
    cpu = 0.0
    ram = 0.0
    counter = 0
    try:
        file = open(csv, 'r')
    except:
        print('não existe')
        return
    lines = file.readlines()
    for line in lines:
        if not line.count(',')==3:
            continue
        temparray = line.split(',')
        counter += 1
        cpu += float(temparray[2])
        ram += float(temparray[3])

    try:
        finalCPU = cpu/counter
        finalRAM = ram/counter
        strCPU = str(finalCPU)
        strRAM = str(finalRAM)
        strCPU=strCPU.replace('.', ',',1)
        strRAM=strRAM.replace('.', ',',1)
        print(strRAM + "" + strCPU)
    except:
        print('estourei')
        # rows_of_numbers = [map(float, line.split(',')) for line in lines]
        # sums = map(sum, zip(*rows_of_numbers))
        # averages = [sum_item / len(lines) for sum_item in sums]
        # return averages


path = "C:/Users/Rtorres/Documents/ASSO/ASSO19_Proj"
client_server = 'Server'
protocol = 'MQTTPublisher'
machine = '30%cap'

fileSize = 1024
numberMessages = 2048
csv = "".join([path, "/", client_server, "/", machine, "/",
               protocol, "-", str(fileSize), "-", str(numberMessages), ".csv"])
get_averages(csv)
