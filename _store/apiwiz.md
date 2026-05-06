---
aid: apiwiz
url: https://raw.githubusercontent.com/api-evangelist/apiwiz/refs/heads/main/apis.yml
name: APIwiz
tags:
  - API Design
  - API Gateway
  - API Governance
  - API Lifecycle
  - API Management
  - API Monetization
  - API Security
  - Automation
  - Low-Code
  - Observability
  - Platform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-19'
position: Consumer
description: APIwiz is a federated API management platform that streamlines the complete API lifecycle from design through monetization. The low-code platform provides centralized control for organizations managing APIs across multiple cloud environments, with federated gateway control, automated governance, security pipeline, compliance monitoring, and API marketplace capabilities. Trusted by 25K+ managed APIs and 10B+ API volume. Gartner Magic Quadrant Honorable Mention (2023).
apis:
  - aid: apiwiz:apiwiz
    name: APIwiz
    tags:
      - API Design
      - API Governance
      - API Lifecycle
      - API Management
      - API Monetization
      - API Security
      - Low-Code
    humanURL: https://www.apiwiz.io/
    properties:
      - url: https://docs.apiwiz.io/docs
        type: Documentation
      - url: https://docs.apiwiz.io/api-reference
        type: APIReference
      - url: https://www.apiwiz.io/platform
        type: Portal
    description: APIwiz is a low-code, end-to-end API management platform enabling the complete API lifecycle including design, build, security, governance, observability, and monetization. It provides a visual API design studio, federated gateway control across multiple cloud environments, eBPF-powered logging, security pipeline with threat detection, automated compliance monitoring, and API marketplace with dynamic pricing models.
common:
  - type: Documentation
    url: https://docs.apiwiz.io/docs
  - type: APIReference
    url: https://docs.apiwiz.io/api-reference
  - type: Portal
    url: https://www.apiwiz.io/platform
  - type: GitHubOrganization
    url: https://github.com/apiwizlabs
  - type: Contact
    url: https://www.apiwiz.io/contact
  - type: Support
    url: https://wizdesk.apiwiz.io
  - type: Features
    data:
      - name: Visual API Design Studio
        description: Collaborative API specification design with linting, changelogs, and versioning.
      - name: Data Modeling
        description: Standardized data structures for consistent API design across teams.
      - name: Low-Code Workflow Builder
        description: Visual workflow builder for API logic orchestration without heavy coding.
      - name: API Discovery
        description: Zero-touch discovery and cataloging of shadow and unmanaged APIs.
      - name: Security Pipeline
        description: Real-time security scanning, threat detection, and automated security alerts.
      - name: Compliance Monitoring
        description: Automated compliance reporting and multi-environment policy enforcement.
      - name: Federated Gateway Control
        description: Centralized management of multiple API gateways across cloud environments.
      - name: eBPF-Powered Observability
        description: Logging and tracing powered by eBPF for deep performance and security insights.
      - name: API Marketplace
        description: Marketplace capabilities with dynamic pricing models for API monetization.
      - name: Revenue Analytics
        description: Fine-grained metering with custom charge rules and revenue reconciliation.
      - name: Scenario-Driven Testing
        description: Automated testing automation with test and virtualization capabilities.
  - type: UseCases
    data:
      - name: Platform Engineering
        description: Build and manage an internal developer platform with full API lifecycle governance.
      - name: API Gateway Migration
        description: Migrate between API gateways with federated control and minimal disruption.
      - name: API Governance
        description: Automate compliance monitoring and enforce API policies across all environments.
      - name: Banking and Fintech
        description: Manage financial APIs with high security, compliance, and monetization requirements.
      - name: Telecommunications
        description: Manage large-scale telecom APIs with federated gateway control and observability.
      - name: API Monetization
        description: Publish APIs to marketplace and configure usage-based pricing for revenue generation.
  - type: Integrations
    data:
      - name: Apigee
        description: API gateway integration for managing APIs through Google Apigee.
      - name: Kong
        description: API gateway integration for managing APIs through Kong.
      - name: IBM API Connect
        description: API gateway integration for managing APIs through IBM API Connect.
      - name: GitHub
        description: SCM integration for source code management and CI/CD workflows.
      - name: GitLab
        description: SCM integration for source code management and CI/CD workflows.
      - name: Bitbucket
        description: SCM integration for source code management and CI/CD workflows.
      - name: Azure DevOps
        description: SCM and DevOps integration for Microsoft Azure DevOps pipelines.
      - name: AWS CodeCommit
        description: SCM integration for Amazon Web Services code repository.
      - name: Okta
        description: Identity management integration for authentication and authorization.
      - name: Active Directory
        description: Identity management integration for Microsoft Active Directory.
      - name: Ping Identity
        description: Identity management integration for enterprise identity governance.
      - name: Slack
        description: Notification integration for alerts and workflow notifications via Slack.
      - name: Jira
        description: Project management integration via Wizdesk connector for issue tracking.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
