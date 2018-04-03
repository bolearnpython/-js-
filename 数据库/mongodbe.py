from mongoengine import *
connect('mydb')
# connect('project1', host='192.168.1.35', port=12345)
# connect('project1', username='webapp', password='pwd123')
# connect('project1', host='mongodb://localhost/database_name')
class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    posted = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    meta = {'allow_inheritance': True}

class TextPost(BlogPost):
    content = StringField(required=True)

class LinkPost(BlogPost):
    url = StringField(required=True)

# Create a text-based post
post1 = TextPost(title='Using MongoEngine', content='See the tutorial')
post1.tags = ['mongodb', 'mongoengine']
post1.save()

# Create a link-based post
post2 = LinkPost(title='MongoEngine Docs', url='hmarr.com/mongoengine')
post2.tags = ['mongoengine', 'documentation']
post2.save()

# Iterate over all posts using the BlogPost superclass
for post in BlogPost.objects:
    print ('===', post.title, '===')
    if isinstance(post, TextPost):
        print (post.content)
    elif isinstance(post, LinkPost):
        print ('Link:', post.url)


# Count all blog posts and its subtypes
BlogPost.objects.count()

TextPost.objects.count()

LinkPost.objects.count()


# Count tagged posts
BlogPost.objects(tags='mongoengine').count()

BlogPost.objects(tags='mongodb').count()





# 返回集合里的所有文档对象的列表
cate = Categories.objects.all()
# 返回所有符合查询条件的结果的文档对象列表
cate = Categories.objects(name="Python")
# 更新查询到的文档:
cate.name = "LinuxZen"
cate.update()
查询数组 默认查询数组"="代表的意思是in:
class Posts(Document):
    artid = IntField(required=True)
    title = StringField(max_length=100, required=True)
    content = StringField(required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=20, required=True), required=True)
    categories = ReferenceField(Categories, required=True)
    comments = IntField(default=0, required=True)

# 将会返回所有tags包含coding的文档
Posts.objects(tags='coding')
Posts.objects.all().first().categories

#查询结果转换成字典
users_dict = User.objects().to_mongo()
# 排序,按日期排列
user = User.objects.order_by("date")
# 按日期倒序
user = User.objects.order_by("-date")

search
	name = ReferenceField('self', dbref=True)#objectsid
    is_active = BooleanField()
    photo = FileField()
marmot_photo = open('marmot.jpg', 'rb')
marmot.photo.put(marmot_photo, content_type = 'image/jpeg')
    
