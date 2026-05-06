---
aid: oracle-database
name: Oracle Database
description: APIs and interfaces for Oracle Database management, querying, and administration.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-20'
modified: '2026-04-28'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/oracle-database/refs/heads/main/apis.yml
apis:
  - name: Oracle REST Data Services (ORDS)
    description: RESTful API development and data access for Oracle Database.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://www.oracle.com/database/technologies/appdev/rest.html
    baseUrl: https://example.oracle.com/ords/
    tags:
      - Data Access
      - Database
      - REST
      - SQL
    properties:
      - type: OpenAPI
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/latest/
      - type: Swagger
        url: https://example.oracle.com/ords/metadata-catalog/
      - type: OpenAPI
        url: openapi/oracle-database-ords-openapi.yml
      - type: JSONSchema
        url: json-schema/oracle-database-table.json
      - type: JSONSchema
        url: json-schema/oracle-database-pluggable-database.json
      - type: JSONLD
        url: json-ld/oracle-database-context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Database API for MongoDB
    description: MongoDB-compatible API for Oracle Database.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://www.oracle.com/database/mongodb-api/
    baseUrl: https://example.oracle.com:27017/
    tags:
      - Database
      - JSON
      - MongoDB
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/mongodb-api/
      - type: Getting Started
        url: https://www.oracle.com/database/mongodb-api/get-started/
    contact:
      - FN: Oracle Support
        email: support@oracle.com
  - name: Oracle Cloud Infrastructure Database API
    description: API for managing Oracle Database services in Oracle Cloud Infrastructure.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://docs.oracle.com/iaas/database/
    baseUrl: https://database.{region}.oraclecloud.com/
    tags:
      - Autonomous Database
      - Cloud
      - Database Management
      - Infrastructure
    properties:
      - type: OpenAPI
        url: https://docs.oracle.com/iaas/api/#/en/database/
      - type: Documentation
        url: https://docs.oracle.com/iaas/Content/Database/home.htm
      - type: SDK
        url: https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm
      - type: API Reference
        url: https://docs.oracle.com/iaas/api/#/en/database/20160918/
      - type: OpenAPI
        url: openapi/oracle-database-oci-openapi.yml
      - type: JSONSchema
        url: json-schema/oracle-database-autonomous-database.json
      - type: JSONSchema
        url: json-schema/oracle-database-pluggable-database.json
      - type: JSONLD
        url: json-ld/oracle-database-context.jsonld
    contact:
      - FN: Oracle Cloud Support
        email: cloud-support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Database JDBC
    description: Java Database Connectivity API for Oracle Database.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://www.oracle.com/database/technologies/appdev/jdbc.html
    tags:
      - Database Driver
      - Java
      - JDBC
      - SQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-database/21/jjdbc/
      - type: Downloads
        url: https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html
      - type: GitHub
        url: https://github.com/oracle/oracle-db-examples/tree/master/java
  - name: Oracle Call Interface (OCI)
    description: C/C++ API for Oracle Database access.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://www.oracle.com/database/technologies/appdev/oci.html
    tags:
      - C
      - C++
      - Database Driver
      - Native API
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnoci/
      - type: Programming Guide
        url: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnoci/introduction.html
  - name: Oracle SQL Developer REST API
    description: RESTful services for Oracle SQL Developer.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://www.oracle.com/database/sqldeveloper/
    tags:
      - Development Tools
      - REST
      - SQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/sql-developer/
      - type: User Guide
        url: https://docs.oracle.com/en/database/oracle/sql-developer/latest/
  - name: Oracle SODA (Simple Oracle Document Access)
    description: NoSQL-style document API for Oracle Database.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/
    tags:
      - Document Database
      - JSON
      - NoSQL
      - REST
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/
      - type: REST API
        url: https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/rest/
      - type: Java API
        url: https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/java/
      - type: OpenAPI
        url: openapi/oracle-database-soda-openapi.yml
      - type: JSONSchema
        url: json-schema/oracle-database-document.json
      - type: JSONSchema
        url: json-schema/oracle-database-collection.json
      - type: JSONLD
        url: json-ld/oracle-database-context.jsonld
  - name: Oracle Transactional Event Queues (TxEventQ)
    description: Kafka-compatible event streaming and message queuing built into Oracle Database.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanUrl: https://docs.oracle.com/en/database/oracle/oracle-database/23/adque/
    baseUrl: https://example.oracle.com/ords/{schema}/database/txeventq/
    tags:
      - Event Streaming
      - Kafka
      - Messaging
      - Pub/Sub
      - Queues
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-database/23/adque/
      - type: AsyncAPI
        url: asyncapi/oracle-database-txeventq-asyncapi.yml
      - type: JSONSchema
        url: json-schema/oracle-database-event-message.json
      - type: JSONLD
        url: json-ld/oracle-database-context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://www.oracle.com/database/technologies/appdev.html
  - type: Documentation
    url: https://docs.oracle.com/en/database/oracle/oracle-database/
  - type: Getting Started
    url: https://www.oracle.com/database/technologies/appdev/quickstartsandtutorials.html
  - type: Support
    url: https://www.oracle.com/support/
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: Blog
    url: https://blogs.oracle.com/database/
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
  - type: Website
    url: https://www.oracle.com/database/
  - type: Console
    url: https://cloud.oracle.com/
  - type: Sign Up
    url: https://signup.cloud.oracle.com/
  - type: GitHub Organization
    url: https://github.com/oracle
  - type: Community
    url: https://forums.oracle.com/ords/apexds/domain/dev-community
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/oracle
  - type: YouTube
    url: https://www.youtube.com/user/Oracle
  - type: Pricing
    url: https://www.oracle.com/database/technologies/oracle-database-pricing.html
tags:
  - Cloud
  - Database
  - Enterprise
  - Oracle
  - REST API
  - SQL
---
