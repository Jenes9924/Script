# TCL语法，expect脚本
# 自己写的项目发布脚本，将maven项目打包后自动上传到服务器并重启tomcat
# 使用此脚本之前需要先执行autoUploadFile.sh脚本


set remote_pwd passwd
set param [lindex $argv 0]


proc tzadminf {} {
    

    spawn ssh root@192.168.199.252
    expect "*assword*" {send "$remote_pwd\r"}
    expect "Last login" {send "./AutoRelease.sh f\r"}
    expect "tzadminf完成" {send "exit\r"}
    expect eof
}

proc tzadminb {} {
    spawn scp /home/root/workspace/tzadminb/target/tzadmin-backend.war root@192.168.199.252:~/
    set remote_pwd tpasswd
    expect "*assword:" {send "$remote_pwd\r"}
    expect eof  

    spawn ssh root@192.168.199.252
    expect "*assword*" {send "$remote_pwd\r"}
    expect "Last login" {send "./AutoRelease.sh b\r"}
    expect "tzadminb完成" {send "exit\r"}
    expect eof
}
# puts "$param"
# if {$param == "f"} {
#     puts "进入tzadminf函数"
#     tzadminf
#     exit 0
# }
# if {$param == "b"} {
#     puts "进入tzadminb函数"
#     tzadminb
#     exit 0
# }
# puts "error param,invaild args"
# exit 1

spawn scp ./credit-interface-0.0.1-SNAPSHOT.jar root@192.168.1.10:/opt/credit-interface/
set remote_pwd passwd
expect "*assword:" {send "$remote_pwd\r"}
expect eof 
exit 0

