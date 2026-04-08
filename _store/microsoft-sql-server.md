---
aid: microsoft-sql-server
url: https://raw.githubusercontent.com/api-evangelist/microsoft-sql-server/refs/heads/main/apis.yml
apis:
- name: SQL Server Database Engine API
  description: Core database engine APIs for querying, managing, and administering SQL Server databases.
  image: https://www.microsoft.com/sql-server/database-engine-logo.png
  humanURL: https://docs.microsoft.com/sql/sql-server/
  baseURL: https://your-server.database.windows.net
  tags:
  - Database
  - Query
  - Transact-SQL
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/sql/sql-server/sql-server-technical-documentation
  - type: OpenAPI
    url: https://docs.microsoft.com/sql/connect/
  - type: Authentication
    url: https://docs.microsoft.com/sql/relational-databases/security/authentication-access/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
    url: https://support.microsoft.com/sql
- name: SQL Server Management Objects (SMO) API
  description: .NET API for managing and administering SQL Server programmatically.
  humanURL: https://docs.microsoft.com/sql/relational-databases/server-management-objects-smo/
  baseURL: https://api.example.com/smo
  tags:
  - .NET
  - Administration
  - Management
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/sql/relational-databases/server-management-objects-smo/overview-smo
  - type: SDK
    url: https://www.nuget.org/packages/Microsoft.SqlServer.SqlManagementObjects
  - type: Code Samples
    url: https://docs.microsoft.com/sql/relational-databases/server-management-objects-smo/create-program/
- name: Azure SQL Database REST API
  description: REST API for managing Azure SQL Database resources and configurations.
  humanURL: https://learn.microsoft.com/en-us/rest/api/sql/
  baseURL: https://management.azure.com
  tags:
  - Azure
  - Cloud
  - Database Management
  - REST API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/sql/
  - type: OpenAPI
    url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/sql
  - type: Authentication
    url: https://docs.microsoft.com/azure/active-directory/develop/
  - type: Pricing
    url: https://azure.microsoft.com/pricing/details/sql-database/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/rest/api/sql/rest-api-sql-create-or-update-database
  contact:
  - FN: Azure Support
    email: azuresupport@microsoft.com
    url: https://azure.microsoft.com/support/
- name: SQL Server Reporting Services (SSRS) API
  description: REST API for managing reports, subscriptions, and data sources in SQL Server Reporting Services.
  humanURL: https://docs.microsoft.com/sql/reporting-services/
  baseURL: https://your-server/reports/api/v2.0
  tags:
  - Business Intelligence
  - Reporting
  - REST API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/reporting-services/developer/rest-api
  - type: OpenAPI
    url: https://app.swaggerhub.com/apis/microsoft-rs/SSRS/2.0
  - type: Tutorial
    url: https://docs.microsoft.com/sql/reporting-services/tutorial-access-rest-api
  - type: APIReference
    url: https://learn.microsoft.com/en-us/rest/api/sql-server-reporting/
- name: SQL Server Integration Services (SSIS) Catalog API
  description: API for managing SSIS packages, projects, and execution in the SSIS Catalog.
  humanURL: https://docs.microsoft.com/sql/integration-services/
  baseURL: https://your-server/SSISDB
  tags:
  - Data Pipeline
  - ETL
  - Integration
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/sql/integration-services/service/package-management-ssis-service
  - type: Stored Procedures
    url: https://docs.microsoft.com/sql/integration-services/system-stored-procedures/
- name: Azure SQL Managed Instance REST API
  description: REST API for creating, configuring, and managing Azure SQL Managed Instances including databases, operations, and scheduling.
  humanURL: https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/api-references-create-manage-instance
  baseURL: https://management.azure.com
  tags:
  - Azure
  - Cloud
  - Database Management
  - Managed Instance
  - REST API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/api-references-create-manage-instance
  - type: APIReference
    url: https://learn.microsoft.com/en-us/rest/api/sql/managed-instances
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/instance-create-quickstart
  - type: Pricing
    url: https://azure.microsoft.com/pricing/details/azure-sql-managed-instance/
