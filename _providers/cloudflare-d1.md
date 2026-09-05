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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Cloudflare D1 Agentic Access
  operation_count: 12
  slug: cloudflare-d1-agentic-access
  summary_line: 12 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: declared
  description: The D1 API from Cloudflare D1 — 8 operation(s) for d1.
  name: Cloudflare D1 D1 API
  slug: cloudflare-d1-d1-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloudflare D1 API
  slug: open-cloudflare-d1-d1-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudflare-d1-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-d1-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudflare-d1-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudflare-d1-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudflare.com/developer-platform/d1/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/d1/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cloudflare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudflare/
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.cloudflare.com/d1/platform/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cloudflarestatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/cloudflare
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudflare-d1-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudflare-d1-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudflare-d1-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cloudflare.com/d1/platform/release-notes/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/cloudflare-typescript
created: '2026-06-13'
description: Cloudflare D1 is a managed, serverless SQLite database service with a REST API for querying D1 databases, executing SQL statements, listing databases, and managing database instances at the edge. D1 offers SQLite semantics, built-in Time Travel point-in-time recovery, global read replication, and seamless integration with Cloudflare Workers and Pages.
examples:
- key_count: 4
  name: D1 Create Database
  slug: d1-create-database
- key_count: 4
  name: D1 List Databases
  slug: d1-list-databases
- key_count: 4
  name: D1 Query Database
  slug: d1-query-database
- key_count: 4
  name: D1 Time Travel Restore
  slug: d1-time-travel-restore
finops:
- name: Cloudflare D1 Finops
  service_category: ''
  slug: cloudflare-d1-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudflare-d1.png
json_schemas:
- name: D1 Account Identifier
  property_count: 0
  slug: d1_account-identifier
- name: D1 Api Response Common Failure
  property_count: 4
  slug: d1_api-response-common-failure
- name: D1 Api Response Common
  property_count: 4
  slug: d1_api-response-common
- name: D1 Batch Query
  property_count: 0
  slug: d1_batch-query
- name: D1 Created At
  property_count: 0
  slug: d1_created-at
- name: D1 Database Details Response
  property_count: 8
  slug: d1_database-details-response
- name: D1 Database Identifier
  property_count: 0
  slug: d1_database-identifier
- name: D1 Database Name
  property_count: 0
  slug: d1_database-name
- name: D1 Database Response
  property_count: 5
  slug: d1_database-response
- name: D1 Database Update Partial Request Body
  property_count: 1
  slug: d1_database-update-partial-request-body
- name: D1 Database Update Request Body
  property_count: 1
  slug: d1_database-update-request-body
- name: D1 Database Version
  property_count: 0
  slug: d1_database-version
- name: D1 File Size
  property_count: 0
  slug: d1_file-size
- name: D1 Jurisdiction Nullable
  property_count: 0
  slug: d1_jurisdiction-nullable
- name: D1 Jurisdiction
  property_count: 0
  slug: d1_jurisdiction
- name: D1 Messages
  property_count: 0
  slug: d1_messages
- name: D1 Params
  property_count: 0
  slug: d1_params
- name: D1 Primary Location Hint
  property_count: 0
  slug: d1_primary-location-hint
- name: D1 Query Meta
  property_count: 11
  slug: d1_query-meta
- name: D1 Query Result Response
  property_count: 3
  slug: d1_query-result-response
- name: D1 Raw Result Response
  property_count: 3
  slug: d1_raw-result-response
- name: D1 Read Replication Details For Request
  property_count: 1
  slug: d1_read-replication-details-for-request
- name: D1 Read Replication Details For Response
  property_count: 1
  slug: d1_read-replication-details-for-response
- name: D1 Served By Colo
  property_count: 0
  slug: d1_served-by-colo
- name: D1 Served By Region
  property_count: 0
  slug: d1_served-by-region
- name: D1 Single Query
  property_count: 2
  slug: d1_single-query
- name: D1 Sql
  property_count: 0
  slug: d1_sql
- name: D1 Table Count
  property_count: 0
  slug: d1_table-count
- name: D1 Time Travel Bookmark
  property_count: 0
  slug: d1_time-travel-bookmark
- name: D1 Time Travel Restore Response
  property_count: 3
  slug: d1_time-travel-restore-response
- name: D1 Time Travel Timestamp
  property_count: 0
  slug: d1_time-travel-timestamp
jsonld:
- class_count: 0
  name: Cloudflare D1 Context
  property_count: 36
  slug: cloudflare-d1-context
layout: provider
modified: '2026-06-13'
name: Cloudflare D1
nav: Providers
network: true
overview: 'Cloudflare D1 publishes 1 API on the [APIs.io](https://apis.io/) network: D1 API. Tagged areas include Database, SQLite, Serverless, Edge Computing, and SQL.


  The Cloudflare D1 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudflare D1''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 12 more developer resources.'
plans:
- name: Cloudflare D1 Plans Pricing
  plan_count: 2
  slug: cloudflare-d1-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 25
  name: Cloudflare D1 Rate Limits
  slug: cloudflare-d1-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cloudflare D1 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cloudflare-d1-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 71.3
    catalog_earned_first_party: 0.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 63.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 68.4
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudflare-d1/refs/heads/main/screenshots/cloudflare-d1-2026-06-20T174554.png
security:
- kind: authentication
  name: Cloudflare D1 Authentication
  slug: cloudflare-d1-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Cloudflare D1 Domain Security
  slug: cloudflare-d1-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare D1 Vulnerability Disclosure
  slug: cloudflare-d1-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cloudflare-d1
tags:
- Database
- SQLite
- Serverless
- Edge Computing
- SQL
- Cloudflare
- Workers
website: https://www.cloudflare.com/developer-platform/d1/
---
