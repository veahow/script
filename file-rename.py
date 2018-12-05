import os

path = r'C:\Users\veahow\Desktop\第13章-vue1.0升级到vue2.0'    # 当前目录的绝对路径
suffix = ".baiduyun.p.downloading"    # 需要修改的文件名特定后缀

if __name__ == '__main__':
    ps = os.listdir(path)    # 列出当前目录所有文件和文件夹
    for p in ps:
        if os.path.isdir(p):    # 判断是否是文件夹
            # 如果是文件夹
            if not os.listdir(p):    # 判断文件夹是否为空
                os.rmdir(p)    # 文件夹为空则删除该文件夹
                print('\"' + p + '\"' + " - 该空文件夹已被删除")
        else:
            # 如果是文件
            if p.endswith(suffix):    # 判断文件名是否以suffix后缀名结尾
                '''
                os.remove(p)   # 以suffix后缀结尾则删除该文件
                print('\"' + p + '\"' + " - 该文件已被删除")
                '''
                # 以suffix后缀结尾则修改文件名
                new_name = p.replace(suffix, '')
                os.rename(p, new_name)
                print('\"' + p + '\"' + " - 该文件的文件名修改为 - " + new_name)
    print("程序运行结束")
        
