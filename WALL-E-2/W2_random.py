# W2_Game Random program.
import random

def W2_random():
    #抽卡模块
    a = random.randint(0, 1)
    print('a', a+1, alist[a]);
    b = random.randint(0, 1);
    if (b == 1):
        print('b', b+1, blist);
    c = random.randint(-1, 4);
    if (c > -1):
        print('c', c+1, clist[c]);
    d1 = random.randint(0, 19);
    print('d', d1+1, dlist[d1]);
    d2 = random.randint(0, 19);
    if d1 == d2:
        d3 = random.randint(0, 19);
        print('d', d3+1, dlist[d3]);
    elif d1 != d2:
        print('d', d2+1, dlist[d2]);
    print(rerool());
    return;

def rerool():
    #重新抽卡模块
    ex = input(':')
    if ex == 'exit':
        exit(0)
    elif ex == 'rerool':
        print(W2_random())
    elif ex == 'help':
        print('输入exit退出\n输入rerool重新选择卡牌')
        print(rerool())
    else:
        ex = input('输入exit退出\n输入rerool重新选择卡牌\n:')
        if ex == 'rerool':
            print(W2_random());
        elif ex == 'exit':
            exit(0)
        else:
            print('请重新输入\n:')
            print(rerool())

def start():
    if input('请输入start开始抽牌:') == 'start':
        print('输入exit退出\n输入rerool重新选择卡牌\n输入help重新显示此提示\n')
        print(W2_random());
    else:
        print(start());

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



print(start())