- name: Data API Builder
  description: Open source configuration-based engine that creates REST and GraphQL APIs for SQL Server, Azure SQL, Azure Cosmos DB, PostgreSQL, and MySQL databases.
  humanURL: https://learn.microsoft.com/en-us/azure/data-api-builder/overview
  baseURL: https://localhost:5000/api
  tags:
  - CRUD
  - Data Access
  - GraphQL
  - Open Source
  - REST API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/data-api-builder/
  - type: SourceCode
    url: https://github.com/Azure/data-api-builder
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/data-api-builder/overview
- name: Azure Analysis Services REST API
  description: REST API for managing Azure Analysis Services resources and performing asynchronous data refreshes of tabular models.
  humanURL: https://learn.microsoft.com/en-us/rest/api/analysisservices/
  baseURL: https://management.azure.com
  tags:
  - Analysis Services
  - Azure
  - Business Intelligence
  - REST API
  - Tabular Models
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/analysisservices/
  - type: ClientLibraries
    url: https://learn.microsoft.com/en-us/analysis-services/client-libraries
  - type: TMSLReference
    url: https://learn.microsoft.com/en-us/analysis-services/tmsl/tabular-model-scripting-language-tmsl-reference
- name: Microsoft SqlClient Data Provider (ADO.NET)
  description: ADO.NET data provider for .NET Framework and .NET Core used for connecting to SQL Server, executing commands, and retrieving results.
  humanURL: https://learn.microsoft.com/en-us/sql/connect/ado-net/overview-sqlclient-driver
  tags:
  - .NET
  - ADO.NET
  - Data Provider
  - SqlClient
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/ado-net/overview-sqlclient-driver
  - type: APIReference
    url: https://learn.microsoft.com/en-us/dotnet/api/microsoft.data.sqlclient
  - type: SDK
    url: https://www.nuget.org/packages/Microsoft.Data.SqlClient
  - type: Download
    url: https://learn.microsoft.com/en-us/sql/connect/ado-net/download-microsoft-sqlclient-data-provider
- name: Microsoft JDBC Driver for SQL Server
  description: Type 4 JDBC driver providing database connectivity to SQL Server through standard JDBC application program interfaces on the Java platform.
  humanURL: https://learn.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server
  tags:
  - Cross-Platform
  - Driver
  - Java
  - JDBC
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server
  - type: APIReference
    url: https://learn.microsoft.com/en-us/sql/connect/jdbc/reference/jdbc-driver-api-reference
  - type: Download
    url: https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server
  - type: SourceCode
    url: https://github.com/microsoft/mssql-jdbc
- name: Microsoft ODBC Driver for SQL Server
  description: ODBC driver providing native-code API connectivity to SQL Server and Azure SQL Database for applications on Windows, Linux, and macOS.
  humanURL: https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server
  tags:
  - Cross-Platform
  - Driver
  - Native Code
  - ODBC
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server
  - type: Download
    url: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
- name: Microsoft OLE DB Driver for SQL Server
  description: Stand-alone OLE DB data access API for low-level COM components requiring high-performance access to SQL Server.
  humanURL: https://learn.microsoft.com/en-us/sql/connect/oledb/oledb-driver-for-sql-server
  tags:
  - COM
  - Driver
  - OLE DB
  - Windows
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/oledb/oledb-driver-for-sql-server
  - type: ProgrammingGuide
    url: https://learn.microsoft.com/en-us/sql/connect/oledb/ole-db/oledb-driver-for-sql-server-programming
  - type: Download
    url: https://learn.microsoft.com/en-us/sql/connect/oledb/download-oledb-driver-for-sql-server
- name: Microsoft Python Driver for SQL Server (mssql-python)
  description: Python driver using Direct Database Connectivity for direct connections to SQL Server without requiring an external driver manager, compliant with Python DB-API 2.0.
  humanURL: https://learn.microsoft.com/en-us/sql/connect/python/mssql-python/python-sql-driver-mssql-python
  tags:
  - Cross-Platform
  - DB-API
  - Driver
  - Python
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/python/mssql-python/python-sql-driver-mssql-python
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/sql/connect/python/mssql-python/python-sql-driver-mssql-python-quickstart
  - type: SourceCode
    url: https://github.com/microsoft/mssql-python
  - type: SDK
    url: https://pypi.org/project/mssql-python/
- name: Node.js Driver for SQL Server (tedious)
  description: Open-source JavaScript implementation of the TDS protocol for connecting to SQL Server from Node.js on Windows, Linux, or macOS.
  humanURL: https://learn.microsoft.com/en-us/sql/connect/node-js/node-js-driver-for-sql-server
  tags:
  - Cross-Platform
  - Driver
  - JavaScript
  - Node.js
  - TDS
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/node-js/node-js-driver-for-sql-server
  - type: SourceCode
    url: https://github.com/tediousjs/tedious
  - type: SDK
    url: https://www.npmjs.com/package/mssql
name: Microsoft SQL Server
tags:
- Cloud
- Data Management
- Database
- Enterprise
- Relational Database
- SQL
type: Contract
image: https://www.microsoft.com/sql-server/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A relational database management system developed by Microsoft for enterprise-scale data management and business intelligence solutions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

