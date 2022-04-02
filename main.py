import sound
import time
def nowtime():
    now = time.localtime()
    print(now.tm_year,"/",now.tm_mon,"/",now.tm_mday,"_",now.tm_wday,
          "\t",now.tm_hour,":",now.tm_min,":",now.tm_sec)
# 메인함수
if __name__ == '__main__':
    working_time = int(input("working time?"))
    break_time = int(input("break time?"))
    go3 = sound.sound.go3()
    time.sleep(working_time)
    jf = sound.sound.jf()
    time.sleep(break_time)
    print("end")
    nowtime()
    time.sleep(1)
    nowtime()
    #뽀모도로 작동시간 설정