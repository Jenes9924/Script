#!/usr/bin/expect
###############################
#
#@Author:   root
#
###############################

set remote_pwd tz233888
set param [lindex $argv 0]


proc tzadminf {} {
    spawn scp ./tzadminf.tar.gz root@192.168.199.252:~/
    set remote_pwd password
    expect "*assword:" {send "$remote_pwd\r"}
    expect eof  

    spawn ssh root@192.168.199.252
    expect "*assword*" {send "$remote_pwd\r"}
    expect "Last login" {send "./AutoRelease.sh f\r"}
    expect "tzadminf完成" {send "exit\r"}
    expect eof
}

proc tzadminb {} {
    spawn scp /home/root/workspace/tzadminb/target/tzadmin-backend.war root@192.168.199.252:~/
    set remote_pwd password
    expect "*assword:" {send "$remote_pwd\r"}
    expect eof  

    spawn ssh root@192.168.199.252
    expect "*assword*" {send "$remote_pwd\r"}
    expect "Last login" {send "./AutoRelease.sh b\r"}
    expect "tzadminb完成" {send "exit\r"}
    expect eof
}
puts "$param"
if {$param == "f"} {
    puts "进入tzadminf函数"
    tzadminf
    exit 0
}
if {$param == "b"} {
    puts "进入tzadminb函数"
    tzadminb
    exit 0
}
    puts "error param,invaild args"
    exit 1

