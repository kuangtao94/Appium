import yaml
import os

# 获取当前脚本所在文件夹路径
basepath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件加
yamlPagesPath = os.path.join(basepath, "pageelement")

def paseryaml():

    pageElements = {}
    #遍历读取 yaml 文件
    """
    第一个参数fpath是遍历打印所有的文件路径
    第二个参数dirname是遍历打印所有的文件夹名称
    第三个参数fnames是遍历打印所有的文件名
    """
    for fpath,dirname,fnames in os.walk(yamlPagesPath):
        for name in fnames:
            print(name)
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath,name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path,"r",encoding="utf-8") as f:
                    # 用load方法转字典 --把文件的内容读取出来
                    page = yaml.load(f,Loader=yaml.FullLoader)
                    pageElements.update(page)
    return pageElements



if __name__ == '__main__':
    a = paseryaml()
    print(a)
    for i in a["Loginpage"]["locators"]:
        print(i)