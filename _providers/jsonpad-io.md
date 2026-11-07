---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: jsonpad.io RESTful API allows managing lists, items, indexes, and identities.
  name: jsonpad.io API
  slug: jsonpad-io-api-2
- baseURL: https://api.jsonpad.io
  baseurl_source: declared
  description: 'jsonpad-io API as documented publicly: 40 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: jsonpad-io API
  slug: jsonpad-io-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/jsonpad-io/rate-limits/jsonpad-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jsonpad-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jsonpad-io/plans/jsonpad-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jsonpad-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jsonpad-io/rules/jsonpad-io-rules.yml
  title: ''
  type: Spectral
  url: rules/jsonpad-io-rules.yml
- group: design
  href: https://artifacts.apis.io/jsonpad-io/json-ld/jsonpad-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jsonpad-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/jsonpad-io/vocabulary/jsonpad-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jsonpad-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jsonpad-io/data-model/jsonpad-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jsonpad-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/jsonpad-io/changelog/jsonpad-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jsonpad-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/jsonpad-io/authentication/jsonpad-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jsonpad-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/jsonpad-io/lifecycle/jsonpad-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jsonpad-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jsonpad-io/errors/jsonpad-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jsonpad-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jsonpad-io/conformance/jsonpad-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jsonpad-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jsonpad-io/llms/jsonpad-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jsonpad-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/jsonpad-io/well-known/jsonpad-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jsonpad-io-security.txt
- group: agent
  href: https://artifacts.apis.io/jsonpad-io/well-known/jsonpad-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jsonpad-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/jsonpad-io/hosts/jsonpad-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jsonpad-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/jsonpad-io/vendors/jsonpad-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jsonpad-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/jsonpad-io/packages/jsonpad-io-packages.yml
  title: ''
  type: SDKs
  url: packages/jsonpad-io-packages.yml
- group: build
  href: https://artifacts.apis.io/jsonpad-io/packages/jsonpad-io-packages.yml
  title: ''
  type: Packages
  url: packages/jsonpad-io-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://jsonpad.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://jsonpad.io/changelog
- group: auth
  href: https://artifacts.apis.io/jsonpad-io/security/jsonpad-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jsonpad-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jsonpad-io/security/jsonpad-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jsonpad-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jsonpad.io/
- group: docs
  title: ''
  type: Documentation
  url: https://jsonpad.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://jsonpad.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://jsonpad.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://jsonpad.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://jsonpad.io/register
- group: other
  title: ''
  type: SignIn
  url: https://jsonpad.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jsonpad.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jsonpad.io/privacy
coverage:
  checked: '2026-10-30'
  detail: The public documentation provides human‑readable API reference but no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://jsonpad.io/docs/api-reference.md
  - status: 200
    url: https://api.jsonpad.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: jsonpad.io provides a JSON storage platform with an instant RESTful API, versioning, validation, search, and real-time updates. Users can create lists, push JSON data, and retrieve it via simple HTTP endpoints without managing any backend infrastructure. The service includes schema validation, data version control, WebSocket streaming, and a free forever plan, making it suitable for rapid prototyping, front-end development, and production workloads.
image: https://jsonpad.io/static/media/jsonpad-logo-simple.dbb13e5b128306d1ba900c582b73d328.svg
json_schemas:
- name: PostIdentitiesLoginRequest
  property_count: 3
  slug: jsonpad-io-post-identities-login-request
- name: PostListsListRulesTestRequest
  property_count: 6
  slug: jsonpad-io-post-lists-list-rules-test-request
- name: PostListsListRulesTestResponse
  property_count: 2
  slug: jsonpad-io-post-lists-list-rules-test-response
- name: PostListsRequest
  property_count: 10
  slug: jsonpad-io-post-lists-request
- name: PostListsSampleListItems9A197Fe4392144AfB92061000B41321ERequ
  property_count: 5
  slug: jsonpad-io-post-lists-sample-list-items9-a197-fe4392144-af-b92061000-b41321-erequ
- name: PostWebhooksRequest
  property_count: 5
  slug: jsonpad-io-post-webhooks-request
jsonld:
- class_count: 19
  name: Jsonpad Io Context
  property_count: 42
  slug: jsonpad-io-context
layout: provider
modified: '2026-10-30'
name: jsonpad-io
nav: Providers
network: true
overview: 'jsonpad-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include JSON Storage, REST API, No-Code Backend, Real-time Updates, and Versioning.


  The jsonpad-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  jsonpad-io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Jsonpad Io Plans Pricing
  plan_count: 1
  slug: jsonpad-io-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Jsonpad Io Rate Limits
  slug: jsonpad-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: jsonpad-io API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: jsonpad-io-rules
scopes:
- name: Jsonpad Io Scopes
  scope_count: 0
  slug: jsonpad-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 78.0
    catalog_earned_first_party: 16.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 27.5
    developer_ergonomics: 33.3
    discoverability: 73.2
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jsonpad-io/jsonpad-io-2026-11-03T134237.png
security:
- kind: authentication
  name: Jsonpad Io Authentication
  slug: jsonpad-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Jsonpad Io Domain Security
  slug: jsonpad-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Jsonpad Io Vulnerability Disclosure
  slug: jsonpad-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jsonpad-io
tags:
- JSON Storage
- REST API
- No-Code Backend
- Real-time Updates
- Versioning
website: https://jsonpad.io/
---
