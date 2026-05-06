---
aid: tomcat
name: Apache Tomcat
description: Apache Tomcat is an open-source implementation of the Jakarta Servlet, Jakarta Server Pages, and other Jakarta EE technologies, providing a pure Java HTTP web server environment for running Java code. The Tomcat Manager application exposes an HTTP API for deploying, managing, and monitoring web applications. The JMX Proxy Servlet provides programmatic access to JMX MBeans for server diagnostics and configuration. Governed by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Server
  - Java
  - Servlet Container
  - Web Server
  - Open Source
  - Apache
created: '2025-01-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tomcat/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tomcat:tomcat-manager-api
    name: Apache Tomcat Manager API
    description: The Apache Tomcat Manager application provides an HTTP text interface for deploying, undeploying, starting, stopping, and reloading web applications. Also includes session management, server status, thread dumps, VM information, SSL/TLS configuration reload, memory leak detection, and configuration saving. Authentication requires roles defined in tomcat-users.xml.
    humanURL: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html
    baseURL: http://localhost:8080/manager
    tags:
      - Java
      - Web Server
      - Application Deployment
      - Server Management
    properties:
      - type: Documentation
        url: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tomcat/refs/heads/main/openapi/tomcat-manager-openapi.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/tomcat/refs/heads/main/capabilities/application-management.yaml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/tomcat/refs/heads/main/rules/tomcat-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/tomcat/refs/heads/main/vocabulary/tomcat-vocabulary.yml
  - aid: tomcat:tomcat-jmx-proxy-api
    name: Apache Tomcat JMX Proxy API
    description: The Apache Tomcat JMX Proxy Servlet provides HTTP-based access to JMX MBeans for querying, getting, setting, and invoking operations on server management beans. Useful for server diagnostics, performance monitoring, and dynamic configuration changes without restarting Tomcat.
    humanURL: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html#Using_the_JMX_Proxy_Servlet
    baseURL: http://localhost:8080/manager/jmxproxy
    tags:
      - JMX
      - Monitoring
      - Java
      - Diagnostics
    properties:
      - type: Documentation
        url: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html#Using_the_JMX_Proxy_Servlet
features:
  - Web application deployment via WAR files
  - Application lifecycle management (start/stop/reload/undeploy)
  - Session management and expiration
  - Server status and diagnostics
  - JMX MBean access via HTTP proxy
  - SSL/TLS configuration reload
  - Memory leak detection
  - Thread dumps
  - VM information
  - Configuration persistence
useCases:
  - Automated application deployment
  - CI/CD pipeline integration
  - Production server monitoring
  - Application health checking
  - Dynamic SSL certificate updates
solutions:
  - DevOps automation
  - Java application hosting
  - Enterprise middleware management
common:
  - type: Website
    url: https://tomcat.apache.org/
  - type: Documentation
    url: https://tomcat.apache.org/tomcat-10.1-doc/
  - type: Manager API Documentation
    url: https://tomcat.apache.org/tomcat-10.1-doc/manager-howto.html
  - type: Downloads
    url: https://tomcat.apache.org/download-10.cgi
  - type: GitHub Repository
    url: https://github.com/apache/tomcat
  - type: Apache Software Foundation
    url: https://www.apache.org/
  - type: Mailing Lists
    url: https://tomcat.apache.org/lists.html
  - type: Security
    url: https://tomcat.apache.org/security.html
  - type: Changelog
    url: https://tomcat.apache.org/tomcat-10.1-doc/changelog.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
