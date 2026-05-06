---
aid: cloudally
name: CloudAlly
url: https://raw.githubusercontent.com/api-evangelist/cloudally/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-27'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
x-type: company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backup
  - Box
  - Data Protection
  - Disaster Recovery
  - Dropbox
  - Google Workspace
  - Microsoft 365
  - OpenText
  - SaaS Backup
  - Salesforce
description: CloudAlly (now part of OpenText Cybersecurity) is a SaaS backup and recovery service that protects business data in Microsoft 365, Google Workspace, Salesforce, Box, Dropbox, SharePoint, and OneDrive. The platform offers automated daily backups, point-in-time restore, cross-user restore, granular search, and partner-portal multitenancy features. Beyond the web console, CloudAlly exposes a REST API at api.cloudally.com that lets administrators and partners automate backup-task management, restore/download requests, user provisioning, partner-portal operations, and billing reporting.
apis:
  - aid: cloudally:cloudally-api
    name: CloudAlly API
    tags:
      - Backup
      - Data Protection
      - Partner Portal
      - Restore
      - SaaS Backup
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://api.cloudally.com/documentation
    baseURL: https://api.cloudally.com
    properties:
      - url: https://api.cloudally.com/documentation
        type: Documentation
      - url: https://support.cloudally.com/
        type: Support
      - url: openapi/cloudally-openapi.yml
        type: OpenAPI
    description: The CloudAlly API is a JSON REST interface at api.cloudally.com. Partners authenticate by exchanging a Client ID and Client Secret at /auth/partner for an access token, while portal users sign in at /auth; the resulting token is presented as an Authorization Bearer header. Endpoints expose backup tasks, restore/download jobs, partner profile data, billing, resellers, and user management. The Partner Portal API today is read-oriented (GET), with administrative actions performed via the standard tenant endpoints.
common:
  - type: Website
    url: https://www.cloudally.com
  - type: Documentation
    url: https://api.cloudally.com/documentation
  - type: Support
    url: https://support.cloudally.com/
  - type: TermsOfService
    url: https://www.cloudally.com/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.cloudally.com/privacy-policy/
  - type: ParentCompany
    url: https://cybersecurity.opentext.com/legacy/cloudally/
  - type: OpenAPI
    url: openapi/cloudally-openapi.yml
  - type: JSONSchema
    url: json-schema/cloudally-backup-task-schema.json
  - type: JSONLDContext
    url: json-ld/cloudally-context.jsonld
  - type: Spectral
    url: rules/cloudally-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cloudally-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
