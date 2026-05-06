---
aid: apache-tomcat
name: Apache Tomcat
description: Apache Tomcat is an open-source implementation of the Java Servlet, JavaServer Pages (JSP), Java Expression Language, and Java WebSocket technologies. It provides a pure Java HTTP web server and servlet container for hosting Java web applications. Tomcat exposes management APIs via the Manager application (HTTP text protocol), JMX for monitoring, and a Virtual Host Manager for configuration management. It is maintained by the Apache Software Foundation and is one of the most widely deployed Java application servers.
type: Index
position: Consumer
access: 3rd-Party
image: https://tomcat.apache.org/res/images/tomcat.png
tags:
  - Application Server
  - Java
  - JSP
  - Open Source
  - Servlet
  - Web Server
created: '2024-01-15'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-tomcat/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-tomcat:apache-tomcat-manager-api
    name: Apache Tomcat Manager API
    description: 'The Tomcat Manager application provides an HTTP text protocol API for deploying, undeploying, starting, stopping, and reloading web applications remotely. Key endpoints include: /manager/text/list (list deployed apps), /manager/text/deploy (deploy a WAR file), /manager/text/undeploy, /manager/text/start, /manager/text/stop, /manager/text/reload, /manager/text/sessions (session statistics), and /manager/text/serverinfo. Requires manager-script role authentication.'
    humanURL: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html
    tags:
      - Administration
      - Deployment
      - Management
      - REST
    properties:
      - type: Documentation
        url: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html
  - aid: apache-tomcat:apache-tomcat-jmx-api
    name: Apache Tomcat JMX API
    description: The Tomcat JMX API exposes management and monitoring beans for Connectors, Engines, Hosts, Contexts, Sessions, DataSources, thread pools, and memory via Java Management Extensions. JMX can be accessed via JConsole, Java VisualVM, or remote JMX clients. Prometheus JMX Exporter can expose Tomcat metrics in Prometheus format via HTTP endpoint.
    humanURL: https://tomcat.apache.org/tomcat-10.1-doc/monitoring.html
    tags:
      - JMX
      - Monitoring
      - Management
      - Java
    properties:
      - type: Documentation
        url: https://tomcat.apache.org/tomcat-10.1-doc/monitoring.html
common:
  - type: GitHubRepository
    url: https://github.com/apache/tomcat
  - type: Documentation
    url: https://tomcat.apache.org/tomcat-10.1-doc/
  - type: Portal
    url: https://tomcat.apache.org/
  - type: GettingStarted
    url: https://tomcat.apache.org/tomcat-10.1-doc/setup.html
  - type: ReleaseNotes
    url: https://tomcat.apache.org/tomcat-10.1-doc/changelog.html
  - type: Support
    url: https://tomcat.apache.org/lists.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Servlet Container
        description: Jakarta Servlet 6.0 (formerly Java EE) compliant servlet container.
      - name: JSP Engine
        description: JavaServer Pages compiler and runtime engine for dynamic HTML generation.
      - name: WebSocket Support
        description: Jakarta WebSocket 2.1 implementation for full-duplex browser-server communication.
      - name: HTTP/2 Support
        description: HTTP/2 multiplexing and server push via APR/Native connector.
      - name: SSL/TLS Termination
        description: Built-in SSL/TLS support via JSSE or APR/OpenSSL connectors.
      - name: Connection Pooling
        description: DBCP2-based database connection pool management via JNDI DataSource.
      - name: Clustering
        description: Session replication across Tomcat cluster nodes via DeltaManager or BackupManager.
  - type: UseCases
    data:
      - name: Java Web Application Hosting
        description: Deploy and host Java Servlet/JSP web applications.
      - name: API Gateway Backend
        description: Host REST API backends built with Spring MVC, JAX-RS, or plain servlets.
      - name: Microservices Container
        description: Embedded Tomcat in Spring Boot for microservices deployment.
      - name: Legacy Application Migration
        description: Host Java EE applications during cloud migration.
  - type: Integrations
    data:
      - name: Spring Boot
        description: Embedded Tomcat as the default servlet container in Spring Boot applications.
      - name: Apache HTTP Server
        description: mod_jk and mod_proxy_ajp for load balancing between Apache httpd and Tomcat.
      - name: Nginx
        description: Nginx reverse proxy for Tomcat with SSL termination and load balancing.
      - name: Prometheus
        description: JMX Exporter for exposing Tomcat metrics in Prometheus format.
      - name: Docker
        description: Official Docker image for containerized Tomcat deployment.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
