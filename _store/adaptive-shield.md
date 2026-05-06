---
aid: adaptive-shield
name: Adaptive Shield
description: Adaptive Shield (now CrowdStrike Falcon Shield) is a SaaS Security Posture Management (SSPM) platform that continuously monitors, remediates, and governs SaaS application security configurations and identity risks. Acquired by CrowdStrike, the platform covers 200+ SaaS integrations with over 3,500 built-in security checks, helping organizations detect misconfigurations, manage human and non-human identities, discover shadow applications, and maintain compliance across their entire SaaS stack. The REST API (v1) enables programmatic access to alerts, user inventory, device inventory, integrations, security checks, and compliance data.
url: https://raw.githubusercontent.com/api-evangelist/adaptive-shield/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - SaaS Security
  - SSPM
  - Security Posture Management
  - Cybersecurity
  - Cloud Security
  - Identity Management
  - Compliance
apis:
  - aid: adaptive-shield:adaptive-shield-api
    name: Adaptive Shield REST API
    description: The Adaptive Shield REST API v1 provides programmatic access to SaaS security posture data including alerts, user and device inventory, integration configurations, security check results, violations, and compliance controls. Authentication uses a per-user API key (access token). Regional endpoints are available for US (api.adaptive-shield.com) and EU (eu.api.adaptive-shield.com) regions.
    humanURL: https://www.crowdstrike.com/platform/falcon-shield/
    tags:
      - SaaS Security
      - SSPM
      - REST API
      - Alerts
      - Compliance
    properties:
      - type: Documentation
        url: https://www.crowdstrike.com/platform/falcon-shield/
      - type: Authentication
        url: https://www.adaptive-shield.com/support
common:
  - type: Website
    url: https://www.crowdstrike.com/platform/falcon-shield/
  - type: Portal
    url: https://www.crowdstrike.com/platform/falcon-shield/
  - type: Blog
    url: https://www.adaptive-shield.com/blog/
  - type: Resources
    url: https://www.adaptive-shield.com/resources
  - type: Integrations
    url: https://www.adaptive-shield.com/integrations
  - type: Support
    url: https://www.adaptive-shield.com/support
  - type: Features
    data:
      - name: SaaS Misconfiguration Detection
        description: Continuously monitors 200+ SaaS applications with 3,500+ built-in security checks to detect and remediate misconfigurations that expose organizations to security risks.
      - name: Identity And Access Governance
        description: Manages both human and non-human identities (NHI) across SaaS platforms, detecting over-privileged accounts and suspicious access patterns.
      - name: Shadow App Discovery
        description: Discovers unsanctioned and shadow SaaS applications connected to the organization's environment, providing visibility into unauthorized integrations.
      - name: AI Agent Visibility And Control
        description: Provides visibility into and governance over AI agents operating within enterprise SaaS platforms including Microsoft 365, Salesforce, and OpenAI.
      - name: Compliance Monitoring
        description: Tracks compliance posture across SaaS applications against frameworks such as SOC 2, ISO 27001, GDPR, and HIPAA using automated security check mappings.
      - name: REST API Access
        description: Public REST API v1 with API key authentication enables programmatic access to alerts, user/device inventory, integration data, security check results, violations, and compliance controls. US and EU regional endpoints available.
      - name: SIEM And Platform Integrations
        description: Integrates with SIEM platforms (Splunk, Datadog), security platforms (CrowdStrike Falcon), and vulnerability management platforms via API and native connectors.
  - type: UseCases
    data:
      - name: SaaS Security Posture Management
        description: Security teams can continuously monitor and remediate misconfigurations across the organization's entire SaaS stack from a single dashboard.
      - name: Identity Risk Detection
        description: Detect and remediate over-privileged users, dormant accounts, and suspicious login behavior across all connected SaaS applications.
      - name: Compliance Audit Automation
        description: Automate compliance evidence collection and posture monitoring for SOC 2, ISO 27001, GDPR, and other frameworks across SaaS applications.
      - name: Third-Party App Risk Management
        description: Identify and assess risk from third-party OAuth apps and browser extensions connected to critical SaaS platforms.
      - name: Security Operations Integration
        description: Pull SaaS security alerts and posture data into SIEM and SOAR platforms via the REST API for unified security operations workflows.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: SaaS security monitoring for Microsoft 365 suite including Exchange, Teams, SharePoint, and OneDrive.
      - name: Salesforce
        description: Security posture monitoring and misconfiguration detection for Salesforce CRM.
      - name: Slack
        description: Configuration monitoring and security checks for Slack workspace settings.
      - name: Zoom
        description: Security configuration monitoring for Zoom video conferencing accounts.
      - name: Okta
        description: Identity provider integration for user access and authentication configuration monitoring.
      - name: Datadog
        description: Sends SaaS posture alerts as Datadog Events via OAuth integration.
      - name: Splunk
        description: Splunk add-on for ingesting Adaptive Shield security events and alerts.
      - name: CrowdStrike Falcon
        description: Native integration with CrowdStrike Falcon platform following acquisition.
maintainers:
  - FN: Kin Lane
    X-twitter: apievangelist
    email: info@apievangelist.com
---
