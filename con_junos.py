import time
import sys
from netmiko import ConnectHandler

'''读取当前VSRX防火墙contorlplane CPU的IDLE值,**kwarges意思为传入字典1个以上的值'''


def ContorlPlaneIdleCpu(**kwargs):
    connect = ConnectHandler(**kwargs)
    ContorlPlaneCpuUsage = connect.send_command('show chassis routing-engine')
    ListContorlplaneCpuUsage = ContorlPlaneCpuUsage.split()
    IdleCpu = ListContorlplaneCpuUsage[53]
    return IdleCpu

'''每隔X秒钟执行一次设备检查'''


def CheckCpuUsage():
    UsageCpu = cpu
    if UsageCpu >= 90:
        AlarmTextRed = '红色告警，当前设备CPU使用率已经超过90%，当前值为：{}'.format(UsageCpu) + '%'
        return AlarmTextRed
    if 90 < UsageCpu <= 50:
        AlarmTextYellow = '黄色告警，当前设备CPU使用率已经超过50%，当前值为：{}'.format(UsageCpu) + '%'
        return AlarmTextYellow
    if 50 < UsageCpu <= 30:
        AlarmTextOrange = '橙色告警，当前设备CPU使用率已经超过30%，当前值为：{}'.format(UsageCpu) + '%'
        return AlarmTextOrange
    if 30 < UsageCpu <= 10:
        AlarmTextBlue = '蓝色告警，当前设备CPU使用率已经超过10%，当前值为：{}'.format(UsageCpu) + '%'
        return AlarmTextBlue
    if UsageCpu < 10:
        AlarmTextNormal = '正常告警，当前设备CPU使用率小于10%，当前值为：{}'.format(UsageCpu) + '%'
        return AlarmTextNormal
vsrx = {
    'device_type': 'juniper_junos',
    'ip': '172.16.100.1',
    'username': 'test',
    'password': 'test123'
}
cpu = 100 - int(ContorlPlaneIdleCpu(**vsrx))
if __name__ == '__main__':
    while True:
        if cpu >= 90:
            print(CheckCpuUsage())
            time.sleep(5)
            continue
        if 90 < cpu <= 50:
            print(CheckCpuUsage())
            time.sleep(30)
            continue
        if 50 < cpu <= 30:
            print(CheckCpuUsage())
            time.sleep(60)
            continue
        if 30 < cpu <= 10:
            print(CheckCpuUsage())
            time.sleep(300)
            continue
        if cpu < 10:
            print(CheckCpuUsage())
            time.sleep(1)
            continue
        else:
            pass
