 cd /home/root/workspace/credit-interface
/opt/apache/apache-maven-3.5.4/bin/mvn clean compile package install -P prod 

 cd target/
    
#mv  /home/root/workspace/tzadminb/target/tzadmin-backend.war /home/root/workspace/tzadminb/target/tzadmin-backend`date +%s`.war
expect ~/shell/AutoScp.sh
echo '传输完成，服务器可能需要手动重启，请检查'
