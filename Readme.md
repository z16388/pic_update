这是一个上传图片到github的工具，目前还不是很成熟，不过已经可以实现压缩并上传图片的目的了，对于写博客来说已经够用了。

使用步骤如下：

1. 创建todo目录
2. 创建pic目录，在github上创建一个空项目，然后pull到这里
3. 修改main.py中的代码，将git_url修改为上一步新建的项目
4. 将图片放到todo文件夹下
5. 执行脚本

经过配置之后，以后只需要将图片放到todo目录下，执行脚本即可。

pip install pyyaml
pip install gitpython
pip install pillow
