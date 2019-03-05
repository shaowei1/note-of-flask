# 导入info目录下的__init__文件中的create_app函数
from info import create_app, db, models
# 导入脚本管理器
from flask_script import Manager
# 导入迁移框架
from flask_migrate import Migrate, MigrateCommand

# 调用create_app来获取app
app = create_app('development')

# 实例化管理器对象
manage = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 添加迁移命令
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    # app.run()
    manage.run()
