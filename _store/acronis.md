---
aid: acronis
url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/apis.yml
name: Acronis
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cybersecurity
  - Data Protection
  - Endpoint Management
description: Acronis is a leading provider of cyber protection solutions that deliver innovative technology to protect data, applications, and systems from the ever-evolving threats of today's digital world. They offer a comprehensive suite of products, including backup and disaster recovery solutions, file sync and share services, and anti-malware protection.
created: '2025-02-17'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: acronis:account-management-api
    name: Acronis Account Management API
    tags:
      - Account Management
      - Acronis
      - Tenants
      - Users
    humanURL: https://developer.acronis.com/doc/account-management/v2/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/outbound/apis/api-library/account/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/openapi/acronis-account-management-openapi.yaml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/capabilities/shared/acronis-account-management.yaml
    description: The Acronis Account Management API allows organizations to manage and automate user accounts within the Acronis platform, including creating, updating, and deleting users, and assigning roles and permissions.
  - aid: acronis:agent-management-rest-api
    name: Acronis Agent Management REST API
    tags:
      - Acronis
      - Agent Management
      - Backup
      - Endpoints
    humanURL: https://developer.acronis.com/doc/agents/v2/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/agents/v2/reference/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/openapi/acronis-agent-management-openapi.yaml
    description: The Acronis Agent Management REST API allows users to remotely manage and monitor Acronis agents from a centralized location, including creating, updating, and deleting agent profiles.
  - aid: acronis:resource-and-policy-management-api
    name: Acronis Resource and Policy Management API
    tags:
      - Acronis
      - Policy Management
      - Resources
    humanURL: https://developer.acronis.com/doc/resource-policy-management/v4/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/resource-policy-management/v4/guide/index.html
    description: Acronis Resource and Policy Management API enables organizations to efficiently manage resources and policies within their IT infrastructure.
  - aid: acronis:task-manager-api
    name: Acronis Task Manager API
    tags:
      - Acronis
      - Backup
      - Monitoring
      - Tasks
    humanURL: https://developer.acronis.com/doc/tasks/v2/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/tasks/v2/guide/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/openapi/acronis-task-manager-openapi.yaml
    description: Acronis Task Manager API allows users to manage tasks and processes within the Acronis backup platform, including creating, editing, and monitoring tasks.
  - aid: acronis:advanced-automation-api
    name: Acronis Advanced Automation API
    tags:
      - Acronis
      - Advanced Automation
      - PSA
    humanURL: https://developer.acronis.com/doc/advanced-automation/v1/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/outbound/apis/api-library/advanced-automation/index.html
    description: The Acronis Advanced Automation API allows users to automate and streamline their backup and recovery processes with custom scripts and workflows.
  - aid: acronis:event-manager-api
    name: Acronis Event Manager API
    tags:
      - Acronis
      - Events
      - Monitoring
    humanURL: https://developer.acronis.com/doc/events/v1/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/vendor-side/apis/api-library/events/index.html
    description: The Acronis Event Manager API allows users to monitor and manage events across their entire Acronis ecosystem with real-time access to event data.
  - aid: acronis:disaster-recovery-service-api
    name: Acronis Disaster Recovery Service API
    tags:
      - Acronis
      - Disaster Recovery
    humanURL: https://developer.acronis.com/doc/disaster-recovery/v2/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/outbound/apis/api-library/dr/index.html
    description: The Acronis Disaster Recovery Service API allows organizations to automate and streamline their disaster recovery processes.
  - aid: acronis:endpoint-detection-and-response-api
    name: Acronis Endpoint Detection and Response API
    tags:
      - Acronis
      - EDR
      - Endpoint Security
    humanURL: https://developer.acronis.com/doc/mdr/v1/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/outbound/apis/api-library/mdr/index.html
    description: The Acronis Endpoint Detection and Response API is a comprehensive security solution that helps organizations detect and respond to cybersecurity threats in real-time.
  - aid: acronis:vault-manager-rest-api
    name: Acronis Vault Manager REST API
    tags:
      - Acronis
      - Storage
      - Vault Management
    humanURL: https://developer.acronis.com/doc/vaultman/v1/reference/index.html
    properties:
      - type: Documentation
        url: https://developer.acronis.com/doc/vaultman/v1/reference/index.html
    description: The Acronis Vault Manager REST API allows users to manage and interact with their Acronis Vault storage solutions programmatically.
common:
  - type: Portal
    url: https://developer.acronis.com/
  - type: GettingStarted
    url: https://developer.acronis.com/doc/outbound/apis/getting-started/index.html
  - type: Authentication
    url: https://developer.acronis.com/doc/outbound/apis/authentication/index.html
  - type: Blog
    url: https://www.acronis.com/en-us/blog/
  - type: Support
    url: https://www.acronis.com/en-us/support/
  - type: Pricing
    url: https://www.acronis.com/en-us/products/cloud/cyber-protect/pricing/
  - type: Partners
    url: https://www.acronis.com/en-us/partners/
  - type: CaseStudies
    url: https://www.acronis.com/en-us/resource-center/category/case-studies/
  - type: GitHubOrganization
    url: https://github.com/acronis
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/capabilities/cyber-protection-operations.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/vocabulary/acronis-vocabulary.yaml
  - type: TermsOfService
    url: https://www.acronis.com/en-us/legal/
  - type: ChangeLog
    url: https://developer.acronis.com/doc/outbound/apis/index.html
  - type: Features
    data:
      - name: Tenant Hierarchy Management
        description: Multi-tier tenant management for MSPs, partners, and customers with offering item quotas.
      - name: Agent Management
        description: Remote management of Acronis backup agents across Windows, Linux, macOS, and cloud workloads.
      - name: Backup Task Monitoring
        description: Real-time monitoring of backup and protection tasks with state, result, and activity tracking.
      - name: Usage Reporting
        description: Automated usage metrics collection and report generation for billing and capacity planning.
      - name: Policy Management
        description: Programmatic creation and application of protection policies to resources.
      - name: Disaster Recovery API
        description: Automated failover and recovery orchestration for business continuity.
      - name: Endpoint Detection and Response
        description: EDR capabilities for threat detection, investigation, and response via API.
  - type: UseCases
    data:
      - name: MSP Platform Automation
        description: Automate tenant provisioning, licensing management, and usage reporting for managed service providers.
      - name: Backup Monitoring Dashboard
        description: Build custom dashboards tracking backup task status, failures, and completion rates.
      - name: Agent Health Monitoring
        description: Monitor agent online status, version compliance, and update management across endpoints.
      - name: Compliance Reporting
        description: Generate automated reports on data protection status for compliance and audit requirements.
      - name: Disaster Recovery Automation
        description: Trigger and monitor DR failover workflows programmatically for RTO/RPO compliance.
  - type: Integrations
    data:
      - name: PSA Platforms
        description: Integration with ConnectWise, Autotask, and other PSA platforms for MSP billing and ticketing.
      - name: SIEM Systems
        description: Event streaming to SIEM platforms via Event Manager API for security monitoring.
      - name: RMM Tools
        description: Integration with RMM platforms for agent deployment and backup policy management.
      - name: Billing Systems
        description: Usage data export for automated billing via usage and offering item APIs.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
