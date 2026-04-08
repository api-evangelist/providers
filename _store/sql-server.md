---
aid: sql-server
url: https://raw.githubusercontent.com/api-evangelist/sql-server/refs/heads/main/apis.yml
apis:
- name: SQL Server Database Engine API
  description: Native database engine APIs for connecting and executing queries against SQL Server.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/sql/sql-server/
  baseURL: ''
  tags:
  - Database Engine
  - Query Execution
  - T-SQL
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sql/connect/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/sql/sql-server/educational-sql-resources
  - type: OpenAPI
    url: ''
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: SQL Server REST API
  description: REST API for managing SQL Server resources in Azure.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/rest/api/sql/
  baseURL: https://management.azure.com
  tags:
  - Azure
  - Cloud
  - Management
  - REST
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/rest/api/sql/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/sql/resource-manager/Microsoft.Sql/stable/2021-11-01/sql.json
  - type: Swagger
    url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/sql
  contact:
  - FN: Azure Support
    email: azuresupport@microsoft.com
- name: SQL Server Management Objects (SMO)
  description: .NET API for programmatically managing SQL Server instances and databases.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/sql/relational-databases/server-management-objects-smo/
  baseURL: ''
  tags:
  - .NET
  - Automation
  - Management
  - SMO
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sql/relational-databases/server-management-objects-smo/
  - type: NuGet Package
    url: https://www.nuget.org/packages/Microsoft.SqlServer.SqlManagementObjects/
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: SQL Server Reporting Services (SSRS) API
  description: REST API for managing and accessing SQL Server Reporting Services.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/sql/reporting-services/
  baseURL: http://localhost/reports/api/v2.0
  tags:
  - Business Intelligence
  - Reporting
  - REST
  - SSRS
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sql/reporting-services/developer/rest-api
  - type: OpenAPI
    url: ''
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: ODBC Driver for SQL Server
  description: ODBC driver API for connecting applications to SQL Server.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/sql/connect/odbc/
  baseURL: ''
  tags:
  - Connectivity
  - Cross-Platform
  - Driver
  - ODBC
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server
  - type: Download
    url: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: JDBC Driver for SQL Server
  description: JDBC driver for connecting Java applications to SQL Server.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/sql/connect/jdbc/
  baseURL: ''
  tags:
  - Connectivity
  - Driver
  - Java
  - JDBC
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server
  - type: Download
    url: https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server
  - type: GitHub
    url: https://github.com/microsoft/mssql-jdbc
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: SQL Server Analysis Services (SSAS) API
  description: APIs for managing and querying SQL Server Analysis Services.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/analysis-services/
  baseURL: ''
  tags:
  - Analysis
  - Business Intelligence
  - OLAP
  - SSAS
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/analysis-services/instances/analysis-services-instance-management
  - type: PowerShellModule
    url: https://docs.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Azure SQL Database REST API
  description: REST API for managing Azure SQL Database resources.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://docs.microsoft.com/en-us/azure/azure-sql/database/
  baseURL: https://management.azure.com
  tags:
  - Azure
  - Cloud
  - PaaS
  - REST
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/rest/api/sql/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/sql/resource-manager/Microsoft.Sql/stable/2021-11-01/databases.json
  contact:
  - FN: Azure Support
    email: azuresupport@microsoft.com
- name: Azure SQL Managed Instance REST API
  description: REST API for creating, configuring, and managing Azure SQL Managed Instances.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/
  baseURL: https://management.azure.com
  tags:
  - Azure
  - Cloud
  - Managed Instance
  - PaaS
  - REST
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/sql/managed-instances
  - type: APIReference
    url: https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/api-references-create-manage-instance
  contact:
  - FN: Azure Support
    email: azuresupport@microsoft.com
