FROM tomcat:9-jre8-alpine

COPY tomcat-users.xml /usr/local/tomcat/conf/
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/
COPY manager-extra.xml /usr/local/tomcat/conf/Catalina/localhost