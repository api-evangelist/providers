---
name: Veritas NetBackup
description: Enterprise-grade data protection and backup solution with comprehensive REST APIs for backup, recovery, and data management operations.
image: https://www.veritas.com/content/dam/veritas/images/logos/veritas-logo.svg
url: https://www.veritas.com/products/backup-and-recovery/netbackup
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
tags:
  - Backup
  - Data Protection
  - Disaster Recovery
  - Enterprise
  - Recovery
  - Storage
apis:
  - name: Veritas NetBackup REST API
    description: Primary REST API for NetBackup operations including backup policies, jobs, catalogs, and asset management.
    image: https://www.veritas.com/content/dam/veritas/images/logos/veritas-logo.svg
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup
    tags:
      - Backup
      - Catalog
      - Jobs
      - Policies
      - Restore
    properties:
      - type: Documentation
        url: https://sort.veritas.com/documents/netbackup/10.1/productguides
      - type: APIReference
        url: https://sort.veritas.com/public/documents/nbu/10.1/windowsandunix/productguides/html/api/nbu_10.1_webapi.html
      - type: Console
        url: https://netbackup-primary-server:1556/api-docs
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: Authentication
        url: https://sort.veritas.com/public/documents/nbu/10.0/windowsandunix/productguides/html/getting-started/
      - type: SDK
        url: https://github.com/VeritasOS/netbackup-api-code-samples
      - type: ChangeLog
        url: https://www.veritas.com/protection/netbackup/whats-new
      - type: ReleaseNotes
        url: https://www.veritas.com/support/en_US/doc/103228346-168289021-0/v168307940-168289021
      - type: Documentation
        url: https://www.veritas.com/support/en_US/article.100043102
      - type: OpenAPI
        url: openapi/veritas-netbackup-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/veritas-netbackup-job-schema.json
      - type: JSONLD
        url: json-ld/veritas-netbackup-context.jsonld
  - name: NetBackup Administration API
    description: API for managing NetBackup jobs including getting job details, listing jobs by filter, restarting, resuming, suspending, canceling, and deleting jobs, and retrieving job file lists and logs.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/admin
    tags:
      - Administration
      - Jobs
      - Management
      - Monitoring
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Asset Management API
    description: API for managing NetBackup assets including servers, clients, and storage devices.
    humanURL: https://www.veritas.com/support/en_US/doc/nbu_assets
    baseURL: https://netbackup-primary-server:1556/netbackup/assets
    tags:
      - Assets
      - Clients
      - Inventory
      - Servers
    properties:
      - type: Documentation
        url: https://sort.veritas.com/documents
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Security API
    description: API endpoints for managing authentication, authorization, certificates, credentials, tokens, and security audit logging configurations.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/security
    tags:
      - Audit
      - Authentication
      - Authorization
      - Certificates
      - Credentials
      - Security
    properties:
      - type: Documentation
        url: https://sort.veritas.com/documents
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Image Management API
    description: API for managing backup images, catalogs, and media retention.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/catalog
    tags:
      - Catalog
      - Images
      - Media
      - Retention
    properties:
      - type: Documentation
        url: https://sort.veritas.com/documents
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Configuration API
    description: API for configuring NetBackup hosts, policies, servers, VM server credentials, and storage settings.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/config
    tags:
      - Configuration
      - Hosts
      - Policies
      - Servers
      - Storage
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Storage API
    description: API for managing storage consumption, capacity reporting, and backup storage on NetBackup primary servers.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/storage
    tags:
      - Capacity
      - Consumption
      - Reporting
      - Storage
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Recovery API
    description: API for VMware and cloud workload recovery operations including restore and instant access.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/recovery
    tags:
      - Cloud
      - Instant-Access
      - Recovery
      - Restore
      - Vmware
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup RBAC Administration API
    description: API for managing role-based access control, permissions, access rules, and access control lists.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/rbac
    tags:
      - Access-Control
      - Permissions
      - Rbac
      - Roles
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Licensing API
    description: API for managing entitlements and tracking Front-end Terabytes (FETBs) consumption for NetBackup licensing.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/licensing
    tags:
      - Consumption
      - Entitlements
      - Licensing
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Service Catalog API
    description: API for managing service-level objectives (SLOs), protection plans, and subscription handling for backup operations.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/servicecatalog
    tags:
      - Protection-Plans
      - Service-Catalog
      - Slo
      - Subscriptions
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Manage API
    description: API for managing alerts and notification operations in NetBackup environments.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/manage
    tags:
      - Alerts
      - Management
      - Notifications
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup Troubleshooting API
    description: API for status code resolution and error reference to assist with troubleshooting NetBackup issues.
    humanURL: https://www.veritas.com/support/en_US/article.100040135
    baseURL: https://netbackup-primary-server:1556/netbackup/troubleshooting
    tags:
      - Diagnostics
      - Errors
      - Status-Codes
      - Troubleshooting
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - name: NetBackup IT Analytics REST API
    description: REST API for accessing NetBackup IT Analytics report data, exporting reports in JSON, XML, HTML, PDF, and CSV formats, and exporting custom dashboards.
    humanURL: https://www.veritas.com/support/en_US/doc/140670999-168357535-0/v149890439-168357535
    baseURL: https://portal-server/api/v1
    tags:
      - Analytics
      - Dashboards
      - Monitoring
      - Reporting
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/140670999-168357535-0/v149890439-168357535
      - type: Authentication
        url: https://www.veritas.com/support/en_US/doc/140670999-149890373-0/v149894265-149890373
      - type: GettingStarted
        url: https://www.veritas.com/support/en_US/doc/140670999-166019911-0/v140669480-166019911
  - name: NetBackup Self Service REST API
    description: REST API for the NetBackup Self Service portal providing backup utilization data, protection status, tenant management, and self-service backup and restore operations.
    humanURL: https://www.veritas.com/protection/netbackup/self-service
    baseURL: https://self-service-server/NetbackupAdapterPanels/Api
    tags:
      - Portal
      - Self-Service
      - Tenants
      - Utilization
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/109536476-156847273-0/v119207347-156847273
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/109536476-167202398-1
  - name: NetBackup Flex Scale REST API
    description: REST API for controlling all aspects of NetBackup Flex Scale configuration including infrastructure monitoring, user management, node management, patch upgrades, and storage licensing.
    humanURL: https://www.veritas.com/support/en_US/doc/139332629-144656221-0/v143532640-144656221
    baseURL: https://management-server:14161/swagger/infra/v1.0
    tags:
      - Appliance
      - Cluster
      - Flex-Scale
      - Infrastructure
      - Node-Management
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/139332629-144656221-0/v143532640-144656221
      - type: SDK
        url: https://github.com/VeritasOS/NetBackup-Flex-Scale-REST-API-nuggets
      - type: GettingStarted
        url: https://www.veritas.com/support/en_US/doc/139332629-144656221-0/v143532640-144656221
