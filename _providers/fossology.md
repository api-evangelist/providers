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
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 85
  human_in_the_loop: 2
  name: Fossology Agentic Access
  operation_count: 167
  slug: fossology-agentic-access
  summary_line: 167 operations · 85 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Administrator tasks
  name: FOSSology Admin API
  slug: fossology-admin-api
- description: Authentication endpoints
  name: FOSSology auth API
  slug: fossology-auth-api
- description: Copyright information
  name: FOSSology Copyrights API
  slug: fossology-copyrights-api
- description: Folder management
  name: FOSSology Folders API
  slug: fossology-folders-api
- description: User group management
  name: FOSSology Groups API
  slug: fossology-groups-api
- description: Basic info about API
  name: FOSSology info API
  slug: fossology-info-api
- description: FOSSology jobs
  name: FOSSology Job API
  slug: fossology-job-api
- description: License and obligation management
  name: FOSSology License API
  slug: fossology-license-api
- description: Maintenance operations
  name: FOSSology Maintenance API
  slug: fossology-maintenance-api
- description: Endpoints for organization of data
  name: FOSSology Organize API
  slug: fossology-organize-api
- description: Overview of FOSSology operations
  name: FOSSology Overview API
  slug: fossology-overview-api
- description: Upload's report
  name: FOSSology Report API
  slug: fossology-report-api
- description: Searching data on FOSSology
  name: FOSSology Search API
  slug: fossology-search-api
- description: Endpoints related to uploads
  name: FOSSology Upload API
  slug: fossology-upload-api
- description: User management
  name: FOSSology User API
  slug: fossology-user-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FOSSology Admin API
  slug: open-fossology-admin-api
- collection_type: open
  name: FOSSology Admin auth API
  slug: open-fossology-auth-api
- collection_type: open
  name: FOSSology Admin Copyrights API
  slug: open-fossology-copyrights-api
- collection_type: open
  name: FOSSology Admin Folders API
  slug: open-fossology-folders-api
- collection_type: open
  name: FOSSology Admin Groups API
  slug: open-fossology-groups-api
- collection_type: open
  name: FOSSology Admin info API
  slug: open-fossology-info-api
- collection_type: open
  name: FOSSology Admin Job API
  slug: open-fossology-job-api
- collection_type: open
  name: FOSSology Admin License API
  slug: open-fossology-license-api
- collection_type: open
  name: FOSSology Admin Maintenance API
  slug: open-fossology-maintenance-api
- collection_type: open
  name: FOSSology Admin Organize API
  slug: open-fossology-organize-api
- collection_type: open
  name: FOSSology Admin Overview API
  slug: open-fossology-overview-api
- collection_type: open
  name: FOSSology Admin Report API
  slug: open-fossology-report-api
- collection_type: open
  name: FOSSology Admin Search API
  slug: open-fossology-search-api
- collection_type: open
  name: FOSSology Admin Upload API
  slug: open-fossology-upload-api
- collection_type: open
  name: FOSSology Admin User API
  slug: open-fossology-user-api
- collection_type: open
  name: FOSSology API
  slug: open-fossology
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/fossology/fossology/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/fossology/fossology/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/fossology/fossology/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fossology-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fossology-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fossology-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fossology-scopes.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.fossology.org/get-started/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/fossology
- group: other
  title: ''
  type: Wiki
  url: https://github.com/fossology/fossology/wiki
- group: commercial
  title: ''
  type: License
  url: https://github.com/fossology/fossology/blob/master/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://www.fossology.org/feed/
created: '2026-03-16'
description: FOSSology is a Linux Foundation project providing open source license compliance software that scans source code for licenses, copyrights, and export control information. It helps organizations manage their open source license obligations through automated scanning, human clearing workflows, and SPDX/compliance reporting via a self-hosted REST API.
examples:
- key_count: 7
  name: Fossology License Example
  slug: fossology-license-example
- key_count: 12
  name: Fossology Upload Example
  slug: fossology-upload-example
finops:
- name: Fossology Finops
  service_category: API
  slug: fossology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fossology.png
json_schemas:
- name: FOSSologyJob
  property_count: 8
  slug: fossology-job
- name: FOSSologyLicense
  property_count: 8
  slug: fossology-license
- name: FOSSologyUpload
  property_count: 12
  slug: fossology-upload
jsonld:
- class_count: 11
  name: Fossology Context
  property_count: 0
  slug: fossology-context
layout: provider
modified: '2026-05-19'
name: FOSSology
nav: Providers
network: true
overview: 'FOSSology publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Admin API, auth API, Copyrights API, and 12 more. Tagged areas include Compliance, Licensing, Linux Foundation, Scanning, and SPDX.


  The FOSSology catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  FOSSology''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Fossology Plans Pricing
  plan_count: 3
  slug: fossology-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Fossology Rate Limits
  slug: fossology-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FOSSology API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fossology-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: FOSSology API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: fossology-rules
scopes:
- name: Fossology Scopes
  scope_count: 2
  slug: fossology-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 63.1
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 50.0
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fossology/refs/heads/main/screenshots/fossology-2026-06-20T181450.png
security:
- kind: authentication
  name: Fossology Authentication
  slug: fossology-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Fossology Domain Security
  slug: fossology-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: fossology
tags:
- Compliance
- Licensing
- Linux Foundation
- Scanning
- SPDX
- Open-Source
---
