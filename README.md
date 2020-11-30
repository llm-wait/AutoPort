# AutoPort
python使用unittest+request+excel搭建的接口自动化框架
Config目录存放测试用例配置文件
case目录存放测试用例
log目录存放日志文件
report目录存放测试报告文件
tool目录中存放封装的方法
    --datastore.py使用excel存储解决接口依赖的问题
    --getdata.py使用反射机制解决cookie和token关联问题
    --htmlTestRunner.py存放测试报告模板
    --http_request.py封装http请求
    --log.py封装日志方法
    --project_path.py封装各种路径
    --readExcel.py封装读写excel用例方法
    --sendmail.py封装发送邮件方法
    --test_http.py封装测试类
    --run.py程序运行的入口
