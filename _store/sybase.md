---
aid: sybase
url: https://raw.githubusercontent.com/api-evangelist/sybase/refs/heads/main/apis.yml
apis:
- name: Sybase ASE REST API
  description: REST API for Sybase Adaptive Server Enterprise administration and monitoring.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_ASE
  baseURL: https://api.sybase.example.com/ase/v1
  tags:
  - Administration
  - Database Management
  - Monitoring
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_ASE/REST_API
  - type: OpenAPI
    url: https://api.sybase.example.com/ase/v1/openapi.json
  - type: Authentication
    url: https://help.sap.com/docs/SAP_ASE/authentication
  - type: Change Log
    url: https://help.sap.com/docs/SAP_ASE/791c41982ee345a19c4ec4b774222c4f/5db753f3a9c24ddcabc2581a98b99585.html
- name: Sybase IQ REST API
  description: REST API for SAP IQ (formerly Sybase IQ) analytics database.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_IQ
  baseURL: https://api.sybase.example.com/iq/v1
  tags:
  - Analytics
  - Big Data
  - Data Warehouse
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_IQ/REST_API
  - type: OpenAPI
    url: https://api.sybase.example.com/iq/v1/openapi.json
- name: SAP Mobile Platform API
  description: APIs for Sybase mobile application development and management.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_MOBILE_PLATFORM
  baseURL: https://api.sybase.example.com/mobile/v1
  tags:
  - Application Development
  - Mobile
  - Synchronization
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_MOBILE_PLATFORM/API
  - type: SDK
    url: https://help.sap.com/docs/SAP_MOBILE_PLATFORM/SDK
- name: SAP SQL Anywhere HTTP Web Services
  description: SAP SQL Anywhere includes a built-in HTTP web server that exposes database objects as OData and REST web services. Developers can create SERVICE objects that transform SQL query results into XML, HTML, and JSON formats, and database tables and views can be automatically exposed via an OData producer.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_SQL_Anywhere
  baseURL: https://{server}:{port}
  tags:
  - Database
  - Embedded Database
  - OData
  - Web Services
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_SQL_Anywhere
  - type: Reference
    url: https://help.sap.com/docs/SAP_SQL_Anywhere/98ad9ec940e2465695685d98e308dff5/8e8c9049a1fe448a820c5f5bc72119e7.html
  - type: Getting Started
    url: https://dcx.sap.com/
- name: SDK for SAP ASE
  description: The SDK for SAP Adaptive Server Enterprise is a set of libraries and utilities for developing client applications. It includes SAP Open Client for C-language applications, Embedded SQL precompilers for C and COBOL, the ASE ODBC driver, ASE ADO.NET Data Provider, and jConnect for JDBC.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_ASE_SDK
  baseURL: https://{server}:{port}
  tags:
  - Client Libraries
  - Database Connectivity
  - JDBC
  - ODBC
  - SDK
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_ASE_SDK
  - type: Reference
    url: https://help.sap.com/docs/SAP_ASE_SDK/882ef48c7e9c4d6e845d98f34378db40/b21b7c31bbf91014ae38f7f5cc782b0b.html
  - type: Getting Started
    url: https://help.sap.com/docs/SAP_ASE_SDK/e12c539de04b44a0bb17a545a148361c/0d968d9bcca6462f9414cf6010088af9.html
- name: SAP Replication Server
  description: SAP Replication Server provides real-time data replication between SAP ASE databases and heterogeneous data sources. It uses Replication Command Language (RCL) to manage replication definitions, publications, and subscriptions for table and stored procedure replication.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_REPLICATION_SERVER
  baseURL: https://{server}:{port}
  tags:
  - Data Synchronization
  - High Availability
  - Replication
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_REPLICATION_SERVER
  - type: Reference
    url: https://help.sap.com/doc/efc57020a2914d40af14c48e08bfd01f/16.0.4.3/en-US/Replication_Server_Reference_Manual_en.pdf
  - type: Getting Started
    url: https://help.sap.com/doc/1699d891ffc746babeaf700da051f89e/16.0.4.1/en-US/SAP_RS_Quick_Start_ASE_en.pdf
- name: SAP ASE Cockpit
  description: SAP ASE Cockpit is a web-based administration and management console for SAP Adaptive Server Enterprise. It provides monitoring, configuration, and management capabilities for ASE servers through a browser-based interface, replacing the earlier Adobe Flash-based console starting with ASE 16.0 SP04.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_ASE/9623e59098a24dc6b9013ba5d709309e/13ec24bd751e1014bf789ad719f1de31.html
  baseURL: https://{server}:{port}
  tags:
  - Administration
  - Management Console
  - Monitoring
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_ASE/9623e59098a24dc6b9013ba5d709309e/13ec24bd751e1014bf789ad719f1de31.html
  - type: Getting Started
    url: https://blogs.sap.com/2018/02/18/first-steps-with-sap-ase-cockpit/
name: Sybase
tags:
- Database
- Enterprise
- SAP
- SQL
type: Contract
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs and resources for Sybase database systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

