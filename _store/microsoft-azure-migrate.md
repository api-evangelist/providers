---
name: Azure Migrate
description: Azure Migrate provides a unified platform for discovering, assessing, and migrating on-premises servers, infrastructure, applications, databases, and data to Azure. Its REST APIs enable programmatic management of migration projects, discovery, assessment, and replication workflows for VMs, databases, and web apps.
image: https://azure.microsoft.com/svghandler/azure-migrate/
tags:
  - Assessment
  - Cloud Migration
  - Database Migration
  - Discovery
  - Migration
  - Replication
  - Server Migration
created: '2026-03-13'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/azure-migrate/
specificationVersion: '0.18'
apis:
  - name: Azure Migrate Projects API
    description: Create and manage Azure Migrate projects which serve as the central container for discovery, assessment, and migration activities. Projects group related assessment and migration solutions for a workload.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/rest/api/migrate/projects
    baseURL: https://management.azure.com
    tags:
      - Migrate Project
      - Migration
      - Project Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/migrate/projects
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/migrate/create-manage-projects
  - name: Azure Migrate Assessments API
    description: Create and manage assessments that evaluate on-premises servers and databases for Azure readiness, sizing, and cost. Returns Azure VM readiness, recommended SKUs, monthly cost estimates, and migration compatibility findings.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/rest/api/migrate/assessment
    baseURL: https://management.azure.com
    tags:
      - Assessment
      - Cost Estimation
      - Readiness
      - Sizing
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/migrate/assessment
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/migrate/concepts-assessment-calculation
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/migrate/tutorial-discover-vmware
  - name: Azure Migrate Discovery API
    description: Manage discovery sites and inventory of on-premises servers, databases, and applications. Provides agentless and agent-based discovery for VMware, Hyper-V, and physical servers as a basis for assessment and migration planning.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/rest/api/migrate/discovery
    baseURL: https://management.azure.com
    tags:
      - Agentless
      - Discovery
      - Hyper-V
      - Inventory
      - VMware
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/migrate/discovery
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/migrate/migrate-appliance
  - name: Azure Migrate Server Migration API
    description: Replicate, test migrate, and migrate on-premises servers including VMware, Hyper-V, and physical machines to Azure. Manages replication jobs, fabrics, and protected items used for server migration.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/rest/api/migrate/migration
    baseURL: https://management.azure.com
    tags:
      - Cutover
      - Replication
      - Server Migration
      - Test Migration
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/migrate/migration
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/migrate/tutorial-migrate-vmware
  - name: Azure Database Migration Service API
    description: Streamline the migration of on-premises databases to Azure data platforms with minimal downtime. Supports SQL Server, MySQL, PostgreSQL, MongoDB, and Oracle source databases moving to Azure SQL, Azure Database services, or Cosmos DB.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/rest/api/datamigration
    baseURL: https://management.azure.com
    tags:
      - Database Migration
      - DMS
      - MySQL
      - PostgreSQL
      - SQL Server
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/datamigration
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/dms/dms-overview
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/dms/quickstart-create-data-migration-service-portal
  - name: Azure Migrate Web Apps Assessment API
    description: Discover and assess on-premises ASP.NET and Java web apps running on IIS and Tomcat for migration to Azure App Service. Returns readiness findings, configuration issues, and recommended Azure App Service plans.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/azure/migrate/concepts-azure-webapps-assessment-calculation
    baseURL: https://management.azure.com
    tags:
      - App Service
      - ASP.NET
      - Java
      - Web Apps
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/migrate/how-to-create-azure-app-service-assessment
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/migrate/concepts-azure-webapps-assessment-calculation
  - name: Azure Migrate Data Box API
    description: Order and manage Azure Data Box devices for offline data transfer of large datasets to Azure when network bandwidth is limited or unavailable. Supports Data Box, Data Box Disk, and Data Box Heavy offerings.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/rest/api/databox
    baseURL: https://management.azure.com
    tags:
      - Data Box
      - Offline Transfer
      - Storage Migration
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/databox
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/databox/data-box-overview
  - name: Azure Site Recovery API
    description: Replicate workloads running on physical and virtual machines from a primary site to a secondary location for disaster recovery and migration. Manages recovery vaults, replication policies, protected items, and recovery plans.
    image: https://azure.microsoft.com/svghandler/azure-migrate/
    humanURL: https://learn.microsoft.com/en-us/rest/api/recoveryservices
    baseURL: https://management.azure.com
    tags:
      - ASR
      - Disaster Recovery
      - Recovery Vault
      - Replication
      - Site Recovery
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/recoveryservices
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/migrate/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/developer/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/azure-migrate/
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/tag/azure-migrate/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/migrate/whats-new
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Website
    url: https://azure.microsoft.com/en-us/products/azure-migrate
  - type: Login
    url: https://portal.azure.com
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
