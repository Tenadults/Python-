import requests
import bs4
from bs4 import BeautifulSoup

url = "http://www.gaokao.com/e/20210629/60da8012c4682.shtml"    # 需要抓取的网站
r = requests.get(url, timeout=30)
# 判断页面请求状态
r.raise_for_status()
# 修改编码
r.encoding = r.apparent_encoding
print(r)
html = r.text
soup = BeautifulSoup(html) # 创建 beautifulsoup 对象

soup_table = soup.find_all(name="div", attrs={"class": "main"})
# 找到表格,表格是div 属性是mian



schools_sorted = []  # 学校排名
schools_name = []    # 学校名字
schools_xingji = []  # 学校星级
schools_leixing = [] # 学校类型
schools_zongshu = [] # 学校总数
ulist = []

for itag in soup_table:

    if isinstance(itag,bs4.element.Tag):
        p = itag('p')

        print(str(p[0]).split("</strong>")[0].split("<strong>")[1])
        # str字符串，分隔</strong>并输出前面的字符，分隔<strong>并输出后面的字符

        trs = itag('tr') # 找到tr开头的字符串
        print(len(trs))  # 输出表格的长度

        for tr in trs[1:]:  # 从trs的第二个开始遍例
            tds = tr('td')  # 找到td开头的字符串

            schools_sorted.append(str(tds[0]).split("</td>")[0].split(";\">")[1].strip())
            # 连续分隔找到列表排名编号

            schools_name.append(str(tds[1]).split("</span>")[0].split("153);\">")[1])
            # 连续分隔找到学校名字

            schools_xingji.append(str(tds[2]).split("</td>")[0].split("49);\">")[1].strip())
            # 连续分隔找到学校星级

            schools_leixing.append(str(tds[3]).split("</td>")[0].split("49);\">")[1].strip())
            # 连续分隔找到学校类型

            schools_zongshu.append(str(tds[4]).split("</td>")[0].split("49);\">")[1].strip())
            # 连续分隔找到学校总数

        for i in range(0,len(schools_name)):
            ulist.append([schools_sorted[i],schools_name[i],schools_xingji[i]])
            # 把学校排名，学校名字，学校等级都加到ulist列表里面

        # 格式化输出一个表头
        print("{:10}\t{:<24}\t{:<20}\t{:<10}\t{:<10}\t".format("排名","学校名字","等级","类型","高校数量"))

        for i in range(0,len(ulist)):
            u = ulist[i]
            print("{:10}\t{:<24}\t{:<20}\t{:<10}\t{:<10}\t".format(u[0],u[1],u[2], "理工", "603"))
            # 对处理后的数据进行格式化的输出
try:

        fo = open(r"D:\笔记保存\职业学院排名.txt","a")   # 输入正确的地址

        for list12 in ulist:
            fo.write(list12[0]+ ' '*(10-len(list12[0])))
            fo.write(list12[1] + ' ' * (30 - len(list12[1])))
            fo.write(list12[2] + ' ' * (10 - len(list12[2])))

            fo.write("\n")    # 当一行的数据打印完成以后进行换行

        fo.close()

    except Exception as e:
        print("Write an exception！", e)  # 当上面输出错误的时候，打印