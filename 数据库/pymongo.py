'''MongoDB配置
mkdir C:\data\db
mkdir C:\data\log
echo log>>C:\data\log\mongod.log
echo systemLog:>>C:\MongoDB\mongod.cfg
echo     destination: file>>C:\MongoDB\mongod.cfg
echo     path: C:\data\log\mongod.log>>C:\MongoDB\mongod.cfg
echo storage:>>C:\MongoDB\mongod.cfg
echo     dbPath: C:\data\db>>C:\MongoDB\mongod.cfg
"C:/mongodb/bin/mongod.exe" --config "C:\mongodb\mongod.cfg" --install
net start MongoDB
'''
安装到C: \MongoDB

from pymongo import MongoClient
import arrow
# client = MongoClient("mongodb://mongodb0.example.net:27019")
client = MongoClient()  # with MongoClient() as client
# test2 db
db = client.test2
# 表xm
col = db.create_collection(name='xm')
# db.xm.drop()
# col=db.xm
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": arrow.now().format()}
new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": arrow.now().format()},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": arrow.now().format()}]
# 插入
col.insert(post)
col.insert_many(new_posts)

# 查询
    col.find_one()
    col.find_one({"author": "Mike"})
    col.find({"author": "Mike"})
    # 范围
    d = datetime.datetime(2009, 11, 12, 12)
    col.find({"date": {"$lt": d}}).sort("author")
    #$lt 小于 $gt大于  多了=$gte$lte
    # in
    col.find({"age": {"$in": (23, 26, 32)}})
    col.find({"age": {"$nin": (23, 26, 32)}})
    # 存在
    col.find({'sex': {'$exists': True}})
    col.find({'sex': {'$exists': False}})
    # re
    col.find({"name": {"$regex": r"(?i)user[135]"}}, ["name"])
    # 大小不分
    col.find({post_text: {$regex: "tutorialspoint", $options: "$i"}})
    # or
    col.find({"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})
    # sort({"likes":-1})降
    col.find().sort([("borough", pymongo.ASCENDING),
                     ("address.zipcode", pymongo.ASCENDING)])
# index
    # create_index(keys, **kwargs)
    # create_indexes(indexes)
    # drop_index(index_or_name)
    # drop_indexes()
    # reindex()
    # list_indexes()
    # index_information()
    col.create_index([("date", pymongo.DESCENDING),
                      ("author", pymongo.ASCENDING)])
    col.create_index([('author', pymongo.ASCENDING)])  # unique=True

# 更新
    # update_one(filter, update, upsert=False)
    # update_many(filter, update, upsert=False)
    # replace_one(filter, replacement, upsert=False)
    # find_one_and_update(filter, update, projection=None, sort=None, return_document=ReturnDocument.BEFORE, **kwargs)
    col.update({'author': 'Eliot'}, dict(post), upsert=True)
# 删除
    # delete_one(filter)
    # delete_many(filter)
    # drop()
    # find_one_and_delete(filter, projection=None, sort=None, kwargs)
    # find_one_and_replace(filter, replacement, projection=None, sort=None,
    # return_document=ReturnDocument.BEFORE, kwargs)
    col.remove({"name": "wu"})
    col.find_one_and_delete({"name": "zheng"})
# 聚合
    col.aggregate(
        [
            {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
        ]
    )
    col.aggregate(
        [
            {"$match": {"borough": "Queens", "cuisine": "Brazilian"}},
            {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}}
        ]
    )
# 常用
    skip()
    limit()
    count()
    sort()
# 其他
自动增长{'_id': getNextSequenceValue("productid")}

#
如果只更新一个键呢，那就不用这么大费周折了，可以使用”$set”这个修改器，指定一个键，如果不存在，就可以创建。比如我要继续更新上面那篇文章的content，可以这样做（记住，修改它，必须先找到它，这里我利用上面查询到的_id值来找）：
posts.update({"_id": post["_id"]}, {
             "$set": {"content": "Test Update SET...."}})
MongoDB的修改是很强大的，你可以把数据类型也给改了，比如把tags的数组改成普通的字符串。”set”过后又想删除这个键，可以使用”unset”。如果我的这个post里面有一个键是views，即文章访问的次数，我想在每次访问这个文章后给它的值增加1，这该怎么办？于是”$inc”修改器出场了，这个可以用来增加已有键的值，如果没有，则创建它，类似的用法是：
posts.update({"_id": post["_id"]}, {"$inc": {"views": 1}})
如果想修改tags这个数组里面的内容怎么办？有一个办法就是用set整体修改，但只是改里面的一些元素呢，MongoDB准备好了用于数组的修改器。比如，想要在tags里面加一个”Test”，这需要使用”push”，它可以在数组末尾添加一个元素：
posts.update({"_id": post["_id"]}, {"$push": {"tags": "Test"}})
为了避免加入了重复的，可以将”push”改为使用”addToSet”，如果需要添加多个值，可以配合”$each”来使用，这样就可以添加不重复的进去，如下面：
posts.update({"_id": post["_id"]}, {"$addToSet": {
             "tags": {"$each": ["Python", "Each"]}}})
可以把数组看成栈和队列，使用”$pop”来操作，比如上面的：
posts.update({"_id": post["_id"]}, {"$pop": {"tags": 1}})
这个会删除tags里面最后一个，改成 - 1则删除第一个。可以使用”pull”来删除数组中指定的值，它会删除数组中所有匹配的值。如何修改其中的一个值呢？可以先删除掉，再增加一个进去，还有就是直接定位修改。比如tags数组中，”Python”是第一个，想把它改成”python”，可以通过下标直接选择, 就是tags[0]，然后使用上面的”set”等修改器，如果不确定可以使用$来定位：
posts.update({"tags": "MongoDB"}, {"$set": {"tags.$": "Hello"}})
这个将先搜索tags中满足”MongoDB”的，如果找到，就把它修改为”Hello”。可以看到上面的update这个函数已经有两个参数了，它还有第3个参数upsert，如果设为”True”，则如果没有找到匹配的文档，就会在匹配的基础上新建一个文档


(1) $all: 判断数组属性是否包含全部条件。
(2) $size: 匹配数组属性元素数量。
(3) $type: 判断属性类型。
    db.users.find({'t': {'$type': 1}})
    db.users.find({'t': {'$type': 2}})
(4) $not: 取反，表示返回条件不成立的文档。
(5) $unset: 和 $set 相反，表示移除文档属性。
(6) $push: 和 $ pushAll 都是向数组属性添加元素。  # 好像两者没啥区别
(7) $addToSet: 和 $push 类似，不过仅在该元素不存在时才添加(Set 表示不重复元素集合)。
(8) $each 添加多个元素用。
(9) $pop: 移除数组属性的元素(按数组下标移除)，$pull 按值移除，$pullAll 移除所有符合提交的元素。
(10) $where: 用 JS 代码来代替有些丑陋的 $lt、$gt。
db.users.find({"$where": "this.age > 7 || this.age < 3"})
# 类型值:
    double: 1
    string: 2
    object: 3
    array: 4
    binary data: 5
    object id: 7
    boolean: 8
    date: 9
    null: 10
    regular expression: 11
    javascript code: 13
    symbol: 14
    javascript code with scope: 15
    32 - bit integer: 16
    timestamp: 17
    64 - bit integer: 18
    min key: 255
    max key: 127
# mapReduce
>db.collection.mapReduce(
    function() {emit(key, value)
                }, // map function
    function(key, values) {return reduceFunction}, // reduce function
    {
        out: collection,
        query: document,
        sort: document,
        limit: number
    }
)
#$explain
indexOnly 的真值代表该查询使用了索引。
cursor 字段指定了游标所用的类型。BTreeCursor 类型代表了使用了索引并且提供了所用索引的名称。BasicCursor 表示进行了完整扫描，没有使用任何索引。
n 代表所返回的匹配文档的数量。
nscannedObjects 表示已扫描文档的总数。
nscanned 所扫描的文档或索引项的总数。
#$hint
$hint 操作符强制索引优化器使用指定的索引运行查询。这尤其适用于测试带有多个索引的查询性能。比如，下列查询指定了用于该查询的 gender 和 user_name 字段的索引：
col.find({gender: "M"}, {user_name: 1, _id: 0}).hint({gender: 1, user_name: 1})
使用 $hint 来优化上述查询：
col.find({gender: "M"}, {user_name: 1, _id: 0}).hint(
    {gender: 1, user_name: 1}).explain()
# ensureIndex
    {
        "address": {
            "city": "Los Angeles",
            "state": "California",
            "pincode": "123"
        },
        "tags": [
            "music",
            "cricket",
            "blogs"
        ],
        "name": "Tom Benzamin"
    }
    使用下列命令创建标签数据的索引：
    col.ensureIndex({"tags": 1})
    创建完该索引后，按照如下方式搜索集合中的标签字段：
    col.find({tags: "cricket"})
    为了验证所使用索引的正确性，使用 explain 命令，如下所示：
    col.find({tags: "cricket"}).explain()
    上述 explain 命令的执行结果是 "cursor": "BtreeCursor tags_1"，表示使用了正确的索引。
    索引子文档字段
    假设需要根据市（city）、州（state）、个人身份号码（pincode）字段来搜索文档。因为所有这些字段都属于地址子文档字段的一部分，所以我们将在子文档的所有字段上创建索引。
    使用如下命令在子文档的所有三个字段上创建索引：
    col.ensureIndex(
        {"address.city": 1, "address.state": 1, "address.pincode": 1})
    一旦创建了索引，就可以使用索引来搜索任何子文档字段：
    col.find({"address.city": "Los Angeles"})
    记住，查询表达式必须遵循指定索引的顺序。因此上面创建的索引将支持如下查询：
    col.find({"address.city": "Los Angeles", "address.state": "California"})
    另外也支持如下这样的查询：
    col.find({"address.city": "LosAngeles",
              "address.state": "California", "address.pincode": "123"})
    ensureIndex() 接收可选参数，可选参数列表如下：
        Parameter   Type    Description
        background  Boolean 建索引过程会阻塞其它数据库操作，background可指定以后台方式创建索引，即增加 "background" 可选参数。 "background" 默认值为false。
        unique  Boolean 建立的索引是否唯一。指定为true创建唯一索引。默认值为false.
        name    string  索引的名称。如果未指定，MongoDB的通过连接索引的字段名和排序顺序生成一个索引名称。
        dropDups    Boolean 在建立唯一索引时是否删除重复记录, 指定 true 创建唯一索引。默认值为 false.
        sparse  Boolean 对文档中不存在的字段数据不启用索引；这个参数需要特别注意，如果设置为true的话，在索引字段中不会查询出不包含对应字段的文档.。默认值为 false.
        expireAfterSeconds  integer 指定一个以秒为单位的数值，完成 TTL设定，设定集合的生存时间。
        v   index version   索引的版本号。默认的索引版本取决于mongod创建索引时运行的版本。
        weights document    索引权重值，数值在 1 到 99, 999 之间，表示该索引相对于其他索引字段的得分权重。
        default_language    string  对于文本索引，该参数决定了停用词及词干和词器的规则的列表。 默认为英语
        language_override   string  对于文本索引，该参数指定了包含在文档中的字段名，语言覆盖默认的language，默认值为 language.
