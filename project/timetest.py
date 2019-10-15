import calendar
import datetime

class MyDate:
    def __init__(self):
        now_time = datetime.datetime.now()#获取现在的时间
        year = now_time.year#获取现在的年
        month = now_time.month#获取现在的月
        # 初始化
        self.result = []
        # 当月总天数/本月最后一天
        total_day = calendar.monthrange(year, month)[1]
        # 当月第一天
        first_day = datetime.datetime(year, month, 1)
        # 获取第一天和最后一天是周几，0-6  0代表周一  6代表周日
        first_week = first_day.weekday()
        last_week = datetime.date(year, month, total_day).weekday()
        all_day = [x for x in range(1, total_day + 1)]#将本月的天数都打印出来
        # 前面补充empty，将第一周前边没有的星期用empty代替，例如【empty,1,2,3,4,5,6】
        lines = []
        for i in range(first_week):
            lines.append("empty")
        for j in range(7 - first_week):
            lines.append(all_day.pop(0))
        self.result.append(lines)
        # 后面补充empty，将最后周后边没有的星期用empty代替，例如【29,30,31，empty，empty，empty，empty】
        while all_day:
            line = []
            for i in range(7):
                if len(line) < 7 and all_day:
                    line.append(all_day.pop(0))
                else:
                    line.append("empty")
            self.result.append(line)

    def get_date(self):
        # 返回结果
        return self.result

    def print_date(self):
        # 将结果打印出来
        print(self.result)


if __name__ == '__main__':
    obj = MyDate()
    b = obj.get_date()
    print('一\t二\t三\t四\t五\t六\t日')
    for i in b:
        for j in i:
            if j == 'empty':
                print(' ',end='\t')
            else:
                print(j,end='\t')
        print()
