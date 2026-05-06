---
aid: oracle-e-business-suite
name: Oracle E-Business Suite
description: A collection of APIs for Oracle E-Business Suite (EBS), Oracle's comprehensive suite of integrated, global business applications that supports today's evolving business models across financials, human capital management, supply chain, and manufacturing.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Business Applications
  - E-Business Suite
  - Enterprise
  - ERP
  - Oracle
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/oracle-e-business-suite/refs/heads/main/apis.yml
apis:
  - name: Oracle EBS Integrated SOA Gateway REST API
    description: RESTful web services for Oracle E-Business Suite modules exposed through the Integrated SOA Gateway (ISG). PL/SQL APIs, Java Bean Services, Application Module Services, and other interface types from the Integration Repository can be deployed as lightweight REST services.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/webservices/rest/
    humanURL: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/T511473T516479.htm
    tags:
      - Enterprise
      - Integration
      - Rest Services
      - Soa Gateway
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
      - type: GettingStarted
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e69284/T660136T660140.htm
      - type: APIReference
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20925/T511175T513043.htm
      - type: OpenAPI
        url: openapi/isg-rest-api.yml
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EBS Integrated SOA Gateway SOAP Web Services
    description: SOAP-based web services for Oracle E-Business Suite exposed through the Integrated SOA Gateway. Supports synchronous and asynchronous interaction patterns for PL/SQL APIs, Concurrent Programs, and Business Service Objects deployed to Oracle SOA Suite.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/webservices/SOAProvider/
    humanURL: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
    tags:
      - Integration
      - Soa Gateway
      - Soap Services
      - Web Services
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
      - type: APIReference
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20923/T291171T291173.htm
      - type: GettingStarted
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20925/T511175T513043.htm
      - type: JSONSchema
        url: json-schema/customer.json
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EBS Financial Services API
    description: APIs for financial management including General Ledger, Accounts Payable, Accounts Receivable, Fixed Assets, and Cash Management. These PL/SQL APIs can be deployed as REST or SOAP services through the Integrated SOA Gateway.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/webservices/rest/
    humanURL: https://docs.oracle.com/cd/E26401_01/index.htm
    tags:
      - Accounting
      - Accounts Payable
      - Financials
      - General Ledger
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
      - type: APIReference
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e22961/toc.htm
      - type: OpenAPI
        url: openapi/financial-services-api.yml
      - type: JSONSchema
        url: json-schema/invoice.json
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EBS Supply Chain Management API
    description: APIs for inventory management, purchasing, order management, and logistics within Oracle E-Business Suite. Provides programmatic access to supply chain operations through PL/SQL interfaces deployable as REST services.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/webservices/rest/
    humanURL: https://docs.oracle.com/cd/E26401_01/index.htm
    tags:
      - Inventory
      - Order Management
      - Purchasing
      - Supply Chain
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
      - type: APIReference
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e22961/toc.htm
      - type: OpenAPI
        url: openapi/supply-chain-api.yml
      - type: JSONSchema
        url: json-schema/purchase-order.json
      - type: JSONSchema
        url: json-schema/supplier.json
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EBS Human Resources API
    description: APIs for human resources management, payroll processing, and workforce administration. Oracle HRMS provides PL/SQL packaged procedures and functions that serve as an open interface for managing employee data, compensation, and benefits.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/webservices/rest/
    humanURL: https://docs.oracle.com/cd/E26401_01/nav/hcm.htm
    tags:
      - Human Capital
      - Human Resources
      - Payroll
      - Workforce Management
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
      - type: APIReference
        url: https://docs.oracle.com/cd/E26401_01/nav/hcm.htm
      - type: OpenAPI
        url: openapi/human-resources-api.yml
      - type: JSONSchema
        url: json-schema/employee.json
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EBS Manufacturing API
    description: APIs for discrete and process manufacturing operations including Bills of Material, Work in Process, and Work Orders. Provides programmatic access to manufacturing execution and planning functions within Oracle E-Business Suite.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/webservices/rest/
    humanURL: https://docs.oracle.com/cd/E26401_01/index.htm
    tags:
      - Bills of Material
      - Manufacturing
      - Production
      - Work Orders
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
      - type: APIReference
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e22961/toc.htm
      - type: OpenAPI
        url: openapi/manufacturing-api.yml
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EBS e-Commerce Gateway API
    description: Oracle e-Commerce Gateway provides EDI transaction support enabling Oracle E-Business Suite to exchange traditional Electronic Data Interchange documents with trading partners. Supports ASC X12 and EDIFACT standards through flat ASCII file integration with third-party EDI translators.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/
    humanURL: https://docs.oracle.com/cd/E26401_01/doc.122/e20931/T168264T168267.htm
    tags:
      - Data Interchange
      - E-Commerce
      - Edi
      - Trading Partners
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e20931/T168264T168267.htm
      - type: OpenAPI
        url: openapi/ecommerce-gateway-api.yml
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EBS PL/SQL API Framework
    description: The PL/SQL API framework provides the core programmatic interface to Oracle E-Business Suite database objects. These stored procedures and functions enable data manipulation across all EBS modules and can be published as REST services through the Integration Repository.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    baseURL: https://{instance}.oracle.com/
    humanURL: https://docs.oracle.com/cd/E26401_01/doc.122/e22961/toc.htm
    tags:
      - Database Api
      - Development Framework
      - Pl/Sql
      - Stored Procedures
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e22961/toc.htm
      - type: GettingStarted
        url: https://docs.oracle.com/cd/E26401_01/doc.122/e69284/T660136T660140.htm
      - type: JSONSchema
        url: json-schema/purchase-order.json
      - type: JSONSchema
        url: json-schema/invoice.json
      - type: JSONSchema
        url: json-schema/employee.json
      - type: JSONSchema
        url: json-schema/customer.json
      - type: JSONSchema
        url: json-schema/supplier.json
      - type: JSONLD
        url: json-ld/context.jsonld
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
common:
  - type: Authentication
    url: https://docs.oracle.com/cd/E26401_01/doc.122/e20927/toc.htm
  - type: Portal
    url: https://developer.oracle.com/
  - type: Documentation
    url: https://docs.oracle.com/cd/E26401_01/index.htm
  - type: GettingStarted
    url: https://docs.oracle.com/cd/E26401_01/doc.122/e20925/T511175T513043.htm
  - type: APIReference
    url: https://docs.oracle.com/cd/E26401_01/doc.122/e22961/toc.htm
  - type: Support
    url: https://support.oracle.com
  - type: Blog
    url: https://blogs.oracle.com/ebstech/
  - type: Blog
    url: https://blogs.oracle.com/ebs/
  - type: ChangeLog
    url: https://docs.oracle.com/cd/E26401_01/index.htm
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms/
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: StatusPage
    url: https://ocistatus.oraclecloud.com/
  - type: SignUp
    url: https://signup.cloud.oracle.com/
  - type: Pricing
    url: https://www.oracle.com/applications/ebusiness/
  - type: GitHubOrganization
    url: https://github.com/oracle
  - type: SDK
    url: https://github.com/oracle/oci-java-sdk
    name: Oracle OCI Java SDK
  - type: SDK
    url: https://github.com/oracle/oci-python-sdk
    name: Oracle OCI Python SDK
  - type: SDK
    url: https://github.com/oracle/oci-go-sdk
    name: Oracle OCI Go SDK
  - type: SDK
    url: https://github.com/oracle/oci-dotnet-sdk
    name: Oracle OCI .NET SDK
  - type: CLI
    url: https://github.com/oracle/oci-cli
    name: Oracle OCI CLI
  - type: Features
    data:
      - Financial management (GL, AP, AR, FA, Cash Management)
      - Supply chain management (Purchasing, Inventory, Order Management)
      - Human capital management (HR, Payroll, Benefits)
      - Manufacturing (Discrete, Process, WIP, BOM)
      - EDI transaction processing via e-Commerce Gateway
      - RESTful API access through Integrated SOA Gateway
      - PL/SQL API framework for programmatic data access
      - Multi-org and multi-currency support
  - type: UseCases
    data:
      - Automate financial close and journal posting
      - Integrate procurement and purchase order workflows
      - Manage employee lifecycle and payroll processing
      - Track manufacturing work orders and material usage
      - Exchange EDI documents with trading partners
      - Build custom integrations via REST and SOAP services
      - Synchronize EBS data with external systems
  - type: Integrations
    data:
      - Oracle SOA Suite for service orchestration
      - Oracle Integration Cloud for hybrid integration
      - EDI translators for ASC X12 and EDIFACT standards
      - Oracle BI Publisher for reporting
      - Oracle Identity Management for SSO
      - Third-party middleware via REST and SOAP APIs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
