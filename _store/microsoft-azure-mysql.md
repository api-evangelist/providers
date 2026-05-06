---
name: Azure Database for MySQL
description: Azure Database for MySQL is a fully managed relational database service based on the open-source MySQL community edition. Its REST APIs enable management of flexible servers, single servers, databases, firewall and network rules, configurations, replicas, and backups with built-in high availability and automated backups.
image: https://azure.microsoft.com/svghandler/mysql/
tags:
  - Database
  - Flexible Server
  - Managed Database
  - MySQL
  - Open Source
  - Relational Database
created: '2026-03-13'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/mysql/
specificationVersion: '0.18'
apis:
  - name: Azure Database for MySQL Flexible Servers API
    description: Create and manage MySQL Flexible Servers, including SKU, storage, networking, high availability mode, maintenance windows, and identity. Flexible Server provides granular control and zone redundant high availability for production workloads.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/servers
    baseURL: https://management.azure.com
    tags:
      - Flexible Server
      - High Availability
      - MySQL
      - Server Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/servers
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal
  - name: Azure Database for MySQL Databases API
    description: Create, list, retrieve, and delete databases hosted on a MySQL Flexible Server. Manage character sets and collations for each database within a server.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/databases
    baseURL: https://management.azure.com
    tags:
      - Charset
      - Collation
      - Database
      - MySQL
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/databases
  - name: Azure Database for MySQL Firewall Rules API
    description: Create and manage server-level firewall rules to grant access to a MySQL Flexible Server from specified client IP address ranges. Required for clients connecting from outside the Azure network.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/firewall-rules
    baseURL: https://management.azure.com
    tags:
      - Access Control
      - Firewall Rules
      - IP Allowlist
      - Networking
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/firewall-rules
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-networking
  - name: Azure Database for MySQL Configurations API
    description: Manage server parameters (configurations) for a MySQL Flexible Server. Adjust MySQL engine variables such as character_set_server, time_zone, and innodb_buffer_pool_size to tune performance and behavior.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/configurations
    baseURL: https://management.azure.com
    tags:
      - Configuration
      - Parameters
      - Server Settings
      - Tuning
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/configurations
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-server-parameters
  - name: Azure Database for MySQL Replicas API
    description: Manage read replicas for MySQL Flexible Server to scale out read-heavy workloads. Create replicas in the same or different region for performance and read distribution.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/replicas
    baseURL: https://management.azure.com
    tags:
      - Read Replica
      - Replication
      - Scale-Out
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/replicas
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-read-replicas
  - name: Azure Database for MySQL Backups API
    description: List and manage automated backups for MySQL Flexible Servers, including on-demand backup creation, retention configuration, and point-in-time restore operations.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/backups
    baseURL: https://management.azure.com
    tags:
      - Backup
      - Disaster Recovery
      - Point-In-Time Restore
      - Retention
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/backups
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-backup-restore
  - name: Azure Database for MySQL Administrators API
    description: Configure Azure Active Directory administrators for MySQL Flexible Server. Allows tenant users, groups, or service principals to be designated as MySQL administrators for AAD-based authentication.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/azure-ad-administrators
    baseURL: https://management.azure.com
    tags:
      - AAD
      - Administrators
      - Authentication
      - Identity
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/azure-ad-administrators
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-azure-ad-authentication
  - name: Azure Database for MySQL Check Name Availability API
    description: Check whether a proposed MySQL Flexible Server name is available within the Azure global namespace before creating a new server.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/check-name-availability
    baseURL: https://management.azure.com
    tags:
      - Availability
      - Name Validation
      - Provisioning
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/check-name-availability
  - name: Azure Database for MySQL Operations API
    description: List Azure Database for MySQL provider operations available in the subscription, including supported operation types and metadata.
    image: https://azure.microsoft.com/svghandler/mysql/
    humanURL: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/operations
    baseURL: https://management.azure.com
    tags:
      - Operations
      - Provider
      - Resource Provider
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/mysql/flexibleserver/operations
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/mysql/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-csharp
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/mysql/
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/tag/azure-database-for-mysql/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/whats-new
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Website
    url: https://azure.microsoft.com/en-us/products/mysql
  - type: Login
    url: https://portal.azure.com
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