- name: SQL Server External REST Endpoint Invocation
  description: Native T-SQL stored procedure sp_invoke_external_rest_endpoint for calling external HTTPS REST endpoints directly from SQL Server 2025 and Azure SQL.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql
  baseURL: ''
  tags:
  - External Endpoints
  - Integration
  - REST
  - SQL Server 2025
  - T-SQL
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Data API Builder for SQL Server
  description: Open-source tool that generates REST and GraphQL endpoints for SQL Server and Azure SQL databases from configuration, without writing custom API code.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/azure/data-api-builder/
  baseURL: ''
  tags:
  - Azure
  - Data API
  - GraphQL
  - Open Source
  - REST
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/data-api-builder/overview
  - type: GitHub
    url: https://github.com/Azure/data-api-builder
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: ADO.NET Provider for SQL Server (Microsoft.Data.SqlClient)
  description: The official .NET data provider for Microsoft SQL Server and Azure SQL databases, providing ADO.NET access to SQL Server.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/connect/ado-net/microsoft-ado-net-sql-server
  baseURL: ''
  tags:
  - .NET
  - ADO.NET
  - Connectivity
  - Driver
  - SqlClient
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/ado-net/introduction-microsoft-data-sqlclient-namespace
  - type: NuGetPackage
    url: https://www.nuget.org/packages/Microsoft.Data.SqlClient
  - type: Download
    url: https://learn.microsoft.com/en-us/sql/connect/ado-net/download-microsoft-sqlclient-data-provider
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: OLE DB Driver for SQL Server
  description: Stand-alone OLE DB data access API for connecting applications to SQL Server.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/connect/oledb/oledb-driver-for-sql-server
  baseURL: ''
  tags:
  - Connectivity
  - Driver
  - OLE DB
  - Windows
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/oledb/oledb-driver-for-sql-server
  - type: Download
    url: https://learn.microsoft.com/en-us/sql/connect/oledb/download-oledb-driver-for-sql-server
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: SQL Server Integration Services (SSIS) API
  description: Programmable object model for building, managing, and executing ETL data integration packages in SQL Server.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services
  baseURL: ''
  tags:
  - Automation
  - Data Integration
  - ETL
  - SSIS
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Node.js Driver for SQL Server
  description: Node.js driver (tedious/mssql) for connecting JavaScript and TypeScript applications to SQL Server and Azure SQL Database.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/connect/node-js/node-js-driver-for-sql-server
  baseURL: ''
  tags:
  - Connectivity
  - Driver
  - JavaScript
  - Node.js
  - Npm
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/node-js/node-js-driver-for-sql-server
  - type: GitHub
    url: https://github.com/tediousjs/node-mssql
  - type: npmPackage
    url: https://www.npmjs.com/package/mssql
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Python Drivers for SQL Server
  description: Python drivers for connecting to SQL Server including the first-party mssql-python driver, pyodbc, and pymssql.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server
  baseURL: ''
  tags:
  - Connectivity
  - Driver
  - Pymssql
  - Pyodbc
  - Python
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/python/mssql-python/python-sql-driver-mssql-python
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Go Driver for SQL Server
  description: Microsoft Go driver (go-mssqldb) for connecting Go applications to SQL Server and Azure SQL Database using the TDS protocol.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/connect/golang/microsoft-go-mssqldb-driver
  baseURL: ''
  tags:
  - Connectivity
  - Driver
  - Go
  - Golang
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/golang/microsoft-go-mssqldb-driver
  - type: GitHub
    url: https://github.com/microsoft/go-mssqldb
  - type: GoPackage
    url: https://pkg.go.dev/github.com/microsoft/go-mssqldb
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: PHP Drivers for SQL Server
  description: Microsoft Drivers for PHP for SQL Server providing SQLSRV and PDO_SQLSRV extensions for connecting PHP applications to SQL Server.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/connect/php/microsoft-php-driver-for-sql-server
  baseURL: ''
  tags:
  - Connectivity
  - Driver
  - PDO
  - PHP
  - SQLSRV
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/php/microsoft-php-driver-for-sql-server
  - type: GitHub
    url: https://github.com/microsoft/msphpsql
  - type: Download
    url: https://learn.microsoft.com/en-us/sql/connect/php/download-drivers-php-sql-server
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Ruby Driver for SQL Server
  description: Ruby driver (TinyTDS) for connecting Ruby applications to SQL Server using FreeTDS DB-Library bindings.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/sql/connect/ruby/step-3-proof-of-concept-connecting-to-sql-using-ruby
  baseURL: ''
  tags:
  - Connectivity
  - Driver
  - Ruby
  - TinyTDS
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sql/connect/ruby/step-3-proof-of-concept-connecting-to-sql-using-ruby
  - type: GitHub
    url: https://github.com/rails-sqlserver/tiny_tds
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Entity Framework Core SQL Server Provider
  description: Entity Framework Core database provider enabling .NET object-relational mapping with SQL Server and Azure SQL databases.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/ef/core/providers/sql-server/
  baseURL: ''
  tags:
  - .NET
  - Driver
  - Entity Framework
  - ORM
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/ef/core/providers/sql-server/
  - type: NuGetPackage
    url: https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.SqlServer
  - type: GitHub
    url: https://github.com/dotnet/efcore
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: SQL Server PowerShell Module
  description: PowerShell cmdlets for managing SQL Server instances, databases, and resources from the command line.
  image: https://www.microsoft.com/sql-server/images/sql-server-logo.png
  humanURL: https://learn.microsoft.com/en-us/powershell/module/sqlserver/
  baseURL: ''
  tags:
  - Automation
  - CLI
  - Management
  - PowerShell
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/powershell/module/sqlserver/
  - type: Download
    url: https://learn.microsoft.com/en-us/powershell/sql-server/download-sql-server-ps-module
  - type: GitHub
    url: https://github.com/microsoft/SQLServerPSModule
  - type: PowerShellGallery
    url: https://www.powershellgallery.com/packages/SqlServer
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
name: Microsoft SQL Server APIs
tags:
- Azure SQL
- Cloud Database
- Data Management
- Database
- Microsoft
- Relational Database
- SQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs and interfaces for interacting with Microsoft SQL Server.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