common:
  - type: Support
    url: https://www.veritas.com/support
  - type: Documentation
    url: https://www.veritas.com/support/en_US/article.100040135
  - type: APIReference
    url: https://www.veritas.com/support/en_US/doc/139300789-139300792-0/index
  - type: GettingStarted
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: Pricing
    url: https://www.veritas.com/products/backup-and-recovery/netbackup/pricing
  - type: Support
    url: https://www.veritas.com/support/en_US/netbackup
  - type: Contact
    url: https://www.veritas.com/company/contact
  - type: KnowledgeCenter
    url: https://www.veritas.com/support/en_US/netbackup.PRODUCT_HOME
  - type: Documentation
    url: https://www.veritas.com/support/en_US/netbackup.download
  - type: Documentation
    url: https://vox.veritas.com/category/cohesity-discussions/discussions/netbackup
  - type: Authentication
    url: https://sort.veritas.com/public/documents/nbu/10.0/windowsandunix/productguides/html/getting-started/
  - type: RateLimits
    url: https://sort.veritas.com/documents/netbackup/10.1/productguides
  - type: Blog
    url: https://www.veritas.com/blogs
  - type: GitHubOrganization
    url: https://github.com/VeritasOS
  - type: SDK
    url: https://github.com/VeritasOS/netbackup-api-code-samples
  - type: CodeExamples
    url: https://veritasos.github.io/netbackup-api-code-samples/
  - type: ChangeLog
    url: https://www.veritas.com/protection/netbackup/whats-new
  - type: ReleaseNotes
    url: https://www.veritas.com/support/en_US/doc/103228346-168289021-0/v168307842-168289021
  - type: Documentation
    url: https://www.veritas.com/support/en_US/article.100032801
  - type: X
    url: https://twitter.com/veritastechllc
  - type: LinkedIn
    url: https://www.linkedin.com/company/veritas-technologies-llc
  - type: TermsOfService
    url: https://www.veritas.com/company/legal/legal-terms-of-use
  - type: PrivacyPolicy
    url: https://www.veritas.com/company/privacy
  - type: Documentation
    url: https://www.veritas.com/company
  - type: Documentation
    url: https://www.veritas.com/protection/netbackup/self-service
  - type: Documentation
    url: https://www.veritas.com/support/en_US/article.100043102
  - type: Documentation
    url: https://www.veritas.com/support/en_US/article.100052421
  - type: Features
    data:
      - name: Enterprise Backup and Recovery
        description: Comprehensive backup and recovery for physical, virtual, and cloud workloads across heterogeneous environments.
      - name: Policy-Based Protection
        description: Create and manage backup policies with configurable schedules, retention rules, and client selections.
      - name: Job Management
        description: Monitor, control, and troubleshoot backup and restore jobs with full lifecycle management via REST API.
      - name: Catalog Management
        description: Query and manage backup image catalogs for tracking, searching, and lifecycle management of backup data.
      - name: Role-Based Access Control
        description: Fine-grained RBAC for managing user permissions across NetBackup operations and resources.
      - name: Self-Service Portal
        description: Enable tenant-level self-service backup and restore operations through the Self Service portal API.
      - name: IT Analytics and Reporting
        description: Access and export analytics reports and dashboards for backup environment monitoring and capacity planning.
      - name: Flex Scale Infrastructure
        description: Manage NetBackup Flex Scale appliance infrastructure including nodes, storage, users, and patch upgrades.
  - type: UseCases
    data:
      - name: Automated Backup Operations
        description: Automate backup policy creation, job scheduling, and monitoring through REST API integration with CI/CD pipelines.
      - name: Disaster Recovery Orchestration
        description: Programmatically manage recovery operations for VMware and cloud workloads with instant access capabilities.
      - name: Compliance and Audit
        description: Track and report on backup coverage, retention compliance, and security audit events across the enterprise.
      - name: Multi-Tenant Backup Management
        description: Provide self-service backup and restore capabilities to multiple tenants through the Self Service portal API.
      - name: Capacity Planning
        description: Use IT Analytics APIs to export reports on storage consumption, backup trends, and capacity forecasting.
  - type: Integrations
    data:
      - name: VMware vSphere
        description: Native integration for backup and instant recovery of VMware virtual machines and vSphere environments.
      - name: Cloud Platforms
        description: Support for backup and recovery of workloads running on AWS, Azure, and Google Cloud Platform.
      - name: Kubernetes
        description: Container workload protection with backup and recovery support for Kubernetes clusters.
      - name: Oracle and SQL Server
        description: Application-consistent backup and granular recovery for Oracle and Microsoft SQL Server databases.
      - name: RESTful API Ecosystem
        description: Comprehensive REST API coverage for programmatic integration with ITSM, orchestration, and monitoring tools.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
