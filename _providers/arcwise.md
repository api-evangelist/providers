---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arcwise's audit logs can be accessed via API with an administrator-created personal access token (Bearer); a GET to /api/event_history returns a JSON list of logged events (warehouse connection, API i
  name: Arcwise Audit Log API
  slug: arcwise-api-2
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/arcwise/conventions/arcwise-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arcwise-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://arcwise.app/security
- group: auth
  href: https://artifacts.apis.io/arcwise/security/arcwise-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/arcwise-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/arcwise/authentication/arcwise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arcwise-authentication.yml
- group: build
  href: https://artifacts.apis.io/arcwise/integrations/arcwise-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/arcwise-integration-edges.yml
- group: design
  href: https://artifacts.apis.io/arcwise/rules/arcwise-rules.yml
  title: ''
  type: Spectral
  url: rules/arcwise-rules.yml
- group: operate
  href: https://artifacts.apis.io/arcwise/changelog/arcwise-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/arcwise-changelog.yml
- group: design
  href: https://artifacts.apis.io/arcwise/conformance/arcwise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcwise-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arcwise/llms/arcwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcwise-llms.txt
- group: agent
  href: https://artifacts.apis.io/arcwise/well-known/arcwise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcwise-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcwise/vendors/arcwise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcwise-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcwise.app/terms-free
- group: auth
  title: ''
  type: Security
  url: https://arcwise.app/security
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcwise.app/arcwise-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcwise.app/
- group: auth
  href: https://artifacts.apis.io/arcwise/security/arcwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcwise.app
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcwise.app/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://sql.arcwise.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcwise.app/terms-paid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arcwisedata/
coverage:
  checked: '2026-11-04'
  detail: Arcwise documents a single REST endpoint (GET https://backend.arcwise.app/api/event_history, Bearer personal access token) only in prose on its GitBook audit-logging page, and backend.arcwise.app serves no OpenAPI/Swagger/AsyncAPI document at any standard path.
  evidence:
  - status: 200
    url: https://docs.arcwise.app/arcwise-setup/audit-logging.md
  - status: 404
    url: https://backend.arcwise.app/openapi.json
  - status: 404
    url: https://backend.arcwise.app/docs
  - status: 404
    url: https://backend.arcwise.app/api/event_history
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Arcwise provides an AI-powered analytics platform that detects metric shifts early and explains them with hallucination‑free, traceable insights linked to your data and documentation. Teams can make informed decisions quickly, leveraging real‑time explanations of why metrics moved, improving operational efficiency and strategic planning.
image: https://cdn.prod.website-files.com/695faa4e2ada6fec687076cc/696a49a8ecb2e28da38df5a5_image%20fill.svg
json_schemas:
- name: GetCubejsApiV1DataSourcesResponse
  property_count: 1
  slug: arcwise-get-cubejs-api-v1-data-sources-response
- name: GetCubejsApiV1EntitiesOrdersResponse
  property_count: 11
  slug: arcwise-get-cubejs-api-v1-entities-orders-response
- name: PostCubejsApiV1ConvertQueryResponse
  property_count: 2
  slug: arcwise-post-cubejs-api-v1-convert-query-response
- name: PostCubejsApiV1LoadResponse
  property_count: 5
  slug: arcwise-post-cubejs-api-v1-load-response
- name: PostCubejsApiV1PreAggregationsJobsRequest
  property_count: 2
  slug: arcwise-post-cubejs-api-v1-pre-aggregations-jobs-request
- name: PostCubejsApiV1SqlFiltersResponse
  property_count: 7
  slug: arcwise-post-cubejs-api-v1-sql-filters-response
jsonld:
- class_count: 11
  name: Arcwise Context
  property_count: 25
  slug: arcwise-context
layout: provider
modified: '2026-11-04'
name: Arcwise
nav: Providers
network: true
overview: 'Arcwise is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Metrics, Analytics, and Decision-Making.


  The Arcwise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arcwise''s developer surface includes authentication, changelog, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Arcwise Plans Pricing
  plan_count: 0
  slug: arcwise-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Arcwise Rate Limits
  slug: arcwise-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Arcwise API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: arcwise-rules
scopes:
- name: Arcwise Scopes
  scope_count: 0
  slug: arcwise-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 14.7
    developer_ergonomics: 22.6
    discoverability: 73.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/arcwise/arcwise-2026-11-03T121116.png
security:
- kind: authentication
  name: Arcwise Authentication
  slug: arcwise-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arcwise Domain Security
  slug: arcwise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Arcwise Trust Center
  slug: arcwise-trust-center
  summary_line: SOC 2 Type II
slug: arcwise
tags:
- Company
- Artificial Intelligence
- Metrics
- Analytics
- Decision-Making
- Business Intelligence
- Root Cause Analysis
website: https://arcwise.app
---
