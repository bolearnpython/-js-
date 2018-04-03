uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
uncle_bob.save() # bob is now stored in the database
grandma = Person.select().where(Person.name == 'Grandma L.').get()
grandma = Person.get(Person.name == 'Grandma L.')
Book.create_table()
book = Book(author="me", title='Peewee is cool')
book.save()
for book in Book.filter(author="me"):
    print book.title



# 1. 导入peewee的模块
from peewee import *
from datetime import datetime

# 2. 建立数据库实例
db = MySQLDatabase(
        database = 'db',
        host = 'localhost',
        port = 3306, 
        user = 'root',
        passwd = '199323',
        charset = 'utf8'
        )   
#######################################################################
# 3. 建立数据表的模型
# 4. 先建立基本模型，具体的模型在此基础上继承而来
class BaseModel(Model):
    class Meta:
        # 指定表所在的数据库
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    class Meta:
        db_table = 'student_info'
class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.now)
    is_published = BooleanField(default=True)

#########################################################################
if __name__ == '__main__':
    try:
        # connect方法不是必须的，但是如果出错可以判断是否是在连接时出的错
        db.connect()
        # 5. 创建表，这里有了safe=True选项，会在创建表之前先检查数据库里表是否已经存在,由于创建表的语句往往只需要使用一次，一般建议写入类或者方法中通过具体命令来调用
        # 注意：peewee里面创建表有两个方法， create_tables是`Database`中的方法，创建表时会建立表之间的关系和表的索引，使用`somedb.create_tables([Models], safe=False)`来调用
        # create_table是`Model`中的方法，仅仅创建表本身，而不包含索引和表之间的关系，使用`somemodel.create_table(safe=False)`来调用
        db.create_tables([User, Tweet], safe=True)
        

        # 6. 断开连接 
        db.close()
    except Exception, e:
        print e




1）插入

q = User.insert(username='admin', active=True, registration_expired=False)
q.execute() 


2）更新
q = User.update(active=False).where(User.registration_expired == True)
q.execute() 


3）.删除
q = User.delete().where(User.active == False)
q.execute() 


4）.查询

# 查询名字为Marry的person
grandma = Person.select().where(Person.name == 'Marry').get()

#列出Person表中所有的person
for person in Person.select():
    print person.name, person.is_relative
#查询Pet表中animal_type为cat的所有pet
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print pet.name, pet.owner.name

#查询Pet表中主人名为Bob的所有pet
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print pet.name

#查询Pet表中person为uncle_bob的所有pet
for pet in Pet.select().where(Pet.owner == uncle_bob):
    print pet.name

#查询Pet表中person为uncle_bob结果按pet名排列
for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print pet.name

#将Person表中的person按生日降序查询
for person in Person.select().order_by(Person.birthday.desc()):
    print person.name, person.birthday

#查询Person表中person所拥有的pet数量及名字和类型
for person in Person.select():
    print person.name, person.pets.count(), 'pets'
    for pet in person.pets:
        print '      ', pet.name, pet.animal_type
#查询Person表中生日小于1940或大于1960的person
d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

#查询Person表中生日在1940和1960之间的person
for person in query:
    print person.name, person.birthday

query = (Person
         .select()
         .where((Person.birthday > d1940) & (Person.birthday < d1960)))

for person in query:
    print person.name, person.birthday

#按照expression查询person名开头为小写或大写 G 的person
expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'g')
for person in Person.select().where(expression):
    print person.name


5）其他
#连接数据库db
db.connect()

#关闭数据库
db.close()

Model类：表
Field类：表上的列的类型
Model实例：表上的一行数据