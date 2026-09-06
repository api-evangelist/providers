---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.cloudally.com'', ''status'': 301, ''note'': ''declared website redirects to https://cybersecurity.opentext.com/legacy/cloudally/ — a different registrable domain (cloudally.com -> opentext.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cloudally Agentic Access
  operation_count: 14
  slug: cloudally-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.cloudally.com
  baseurl_source: declared
  description: Token issuance and refresh.
  name: CloudAlly Authentication API
  slug: cloudally-authentication-api
- baseURL: https://api.cloudally.com
  baseurl_source: declared
  description: Backup tasks and status.
  name: CloudAlly Backups API
  slug: cloudally-backups-api
- baseURL: https://api.cloudally.com
  baseurl_source: declared
  description: Billing and invoicing data.
  name: CloudAlly Billing API
  slug: cloudally-billing-api
- baseURL: https://api.cloudally.com
  baseurl_source: declared
  description: Partner-portal account, billing, and reseller endpoints.
  name: CloudAlly Partners API
  slug: cloudally-partners-api
- baseURL: https://api.cloudally.com
  baseurl_source: declared
  description: Restore and download requests.
  name: CloudAlly Restore API
  slug: cloudally-restore-api
- baseURL: https://api.cloudally.com
  baseurl_source: declared
  description: Long-running task status.
  name: CloudAlly Tasks API
  slug: cloudally-tasks-api
- baseURL: https://api.cloudally.com
  baseurl_source: declared
  description: User and account management.
  name: CloudAlly Users API
  slug: cloudally-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CloudAlly Authentication API
  slug: open-cloudally-authentication-api
- collection_type: open
  name: CloudAlly Authentication Backups API
  slug: open-cloudally-backups-api
- collection_type: open
  name: CloudAlly Authentication Billing API
  slug: open-cloudally-billing-api
- collection_type: open
  name: CloudAlly Authentication Partners API
  slug: open-cloudally-partners-api
- collection_type: open
  name: CloudAlly Authentication Restore API
  slug: open-cloudally-restore-api
- collection_type: open
  name: CloudAlly Authentication Tasks API
  slug: open-cloudally-tasks-api
- collection_type: open
  name: CloudAlly Authentication Users API
  slug: open-cloudally-users-api
- collection_type: open
  name: CloudAlly API
  slug: open-cloudally
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudally-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudally-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudally-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudally-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudally
- group: company
  title: ''
  type: Website
  url: https://www.cloudally.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.cloudally.com/documentation
- group: operate
  title: ''
  type: Support
  url: https://support.cloudally.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudally.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudally.com/privacy-policy/
- group: other
  title: ''
  type: ParentCompany
  url: https://cybersecurity.opentext.com/legacy/cloudally/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cloudally-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cloudally-backup-task-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cloudally-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudally-rules.yml
created: '2026-03-27'
description: CloudAlly (now part of OpenText Cybersecurity) is a SaaS backup and recovery service that protects business data in Microsoft 365, Google Workspace, Salesforce, Box, Dropbox, SharePoint, and OneDrive. The platform offers automated daily backups, point-in-time restore, cross-user restore, granular search, and partner-portal multitenancy features. Beyond the web console, CloudAlly exposes a REST API at api.cloudally.com that lets administrators and partners automate backup-task management, restore/download requests, user provisioning, partner-portal operations, and billing reporting.
finops:
- name: Cloudally Finops
  service_category: API
  slug: cloudally-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudally.png
json_schemas:
- name: CloudAlly Backup Task
  property_count: 8
  slug: cloudally-backup-task
jsonld:
- class_count: 4
  name: Cloudally Context
  property_count: 8
  slug: cloudally-context
layout: provider
modified: '2026-05-19'
name: CloudAlly
nav: Providers
network: true
overview: 'CloudAlly publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Backups API, Billing API, and 4 more. Tagged areas include Backup, Box, Data Protection, Disaster Recovery, and Dropbox.


  The CloudAlly catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CloudAlly''s developer surface includes authentication, documentation, support, and 12 more developer resources.'
plans:
- name: Cloudally Plans Pricing
  plan_count: 3
  slug: cloudally-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Cloudally Rate Limits
  slug: cloudally-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CloudAlly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cloudally-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: CloudAlly API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: cloudally-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 55.5
    catalog_earned_first_party: 0.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 54.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudally/refs/heads/main/screenshots/cloudally-2026-06-20T174540.png
security:
- kind: authentication
  name: Cloudally Authentication
  slug: cloudally-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudally Domain Security
  slug: cloudally-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloudally Trust Center
  slug: cloudally-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: cloudally
tags:
- Backup
- Box
- Data Protection
- Disaster Recovery
- Dropbox
- Google Workspace
- Microsoft-365
- OpenText
- SaaS Backup
- Salesforce
website: https://www.cloudally.com
---
