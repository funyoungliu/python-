def sandwichs_info(*dosings):
    print('这个三明治需要一下配料：')
    for dosing in dosings:
        print(dosing)
sandwichs_info('面包片','沙拉')
sandwichs_info('面包片','沙拉','香肠')
sandwichs_info('面包片','沙拉','香肠','生菜')