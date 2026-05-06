---
aid: spanning
name: Spanning
description: Spanning (by Kaseya) is a SaaS backup and recovery platform providing cloud-to-cloud data protection for Microsoft 365, Google Workspace, and Salesforce. It protects over 24,000 organizations and 2.5 million users with automated daily backups, unlimited on-demand backups, infinite retention, and granular point-in-time restore. Spanning exposes RESTful APIs for managing user licenses and exporting backed-up account data for Google Workspace and Microsoft 365.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Protection
  - SaaS Backup
  - Cloud Backup
  - Microsoft 365
  - Google Workspace
  - Salesforce
url: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spanning:spanning-google-workspace-api
    name: Spanning Backup for Google Workspace API
    description: RESTful API for managing Spanning Backup for Google Workspace. Supports user license management (assign, unassign, list, get), shared drives backup management (list, export), and export operations (initiate, list, get). Authentication uses API tokens obtained from the Spanning admin portal Settings tab.
    humanURL: https://spanning.com/products/google-workspace-backup/
    baseURL: https://api.spanningbackup.com
    tags:
      - Data Protection
      - SaaS Backup
      - Google Workspace
      - Cloud Backup
    properties:
      - type: Documentation
        url: https://api.spanningbackup.com/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/openapi/spanning-google-workspace-api-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/rules/spanning-rules.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/json-schema/spanning-user-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/json-structure/spanning-user-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/json-ld/spanning-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/vocabulary/spanning-vocabulary.yml
  - aid: spanning:spanning-microsoft365-api
    name: Spanning Backup for Microsoft 365 API
    description: RESTful API for managing Spanning Backup for Microsoft 365. Region-specific endpoints (US, EU, AP, CA, UK) for user license management and data export operations. Authentication uses API tokens obtained from the Spanning admin portal.
    humanURL: https://spanning.com/products/microsoft-365-backup/
    baseURL: https://o365-us.spanningbackup.com
    tags:
      - Data Protection
      - SaaS Backup
      - Microsoft 365
      - Cloud Backup
    properties:
      - type: Documentation
        url: https://o365-docs.spanningbackup.com/
      - type: GitHubRepository
        url: https://github.com/SpanningCloudApps/SB365-Powershell
common:
  - type: Website
    url: https://spanning.com
  - type: Documentation
    url: https://spanning.com/resources
  - type: APIReference
    url: https://api.spanningbackup.com/index.html
  - type: GitHub
    url: https://github.com/SpanningCloudApps
  - type: Pricing
    url: https://spanning.com/pricing/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
