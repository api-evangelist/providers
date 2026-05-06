---
name: Microsoft Defender
description: Collection of Microsoft Defender security APIs for threat protection, endpoint security, and security operations.
image: https://www.microsoft.com/favicon.ico
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.18'
url: https://raw.githubusercontent.com/api-evangelist/microsoft-defender/refs/heads/main/apis.yml
apis:
  - name: Microsoft Defender for Endpoint API
    description: API for endpoint detection and response, threat and vulnerability management, and automated investigation and remediation.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/
    baseUrl: https://api.securitycenter.microsoft.com/api
    tags:
      - EDR
      - Endpoint Security
      - Threat Detection
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/apis-intro
      - type: OpenAPI
        url: openapi/microsoft-defender-for-endpoint-api-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-defender-alert-schema.json
      - type: JSONLD
        url: json-ld/microsoft-defender-context.jsonld
      - type: Authentication
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/exposed-apis-create-app-webapp
      - type: Pricing
        url: https://www.microsoft.com/en-us/security/business/endpoint-security/microsoft-defender-endpoint-pricing
      - type: API Reference
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/exposed-apis-list
      - type: Release Notes
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/api-release-notes
      - type: Management APIs
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/management-apis
      - type: Alerts API
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/get-alerts
      - type: Vulnerabilities API
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/get-all-vulnerabilities
      - type: Security Recommendations API
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/get-security-recommendations
    contact:
      - type: Support
        url: https://learn.microsoft.com/en-us/defender-endpoint/api/troubleshoot-api
  - name: Microsoft Defender for Cloud Apps API
    description: Cloud Access Security Broker (CASB) API for discovering, investigating, and governing cloud apps.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/defender-cloud-apps/
    baseUrl: https://portal.cloudappsecurity.com/api
    tags:
      - CASB
      - Cloud Security
      - Data Protection
      - Shadow IT
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/defender-cloud-apps/api-introduction
      - type: Authentication
        url: https://learn.microsoft.com/en-us/defender-cloud-apps/api-authentication
      - type: Activities API
        url: https://learn.microsoft.com/en-us/defender-cloud-apps/api-activities
      - type: Alerts API
        url: https://learn.microsoft.com/en-us/defender-cloud-apps/api-alerts
      - type: Entities API
        url: https://learn.microsoft.com/en-us/defender-cloud-apps/api-entities
      - type: Cloud Discovery API
        url: https://learn.microsoft.com/en-us/defender-cloud-apps/api-discovery
  - name: Microsoft Defender Threat Intelligence API
    description: Access threat intelligence data, indicators of compromise (IOCs), and threat analytics.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/defender/threat-intelligence/
    baseUrl: https://graph.microsoft.com/v1.0/security/threatIntelligence
    tags:
      - IOC
      - Security Intelligence
      - Threat Analytics
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-threatintelligence-overview
      - type: API Reference
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
  - name: Microsoft Graph Security API
    description: Unified API for Microsoft security products including Defender alerts, secure scores, and security actions.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/graph/security-concept-overview
    baseUrl: https://graph.microsoft.com/v1.0/security
    tags:
      - Alerts
      - Secure Score
      - Security Graph
      - Threat Protection
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview
      - type: OpenAPI
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Code Samples
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview#common-use-cases
  - name: Microsoft Defender for Office 365 API
    description: API for email and collaboration protection including anti-phishing, anti-malware, and safe attachments.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/
    baseUrl: https://graph.microsoft.com/v1.0/security
    tags:
      - Collaboration Security
      - Email Security
      - Phishing Protection
      - Safe Attachments
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/defender-for-office-365
      - type: Threat Protection
        url: https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/threat-explorer
      - type: Safe Links
        url: https://learn.microsoft.com/en-us/defender-office-365/safe-links-about
      - type: Safe Attachments
        url: https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-about
      - type: Service Description
        url: https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description
  - name: Microsoft Defender XDR API
    description: Unified extended detection and response API for automating workflows based on shared incident and advanced hunting tables across Microsoft security products.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/defender-xdr/api-overview
    baseUrl: https://api.security.microsoft.com/api
    tags:
      - Advanced Hunting
      - Event Streaming
      - Incidents
      - Threat Protection
      - XDR
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/defender-xdr/api-overview
      - type: API Reference
        url: https://learn.microsoft.com/en-us/defender-xdr/api-supported
      - type: Authentication
        url: https://learn.microsoft.com/en-us/defender-xdr/api-access
      - type: Incidents API
        url: https://learn.microsoft.com/en-us/defender-xdr/api-incident
      - type: Advanced Hunting API
        url: https://learn.microsoft.com/en-us/defender-xdr/api-advanced-hunting
      - type: Streaming API
        url: https://learn.microsoft.com/en-us/defender-xdr/streaming-api
      - type: Supported Event Types
        url: https://learn.microsoft.com/en-us/defender-xdr/supported-event-types
      - type: Error Codes
        url: https://learn.microsoft.com/en-us/defender-xdr/api-error-codes
  - name: Microsoft Defender for Cloud REST API
    description: REST API for unified security management and advanced threat protection across hybrid cloud workloads in Azure, other clouds, and on-premises.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction
    baseUrl: https://management.azure.com
    tags:
      - Azure Security
      - Cloud Security
      - CSPM
      - Security Posture
      - Workload Protection
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/defender-for-cloud/get-started
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/
      - type: Release Notes
        url: https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes
  - name: Microsoft Defender for Identity API
    description: API for identity-based attack detection and investigation across on-premises Active Directory and hybrid environments, with sensor management via Microsoft Graph.
    image: https://www.microsoft.com/favicon.ico
    humanUrl: https://learn.microsoft.com/en-us/defender-for-identity/
    baseUrl: https://graph.microsoft.com/v1.0/security/identities
    tags:
      - Active Directory
      - Identity Security
      - Identity Threat Detection
      - Sensor Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/defender-for-identity/
      - type: Overview
        url: https://learn.microsoft.com/en-us/defender-for-identity/what-is
      - type: Architecture
        url: https://learn.microsoft.com/en-us/defender-for-identity/architecture
      - type: Graph Security API
        url: https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://security.microsoft.com
  - type: Documentation Hub
    url: https://learn.microsoft.com/en-us/microsoft-365/security/
  - type: Status Page
    url: https://status.azure.com/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Developer Changelog
    url: https://developer.microsoft.com/en-us/changelog
  - type: Security Blog
    url: https://www.microsoft.com/en-us/security/blog/
  - type: Microsoft Graph Explorer
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  - type: Authentication Overview
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Security Pricing Overview
    url: https://www.microsoft.com/en-us/security/pricing-overview
---
