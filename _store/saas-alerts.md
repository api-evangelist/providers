---
aid: saas-alerts
name: SaaS Alerts
description: SaaS Alerts is a SaaS security monitoring platform purpose-built for Managed Service Providers (MSPs). The platform detects anomalous user behavior, data exfiltration, account compromise, and unauthorized access across cloud applications including Microsoft 365, Google Workspace, Salesforce, Slack, and Dropbox. Key capabilities include machine learning-based threat detection, automated remediation workflows, multi-tenant MSP management, and integration with PSA and RMM platforms. SaaS Alerts was acquired by Kaseya in 2023.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/saas-alerts/refs/heads/main/apis.yml
tags:
  - MSP
  - SaaS Security
  - Security Monitoring
  - Threat Detection
  - Microsoft 365
  - Google Workspace
  - MSSP
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: saas-alerts:saas-alerts
    name: SaaS Alerts API
    description: REST API (v0.20.0) providing programmatic access to the SaaS Alerts security monitoring platform. Enables MSP tools and SIEM/SOAR integrations to query security events, retrieve alerts, and access monitored user and customer data. Eight API methods including GET and POST operations for event querying and reporting. Authentication uses API keys generated in the management interface.
    humanURL: https://help.saasalerts.kaseya.com/help/Content/How-To/using-the-saas-alerts-api.htm
    baseURL: https://api.saasalerts.com
    tags:
      - SaaS Security
      - Events
      - Alerts
      - MSP
    properties:
      - type: Documentation
        url: https://help.saasalerts.kaseya.com/help/Content/How-To/using-the-saas-alerts-api.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/saas-alerts/refs/heads/main/openapi/saas-alerts-openapi.yml
      - type: SwaggerHub
        url: https://app.swaggerhub.com/apis/SaaS_Alerts/functions/0.20.0
      - type: Authentication
        url: https://help.saasalerts.kaseya.com/help/Content/How-To/using-the-saas-alerts-api.htm
common:
  - type: Website
    url: https://www.saasalerts.com
  - type: Documentation
    url: https://help.saasalerts.kaseya.com/help/Content/Home/saas-alerts-msp-admin-guide.htm
  - type: APIDocumentation
    url: https://help.saasalerts.kaseya.com/help/Content/How-To/using-the-saas-alerts-api.htm
  - type: Blog
    url: https://www.saasalerts.com/blog
  - type: PlatformOverview
    url: https://saasalerts.com/platform-overview-for-msps/
  - type: Integrations
    url: https://saasalerts.com/msp-tools/
  - type: PrivacyPolicy
    url: https://www.saasalerts.com/privacy-policy
  - type: TermsOfService
    url: https://www.saasalerts.com/terms
  - type: Login
    url: https://app.saasalerts.com
  - type: Pricing
    url: https://www.saasalerts.com/pricing
features:
  - Anomalous Login Detection
  - Data Exfiltration Monitoring
  - OAuth Permission Monitoring
  - Email Forwarding Rule Detection
  - Impossible Travel Detection
  - Brute Force Attack Detection
  - MFA Monitoring
  - Multi-tenant MSP Console
  - Automated Remediation
  - Custom Alert Policies
solutions:
  - MSP Security Services
  - SaaS Application Security
  - Insider Threat Detection
  - Account Compromise Response
  - Compliance Monitoring
integrations:
  - Microsoft 365
  - Google Workspace
  - Salesforce
  - Slack
  - Dropbox
  - Kaseya BMS
  - Autotask
  - ConnectWise Manage
  - Datto RMM
  - N-able N-central
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
