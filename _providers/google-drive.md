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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Drive Agentic Access
  operation_count: 8
  slug: google-drive-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The Files API from Google Drive — 4 operation(s) for files.
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
artifact_total: 38
collections:
- collection_type: open
  name: Google Drive Files API
  slug: open-google-drive-files-api
- collection_type: open
  name: Google Drive API
  slug: open-google-drive
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-drive/overview
- group: commercial
  href: https://artifacts.apis.io/google-drive/plans/google-drive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-drive-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/google-drive/finops/google-drive-finops.yml
  title: ''
  type: FinOps
  url: finops/google-drive-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: other
  href: https://artifacts.apis.io/google-drive/overlays/google-drive-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/google-drive-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/google-drive/agentic-access/google-drive-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-drive-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/security/google-drive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-drive-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/security/google-drive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-drive-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/security/google-drive-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/google-drive-trust-center.yml
- group: build
  href: https://artifacts.apis.io/google-drive/packages/google-drive-packages.yml
  title: ''
  type: Packages
  url: packages/google-drive-packages.yml
- group: agent
  href: https://artifacts.apis.io/google-drive/well-known/google-drive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-drive-well-known.yml
- group: agent
  href: https://artifacts.apis.io/google-drive/mcp/google-drive-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-drive-mcp.yml
- group: agent
  href: https://artifacts.apis.io/google-drive/llms/google-drive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-drive-llms.txt
- group: design
  href: https://artifacts.apis.io/google-drive/conformance/google-drive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-drive-conformance.yml
- group: design
  href: https://artifacts.apis.io/google-drive/errors/google-drive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-drive-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-drive/lifecycle/google-drive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-drive-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/scopes/google-drive-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-drive-scopes.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/authentication/google-drive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-drive-authentication.yml
- group: design
  href: https://artifacts.apis.io/google-drive/conventions/google-drive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-drive-conventions.yml
- group: operate
  href: https://artifacts.apis.io/google-drive/changelog/google-drive-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-drive-changelog.yml
- group: design
  href: https://artifacts.apis.io/google-drive/components/google-drive-components.yml
  title: ''
  type: Components
  url: components/google-drive-components.yml
- group: design
  href: https://artifacts.apis.io/google-drive/data-model/google-drive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-drive-data-model.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-upsert-file-by-name-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-upsert-file-by-name-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-provision-folder-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-provision-folder-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-share-file-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-share-file-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-copy-template-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-copy-template-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-backup-and-delete-workflow.yml
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
  href: https://artifacts.apis.io/google-drive/json-ld/google-drive-context.jsonld
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
- has_sources: true
  method: derived
  name: Google Drive Finops
  primary_unit: user
  service_category: ''
  slug: google-drive-finops
  template: false
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
- description: Google operates an official remote Model Context Protocol server for Google Drive (Developer Preview). It acts as a proxy that lets AI applications (e.g. Google Antigravity, Claude) read and act on Dr
  name: Google Drive MCP Server
  slug: google-drive
modified: '2026-06-20'
name: Google Drive
nav: Providers
network: true
overview: 'Google Drive publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Files API. Tagged areas include Cloud Storage, Collaboration, Document Management, Drives, and File.


  The Google Drive catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Drive''s developer surface includes authentication, changelog, developer portal, getting-started guide, and 31 more developer resources.'
plans:
- name: Google Drive Plans Pricing
  plan_count: 4
  slug: google-drive-plans-pricing
- name: Google Drive Price Estimates
  plan_count: 0
  slug: google-drive-price-estimates
random_paper: 20
rate_limits:
- limit_count: 2
  name: Google Drive Rate Limits
  slug: google-drive-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Drive — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-drive-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Drive API Rules
  rule_count: 17
  severity_counts:
    error: 10
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
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 71.9
    catalog_earned_first_party: 12.0
    catalog_gap: 43.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 53.8
    developer_ergonomics: 44.0
    discoverability: 65.0
    operational_transparency: 52.6
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/google-drive/google-drive-2026-08-17T083537.png
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
- Drives
- File
- Google
- Storage
website: https://www.google.com/
---
