# 笔记放在github上

1.安装 ubuntu  sudo apt-get install git

2.测试是否安装成功 git  --version

3.Git的基本配置（用户名和邮箱）

git config --global user.name "lijusheng90"

git config --global user.email "lijusheng@hotmail"

1. git clone https://github.com/lijusheng90/lijusheng90.github.io.git
2. git add .（注：别忘记后面的.，此操作是把Test文件夹下面的文件都添加进来）
3. git commit  -m  "提交信息" （注：“提交信息”里面换成你需要，如“first commit”）
4. git push -u origin master  （注：此操作目的是把本地仓库push到github上面，此步骤需要你输入帐号和密码）
5. 搞定
