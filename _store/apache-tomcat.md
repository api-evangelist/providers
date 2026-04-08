---
aid: apache-tomcat
url: https://raw.githubusercontent.com/api-evangelist/apache-tomcat/refs/heads/main/apis.yml
apis:
- name: Tomcat Manager API
  description: RESTful API for managing web applications deployed on Tomcat.
  baseURL: http://localhost:8080/manager
  humanURL: https://tomcat.apache.org/tomcat-9.0-doc/manager-howto.html
  image: https://tomcat.apache.org/res/images/tomcat.png
  version: '9.0'
  tags:
  - Administration
  - Deployment
  - Management
  properties:
  - type: Documentation
    url: https://tomcat.apache.org/tomcat-9.0-doc/manager-howto.html
  - type: OpenAPI
    url: https://tomcat.apache.org/manager-api-spec.yaml
  contact:
  - type: Mailing List
    url: https://tomcat.apache.org/lists.html
  - type: Issues
    url: https://bz.apache.org/bugzilla/describecomponents.cgi?product=Tomcat+9
- name: Tomcat JMX API
  description: Java Management Extensions API for monitoring and managing Tomcat instances.
  baseURL: service:jmx:rmi:///jndi/rmi://localhost:9000/jmxrmi
  humanURL: https://tomcat.apache.org/tomcat-9.0-doc/monitoring.html
  image: https://tomcat.apache.org/res/images/tomcat.png
  version: '9.0'
  tags:
  - JMX
  - Management
  - Monitoring
  properties:
  - type: Documentation
    url: https://tomcat.apache.org/tomcat-9.0-doc/monitoring.html
  - type: Guide
    url: https://tomcat.apache.org/tomcat-9.0-doc/mbeans-descriptors-howto.html
- name: Tomcat Host Manager API
  description: API for managing virtual hosts within Tomcat.
  baseURL: http://localhost:8080/host-manager
  humanURL: https://tomcat.apache.org/tomcat-9.0-doc/host-manager-howto.html
  image: https://tomcat.apache.org/res/images/tomcat.png
  version: '9.0'
  tags:
  - Administration
  - Management
  - Virtual Hosts
  properties:
  - type: Documentation
    url: https://tomcat.apache.org/tomcat-9.0-doc/host-manager-howto.html
name: Apache Tomcat
tags:
- Application Server
- Java
- JSP
- Open Source
- Servlet
- Web Server
type: Contract
image: https://tomcat.apache.org/res/images/tomcat.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Tomcat is an open-source implementation of the Java Servlet, JavaServer Pages, Java Expression Language and Java WebSocket technologies.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

