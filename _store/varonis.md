---
name: Varonis
description: Varonis is a pioneer in data security and analytics, specializing in software for data security, governance, threat detection and response. The company provides solutions for protecting enterprise data across cloud and on-premises environments including data classification, access governance, behavioral threat detection, and automated remediation.
image: https://www.varonis.com/favicon.ico
url: https://www.varonis.com
created: '2025'
modified: '2026-05-03'
tags:
  - Cloud Security
  - Compliance
  - Data Analytics
  - Data Governance
  - Data Security
  - Threat Detection
apis:
  - name: Varonis DatAlert API
    description: API for accessing threat detection and incident response capabilities from Varonis DatAlert. Provides endpoints for retrieving alerts, managing alert status, adding notes to alerts, and accessing alerted events for investigation and threat hunting. The DatAlert API enables integration with SIEM and SOAR platforms for centralized security operations.
    image: https://www.varonis.com/favicon.ico
    humanURL: https://www.varonis.com/products/datalert
    baseURL: https://api.varonis.com/datalert
    tags:
      - Incident Response
      - Security Alerts
      - Threat Detection
    properties:
      - type: Documentation
        url: https://docs.varonis.com/api/datalert
      - type: OpenAPI
        url: openapi/varonis-datalert-openapi.yml
      - type: Authentication
        url: https://docs.varonis.com/api/authentication
      - type: JSONSchema
        url: json-schema/varonis-datalert-alert-schema.json
        title: Alert Schema
      - type: JSONSchema
        url: json-schema/varonis-datalert-alerted-event-schema.json
        title: Alerted Event Schema
      - type: JSONSchema
        url: json-schema/varonis-datalert-threat-model-schema.json
        title: Threat Model Schema
      - type: JSONStructure
        url: json-structure/varonis-datalert-alert-structure.json
        title: Alert Structure
      - type: JSONStructure
        url: json-structure/varonis-datalert-alerted-event-structure.json
        title: Alerted Event Structure
      - type: Example
        url: examples/varonis-datalert-alert-example.json
        title: Alert Example
      - type: Example
        url: examples/varonis-datalert-alerted-event-example.json
        title: Alerted Event Example
  - name: Varonis Data Security Platform API
    description: API for integrating with Varonis Data Security Platform to manage data security policies, access permissions, and threat detection.
    image: https://www.varonis.com/favicon.ico
    humanURL: https://www.varonis.com/products/data-security-platform
    baseURL: https://api.varonis.com
    tags:
      - Access Control
      - Data Security
      - Permissions
    properties:
      - type: Documentation
        url: https://docs.varonis.com/api
      - type: Authentication
        url: https://docs.varonis.com/api/authentication
  - name: Varonis DataPrivilege API
    description: REST and SOAP API for integrating Varonis DataPrivilege with IAM and ITSM solutions. Enables synchronization of managed data, execution and reporting on access requests and access control changes, and automation of entitlement reviews and self-service access workflows.
    image: https://www.varonis.com/favicon.ico
    humanURL: https://www.varonis.com/products/dataprivilege
    baseURL: https://api.varonis.com
    tags:
      - Access Governance
      - Entitlement Reviews
      - Identity Management
      - Self-Service Access
    properties:
      - type: Documentation
        url: https://www.varonis.com/blog/introducing-gdpr-patterns-and-dataprivilege-api
  - name: Varonis MCP Server
    description: Model Context Protocol server that interfaces with Varonis APIs, allowing AI clients such as ChatGPT, Claude, and GitHub Copilot to access and orchestrate the Varonis Data Security Platform using natural language. Enables complex workflows including alert retrieval, access remediation, and compliance reporting.
    image: https://www.varonis.com/favicon.ico
    humanURL: https://www.varonis.com/blog/mcp-server
    baseURL: https://api.varonis.com
    tags:
      - AI Integration
      - Automation
      - MCP
      - Natural Language
    properties:
      - type: Documentation
        url: https://www.varonis.com/blog/mcp-server
      - type: SDK
        url: https://www.npmjs.com/package/@varonis/mcp
        title: MCP Server npm Package
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
include:
  - name: Varonis Support Portal
    url: https://support.varonis.com
