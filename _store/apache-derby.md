---
aid: apache-derby
name: Apache Derby
description: Apache Derby is an open-source relational database implemented entirely in Java, formerly governed by the Apache Software Foundation (retired October 2025). It provides a small-footprint (~3.5MB) database engine with full SQL support, JDBC compliance, ACID transactions, stored procedures, and triggers. Derby operates in both embedded mode (bundled inside Java applications) and client/server mode via the Derby Network Server.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Database
  - Embedded
  - Java
  - JDBC
  - Open Source
  - Relational
  - SQL
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-derby:apache-derby
    name: Apache Derby
    description: Derby provides a standard JDBC API for database operations in both embedded (org.apache.derby.jdbc.EmbeddedDriver) and client/server (org.apache.derby.jdbc.ClientDriver) modes, supporting full SQL, stored procedures, triggers, views, indexes, and complete ACID transaction management. The Derby Network Server also exposes a simple text-based administrative protocol.
    humanURL: https://db.apache.org/derby/manuals/index.html
    tags:
      - Embedded
      - Java
      - JDBC
      - Network Server
      - SQL
      - Transactions
    properties:
      - type: Documentation
        url: https://db.apache.org/derby/manuals/index.html
      - type: GettingStarted
        url: https://db.apache.org/derby/quick_start.html
      - type: APIReference
        url: https://db.apache.org/derby/javadoc/publishedapi/jdbc4/
      - type: GitHubRepository
        url: https://github.com/apache/derby
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.derby/derby
        title: derby (Maven Central)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.derby/derbyclient
        title: derbyclient (Maven Central)
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.derby/derbynet
        title: derbynet Network Server (Maven Central)
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/json-schema/apache-derby-connection-config-schema.json
        title: Connection Config
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/json-schema/apache-derby-table-info-schema.json
        title: Table Info
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/json-structure/apache-derby-connection-config-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/json-structure/apache-derby-table-info-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/json-ld/apache-derby-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/examples/apache-derby-connection-config-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/examples/apache-derby-table-info-example.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: Portal
    url: https://db.apache.org/derby/
  - type: Documentation
    url: https://db.apache.org/derby/manuals/index.html
  - type: GettingStarted
    url: https://db.apache.org/derby/quick_start.html
  - type: GitHubRepository
    url: https://github.com/apache/derby
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/apache-derby
  - type: Features
    data:
      - name: Embedded Mode
        description: Derby can be embedded directly in Java applications as a library, providing a zero-administration database with no separate server process required.
      - name: Client/Server Mode
        description: Derby Network Server supports multiple concurrent JDBC clients connecting over TCP/IP using the Derby Network Client driver.
      - name: Full SQL Support
        description: Supports ANSI SQL-92 with extensions including subqueries, joins, constraints, triggers, views, stored procedures, and user-defined functions.
      - name: ACID Transactions
        description: Full ACID transaction support with row-level locking, MVCC-style isolation levels, and savepoints.
      - name: Small Footprint
        description: The base Derby engine and embedded JDBC driver is approximately 3.5MB, making it suitable for desktop and embedded applications.
      - name: Java Stored Procedures
        description: Supports Java-based stored procedures and functions callable directly from SQL using standard JDBC interfaces.
  - type: UseCases
    data:
      - name: Embedded Application Database
        description: Embed Derby in desktop Java applications, IDEs, or tools that need a local SQL database without a separate server.
      - name: Unit and Integration Testing
        description: Use Derby as an in-memory or on-disk test database for Java application integration tests with JDBC.
      - name: Lightweight Development Database
        description: Use Derby as a development database when production uses a heavier RDBMS, without installing MySQL or PostgreSQL.
      - name: Data Migration and ETL
        description: Use Derby as a staging database for ETL processes in Java-based data pipelines.
  - type: Integrations
    data:
      - name: JDBC
        description: Derby provides JDBC 4.0/4.1/4.2 compliant embedded and network client drivers.
      - name: Spring Framework
        description: Commonly used with Spring DataSource and JPA/Hibernate for test database configuration.
      - name: Hibernate / JPA
        description: Derby has a Hibernate dialect (DerbyDialect) for ORM integration.
      - name: Apache Maven
        description: Derby artifacts are available on Maven Central under org.apache.derby group ID.
      - name: Eclipse IDE
        description: Eclipse IDE includes Derby as a built-in SQL explorer and development database.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/vocabulary/apache-derby-vocabulary.yaml
---
