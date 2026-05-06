---
aid: commvault
name: Commvault
description: Commvault is a cloud-native cyber resilience platform that delivers unified data security, identity resilience, and cyber recovery. The Commvault REST API, Command Center API, and Automation API provide programmatic access to backup, restore, replication, threat scan, reporting, and orchestration capabilities across enterprise workloads spanning on-premises, virtual machines, and cloud applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/apis.yml
tags:
  - Backup
  - Cloud Storage
  - Cyber Recovery
  - Data Management
  - Data Protection
  - Disaster Recovery
  - Enterprise Software
created: '2025-01-20'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
apis:
  - aid: commvault:rest-api
    name: Commvault REST API
    description: The Commvault REST API provides programmatic access to Commvault data protection and management operations including authentication, clients, agents, subclients, backup and restore jobs, schedules, storage policies, and reporting. Authentication is token-based using a QSDK token issued by the Login operation, sent in the Authtoken header on subsequent calls.
    image: https://www.commvault.com/wp-content/themes/commvault/assets/images/commvault-logo.svg
    humanURL: https://documentation.commvault.com/v11/essential/rest_api_overview.html
    baseURL: https://webserver.commvault.com/webconsole/api
    tags:
      - Backup
      - Clients
      - Data Management
      - Jobs
      - REST API
      - Restore
      - Subclients
    properties:
      - type: Documentation
        url: https://documentation.commvault.com/v11/essential/rest_api_overview.html
      - type: Authentication
        url: https://documentation.commvault.com/v11/essential/rest_api_authentication.html
      - type: Postman Collection
        url: https://documenter.getpostman.com/view/2046098/RW1aHzQg
      - type: API Reference
        url: https://api.commvault.com/swagger/
      - type: OpenAPI
        url: openapi/commvault-rest-openapi.yml
      - type: Spectral Rules
        url: rules/commvault-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/commvault-backup-management.yml
    features:
      - title: Token-based Authentication
        description: QSDK token authentication via Login/Logout endpoints with token sent in Authtoken header.
      - title: Client Lifecycle
        description: Register, retrieve, update, and retire client servers, workstations, and VM proxies.
      - title: Subclient Management
        description: Create and configure subclients that define backup content, schedules, and storage policies.
      - title: Backup and Restore Jobs
        description: Trigger backups (full, incremental, differential, synthetic full) and restore jobs with targeted destinations.
      - title: Job Monitoring
        description: List and inspect backup, restore, and administrative jobs with status, progress, and failure details.
      - title: Storage Policy Management
        description: Manage storage policies and copies that govern retention, deduplication, and replication.
      - title: Schedule Policies
        description: Define schedule policies that automate backup operations across clients.
      - title: Alerts and Reporting
        description: Configure alerts and access reporting endpoints for compliance and operational visibility.
    useCases:
      - title: Automated Backup Orchestration
        description: Trigger and monitor backup jobs across thousands of clients from CI/CD or orchestration pipelines.
      - title: Disaster Recovery
        description: Initiate restore operations to alternate destinations as part of disaster recovery runbooks.
      - title: Cyber Recovery
        description: Integrate with SOC tooling to recover clean copies of data after a ransomware event.
      - title: Compliance Reporting
        description: Pull job and storage data into governance dashboards for retention and SLA reporting.
  - aid: commvault:command-center-api
    name: Commvault Command Center API
    description: The Commvault Command Center API exposes the operations behind the modern web-based Command Center UI, providing centralized management, monitoring, dashboards, server group control, and workflow execution for Commvault environments.
    humanURL: https://documentation.commvault.com/2024/essential/command_center_overview.html
    baseURL: https://commandcenter.commvault.com/commandcenter/api
    tags:
      - Command Center
      - Dashboards
      - Management
      - Monitoring
    properties:
      - type: Documentation
        url: https://documentation.commvault.com/2024/essential/rest_api_command_center.html
      - type: API Reference
        url: https://api.commvault.com/
      - type: OpenAPI
        url: openapi/commvault-command-center-openapi.yml
      - type: Spectral Rules
        url: rules/commvault-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/commvault-backup-management.yml
    features:
      - title: Centralized Dashboards
        description: Aggregate environment health, job, and storage metrics across CommCells.
      - title: Server Group Management
        description: Manage server groups, plans, and policy assignments from a unified surface.
      - title: Workflow Execution
        description: Run pre-built and custom workflows for routine operations and approvals.
    useCases:
      - title: Multi-CommCell Operations
        description: Manage data protection across multiple CommCells from a single Command Center.
      - title: Operational Monitoring
        description: Surface dashboard data into NOC and observability tools.
  - aid: commvault:automation-api
    name: Commvault Automation API
    description: The Commvault Automation API provides endpoints for executing Commvault Workflows, managing job scheduling, and orchestrating policy-driven operations across the protected estate. Workflows are reusable automation packages that combine REST calls, decision logic, and approvals.
    humanURL: https://documentation.commvault.com/v11/essential/automation_overview.html
    baseURL: https://webserver.commvault.com/webconsole/api
    tags:
      - Automation
      - Orchestration
      - Scheduling
      - Workflows
    properties:
      - type: Documentation
        url: https://documentation.commvault.com/v11/essential/rest_api_automation.html
      - type: OpenAPI
        url: openapi/commvault-automation-openapi.yml
      - type: Spectral Rules
        url: rules/commvault-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/commvault-backup-management.yml
    features:
      - title: Workflow Execution
        description: Execute custom and Commvault-shipped Workflows with structured inputs.
      - title: Job Scheduling
        description: Programmatically create, update, and remove schedule policies and individual schedules.
      - title: Policy Management
        description: Manage storage and schedule policies that govern protection behavior.
    useCases:
      - title: Run Books
        description: Encode operational run books as Workflows triggered by external events.
      - title: Self-Service Automation
        description: Expose curated Workflows to tenants and application teams for self-service operations.
common:
  - type: Portal
    url: https://cloud.commvault.com/
  - type: Documentation
    url: https://documentation.commvault.com/
  - type: Support
    url: https://www.commvault.com/support
  - type: Login
    url: https://login.commvault.com/
  - type: Status
    url: https://status.commvault.com/
  - type: Blog
    url: https://www.commvault.com/blogs
  - type: Contact
    url: https://www.commvault.com/contact-us
  - type: Privacy Policy
    url: https://www.commvault.com/privacy-policy
  - type: Terms of Service
    url: https://www.commvault.com/terms-of-use
  - type: JSON-LD
    url: json-ld/commvault-context.jsonld
  - type: JSONSchema
    url: json-schema/commvault-backup-job-schema.json
  - type: JSONSchema
    url: json-schema/commvault-client-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
