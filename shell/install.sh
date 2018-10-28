#!/bin/bash

#工作环境配置
#新电脑自动安装常用软件脚本


# 安装清单：
# 1.google chrome
# 2.shadowsocks-qt5
# 3.sougou拼音
# 4.zsh
# 5.pycharm
# 6.IntelliJ IDEA
# 7.paper theme等主题
# 8.sublime text
# 9.jdk
# 10.python3-pip lxml
# 11.vim unzip unrar
# 12.indicator-multiload

function installLNMP(){
    wget http://soft.vpser.net/lnmp/lnmp1.4-full.tar.gz
    echo 'lnmp安装包下载完成，开始安装.....'
    mkdir lnmp
    tar zxf lnmp*.gz
    if [ `echo $DISPLAY`  = '' ]
    then
        if [ "$1" == "y" ]
        then
            sudo ./lnmp/lnmp1.4-full/install.sh
        else
            sudo ./lnmp/lnmp1.4-full/install.sh nginx
            sudo ./lnmp/lnmp1.4-full/install.sh db
        fi
    else
        sudo ./lnmp/lnmp1.4-full/install.sh db
    fi
}


function installSoftware(){
    echo '检测到屏幕，个人电脑将安装sublime text，idea，pycharm，gnome主题等软件'
    #获取并安装搜狗拼音以及谷歌chrome
    wget 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
    sudo dpkg -i ./*.deb
    sudo apt install -f
    sudo add-apt-repository -y ppa:hzwhuang/ss-qt5

    echo '以下添加的源可能耗时很长，请确认是否需要继续(建议手动安装)？'
    read continue
    if [ "$continue" == "n" ]
    then
        return 0
    fi

    #安装sublime 3 密钥
    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    sudo add-apt-repository -y ppa:noobslab/themes
    sudo add-apt-repository -y ppa:noobslab/icons
    sudo add-apt-repository -y ppa:numix/ppa
    sudo add-apt-repository -y ppa:noobslab/themes

    sudo apt-get update && sudo apt-get upgrade

    sudo apt-get install -y ultra-flat-icons numix-wallpaper-* \
     numix-gtk-theme numix-icon-theme-circle shadowsocks-qt5 sublime-text flatabulous-theme ultra-flat-icons
    sudo apt-get install -y numix-wallpaper-*
    sudo apt-get install -y ambiance-dark
    sudo apt-get install -y numix-gtk-theme numix-icon-theme-circle
    sudo apt-get install -y shadowsocks-qt5
    sudo apt-get install -y sublime-text
    sudo apt-get install -y flatabulous-theme
    sudo apt-get install -y ultra-flat-icons


    #解决sublime无法输入中文的问题
    git clone https://github.com/lyfeyaj/sublime-text-imfix.git && cd sublime-text-imfix && ./sublime-imfix

}
#判断是否root用户
if [[ `whoami` != 'root' ]]
then
	#statements
	echo '你傻啊，root权限被你吃了？'
	exit 0
fi

#获取当前脚本路径
cd ` dirname $0 `
sh_path=`pwd`

#刷新源
apt-get update

#必备软件git
if [ ` which git ` = '' ]; then
	echo '准备安装 git'
	apt install -y git
fi

# 直接安装已知有源的软件
apt install -y unzip unrar python3-pip python3-lxml vim aptitude clipt indicator-multiload

#安装zsh之前需要测试git是否安装
apt install -y zsh && git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
&& chsh -s /bin/zsh


#检查是否存在jdk
mkdir /usr/local/java
#chown /usr/lcoal/java
if [[ `ls ./ |grep jdk*.tar.gz` = "" ]]; then

	#下载安装jdk1.8
 	wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz
fi


#判断是否有图形界面
if [ `echo $DISPLAY`  = '' ]; then
    echo '未检测到屏幕，此机器被判断为服务器'
    echo '服务器端将不安装主题之类的UI软件'
else
    installSoftware
fi

echo '是否需要安装LNMP环境？(y/n)'
read lnmp_need
if [ "$lnmp_need" == "y" ]
then
    echo '是否需要安装PHP？(y/n)'
        read need
        installLNMP $need
    fi


#查找打包一起的IDE，譬如pycharm,IntelliJ IDEA之类的





# 解压jdk，移动到/usr/local/java/下
tar zxvf ./jdk*.tar.gz && mv ./jdk1.8* /usr/local/java/

#添加jdk path，并在zshrc中添加source /etc/profile
echo '
' >> /etc/profile
echo 'export JAVA_HOME=/usr/local/java/jdk1.8.0/' >> /etc/profile
echo '
' >> /etc/profile
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /etc/profile
echo '
' >> /etc/profile
echo 'export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar' >> /etc/profile
echo '
' >> /etc/profile

echo '
' >> /etc/zsh/zshrc
echo 'source /etc/profile' >> /etc/zsh/zshrc




