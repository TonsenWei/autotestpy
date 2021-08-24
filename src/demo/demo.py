# -*- coding: utf-8 -*-
import datetime
import time

def time_analazy(time_str = ""):
    '''
    09-28 06:35:20:050863
    '''
    time_strs = time_str.split()  # 默认以空格或多个空格为分割点
    for every_str in time_strs:
        print(every_str)
    
    date_strs = time_strs[0].split("-")
    for i in date_strs:
        print("data-time: " + i)

    time_strs = time_strs[1].split(":")
    for i in time_strs:
        print("time: " + i)
    
    data_time_strs = date_strs + time_strs
    print (data_time_strs)

    for i in data_time_strs:
        print(int(i))

def time_str_to_time(time_str = ""):
    timetuple = datetime.datetime.strptime(time_str, "%m-%d %H:%M:%S:%f")
    print(timetuple)
    return timetuple

def caculate_time(time_str_start="", time_str_end=""):
    start_time = datetime.datetime.strptime(time_str_start, "%m-%d %H:%M:%S:%f")
    end_time = datetime.datetime.strptime(time_str_end, "%m-%d %H:%M:%S:%f")
    month = end_time.month - start_time.month
    day = end_time.day - start_time.day
    hour = end_time.hour - start_time.hour
    minute = end_time.minute - start_time.minute
    second = end_time.second - start_time.second
    microsecond = end_time.microsecond - start_time.microsecond
    millisecond = int(microsecond/1000);
    last_microsecond = microsecond%1000;
    print("cost time = " + str(month) + " months, " + str(day) + " days," + \
        str(hour) + " hours, " + str(minute) + " minutes, " + str(second) + " seconds, " + \
        str(millisecond) + " milliseconds, " + str(last_microsecond) + " microseconds")

def caculate_time_millisecond(time_str_start="", time_str_end=""):
    '''
    make sure start time and end time is in 24 hours
    '''
    start_time = datetime.datetime.strptime(time_str_start, "%m-%d %H:%M:%S:%f")
    end_time = datetime.datetime.strptime(time_str_end, "%m-%d %H:%M:%S:%f")
    month = end_time.month - start_time.month
    day = end_time.day - start_time.day
    hour = end_time.hour - start_time.hour
    minute = end_time.minute - start_time.minute
    second = end_time.second - start_time.second
    microsecond = end_time.microsecond - start_time.microsecond
    millisecond = int(microsecond/1000);
    last_microsecond = microsecond%1000;
    print("cost time = " + str(month) + " months, " + str(day) + " days," + \
        str(hour) + " hours, " + str(minute) + " minutes, " + str(second) + " seconds, " + \
        str(millisecond) + " milliseconds, " + str(last_microsecond) + " microseconds")
    total_millisecond = day*24*60*1000 + hour**60*1000 + second*1000 + microsecond/1000
    print("total_millisecond = " + str(total_millisecond))
    return total_millisecond

if __name__ == "__main__":
    # time_analazy("09-28 06:35:20:050863")
    # print(datetime.datetime.now())
    # #格式化输出
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    # print(datetime.datetime.today())
    # start = datetime.datetime.now()
    # while True:
    #     for i in range(10000000):
    #         pass
    #     break
    # end = datetime.datetime.now()
    # print("程序运行时间："+str((end-start).seconds)+"秒")
    caculate_time("09-28 06:35:20:050930", "09-28 06:35:20:051152")
    caculate_time_millisecond("09-28 06:35:20:050930", "09-28 06:35:20:051152")
