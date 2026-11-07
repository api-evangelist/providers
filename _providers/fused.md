---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 8
apis:
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: Fused provides AI‑powered data integration and workflow automation platform.
  name: Fused API
  slug: fused-api
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: The Fc Your Canvas Token API from Fused — 1 operation(s) for fc your canvas token.
  name: Fused Fc Your Canvas Token API
  slug: fused-fc-your-canvas-token-api
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: The Files API from Fused — 2 operation(s) for files.
  name: Fused Files API
  slug: fused-files-api
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: The Secrets API from Fused — 2 operation(s) for secrets.
  name: Fused Secrets API
  slug: fused-secrets-api
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: The Server API from Fused — 8 operation(s) for server.
  name: Fused Server API
  slug: fused-server-api
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: The Session Token API from Fused — 1 operation(s) for session token.
  name: Fused Session Token API
  slug: fused-session-token-api
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: The Udf API from Fused — 8 operation(s) for udf.
  name: Fused Udf API
  slug: fused-udf-api
- baseURL: https://www.fused.io
  baseurl_source: spec
  description: The User API from Fused — 1 operation(s) for user.
  name: Fused User API
  slug: fused-user-api
artifact_total: 21
common:
- group: commercial
  href: https://artifacts.apis.io/fused/plans/fused-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fused-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fused/rules/fused-rules.yml
  title: ''
  type: Spectral
  url: rules/fused-rules.yml
- group: design
  href: https://artifacts.apis.io/fused/json-ld/fused-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fused-context.jsonld
- group: design
  href: https://artifacts.apis.io/fused/vocabulary/fused-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fused-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fused/data-model/fused-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fused-data-model.yml
- group: build
  href: https://artifacts.apis.io/fused/cli/fused-cli.yml
  title: ''
  type: CLI
  url: cli/fused-cli.yml
- group: operate
  href: https://artifacts.apis.io/fused/changelog/fused-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fused-changelog.yml
- group: auth
  href: https://artifacts.apis.io/fused/authentication/fused-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fused-authentication.yml
- group: design
  href: https://artifacts.apis.io/fused/conformance/fused-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fused-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fused/llms/fused-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fused-llms.txt
- group: other
  href: https://artifacts.apis.io/fused/hosts/fused-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fused-hosts.yml
- group: other
  href: https://artifacts.apis.io/fused/vendors/fused-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fused-vendors.yml
- group: build
  href: https://artifacts.apis.io/fused/packages/fused-packages.yml
  title: ''
  type: SDKs
  url: packages/fused-packages.yml
- group: build
  href: https://artifacts.apis.io/fused/packages/fused-packages.yml
  title: ''
  type: Packages
  url: packages/fused-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fused.io/python-sdk/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.fused.io/blog
- group: auth
  href: https://artifacts.apis.io/fused/security/fused-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fused-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fused.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fused.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fused.io/guide/getting-started/first-udf-basics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fused.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fused.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fused.io/privacy
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.fused.io/openapi.json
  - status: 404
    url: https://api.fused.io/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Fused provides an analytics platform that combines AI, real‑time Python execution, and data context to enable teams to unlock insights instantly. Users can build workflows, connect to any data source, and deploy applications with end‑to‑end Python UDFs, leveraging built‑in data‑aware AI. The platform offers a low‑code environment, extensive integrations, and collaborative tools such as a Discord community and extensive documentation to accelerate data‑driven projects.
finops:
- has_sources: true
  method: derived
  name: Fused Finops
  primary_unit: seat
  service_category: ''
  slug: fused-finops
  template: false
image: https://framerusercontent.com/images/feIc3iYdxE3MTKtAmkh9qGbbz4.png
json_schemas:
- name: GetUdfSelfResponse
  property_count: 10
  slug: fused-get-udf-self-response
- name: GetUserSelfResponse
  property_count: 7
  slug: fused-get-user-self-response
- name: PostSessionTokenByAccessTokenCanvastokenResponse
  property_count: 3
  slug: fused-post-session-token-by-access-token-canvastoken-response
- name: PostUdfByIdUdfidRequest
  property_count: 3
  slug: fused-post-udf-by-id-udfid-request
- name: PostUdfNewRequest
  property_count: 6
  slug: fused-post-udf-new-request
- name: PostUserSelfResponse
  property_count: 7
  slug: fused-post-user-self-response
jsonld:
- class_count: 30
  name: Fused Context
  property_count: 36
  slug: fused-context
layout: provider
modified: '2026-10-13'
name: Fused
nav: Providers
network: true
overview: 'Fused is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Fc Your Canvas Token API, Files API, and 6 more. Tagged areas include Company, Analytics, Artificial Intelligence, Data Platform, and Python.


  The Fused catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fused''s developer surface includes CLI, changelog, authentication, engineering blog, documentation, getting-started guide, pricing, and 16 more developer resources.'
plans:
- name: Fused Plans Pricing
  plan_count: 4
  slug: fused-plans-pricing
- name: Fused Price Estimates
  plan_count: 0
  slug: fused-price-estimates
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Fused API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: fused-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 75.8
    catalog_earned_first_party: 12.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 27.3
    developer_ergonomics: 38.1
    discoverability: 69.6
    operational_transparency: 7.9
  previous_composite: 47.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/fused/fused-2026-11-03T132403.png
security:
- kind: authentication
  name: Fused Authentication
  slug: fused-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fused Domain Security
  slug: fused-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fused
tags:
- Company
- Analytics
- Artificial Intelligence
- Data Platform
- Python
- Low-Code
website: https://www.fused.io/
---
