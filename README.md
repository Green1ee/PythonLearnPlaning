## 你好
### 即将开始
## Shoping.py 商品购买以及商品管理
> 用到了初学的两种字符串拼接技巧：
```
"I`m %s"%name
```
和
```
"{name}".format(name = "GreenLee")
```
> 以及异常处理：
```
try:
    pass
except:
    pass
```
> 文件操作，用with以防忘记关闭，类似.net中的using(){}：
> 使用open操作文件的时候，注意mode中如果带**+**，则文件内容
> 会被清空，需要特别注意
```
with open(filepath, mode, encode) as var:
    fileContent = var.read()
```
> 数组的操作：
```
arr = []	
arr.append("GreenLee")
arr.pop(0)
```
> 由于还没有学习函数，因此过程实现不够清爽