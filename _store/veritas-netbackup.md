---
aid: veritas-netbackup
url: https://raw.githubusercontent.com/api-evangelist/veritas-netbackup/refs/heads/main/apis.yml
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
  - type: X-documentation
    url: https://sort.veritas.com/documents/netbackup/10.1/productguides
  - type: X-openapi
    url: https://sort.veritas.com/public/documents/nbu/10.1/windowsandunix/productguides/html/api/nbu_10.1_webapi.html
  - type: X-api-console
    url: https://netbackup-primary-server:1556/api-docs
  - type: X-getting-started
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-authentication
    url: https://sort.veritas.com/public/documents/nbu/10.0/windowsandunix/productguides/html/getting-started/
  - type: X-sdk
    url: https://github.com/VeritasOS/netbackup-api-code-samples
  - type: X-change-log
    url: https://www.veritas.com/protection/netbackup/whats-new
  - type: X-release-notes
    url: https://www.veritas.com/support/en_US/doc/103228346-168289021-0/v168307940-168289021
  - type: X-support-statement
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/documents
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/documents
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/documents
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
  - type: X-getting-started
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
  - type: X-documentation
    url: https://www.veritas.com/support/en_US/doc/140670999-168357535-0/v149890439-168357535
  - type: X-authentication
    url: https://www.veritas.com/support/en_US/doc/140670999-149890373-0/v149894265-149890373
  - type: X-getting-started
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
  - type: X-documentation
    url: https://www.veritas.com/support/en_US/doc/109536476-156847273-0/v119207347-156847273
  - type: X-configuration-guide
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
  - type: X-documentation
    url: https://www.veritas.com/support/en_US/doc/139332629-144656221-0/v143532640-144656221
  - type: X-sdk
    url: https://github.com/VeritasOS/NetBackup-Flex-Scale-REST-API-nuggets
  - type: X-getting-started
    url: https://www.veritas.com/support/en_US/doc/139332629-144656221-0/v143532640-144656221
name: Veritas NetBackup
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
type: Contract
image: https://www.veritas.com/content/dam/veritas/images/logos/veritas-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Enterprise-grade data protection and backup solution with comprehensive REST APIs for backup, recovery, and data management operations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

