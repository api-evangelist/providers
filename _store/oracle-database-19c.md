---
aid: oracle-database-19c
url: https://raw.githubusercontent.com/api-evangelist/oracle-database-19c/refs/heads/main/apis.yml
apis:
- name: Oracle REST Data Services (ORDS)
  description: RESTful web services for Oracle Database enabling HTTP access to database resources, SQL queries, and PL/SQL procedures.
  image: https://www.oracle.com/a/ocom/img/sql.svg
  humanURL: https://www.oracle.com/database/technologies/appdev/rest.html
  baseURL: https://example.oracle.com:8443/ords/
  tags:
  - Database
  - Oracle
  - Rest
  - Sql
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/19.2/
  - type: OpenAPI
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/19.2/openapi.json
  - type: Authentication
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/19.2/orddg/developing-REST-applications.html#GUID-6C4B8D2F-A5F0-4E1E-8F9E-8B6F5E9C9F9E
  contact:
  - type: Support
    url: https://support.oracle.com
- name: Oracle Database SODA (Simple Oracle Document Access)
  description: Document-oriented NoSQL-style API for storing, retrieving, and querying JSON documents in Oracle Database.
  image: https://www.oracle.com/a/ocom/img/sql.svg
  humanURL: https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/
  baseURL: https://example.oracle.com:8443/ords/
  tags:
  - Document-Store
  - Json
  - Nosql
  - Oracle
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/rest/
  - type: REST API Guide
    url: https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/rest/adrst/index.html
  - type: Tutorial
    url: https://oracle.github.io/json-in-db/
- name: Oracle SQL Developer Web
  description: Browser-based interface for Oracle Database providing SQL worksheet, data modeler, and database administration capabilities.
  image: https://www.oracle.com/a/ocom/img/sql.svg
  humanURL: https://www.oracle.com/database/technologies/appdev/sql-developer-web.html
  baseURL: https://example.oracle.com:8443/ords/sql-developer/
  tags:
  - Administration
  - Development
  - Sql
  - Web-Interface
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/sql-developer-web/
  - type: Getting Started
    url: https://docs.oracle.com/en/database/oracle/sql-developer-web/sdwad/
- name: Oracle Database API for MongoDB
  description: MongoDB-compatible API allowing MongoDB applications to connect to Oracle Database.
  image: https://www.oracle.com/a/ocom/img/sql.svg
  humanURL: https://www.oracle.com/database/mongodb-api/
  baseURL: mongodb://example.oracle.com:27017/
  tags:
  - Compatibility
  - Document-Store
  - Mongodb
  - Nosql
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/mongodb-api/
  - type: Quick Start
    url: https://www.oracle.com/database/mongodb-api/quickstart.html
- name: Oracle Database JSON Collections API
  description: RESTful API for managing JSON document collections with CRUD operations.
  image: https://www.oracle.com/a/ocom/img/sql.svg
  humanURL: https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/
  baseURL: https://example.oracle.com:8443/ords/
  tags:
  - Collections
  - Document-Api
  - Json
  - Rest
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/json-collections.html
  - type: Developer Guide
    url: https://docs.oracle.com/en/database/oracle/oracle-database/19/adjsn/
- name: Oracle Database REST API for AutoML
  description: REST APIs for Oracle Machine Learning AutoML capabilities including model building and deployment.
  image: https://www.oracle.com/a/ocom/img/sql.svg
  humanURL: https://docs.oracle.com/en/database/oracle/machine-learning/
  baseURL: https://example.oracle.com:8443/omlmod/
  tags:
  - Ai
  - Analytics
  - Automl
  - Machine-Learning
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/machine-learning/oml4sql/19/
  - type: API Reference
    url: https://docs.oracle.com/en/cloud/paas/autonomous-database/omlug/rest-endpoints.html
name: Oracle Database 19c
tags:
- Database
- Enterprise
- Json
- Machine-Learning
- Nosql
- Oracle
- Rest
- Sql
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Database 19c is a multi-model database management system that provides a comprehensive platform for enterprise data management, analytics, and application development.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

