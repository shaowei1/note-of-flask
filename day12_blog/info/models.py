from info import db


class Category(db.Model):
    """新闻分类"""
    __tablename__ = "categorys"

    id = db.Column(db.Integer, primary_key=True)  # 分类编号
    name = db.Column(db.String(64), nullable=False)  # 分类名
    blog_category = db.relationship('Blog', backref='category', lazy='dynamic')

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "name": self.name
        }
        return resp_dict


class Blog(db.Model):
    """新闻"""
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categorys.id"))

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category_id,
        }
        return resp_dict
