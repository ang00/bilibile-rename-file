# bilibili-rename-file

* java
    * 使用第三方库 json

```maven
    <dependency>
      <groupId>cn.hutool</groupId>
      <artifactId>hutool-all</artifactId>
      <version>5.7.16</version>
    </dependency>
```

* python
    * 使用解析 json 库

```python
import json
import os.path
import shutil
```

* shell
    * 使用第三方 jq

> 安装 jq [https://stedolan.github.io/jq/download/](https://stedolan.github.io/jq/download/)

* golang
    * 使用idea 不能加载 `GOPATH` 修改安装目录下 `go1.17.5\src\runtime\internal\sys\zversion.go` 文件 打开 `zversion.go` 文件，追加一行并保存
  > const TheVersion = `go1.17.5`
    * 引入第三方 gjson [https://github.com/tidwall/gjson](https://github.com/tidwall/gjson)

```shell
//导入第三方 json 解析
go get -u github.com/tidwall/gjson
```
