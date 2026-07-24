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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cloudally Agentic Access
  operation_count: 14
  slug: cloudally-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 7
apis:
- description: Token issuance and refresh.
  name: CloudAlly Authentication API
  slug: cloudally-authentication-api
- description: Backup tasks and status.
  name: CloudAlly Backups API
  slug: cloudally-backups-api
- description: Billing and invoicing data.
  name: CloudAlly Billing API
  slug: cloudally-billing-api
- description: Partner-portal account, billing, and reseller endpoints.
  name: CloudAlly Partners API
  slug: cloudally-partners-api
- description: Restore and download requests.
  name: CloudAlly Restore API
  slug: cloudally-restore-api
- description: Long-running task status.
  name: CloudAlly Tasks API
  slug: cloudally-tasks-api
- description: User and account management.
  name: CloudAlly Users API
  slug: cloudally-users-api
artifact_total: 19
collections:
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
  url: openapi/cloudally-openapi.yml
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
random_paper: 0
rate_limits:
- limit_count: 5
  name: Cloudally Rate Limits
  slug: cloudally-rate-limits
rules:
- name: CloudAlly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cloudally-jsonschema-spectral-rules
- name: CloudAlly API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: cloudally-rules
score:
  band: developing
  composite: 52.3
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 56.5
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 52.3
  schema_version: 0.5
  scored_at: '2026-07-23'
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
- Microsoft 365
- OpenText
- SaaS Backup
- Salesforce
website: https://www.cloudally.com
---
