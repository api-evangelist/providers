---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Drive Agentic Access
  operation_count: 8
  slug: google-drive-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: The Files API from Google Drive — 4 operation(s) for files.
  name: Google Drive Files API
  slug: google-drive-files-api
arazzos:
- description: Resolve a file, copy it into an archive folder, verify the backup exists, and only then permanently delete the original.
  name: Google Drive Back Up a File Before Permanently Deleting It
  slug: google-drive-backup-and-delete-workflow
- description: Resolve a template file, copy it into a destination folder under a new name, and read the copy back.
  name: Google Drive Copy a Template File into a Folder
  slug: google-drive-copy-template-workflow
- description: Create a folder, create a file inside it, and read the file back to confirm placement.
  name: Google Drive Provision a Folder and Seed a File
  slug: google-drive-provision-folder-workflow
- description: Verify a file, audit who already has access, grant a new permission, and confirm the resulting access list.
  name: Google Drive Share a File and Audit Its Access
  slug: google-drive-share-file-workflow
- description: Find a file by name within a folder and update it if it exists, otherwise create it.
  name: Google Drive Upsert a File by Name
  slug: google-drive-upsert-file-by-name-workflow
artifact_total: 36
collections:
- collection_type: open
  name: Google Drive API
  slug: open-google-drive
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-drive-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-drive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-drive-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-drive-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-drive-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-drive-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-drive-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-drive-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/google-drive-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-drive-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-drive-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-drive-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-drive-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-drive-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-drive-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/google-drive-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-drive-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-drive-upsert-file-by-name-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-drive-provision-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-drive-share-file-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-drive-copy-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-drive-backup-and-delete-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://console.cloud.google.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/drive/api/v3/enable-drive-api
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/drive/api/v3/releases
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.google.com/drive/api/v3/handle-errors#rate-limit-exceeded
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-drive-context.jsonld
created: '2024-01-15'
description: The Google Drive API allows developers to integrate with Google Drive to create, read, update, and delete files and folders stored in Google Drive. The v3 REST API supports file metadata operations, content upload and download, folder hierarchies, sharing and permissions, and search across a user's Drive.
features:
- 'Google Drive (and Workspace): hundreds of services across File Storage and Productivity'
- 'Detailed pricing: see https://workspace.google.com/pricing.html'
- 'Service: Drive API v3'
- 'Service: Drive Activity API'
- 'Service: Docs API'
- 'Service: Sheets API'
- 'Service: Slides API'
- 'Service: Forms API'
- 'Service: Apps Script'
- 'Service: Workspace Marketplace API'
- 'Service: Drive Labels API'
finops:
- name: Google Drive Finops
  service_category: File Storage and Productivity
  slug: google-drive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-drive.png
json_schemas:
- name: Google Drive File
  property_count: 14
  slug: google-drive-file
- name: FileList
  property_count: 2
  slug: google-drive-filelist
- name: Permission
  property_count: 5
  slug: google-drive-permission
- name: PermissionList
  property_count: 2
  slug: google-drive-permissionlist
json_structures:
- name: Google Drive Structure
  property_count: 0
  slug: google-drive-structure
jsonld:
- class_count: 18
  name: Google Drive Context
  property_count: 0
  slug: google-drive-context
layout: provider
mcp_servers:
- description: ''
  name: google-drive-mcp.yml
  slug: google-drive-mcpyml
modified: '2026-06-20'
name: Google Drive
nav: Providers
network: true
overview: 'Google Drive publishes 1 API on the [APIs.io](https://apis.io/) network: Files API. Tagged areas include Cloud Storage, Collaboration, Document Management, Drive, and Files.


  The Google Drive catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Drive''s developer surface includes authentication, changelog, developer portal, getting-started guide, and 26 more developer resources.'
plans:
- name: Google Drive Plans Pricing
  plan_count: 3
  slug: google-drive-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 2
  name: Google Drive Rate Limits
  slug: google-drive-rate-limits
rules:
- name: Google Drive API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-drive-jsonschema-spectral-rules
- name: Google Drive API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 5
  slug: google-drive-spectral-rules
scopes:
- name: Google Drive Scopes
  scope_count: 13
  slug: google-drive-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 58.6
  delta: 4.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 62.8
    developer_ergonomics: 39.1
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 57.9
  previous_composite: 54.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-drive/refs/heads/main/screenshots/google-drive-2026-06-20T182159.png
security:
- kind: authentication
  name: Google Drive Authentication
  slug: google-drive-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Google Drive Domain Security
  slug: google-drive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Drive Vulnerability Disclosure
  slug: google-drive-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Drive Trust Center
  slug: google-drive-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, PCI DSS, HIPAA, FedRAMP, GDPR
slug: google-drive
tags:
- Cloud Storage
- Collaboration
- Document Management
- Drive
- Files
- Google
- Storage
website: https://console.cloud.google.com/
---
