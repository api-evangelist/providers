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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Spanning Agentic Access
  operation_count: 9
  slug: spanning-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- description: RESTful API for managing Spanning Backup for Microsoft 365. Region-specific endpoints (US, EU, AP, CA, UK) for user license management and data export operations. Authentication uses API tokens obtain
  name: Spanning Backup for Microsoft 365 API
  slug: spanning-microsoft365-api
- description: Data export management operations
  name: Spanning Exports API
  slug: spanning-exports-api
- description: Shared drive backup and export operations
  name: Spanning Shared Drives API
  slug: spanning-shared-drives-api
- description: User backup license management operations
  name: Spanning Users API
  slug: spanning-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spanning Backup for Google Workspace Exports API
  slug: open-spanning-exports-api
- collection_type: open
  name: Spanning Backup for Google Workspace API
  slug: open-spanning-google-workspace-api
- collection_type: open
  name: Spanning Backup for Google Workspace Exports Shared Drives API
  slug: open-spanning-shared-drives-api
- collection_type: open
  name: Spanning Backup for Google Workspace Exports Users API
  slug: open-spanning-users-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/SpanningCloudApps/SB365-Powershell/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/SpanningCloudApps/SB365-Powershell/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/SpanningCloudApps/SB365-Powershell/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spanning-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spanning-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spanning-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spanning-cloud-apps
- group: company
  title: ''
  type: Website
  url: https://spanning.com
- group: docs
  title: ''
  type: Documentation
  url: https://spanning.com/resources
- group: docs
  title: ''
  type: APIReference
  url: https://api.spanningbackup.com/index.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SpanningCloudApps
- group: commercial
  title: ''
  type: Pricing
  url: https://spanning.com/pricing/
created: '2026-03-27'
description: Spanning (by Kaseya) is a SaaS backup and recovery platform providing cloud-to-cloud data protection for Microsoft 365, Google Workspace, and Salesforce. It protects over 24,000 organizations and 2.5 million users with automated daily backups, unlimited on-demand backups, infinite retention, and granular point-in-time restore. Spanning exposes RESTful APIs for managing user licenses and exporting backed-up account data for Google Workspace and Microsoft 365.
examples:
- key_count: 4
  name: Spanning List Users Example
  slug: spanning-list-users-example
finops:
- name: Spanning Finops
  service_category: API
  slug: spanning-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spanning.png
json_schemas:
- name: Spanning Backup User
  property_count: 8
  slug: spanning-user
json_structures:
- name: Spanning User Structure
  property_count: 0
  slug: spanning-user-structure
jsonld:
- class_count: 10
  name: Spanning Context
  property_count: 11
  slug: spanning-context
layout: provider
modified: '2026-05-19'
name: Spanning
nav: Providers
network: true
overview: 'Spanning publishes 3 APIs on the [APIs.io](https://apis.io/) network: Exports API, Shared Drives API, and Users API. Tagged areas include Data Protection, SaaS Backup, Cloud Backup, Microsoft-365, and Google Workspace.


  The Spanning catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spanning''s developer surface includes authentication, documentation, API reference, GitHub presence, pricing, and 7 more developer resources.'
plans:
- name: Spanning Plans Pricing
  plan_count: 3
  slug: spanning-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Spanning Rate Limits
  slug: spanning-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spanning API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spanning-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: Spanning API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 5
  slug: spanning-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 67.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spanning/refs/heads/main/screenshots/spanning-2026-06-20T194245.png
security:
- kind: authentication
  name: Spanning Authentication
  slug: spanning-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spanning Domain Security
  slug: spanning-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spanning
tags:
- Data Protection
- SaaS Backup
- Cloud Backup
- Microsoft-365
- Google Workspace
- Salesforce
website: https://spanning.com
---
