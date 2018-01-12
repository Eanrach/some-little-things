# W2_Game Random program.
import random #导入随机模块

def W2_random():
    #抽卡模块
    a = random.randint(0, 1)#抽取a卡片
    print('a', a+1, alist[a]);#输出a卡片内容
    b = random.randint(0, 1);#抽取b卡片
    if (b == 1):
        #如果抽到b卡片则输出b卡片内容
        print('b', b+1, blist);
    c = random.randint(-1, 4);#抽取c卡片
    if (c > -1):
        #如果抽到c卡片则输出卡片内容
        print('c', c+1, clist[c]);
    d1 = random.randint(0, 19);#抽取d卡片
    print('d', d1+1, dlist[d1]);#输出d卡片内容
    d2 = random.randint(0, 19);
    if d1 == d2:
    #由于要抽取两张d卡片,分散d卡片的内容
        d3 = random.randint(0, 19);
        print('d', d3+1, dlist[d3]);
    elif d1 != d2:
        print('d', d2+1, dlist[d2]);
    rerool()

def rerool():
    #重新抽卡模块
    ex = input(':')
    if ex == 'exit':
        #如果输入值为exit则退回到start()层
        start()
    elif ex == 'rerool':
        #如果输入值为rerool则使用W2_random()重新抽卡
        W2_random()
    elif ex == 'help':
        #输入值为help的情况下则显示帮助
        print('输入exit退出\n输入rerool重新选择卡牌')
        rerool()
    else:
        #输入其他值时运行上述内容
        ex = input(':')
        if ex == 'rerool':
            W2_random()
        elif ex == 'exit':
            start()
        elif ex == 'help':
            print('输入exit退出\n输入rerool重新选择卡牌')
            rerool()
        else:
            #如无输入则返回rerool()方法继续等待指令
            rerool()

si = 0 #全局变量,start()启动次数
def start():
    #开始模块,调用其它函数的循环
    global si
    while si == 0:
        #判断start()启动次数
        st=input('请输入start开始抽牌\n或者exit退出\n#')
        while  st== 'start':
            print('输入exit退出\n输入rerool重新选择卡牌\n输入help重新显示此提示\n')
            si = si + 1
            W2_random()
        if st=='exit':
            exit()
        print(start())
    st = input('#')
    while st == 'start':
        W2_random()
    if st == 'exit':
        exit()
    elif st == 'help':
        print('请输入start开始抽牌\n或者exit退出')
    start()


alist = ['有助于', '有害于'];
blist = '重于';
clist = [
    '公平', '正义', '自由',
    '效率', '人性尊严'];
dlist = [
    '查资料', '科研补习',
    '政论节目', '作弊',
    '弃赛', '山寨机文化',
    '写一辩稿', '堕胎',
    '说谎', '性别刻板印象',
    '垃圾食品', '全球暖化',
    '谈恋爱', '熬夜',
    '一夜情', '打练习赛',
    '失业', '灌论点',
    '酒后驾驶', '人口老化'];



if __name__=='__main__':
    start()

