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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 75
  human_in_the_loop: 3
  name: Grist Agentic Access
  operation_count: 120
  slug: grist-agentic-access
  summary_line: 120 operations · 75 acting · 3 human-in-the-loop
api_count: 17
apis:
- description: Documents may include attached files. Data records can refer to these using a column of type `Attachments`.
  name: Grist attachments API
  slug: grist-attachments-api
- description: Tables are structured as a collection of columns.
  name: Grist columns API
  slug: grist-columns-api
- description: Work with table data, using a (now deprecated) columnar format. We now recommend the `records` endpoints.
  name: Grist data API
  slug: grist-data-api
- description: Workspaces contain collections of Grist documents.
  name: Grist docs API
  slug: grist-docs-api
- description: The forms API from Grist — 1 operation(s) for forms.
  name: Grist forms API
  slug: grist-forms-api
- description: Team sites and personal spaces are called 'orgs' in the API.
  name: Grist orgs API
  slug: grist-orgs-api
- description: The profile API from Grist — 4 operation(s) for profile.
  name: Grist profile API
  slug: grist-profile-api
- description: Tables contain collections of records (also called rows).
  name: Grist records API
  slug: grist-records-api
- description: Impersonations to manage grist resources through REST APIs with specific rights.
  name: Grist service accounts API
  slug: grist-service-accounts-api
- description: The session API from Grist — 2 operation(s) for session.
  name: Grist session API
  slug: grist-session-api
- description: Sql endpoint to query data from documents.
  name: Grist sql API
  slug: grist-sql-api
- description: Documents are structured as a collection of tables.
  name: Grist tables API
  slug: grist-tables-api
- description: The templates API from Grist — 2 operation(s) for templates.
  name: Grist templates API
  slug: grist-templates-api
- description: Grist users.
  name: Grist users API
  slug: grist-users-api
- description: Document changes can trigger requests to URLs called webhooks.
  name: Grist webhooks API
  slug: grist-webhooks-api
- description: The widgets API from Grist — 1 operation(s) for widgets.
  name: Grist widgets API
  slug: grist-widgets-api
- description: Sites can be organized into groups of documents called workspaces.
  name: Grist workspaces API
  slug: grist-workspaces-api
artifact_total: 32
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
random_paper: 78
rate_limits:
- limit_count: 6
  name: Grist Rate Limits
  slug: grist-rate-limits
rules:
- name: Grist API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: grist-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.9
  scored_at: '2026-08-03'
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
- Webhooks
- Open Source
website: https://www.getgrist.com/
---
