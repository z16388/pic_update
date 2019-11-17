import os
import time
import yaml
from PIL import Image
from git import Repo

f = open('./config.yml', encoding='utf-8')
config = yaml.load(f)

pic_dir = config['pic_dir']
todo_dir = config['todo_dir']
md_dir = config['md_dir']
git_url = config['git_url']
max_width = config['max_width']

new_list = []

def save_pic(img, to_file):
    if to_file.lower().endswith("png") == False:
        img = img.convert('RGB')
    try:
        img.save(to_file)
    except:
        img = img.convert('RGB')
        img.save(to_file)

def scale_pic(a_file, to_file):
    img = Image.open(a_file)
    w, h = img.size
    new_width = w
    new_height = h
    if w > max_width:
        new_width = max_width
        new_height = int(h * max_width / w)

    out = img.resize((new_width, new_height), Image.ANTIALIAS)
    save_pic(out, to_file)

def deal_pic(file_name):
    ts = str(int(time.time() * 10000))
    to_file = ts + ".png"
    to_dir = pic_dir + to_file
    scale_pic(file_name, to_dir)
    new_list.append(to_file)
    os.remove(file_name)

def enter_mian():
    # 保证目录和文件的存在
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)
    if not os.path.exists(todo_dir):
        os.makedirs(todo_dir)
    if not os.path.exists(todo_dir):
        os.makedirs(todo_dir)
    if not os.path.exists(md_dir):
        pic_log = open(md_dir, mode="w", encoding="utf-8")
        pic_log.close()

    # 开始处理
    pics = os.listdir(todo_dir)
    for picname in pics:
        deal_pic(todo_dir + picname)
    
    f = open(md_dir, 'w')
    for file_name in new_list:
        f.write("!["+file_name.replace(".png","")+"]("+ git_url + "blob/master/" +file_name +"?raw=true)\n")
    f.close()

    # 处理上传
    Repo.init(pic_dir)
    git = Repo(pic_dir)
    add_pics = os.listdir(pic_dir)
    for picname in add_pics:
        if picname == ".git":
            continue
        git.index.add(picname)
        
    git.index.commit("update pic to git")
    git.remote().push()

    # 打开最近上传记录表
    os.system("start " + md_dir)

enter_mian()