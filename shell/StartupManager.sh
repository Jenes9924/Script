#!/usr/bin/env bash

# 注意：路径针对本人服务器


#启动JetBrains破解
nohup sudo /opt/crack/IntelliJIDEALicenseServer_linux_386 > /opt/crack/log.log 2>&1 &

#启动leanote服务
sudo  service leanote start  >/dev/null 2>&1
if [[ `sudo service mariadb status |grep 'active (running)'` != '' ]]; then
    echo leanote服务启动成功
    else
    echo leanote服务启动失败
fi

#启动gogs服务
sudo service gogs start  >/dev/null 2>&1
if [[ `sudo service gogs status |grep 'active (running)'` != '' ]]; then
    echo gogs服务启动成功
    else
    echo gogs服务启动失败
fi

