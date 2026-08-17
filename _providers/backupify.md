---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Backupify Agentic Access
  operation_count: 3
  slug: backupify-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: SaaS domain and customer account management
  name: Backupify Domains API
  slug: backupify-domains-api
- description: User and resource seat licensing and management
  name: Backupify Seats API
  slug: backupify-seats-api
artifact_total: 54
collections:
- collection_type: postman
  name: Backupify SaaS Protection Domains API
  slug: postman-backupify-domains-api
- collection_type: postman
  name: Backupify SaaS Protection Domains Seats API
  slug: postman-backupify-seats-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Backupify SaaS Protection Domains API
  slug: open-backupify-domains-api
- collection_type: open
  name: Backupify SaaS Protection Domains Seats API
  slug: open-backupify-seats-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/backupify/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/backupify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backupify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/backupify-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/backupify
- group: company
  title: ''
  type: Website
  url: https://www.backupify.com
- group: docs
  title: ''
  type: Documentation
  url: https://saasprotection.datto.com/help/M365/Content/Other_Administrative_Tasks/using-rest-api-saas-protection.htm
- group: start
  title: ''
  type: Portal
  url: https://portal.dattobackup.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.backupify.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.datto.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.datto.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datto.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datto.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/backupify
- group: design
  title: ''
  type: SpectralRules
  url: rules/backupify-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/backupify-vocabulary.yaml
created: '2026-03-27'
description: Backupify (by Datto/Kaseya) is a SaaS backup platform providing automated cloud-to-cloud data protection for Google Workspace and Microsoft 365. It offers seat-level backup coverage for users, shared mailboxes, SharePoint sites, team sites, and Microsoft Teams. The SaaS Protection REST API enables MSPs and enterprise IT teams to automate domain administration and seat licensing programmatically.
examples:
- key_count: 1
  name: Saas Protection Api Bulk Seat Change Request Example
  slug: saas-protection-api-bulk-seat-change-request-example
- key_count: 1
  name: Saas Protection Api Bulk Seat Change Response Example
  slug: saas-protection-api-bulk-seat-change-response-example
- key_count: 4
  name: Saas Protection Api Domain Example
  slug: saas-protection-api-domain-example
- key_count: 1
  name: Saas Protection Api Domains Response Example
  slug: saas-protection-api-domains-response-example
- key_count: 3
  name: Saas Protection Api Seat Change Example
  slug: saas-protection-api-seat-change-example
- key_count: 3
  name: Saas Protection Api Seat Change Result Example
  slug: saas-protection-api-seat-change-result-example
- key_count: 6
  name: Saas Protection Api Seat Example
  slug: saas-protection-api-seat-example
- key_count: 1
  name: Saas Protection Api Seats Response Example
  slug: saas-protection-api-seats-response-example
features:
- description: Automated cloud-to-cloud backup for Exchange, OneDrive, SharePoint, and Teams.
  name: Microsoft 365 Backup
- description: Automated backup for Gmail, Drive, Contacts, and Calendar.
  name: Google Workspace Backup
- description: License, unlicense, or pause backup at the individual user, mailbox, site, or team level.
  name: Seat-Level Control
- description: Manage up to 100 seat changes in a single API call.
  name: Bulk Seat Management
- description: Manage backup across multiple customer domains from a single pane of glass.
  name: MSP Multi-Tenant
- description: Restore data to any point in time with granular item-level recovery.
  name: Point-in-Time Recovery
finops:
- name: Backupify Finops
  service_category: API
  slug: backupify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/backupify.png
integrations:
- description: Native integration with Exchange Online, OneDrive, SharePoint, and Microsoft Teams.
  name: Microsoft 365
- description: Native integration with Gmail, Google Drive, Contacts, and Calendar.
  name: Google Workspace
- description: Integration with Kaseya RMM for MSP workflow automation.
  name: Kaseya VSA
- description: Integration with Datto RMM for endpoint and SaaS backup orchestration.
  name: Datto RMM
json_schemas:
- name: BulkSeatChangeRequest
  property_count: 1
  slug: saas-protection-api-bulk-seat-change-request
- name: BulkSeatChangeResponse
  property_count: 1
  slug: saas-protection-api-bulk-seat-change-response
- name: Domain
  property_count: 4
  slug: saas-protection-api-domain
- name: DomainsResponse
  property_count: 1
  slug: saas-protection-api-domains-response
- name: SeatChangeResult
  property_count: 3
  slug: saas-protection-api-seat-change-result
- name: SeatChange
  property_count: 3
  slug: saas-protection-api-seat-change
- name: Seat
  property_count: 6
  slug: saas-protection-api-seat
- name: SeatsResponse
  property_count: 1
  slug: saas-protection-api-seats-response
json_structures:
- name: Saas Protection Api Bulk Seat Change Request Structure
  property_count: 1
  slug: saas-protection-api-bulk-seat-change-request-structure
- name: Saas Protection Api Bulk Seat Change Response Structure
  property_count: 1
  slug: saas-protection-api-bulk-seat-change-response-structure
- name: Saas Protection Api Domain Structure
  property_count: 4
  slug: saas-protection-api-domain-structure
- name: Saas Protection Api Domains Response Structure
  property_count: 1
  slug: saas-protection-api-domains-response-structure
- name: Saas Protection Api Seat Change Result Structure
  property_count: 3
  slug: saas-protection-api-seat-change-result-structure
- name: Saas Protection Api Seat Change Structure
  property_count: 3
  slug: saas-protection-api-seat-change-structure
- name: Saas Protection Api Seat Structure
  property_count: 6
  slug: saas-protection-api-seat-structure
- name: Saas Protection Api Seats Response Structure
  property_count: 1
  slug: saas-protection-api-seats-response-structure
jsonld:
- class_count: 8
  name: Backupify Context
  property_count: 16
  slug: backupify-context
layout: provider
modified: '2026-05-19'
name: Backupify
nav: Providers
network: true
overview: 'Backupify publishes 2 APIs on the [APIs.io](https://apis.io/) network: Domains API and Seats API. Tagged areas include SaaS Backup, Data Protection, Cloud Backup, Microsoft 365, and Google Workspace.


  The Backupify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Backupify''s developer surface includes authentication, documentation, developer portal, pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Backupify Plans Pricing
  plan_count: 3
  slug: backupify-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Backupify Rate Limits
  slug: backupify-rate-limits
rules:
- name: Backupify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: backupify-jsonschema-spectral-rules
- name: Backupify API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: backupify-spectral-rules
score:
  band: thin
  composite: 39.3
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 24.3
    developer_ergonomics: 39.1
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backupify/refs/heads/main/screenshots/backupify-2026-06-20T172919.png
security:
- kind: authentication
  name: Backupify Authentication
  slug: backupify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Backupify Domain Security
  slug: backupify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backupify
tags:
- SaaS Backup
- Data Protection
- Cloud Backup
- Microsoft 365
- Google Workspace
use_cases:
- description: Protect Microsoft 365 and Google Workspace data from accidental deletion, ransomware, and insider threats.
  name: SaaS Data Protection
- description: Automate backup seat provisioning and de-provisioning across multiple customer tenants.
  name: MSP Backup Management
- description: Maintain immutable backups for compliance, legal hold, and audit requirements.
  name: Compliance and Archival
- description: Backup source data before and during cloud-to-cloud migrations.
  name: Migration Support
website: https://www.backupify.com
---
