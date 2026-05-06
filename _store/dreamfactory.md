---
aid: dreamfactory
url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/apis.yml
apis:
  - aid: dreamfactory:system-api
    name: DreamFactory System API
    tags:
      - Administration
      - Automation
      - Deployment
      - Documentation
      - Generation
      - Security
    humanURL: https://guide.dreamfactory.com/docs/using-the-system-apis/
    baseURL: https://{instance}/api/v2/system
    properties:
      - url: https://guide.dreamfactory.com/docs/using-the-system-apis/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/openapi/dreamfactory-system-api-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/asyncapi/dreamfactory-system-api-asyncapi.yml
        type: AsyncAPI
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/json-schema/dreamfactory-admin.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/json-schema/dreamfactory-app.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/json-schema/dreamfactory-role.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/json-schema/dreamfactory-service.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/json-schema/dreamfactory-user.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/json-ld/dreamfactory-context.jsonld
        type: JSONLD
    description: The DreamFactory System API provides administrative management capabilities for DreamFactory instances. It allows managing services, apps, roles, users, CORS configurations, email templates, environment settings, lookups, rate limits, events, scripts, and more via REST endpoints under /api/v2/system/.
name: DreamFactory
tags:
  - Automation
  - Deployment
  - Documentation
  - Generation
  - Security
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/dreamfactorysoftware
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://www.dreamfactory.com/
    name: DreamFactory | Code Automation for Generating REST APIs
    type: Website
    description: 'null'
  - url: https://docs.dreamfactory.com/?_gl=1*yrriox*_gcl_au*MTgxMzQyMDU4OC4xNzQ5MTM5NjA0
    name: DreamFactory Docs | DreamFactory Docs
    type: Documentation
    description: 'null'
  - url: https://www.dreamfactory.com/stories
    name: Customer Use Cases | DreamFactory
    type: CaseStudies
    description: 'null'
  - url: https://www.dreamfactory.com/resources/whitepapers
    name: Whitepapers | DreamFactory
    type: WhitePapers
    description: 'null'
  - url: https://blog.dreamfactory.com/
    name: Blog
    type: Blog
    description: 'null'
  - url: https://guide.dreamfactory.com/docs/
    name: Getting Started With DreamFactory | DreamFactory
    type: Guide
    description: 'null'
  - url: https://www.dreamfactory.com/partners
    name: Partners | DreamFactory
    type: Partners
    description: 'null'
  - url: https://www.dreamfactory.com/support
    name: Support Center | DreamFactory
    type: Support
    description: 'null'
  - url: https://www.dreamfactory.com/terms-of-use
    name: Terms of Use | DreamFactory
    type: TermsOfService
    description: 'null'
  - url: https://www.dreamfactory.com/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.dreamfactory.com/features
    name: Features
    type: Features
    data:
      - name: Customer Hosted
      - name: Application Migration
      - name: API Publishing
      - name: Admin Console
      - name: Database API Generation
      - name: Network API Generation
      - name: Expert SQL Support
      - name: Unlimited API Creation
      - name: Unlimited API Volume
      - name: Live API Docs
      - name: Security
      - name: Logging
      - name: Reporting
      - name: Role-Based Access Control (Rbac)
      - name: API Key Management
      - name: Service Side Scripting
      - name: SOAP to REST
  - url: https://www.dreamfactory.com/connectors
    name: Integrations
    type: Integrations
    data:
      - name: Alloydb
      - name: Apache Hive
      - name: AWS S3
      - name: Azure Documentdb
      - name: Azure Table Storage
      - name: Azureblob
      - name: Cassandra
      - name: Cosmosdb
      - name: Couchdb
      - name: Databricks
      - name: Dremio
      - name: Dynamodb
      - name: Firebird
      - name: Ftp/Sftp
      - name: Gridfs
      - name: IBM DB2
      - name: IBM Informix
      - name: Local Storage
      - name: Mariadb
      - name: Mongodb
      - name: Mysql
      - name: Oracle
      - name: Postgresql
      - name: Rackspace Cloud Files
      - name: Redshift
      - name: Salesforce
      - name: Sap SQL Anywhere
      - name: Singlestore
      - name: Snowflake
      - name: SQL Server
      - name: Sqlite
  - name: Use Cases
    type: UseCases
    data:
      - name: API Generation
      - name: API Management
      - name: Api-First Development and Microservices
      - name: Data Centralization
      - name: Data Ingestion
      - name: Data Integration and Migration
      - name: Data Security
      - name: Iot and Device Management
      - name: Legacy System Modernization
      - name: Microservices Architecture
      - name: Mobile and Web App Development
      - name: Restful API Access
      - name: Secure Data Exchange
created: '2025-06-05'
modified: '2026-04-28'
position: Consumer
description: Automate the building, securing, and documenting of REST APIs for data products with built-in enterprise security on bare-metal, VMs, or containers.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
