---
aid: valence-security
name: Valence Security
description: Valence Security is the leader in SaaS and AI Security, built for the agentic era. The platform provides SaaS security posture management (SSPM), AI security posture management (AI-SPM), identity threat detection and response (ITDR), and risk remediation across 175+ SaaS and AI applications including Microsoft 365, Google Workspace, Salesforce, Okta, GitHub, OpenAI, and Anthropic.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - SaaS Security
  - SSPM
  - AI Security
  - Identity Security
  - ITDR
  - Posture Management
  - Risk Remediation
url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: valence-security:valence-security-api
    name: Valence Security API
    description: The Valence Security REST API enables integration with the Valence platform for ingesting security data from custom sources, exporting alerts and audit logs, and configuring security monitoring via the Connector Studio.
    humanURL: https://www.valencesecurity.com
    tags:
      - SaaS Security
      - SSPM
      - API Integration
      - Security
      - Alerts
      - Audit Logs
    properties:
      - type: Documentation
        url: https://www.valencesecurity.com/resources
      - type: Connector Studio
        url: https://www.valencesecurity.com/solutions/valence-connector-studio
    features:
      - name: SaaS Discovery
        description: Inventory all SaaS and AI application usage across the organization
      - name: Security Posture Management
        description: Identify and prioritize misconfigurations and risks in SaaS applications
      - name: AI-SPM
        description: Assess and govern AI tool and agent usage and associated risks
      - name: Risk Remediation
        description: Operationalize risk remediation with flexible manual to automated workflows
      - name: Identity Threat Detection and Response
        description: Monitor human and non-human identity activities to detect threats
      - name: Connector Studio
        description: REST API-based integration for ingesting data from custom sources
      - name: Datadog Integration
        description: Export alerts and audit logs to Datadog via API key authentication
      - name: Microsoft Security Copilot
        description: Integration with Microsoft Security Copilot for AI-assisted security
    useCases:
      - name: Shadow SaaS Discovery
        description: Discover unauthorized SaaS and AI applications in use
      - name: SaaS Configuration Management
        description: Manage and enforce secure configurations across SaaS applications
      - name: AI Agent Security
        description: Secure AI agents and non-human identities
      - name: Compliance
        description: Map SaaS security posture to industry compliance standards
      - name: ITDR
        description: Detect and respond to identity-based threats across SaaS
    integrations:
      - name: Microsoft 365
        description: Security posture management for Microsoft 365
      - name: Google Workspace
        description: Security posture management for Google Workspace
      - name: Salesforce
        description: Security posture management for Salesforce
      - name: Okta
        description: Identity security integration with Okta
      - name: GitHub
        description: Security monitoring for GitHub
      - name: OpenAI
        description: AI security monitoring for OpenAI usage
      - name: Anthropic
        description: AI security monitoring for Anthropic Claude usage
      - name: Snowflake
        description: Data security posture management for Snowflake
      - name: Datadog
        description: Export alerts and audit logs to Datadog SIEM
      - name: Microsoft Security Copilot
        description: AI-assisted security analysis via Microsoft Security Copilot plugin
common:
  - type: Website
    url: https://www.valencesecurity.com
  - type: Documentation
    url: https://www.valencesecurity.com/resources
  - type: Connector Studio
    url: https://www.valencesecurity.com/solutions/valence-connector-studio
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/json-schema/valence-security-alert-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/json-schema/valence-security-integration-schema.json
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/json-ld/valence-security-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/vocabulary/valence-security-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
