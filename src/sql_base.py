import leancloud
import cfg

leancloud.init(cfg.get_app_id(), cfg.get_app_key())
# leancloud.init("appId", master_key="masterKey")


TestObject = leancloud.Object.extend('TestObject')
test_object = TestObject()
test_object.set('words', "Hello World!")
test_object.save()


class Todo(leancloud.Object):
    pass

# Todo = leancloud.Object.extend('Todo')

todo = Todo()
todo.set('title', 'Eng meeting')
todo.set('content', '1/report your plan; 2/update your codes')
todo.save()