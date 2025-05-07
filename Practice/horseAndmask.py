def horse(mask):
    horse = mask # f1中horse代表拉姆大函数
    def mask(horse): # f1中的mask变成了一个新的函数
        return horse
    return horse(mask)

mask = lambda horse : horse(2) # 主框架中mask 代表一个拉姆达函数
horse(mask)
