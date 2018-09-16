# 基础指令
git init #仓库初始化，在目录中生成.git目录
 
git config user.name #项目级别签名
git config user.email #信息存放于.git/config

git config --global user.name #用户级别签名
git config --global user.email #信息存放于~/.gitconfig

git status #分支信息、工作区、暂存区状态

git add file #添加文件
git rm --cached file #删除追踪
git rm file #删除追踪和文件

git commit #提交commit commit所有改动文件
git commit -m "commit message" file #直接输入commit信息并提交某一个文件

git log #查看完整历史记录
git log --pretty=oneline #简洁显示 完整哈希
git log --oneline #简洁显示 简洁哈希
git reflog #简洁显示 HEAD@{移动到当前版本需要的步数} 后退之后还能显示之前的版本

git reset --hard hash #基于hash前进后退
git reset --hard HEAD^ #只能后退 一个^后退一步
git reset --hard HEAD~n #只能后退 后退n步

git reset -- soft mixed hard
--soft 仅在工作目录移动HEAD指针
--mixed 在工作目录移动HEAD指针 重置暂存区
--hard 在工作目录移动HEAD指针 重置暂存区和工作区

git reset --hard 之后如果有commit，那么可以找回原文件；如果直接push到了一个unprotected的远程分支，那么就直接将之前的commit全部覆盖掉

git diff file #将工作目录和暂存区文件进行比较
git diff HEAD / hash #将工作目录和工作区进行比较
git diff --stat #统计diff的状态

git branch -v #查看分支信息
git branch branch_name #创建分支
git checkout branch_name #切换分支
git merge branch_name #合并分支 在此之前需要先切换到目标分支 然后合并作出修改的分支 | 合并有冲突的话需要手动去merge

git remote -v #查看远程仓库
git remote add origin https://xxx.com #添加远程仓库 origin是别名 地址是https格式
git remote add origin_ssh git@ssh #添加远程仓库 地址是ssh格式

git fetch origin master #抓取远程内容 但是不merge（参数是远程地址别名和远程分支名）
git checkout origin/master #切换到拉取的远程库

git pull = git fetch + git merge #拉取远程库并合并
