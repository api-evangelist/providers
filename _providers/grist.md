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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 75
  human_in_the_loop: 3
  name: Grist Agentic Access
  operation_count: 120
  slug: grist-agentic-access
  summary_line: 120 operations · 75 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Documents may include attached files. Data records can refer to these using a column of type `Attachments`.
  name: Grist attachments API
  slug: grist-attachments-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Tables are structured as a collection of columns.
  name: Grist columns API
  slug: grist-columns-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Work with table data, using a (now deprecated) columnar format. We now recommend the `records` endpoints.
  name: Grist data API
  slug: grist-data-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Workspaces contain collections of Grist documents.
  name: Grist docs API
  slug: grist-docs-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: The forms API from Grist — 1 operation(s) for forms.
  name: Grist forms API
  slug: grist-forms-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Team sites and personal spaces are called 'orgs' in the API.
  name: Grist orgs API
  slug: grist-orgs-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: The profile API from Grist — 4 operation(s) for profile.
  name: Grist profile API
  slug: grist-profile-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Tables contain collections of records (also called rows).
  name: Grist records API
  slug: grist-records-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Impersonations to manage grist resources through REST APIs with specific rights.
  name: Grist service accounts API
  slug: grist-service-accounts-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: The session API from Grist — 2 operation(s) for session.
  name: Grist session API
  slug: grist-session-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Sql endpoint to query data from documents.
  name: Grist sql API
  slug: grist-sql-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Documents are structured as a collection of tables.
  name: Grist tables API
  slug: grist-tables-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: The templates API from Grist — 2 operation(s) for templates.
  name: Grist templates API
  slug: grist-templates-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Grist users.
  name: Grist users API
  slug: grist-users-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Document changes can trigger requests to URLs called webhooks.
  name: Grist webhooks API
  slug: grist-webhooks-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: The widgets API from Grist — 1 operation(s) for widgets.
  name: Grist widgets API
  slug: grist-widgets-api
- baseURL: https://docs.getgrist.com/api
  baseurl_source: declared
  description: Sites can be organized into groups of documents called workspaces.
  name: Grist workspaces API
  slug: grist-workspaces-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grist attachments API
  slug: open-grist-attachments-api
- collection_type: open
  name: Grist attachments columns API
  slug: open-grist-columns-api
- collection_type: open
  name: Grist attachments data API
  slug: open-grist-data-api
- collection_type: open
  name: Grist attachments docs API
  slug: open-grist-docs-api
- collection_type: open
  name: Grist attachments forms API
  slug: open-grist-forms-api
- collection_type: open
  name: Grist attachments orgs API
  slug: open-grist-orgs-api
- collection_type: open
  name: Grist attachments profile API
  slug: open-grist-profile-api
- collection_type: open
  name: Grist attachments records API
  slug: open-grist-records-api
- collection_type: open
  name: Grist attachments service accounts API
  slug: open-grist-service-accounts-api
- collection_type: open
  name: Grist attachments session API
  slug: open-grist-session-api
- collection_type: open
  name: Grist attachments sql API
  slug: open-grist-sql-api
- collection_type: open
  name: Grist attachments tables API
  slug: open-grist-tables-api
- collection_type: open
  name: Grist attachments templates API
  slug: open-grist-templates-api
- collection_type: open
  name: Grist attachments users API
  slug: open-grist-users-api
- collection_type: open
  name: Grist attachments webhooks API
  slug: open-grist-webhooks-api
- collection_type: open
  name: Grist attachments widgets API
  slug: open-grist-widgets-api
- collection_type: open
  name: Grist attachments workspaces API
  slug: open-grist-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/grist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grist-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.getgrist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.getgrist.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gristlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grist-labs/
- group: other
  title: ''
  type: X
  url: https://twitter.com/getgrist
- group: company
  title: ''
  type: Blog
  url: https://www.getgrist.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getgrist.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/gristlabs/grist-core/releases
- group: operate
  title: ''
  type: Community
  url: https://community.getgrist.com/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/MYKpYQ3fbP
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/grist/refs/heads/main/plans/grist-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/grist/refs/heads/main/rate-limits/grist-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/grist/refs/heads/main/finops/grist-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/grist/refs/heads/main/vocabulary/grist-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/grist/refs/heads/main/json-ld/grist-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://raw.githubusercontent.com/api-evangelist/grist/refs/heads/main/blogs/blogs.json
created: '2026-06-12'
description: Grist is a collaborative spreadsheet and relational database platform that combines the flexibility of spreadsheets with the power of a structured database. It provides a REST API for reading and writing table records, managing organizations, workspaces, and documents, executing SQL queries against document data, and configuring outgoing webhooks triggered by data changes. Grist is available as a cloud-hosted SaaS at getgrist.com and as an open-source self-hosted deployment via the Apache-licensed grist-core repository maintained by Grist Labs.
examples:
- key_count: 1
  name: Add Records Request
  slug: add-records-request
- key_count: 1
  name: Create Webhook Request
  slug: create-webhook-request
- key_count: 1
  name: List Records Response
  slug: list-records-response
- key_count: 3
  name: Run Sql Request
  slug: run-sql-request
finops:
- name: Grist Finops
  service_category: ''
  slug: grist-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grist.png
json_schemas:
- name: GristDocument
  property_count: 5
  slug: grist-document
- name: GristRecord
  property_count: 2
  slug: grist-record
- name: GristWebhook
  property_count: 3
  slug: grist-webhook
jsonld:
- class_count: 45
  name: Grist Context
  property_count: 6
  slug: grist-context
layout: provider
modified: '2026-06-12'
name: Grist
nav: Providers
network: true
overview: 'Grist publishes 17 APIs on the [APIs.io](https://apis.io/) network, including attachments API, columns API, data API, and 14 more. Tagged areas include Spreadsheet, Database, Collaboration, No-Code, and Data Management.


  The Grist catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Grist''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 14 more developer resources.'
plans:
- name: Grist Plans Pricing
  plan_count: 5
  slug: grist-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 6
  name: Grist Rate Limits
  slug: grist-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Grist API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: grist-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 80.3
    catalog_earned_first_party: 0.0
    catalog_gap: 34.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 56.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grist/refs/heads/main/screenshots/grist-2026-06-20T182409.png
security:
- kind: authentication
  name: Grist Authentication
  slug: grist-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Grist Domain Security
  slug: grist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grist
tags:
- Spreadsheet
- Database
- Collaboration
- No-Code
- Data Management
- Webhook
- Open-Source
website: https://www.getgrist.com/
---
