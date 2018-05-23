## git常用命令

### git init

- 解释：

	在项目根目录执行，初始化git


### .gitignore文件

- 命令：

```bash
vim .gitignore
```

- 解释：

	在项目根目录建立该文件，在该目录中的文件文件夹不被追踪

### git status

- 命令：

```bash 
git status  查看当前git状态
```

### 添加远程目录

- 命令：

```bash
git remote add origin
git@github.com:hongwangli/python.git
```

- 解释：

	git remote add：为命令关键字
	
	origin： 为自定义名字
	
	git@github.com:hongwangli/python.git： 为github项地址


### 查看远程目录

- 命令：

```bash
git remote -v
```

- 解释：

	显示文件夹中已经配置的githup仓库的地址别名
	
### 添加文件 

- 命令

```bash
git add <filename>/<dirname>
git add .
```

- 解释：

	git add <filename>/<dirname> 添加制定的文件或文件夹，添加多个用空格分隔

	git add .  添加所有不在.gitignore中的文件



### 提交文件

- 命令

```bash
git commit -m 'this is a commit'

git commit -am 'this commond join add and commit '
```

- 解释：

	git commit -m <note> 一般在git add 之后用 
    
	git commit -am <note> 合并git add 和 git commit 修改文件后不用使用git add 命令



### 推送到远程仓库

- 命令：

```bash
git push -u origin master
```

- 解释：

	origin  远程仓库别名
	
	master 分支名



###  查看提交历史

- 命令：

```bash
git log
```


###
查看哪些文件在追踪

- 命令：

```bash
git ls-files
```

### 构建分支

- 命令

```bash
git checkout -b dev
git branch dev
git checkout dev
git branch -d dev
```

- 解释：

	git checkout -b dev  : 构建并切换到dev分支

	git branch dev  :构建dev分支

	git checkout dev  : 切换到dev分支

	git checkout -d dev  : 删除dev分支


### 合并分支

- 命令：

```bash
git checkout master
git merge dev
```
### 删除文件

- 命令

```bash
git rm <filename/dirnaem>
git rm --cache <filename/dirname>|
```

- 解释：

	git rm <filename/dirnaem>  本地和远程都删除
	
	git rm --cache <filename/dirname> 只在远程删除


### 重命名文件

- 命令：

```bash
git mv <oldname> <newname>
```

### 生成并添加ssh-key

- 命令：

```bash
ssh-keygen -t
rsa -C "e-mail@163.com"

```

- 解释：

	生成的公钥放到github上就能免密码提交


###
查看提交历史

- 命令：

```bash
git log
```

### 恢复到指定版本

- 命令：

```bash
git reset --hard
```

- 解释：

	hard 后面加提交的head的地址


### 查看更改内容

- 命令：

```bash
git diff [<filename>]
```



### 参考链接：
[git教程廖雪峰](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

[git简明指南](https://rogerdudler.github.io/git-guide/index.zh.html)


