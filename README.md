# django-basis
基本的django后端框架
## 进行mysql数据库和django框架的连接
1. django-admin startproject basis
2. python manage.py migrate
3. 修改settings.py中的数据库信息
4. 为了导入模型我们需要创建一个app，此处为
    django-admin startapp basisModel
5. 接下来在 settings.py 中找到INSTALLED_APPS这一项，并加入一项'basisModel'表示新建的app
6. python manage.py inspectdb > basisModel/models.py 用来导入连接数据库中的结构(注：不需要进行数据库迁移，因为迁移的本质是根据你定义的模型类生成相应的数据库表结构，并将其映射到数据库中，可以理解为inspectdb是migrate的逆映射)（此处编码可能会有一点问题，可以直接在终端输出后再复制进models.py中）
7. 接下来尝试对数据库进行操作，具体代码可以看testdb.py中的文件(注：为了让该代码在服务器上执行，需要在urls.py添加相应的调用path),简易教程看这个<a href="https://www.runoob.com/django/django-model.html">mysql in py</a>
想做的更复杂看[CarSystem](https://github.com/cwyLeo/CarSystem)中的testdb.py
## 前端网页的设计
1. 在项目目录下创建templates文件夹用来放置html文件；
2. 接下来我们需要向Django说明模板文件的路径,修改settings.py中的模板类DIR为:[os.path.join(BASE_DIR, 'templates')],这时候我们就可以在该项目的任意地方(严谨调用文件的话，一般需要在特定的视图渲染文件中render读取需要的文件，以符合MVC的思想)读取模板文件了;
3. 在设计html文件代码时,基本的html操作不做赘述，django主要实现了可以使用“{{ variable }}”来调用变量的值，“{% code %}”可以在html实现简单的编程，其中对于if-else需要在基础上添加{% endif %},for类似，其中变量通过视图文件中的render函数传递字典参数实现，具体情况请看pagelinks.py文件(命名有点垃圾，要多向chatgpt学习捏···);
4. 和第一个模块类似，在urls.py中添加相应的调用path，第二个参数为调用渲染网页的函数;
5. 配置静态文件，我们在根目录下创建static文件夹，并在settings.py中添加STATICFILES_DIRS = [ 
    os.path.join(BASE_DIR, "static"), 
]
6. 注意引入路径的使用settings.py中定义的文件别名，在模板中使用静态文件需要添加```{% load static %}```,引入图片方式为```src="{% static 'images/*.png' %}"```
一些提高效率的小彩蛋：模板继承，即网页中会有一些组件结构需要在其他网页得到复用，如nav,footer等
父模板定义如下：
```
{% block 名称 %} 
预留给子模板的区域，可以设置设置默认内容
{% endblock 名称 %}
```
子模板定义如下：
```
{% extends "父模板路径"%} 
{ % block 名称 % }
内容 
{% endblock 名称 %}
```