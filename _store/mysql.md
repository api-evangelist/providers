---
aid: mysql
name: MySQL
description: MySQL is the world's most popular open-source relational database management system. This index covers the developer-facing APIs and interfaces for MySQL, including the MySQL REST Service, X DevAPI, and native connectors.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.mysql.com
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Database
  - Open Source
  - RDBMS
  - Relational Database
  - SQL
apis:
  - aid: mysql:mysql-rest-service
    name: MySQL REST Service
    description: The MySQL REST Service (MRS) provides a RESTful interface for accessing MySQL databases. Endpoints are dynamically defined per database schema and table by the database administrator.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dev.mysql.com/doc/dev/mysql-rest-service/latest/
    tags:
      - Database Operations
      - REST
    properties:
      - type: Documentation
        url: https://dev.mysql.com/doc/dev/mysql-rest-service/latest/
  - aid: mysql:x-devapi
    name: MySQL X DevAPI
    description: Modern API for MySQL with CRUD operations and NoSQL document store capabilities, available across multiple language connectors.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dev.mysql.com/doc/x-devapi-userguide/en/
    tags:
      - CRUD
      - DevAPI
      - NoSQL
    properties:
      - type: Documentation
        url: https://dev.mysql.com/doc/x-devapi-userguide/en/
      - type: Protocol
        url: https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_MYSQLX_PROTOCOL.html
  - aid: mysql:connectors
    name: MySQL Connector APIs
    description: Native driver APIs for connecting applications to MySQL across multiple programming languages including Python, Node.js, Java, and .NET.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dev.mysql.com/doc/index-connectors.html
    tags:
      - Connectors
      - Drivers
    properties:
      - type: Documentation
        url: https://dev.mysql.com/doc/index-connectors.html
      - type: Python
        url: https://dev.mysql.com/doc/connector-python/en/
      - type: Node.js
        url: https://dev.mysql.com/doc/dev/connector-nodejs/
      - type: Java
        url: https://dev.mysql.com/doc/connector-j/en/
      - type: .NET
        url: https://dev.mysql.com/doc/connector-net/en/
common:
  - type: Getting Started
    url: https://dev.mysql.com/doc/mysql-getting-started/en/
  - type: Documentation
    url: https://dev.mysql.com/doc/
  - type: Downloads
    url: https://dev.mysql.com/downloads/
  - type: Community
    url: https://www.mysql.com/community/
  - type: Blog
    url: https://blogs.oracle.com/mysql/
  - type: GitHub Organization
    url: https://github.com/mysql
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/mysql
  - type: Terms of Service
    url: https://www.mysql.com/about/legal/
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
