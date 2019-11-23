import os
import jinja2
import yaml
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

def get_page_list(yamlpage):
    """
    function:把yaml对象转成需要的页面对象数据：页面对象-->定位list
    yaml解析成 dict对象
    """
    page_object = {}
    for page,names in yamlpage.items():
        loc_names = []
        #获取所有的locators定位方法
        locs = names["locators"]
        #添加定位name到列表
        for loc in locs:
            loc_names.append(loc["name"])
        page_object[page] = loc_names
    return page_object

def create_pages_py(page_list):
    """
    function:用jinya2把templetpage模板生成pages.py文件
    args:传get_page_list返回的内容：
    eg:
        {"Homepage":["城市选择","首页搜索"],"Mypage":["我的","请点击登录"]}
    :return:None
    """
    print(os.path.join(basepath,"templetpage"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars = {
        "page_list":page_list
    }
    template = template_env.get_template("templetpage")
    with open(os.path.join(basepath,"pages.py"),"w",encoding="utf-8") as f:
        f.write(template.render(templateVars))

if __name__ == '__main__':
    create_pages_py()