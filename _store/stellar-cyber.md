---
aid: stellar-cyber
name: Stellar Cyber
description: Stellar Cyber is an Open XDR platform that provides AI-driven security operations capabilities including threat detection, investigation, and response. The platform offers an OAS-compliant REST API that enables downstream applications to perform complex queries, join results, analyze data, and automate security operations workflows. Stellar Cyber maintains several sample Python Jupyter Notebooks in GitHub that can help build analyses outside of the platform with the API or connect custom applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cybersecurity
  - Security
  - XDR
  - SIEM
  - SOAR
  - AI
created: '2025-02-06'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/stellar-cyber/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: stellar-cyber:stellar-cyber
    name: Stellar Cyber Open XDR API
    description: The Stellar Cyber REST API provides programmatic access to the Open XDR platform, enabling automation of security operations including case management, tenant administration, connector management, alert handling, query operations, user management, watchlists, sensors, and security event management. The API uses JWT-based authentication and is available at the base path /connect/api/v1/ on the platform hostname.
    humanURL: https://docs.stellarcyber.ai/
    baseURL: https://{platform-hostname}/connect/api/v1
    tags:
      - Cybersecurity
      - Security
      - XDR
      - SIEM
      - SOAR
      - Threat Detection
      - Incident Response
    properties:
      - type: Documentation
        url: https://docs.stellarcyber.ai/
      - type: Reference
        url: https://docs.stellarcyber.ai/6.3.x/Using/API/API-Intro.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stellar-cyber/refs/heads/main/openapi/stellar-cyber-openapi.yml
    contact:
      - FN: Stellar Cyber Support
        url: https://stellarcyber.zendesk.com
common:
  - type: Portal
    url: https://stellarcyber.ai/
  - type: Documentation
    url: https://docs.stellarcyber.ai/
  - type: Website
    url: https://stellarcyber.ai/
  - type: Login
    url: https://stellarcyber.ai/login/
  - type: Pricing
    url: https://stellarcyber.ai/pricing/
  - type: Blog
    url: https://stellarcyber.ai/blog/
  - type: GitHub Organization
    url: https://github.com/stellarcyber
features:
  - name: Open XDR Platform
    description: AI-driven security operations platform with 500+ integrations
  - name: Case Management API
    description: Create, retrieve, update, and close security cases programmatically
  - name: Multi-Tenant Architecture
    description: Full tenant administration, grouping, and isolation capabilities
  - name: Connector Management
    description: Manage data connectors for ingesting security telemetry from diverse sources
  - name: JWT Authentication
    description: Secure time-limited JWT tokens with automatic expiry and refresh support
  - name: ElasticSearch Query API
    description: Direct ElasticSearch query access on platform indices for advanced analytics
  - name: Automated Response
    description: ATH Playbook and System Action Center rules for automated threat response
useCases:
  - name: SOC Automation
    description: Automate security operations workflows including alert triage, case creation, and response actions
  - name: Threat Hunting
    description: Use the query and ElasticSearch APIs to hunt for threats across security telemetry
  - name: Custom Integrations
    description: Build custom SIEM, SOAR, and ticketing integrations via the REST API
  - name: Multi-Tenant MSSP
    description: Manage multiple customer tenants programmatically with tenant API operations
  - name: Compliance Reporting
    description: Generate and retrieve security reports for compliance and audit purposes
integrations:
  - name: SIEM Integrations
    description: Ingest logs and alerts from third-party SIEM platforms
  - name: Ticketing Systems
    description: Integrate with ServiceNow, Jira, and other ticketing systems for case management
  - name: Threat Intelligence
    description: Enrich alerts with threat intelligence via connector API
  - name: Endpoint Detection
    description: Integrate with EDR and endpoint security tools for response actions
solutions:
  - name: Open XDR
    description: Unified threat detection and response across all security layers
  - name: AI SIEM
    description: AI-powered SIEM with automated correlation and detection
  - name: NDR
    description: Network Detection and Response capabilities
  - name: SOAR
    description: Security Orchestration, Automation, and Response capabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
