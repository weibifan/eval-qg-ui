# eval-qg-ui
ParaQG: A System for Generating Questions and Answers from Paragraphs, EMNLP19  

## 安装方法
1）从Github克隆到本地。  
2）安装NodeJS。   
3）安装Stanford NLPCore  
4）安装Flask框架  
5）下载bert模型，用于predict.py和Flask API  
6）下载spacy模型，用于spacy库。  

## 使用方法
1）进入qg-ui目录。  
2）启动Stanford NLPCore 服务  http://localhost:9000  
3）启动Flask服务器：http://0.0.0.0:5000/translator/translate
4）在console中执行 node ./bin/www  
5）打开浏览器输入：http://127.0.0.1:3000。  

注释：
未使用中间件服务   


启动过程
Express 启动：启动www，调用app.js，调用index.js，响应post函数，  

创建子进程，调用python ./python_code/create_para_v1.py，等待输入   

为该进程拼接数据，输入数据，然后捕获数据。  这一步不成功，原因未知。 


问题：问题生成过程，及用到了spawn子进程，又用到了Flask API，为啥不只用任何一个？  


# 文件说明  

create_para_v1.py  调用spacy模型，不知道在干啥，使用null_loop.py替换   

bio_tag_np_v2.py  调用Stanford NLPCore的服务，识别短语，用于关键字识别  

ner-v4.py  调用Stanford NLPCore的服务，识别命名实体，

v1_group.py     

### 测试文本  
A computer is a digital electronic machine that can be programmed to carry out sequences of arithmetic or logical operations (computation) automatically. 
Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. 
A computer system is a complete computer that includes the hardware, operating system (main software), and peripheral equipment needed and used for full operation. 
This term may also refer to a group of computers that are linked and function together, such as a computer network or computer cluster.   
The above text is from the website of Wikipedia.

OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a 
valid path to a data directory. #4577    

手工下载：   
python -m spacy download en_core_web_sm
python -m spacy.en.download en_core_web_sm --data-path /some/dir





