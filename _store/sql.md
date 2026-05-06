---
aid: sql
name: SQL
description: SQL (Structured Query Language) is the ANSI/ISO standard language for managing and querying relational databases. SQL defines the interface for creating, reading, updating, and deleting data in relational database management systems (RDBMS). Database connectivity standards including ODBC (Open Database Connectivity) and JDBC (Java Database Connectivity) expose SQL capabilities as programmatic APIs, enabling applications to connect to and interact with SQL-compliant databases. Major implementations include MySQL, PostgreSQL, Microsoft SQL Server, Oracle, SQLite, and many others.
image: https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png
url: https://www.iso.org/standard/76583.html
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - name: ODBC API
    description: Open Database Connectivity (ODBC) is a standard C-language API for accessing database management systems. ODBC allows applications to connect to any ODBC-compliant database using a unified programming interface, abstracting database-specific details through drivers. Originally developed by Microsoft and standardized by ISO/IEC in SQL/CLI (Call Level Interface).
    humanUrl: https://learn.microsoft.com/en-us/sql/odbc/reference/odbc-programmer-s-reference
    baseUrl: ''
    tags:
      - Database Connectivity
      - ODBC
      - Standard
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/sql/odbc/reference/odbc-programmer-s-reference
      - type: Wikipedia
        url: https://en.wikipedia.org/wiki/Open_Database_Connectivity
      - type: Specification
        url: https://www.iso.org/standard/53681.html
  - name: JDBC API
    description: Java Database Connectivity (JDBC) is the standard Java API for connecting Java applications to relational databases. JDBC provides a uniform interface for executing SQL queries, managing transactions, and retrieving results, regardless of the underlying database system. It is part of the Java SE standard library.
    humanUrl: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/java/sql/package-summary.html
    baseUrl: ''
    tags:
      - Database Connectivity
      - Java
      - JDBC
      - Standard
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/java/sql/package-summary.html
      - type: Wikipedia
        url: https://en.wikipedia.org/wiki/Java_Database_Connectivity
      - type: Specification
        url: https://jcp.org/en/jsr/detail?id=221
common:
  - type: JSONSchema
    url: json-schema/sql-query-schema.json
  - type: JSONSchema
    url: json-schema/sql-result-schema.json
  - type: JSONLD
    url: json-ld/sql-context.jsonld
  - type: Vocabulary
    url: vocabulary/sql-vocabulary.yml
  - type: ISO Standard
    url: https://www.iso.org/standard/76583.html
  - type: ANSI Standard
    url: https://www.ansi.org/
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/SQL
  - type: W3Schools Tutorial
    url: https://www.w3schools.com/sql/
  - type: MDN Web Docs
    url: https://developer.mozilla.org/en-US/docs/Learn/Server-side/SQL
maintainers:
  - name: ISO/IEC JTC 1/SC 32
    url: https://www.iso.org/committee/45342.html
tags:
  - ANSI Standard
  - Data Management
  - Database
  - ISO Standard
  - Query Language
  - Relational Database
  - SQL
---