common:
  - type: Portal
    url: https://www.varonis.com/developers
  - type: Website
    url: https://www.varonis.com
  - type: Support
    url: https://www.varonis.com/resources/support
  - type: Blog
    url: https://www.varonis.com/blog
  - type: PrivacyPolicy
    url: https://www.varonis.com/trust/privacy
  - type: TermsOfService
    url: https://www.varonis.com/terms
  - type: StatusPage
    url: https://status.varonis.com
  - type: ChangeLog
    url: https://www.varonis.com/platform/changelog
  - type: Security
    url: https://www.varonis.com/trust/security
  - type: Login
    url: https://my.varonis.io/
  - type: SignUp
    url: https://help.varonis.com/s/article/WDOC-2305
  - type: HelpCenter
    url: https://help.varonis.com/s/
  - type: TrustCenter
    url: https://www.varonis.com/trust
  - type: Integrations
    url: https://www.varonis.com/security-ecosystem-integrations
  - type: Training
    url: https://www.varonis.com/product-training
  - type: ContentLibrary
    url: https://www.varonis.com/resources
  - type: GitHubOrganization
    url: https://github.com/varonis
  - type: PartnerPortal
    url: https://partners.varonis.com/
  - type: SpectralRules
    url: rules/varonis-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/threat-detection-response.yaml
    title: Threat Detection and Response
  - type: Vocabulary
    url: vocabulary/varonis-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/varonis-datalert-context.jsonld
  - type: Features
    data:
      - name: Behavioral Threat Detection
        description: AI-powered detection of abnormal user and data access behavior using DatAlert threat models aligned to MITRE ATT&CK.
      - name: Data Classification
        description: Automated sensitive data discovery and classification across cloud and on-premises data stores.
      - name: Access Governance
        description: DataPrivilege workflow automation for entitlement reviews, access requests, and permission remediation.
      - name: Forensic Investigation
        description: Detailed event-level forensics including file access, permission changes, and login activity for incident investigation.
      - name: SIEM and SOAR Integration
        description: REST API integration with SIEM platforms (Splunk, QRadar, Sentinel) and SOAR platforms (XSOAR, Phantom) for automated response.
      - name: AI-Assisted Security (MCP)
        description: Model Context Protocol server enabling natural language security operations with Claude, ChatGPT, and GitHub Copilot.
      - name: Compliance Reporting
        description: Built-in reporting for GDPR, HIPAA, PCI-DSS, SOX, and other compliance frameworks.
      - name: Cloud Security Posture
        description: Data security posture management for Microsoft 365, AWS, Azure, and Google Cloud environments.
  - type: UseCases
    data:
      - name: Insider Threat Detection
        description: Detect and respond to abnormal access patterns that indicate potential insider threats or compromised accounts.
      - name: Ransomware Detection
        description: Identify ransomware activity through mass file access, renaming, and encryption patterns.
      - name: Data Breach Investigation
        description: Investigate potential data breaches using forensic event trails to determine scope and blast radius.
      - name: Privileged Access Review
        description: Automate periodic entitlement reviews to ensure least-privilege access to sensitive data.
      - name: Compliance Audit
        description: Generate audit-ready reports demonstrating data access controls for regulatory frameworks.
      - name: SOAR Automation
        description: Integrate alert triage and remediation into automated playbooks via the DatAlert REST API.
      - name: AI-Driven Security Operations
        description: Use the Varonis MCP Server to enable AI assistants to query alerts, investigate events, and execute remediation.
  - type: Integrations
    data:
      - name: Microsoft Sentinel
        description: Ingest Varonis alerts and events into Microsoft Sentinel for correlation and automated response.
      - name: Splunk
        description: Stream DatAlert events to Splunk via the official Varonis App for Splunk SIEM integration.
      - name: IBM QRadar
        description: Forward Varonis DatAlert events to QRadar using the official integration guide.
      - name: CrowdStrike Falcon
        description: Enrich endpoint threat data with Varonis user and data access context.
      - name: ServiceNow
        description: Create and manage security incident tickets in ServiceNow from Varonis alerts.
      - name: Palo Alto XSOAR
        description: Automate alert triage and remediation workflows using the Varonis XSOAR integration.
      - name: Microsoft 365
        description: Monitor and protect SharePoint, OneDrive, Exchange, and Teams data natively.
      - name: AWS
        description: Data security posture management for S3, RDS, and other AWS data services.
---
