from . import blog_blu
from flask import request, current_app, jsonify
from info.utils.response_code import RET
from info.models import Blog, Category


@blog_blu.route('/', )
def index():
    return 'yangxinyue'


@blog_blu.route('/category', methods=['POST', 'GET'])
def get_news_list():
    # 获取参数
    cid = request.args.get("cid", '1')
    page = request.args.get("page", '1')
    per_page = request.args.get("per_page", '1')
    # 检查参数,转换数据类型
    try:
        cid, page, per_page = int(cid), int(page), int(per_page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数类型错误')
    filters = []
    # 判断分类id大于1，那就是：2、3、4、5

    # 根据分类id查询数据库
    try:
        # *filters是python语法中的拆包，
        # paginate = News.query.filter(News.category_id == cid).order_by(News.create_time.desc()).paginate(page,per_page,False)

        paginate = Blog.query.filter(Category.id == cid).paginate(page, per_page, False)
        # paginate = Blog.query.all().paginate(page, per_page, False)
        # paginate = Category.query.filter(Category.id == cid).first().blog_list.all().paginate(page, per_page, False)
        print(paginate)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询新闻列表数据失败')
    # 直接获取分页后的新闻列表、总页数、当前页数
    news_list = paginate.items
    current_page = paginate.page
    total_page = paginate.pages
    # 定义列表
    news_dict_list = []
    # 遍历分页后的新闻列表
    for news in news_list:
        news_dict_list.append(news.to_dict())
    # 定义字典，转成json字符串
    data = {
        'news_dict_list': news_dict_list,
        'total_page': total_page,
        'current_page': current_page
    }

    return jsonify(errno=RET.OK, errmsg='OK', data=data)
