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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Nocodb Agentic Access
  operation_count: 32
  slug: nocodb-agentic-access
  summary_line: 32 operations · 21 acting
api_count: 9
apis:
- description: File attachment operations
  name: NocoDB Attachments API
  slug: nocodb-attachments-api
- description: Authentication and token management
  name: NocoDB Auth API
  slug: nocodb-auth-api
- description: Base (database) management operations
  name: NocoDB Bases API
  slug: nocodb-bases-api
- description: Field/column management operations
  name: NocoDB Fields API
  slug: nocodb-fields-api
- description: Webhook management operations
  name: NocoDB Hooks API
  slug: nocodb-hooks-api
- description: Link relationship operations between records
  name: NocoDB Links API
  slug: nocodb-links-api
- description: CRUD operations on table rows/records
  name: NocoDB Records API
  slug: nocodb-records-api
- description: Table management operations
  name: NocoDB Tables API
  slug: nocodb-tables-api
- description: View management operations
  name: NocoDB Views API
  slug: nocodb-views-api
artifact_total: 40
collections:
- collection_type: postman
  name: NocoDB Data Attachments API
  slug: postman-nocodb-attachments-api
- collection_type: postman
  name: NocoDB Data Attachments Auth API
  slug: postman-nocodb-auth-api
- collection_type: postman
  name: NocoDB Data Attachments Bases API
  slug: postman-nocodb-bases-api
- collection_type: postman
  name: NocoDB Data Attachments Fields API
  slug: postman-nocodb-fields-api
- collection_type: postman
  name: NocoDB Data Attachments Hooks API
  slug: postman-nocodb-hooks-api
- collection_type: postman
  name: NocoDB Data Attachments Links API
  slug: postman-nocodb-links-api
- collection_type: postman
  name: NocoDB Data Attachments Records API
  slug: postman-nocodb-records-api
- collection_type: postman
  name: NocoDB Data Attachments Tables API
  slug: postman-nocodb-tables-api
- collection_type: postman
  name: NocoDB Data Attachments Views API
  slug: postman-nocodb-views-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NocoDB Data Attachments API
  slug: open-nocodb-attachments-api
- collection_type: open
  name: NocoDB Data Attachments Auth API
  slug: open-nocodb-auth-api
- collection_type: open
  name: NocoDB Data Attachments Bases API
  slug: open-nocodb-bases-api
- collection_type: open
  name: NocoDB Data Attachments Fields API
  slug: open-nocodb-fields-api
- collection_type: open
  name: NocoDB Data Attachments Hooks API
  slug: open-nocodb-hooks-api
- collection_type: open
  name: NocoDB Data Attachments Links API
  slug: open-nocodb-links-api
- collection_type: open
  name: NocoDB Data Attachments Records API
  slug: open-nocodb-records-api
- collection_type: open
  name: NocoDB Data Attachments Tables API
  slug: open-nocodb-tables-api
- collection_type: open
  name: NocoDB Data Attachments Views API
  slug: open-nocodb-views-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/nocodb/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nocodb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nocodb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nocodb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nocodb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nocodb.com/docs/product-docs/developer-resources/rest-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nocodb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nocodb
- group: company
  title: ''
  type: Blog
  url: https://nocodb.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nocodb.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nocodb.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://nocodb.com/changelog
- group: other
  title: ''
  type: X
  url: https://x.com/nocodb
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/nocodb-sdk
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/plans/nocodb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/rate-limits/nocodb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/finops/nocodb-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/vocabulary/nocodb-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/json-ld/nocodb-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/json-schema/nocodb-record-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/json-schema/nocodb-table-schema.json
- group: company
  title: ''
  type: Blog
  url: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/blogs/blogs.json
created: '2026-06-12'
description: NocoDB is an open-source, self-hostable alternative to Airtable that turns any relational database — MySQL, PostgreSQL, Microsoft SQL Server, or SQLite — into a collaborative smart spreadsheet. It exposes a versioned REST API (v2 and v3) with separate Data APIs for record CRUD operations and Meta APIs for managing workspaces, bases, tables, fields, views, and attachments. Authentication is handled via API tokens or session auth tokens, with Swagger UI bundled into every instance for live exploration. NocoDB is available as a free community self-hosted deployment or as a managed cloud service with tiered plans ranging from Free to Enterprise.
examples:
- key_count: 4
  name: Nocodb Create Record Example
  slug: nocodb-create-record-example
- key_count: 4
  name: Nocodb List Records Example
  slug: nocodb-list-records-example
finops:
- name: Nocodb Finops
  service_category: ''
  slug: nocodb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nocodb.png
json_schemas:
- name: NocoDB Record
  property_count: 3
  slug: nocodb-record
- name: NocoDB Table
  property_count: 9
  slug: nocodb-table
jsonld:
- class_count: 9
  name: Nocodb Context
  property_count: 33
  slug: nocodb-context
layout: provider
modified: '2026-06-12'
name: NocoDB
nav: Providers
network: true
overview: 'NocoDB publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Auth API, Bases API, and 6 more. Tagged areas include Database, No-Code, Low-Code, Airtable Alternative, and Open Source.


  The NocoDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NocoDB''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 17 more developer resources.'
plans:
- name: Nocodb Plans Pricing
  plan_count: 9
  slug: nocodb-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 2
  name: Nocodb Rate Limits
  slug: nocodb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: NocoDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nocodb-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.9
  delta: -5.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 68.8
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 55.3
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/nocodb/refs/heads/main/screenshots/nocodb-2026-06-20T190347.png
security:
- kind: authentication
  name: Nocodb Authentication
  slug: nocodb-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nocodb Domain Security
  slug: nocodb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nocodb
tags:
- Database
- No-Code
- Low-Code
- Airtable Alternative
- Open Source
- Spreadsheet
- REST API
- Self-Hosted
website: https://nocodb.com/
---
