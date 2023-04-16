# django-basis
基本的django后端框架
1. django-admin startproject basis
2. python manage.py migrate
3. 修改settings.py中的数据库信息
4. 为了导入模型我们需要创建一个app，此处为
    django-admin startapp basisModel
5. 接下来在 settings.py 中找到INSTALLED_APPS这一项，并加入一项'basisModel'表示新建的app
6. python manage.py inspectdb > basisModel/models.py 用来导入连接数据库中的结构(注：不需要进行数据库迁移，因为迁移的本质是根据你定义的模型类生成相应的数据库表结构，并将其映射到数据库中，可以理解为inspectdb是migrate的逆映射)（此处编码可能会有一点问题，可以直接在终端输出后再复制进models.py中）
7. 接下来尝试对数据库进行操作，具体代码可以看testdb.py中的文件(注：为了让该代码在服务器上执行，需要在urls.py添加相应的调用path),简易教程看这个<a href="https://www.runoob.com/django/django-model.html">mysql in py</a>
想做的更复杂看CarSystem中的testdb.py
