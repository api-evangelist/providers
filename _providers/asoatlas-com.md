---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for in-app feedback, allowing apps to send feedback, read replies, and handle review requests.
  name: Feedback API
  slug: feedback-api
- description: 'ASO Atlas API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: ASO Atlas API
  slug: asoatlas-com-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/asoatlas-com/plans/asoatlas-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asoatlas-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asoatlas-com/rules/asoatlas-com-rules.yml
  title: ''
  type: Spectral
  url: rules/asoatlas-com-rules.yml
- group: design
  href: https://artifacts.apis.io/asoatlas-com/json-ld/asoatlas-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asoatlas-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/asoatlas-com/vocabulary/asoatlas-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asoatlas-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/asoatlas-com/data-model/asoatlas-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asoatlas-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/asoatlas-com/authentication/asoatlas-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asoatlas-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/asoatlas-com/conformance/asoatlas-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asoatlas-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asoatlas-com/well-known/asoatlas-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asoatlas-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asoatlas-com/hosts/asoatlas-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asoatlas-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asoatlas-com/vendors/asoatlas-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asoatlas-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://asoatlas.com/docs/plans-billing
- group: start
  title: ''
  type: Login
  url: https://asoatlas.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://asoatlas.com/docs/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asoatlas
- group: auth
  href: https://artifacts.apis.io/asoatlas-com/security/asoatlas-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asoatlas-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asoatlas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asoatlas.com/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asoatlas.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asoatlas.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Documentation provides API details but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://asoatlas.com/docs/feedback-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ASO Atlas is a SaaS platform that provides App Store Optimization tools, including keyword research, rank tracking, competitor analysis, and metadata optimization. It offers a web app and a native macOS app, integrates AI assistants via MCP, and supports both iOS and Mac App Store analytics. Pricing starts at $9 per month with unlimited apps and keywords.
image: https://asoatlas.com/favicon.svg
json_schemas:
- name: GetApiV1FeedbackResponse
  property_count: 2
  slug: asoatlas-com-get-api-v1-feedback-response
- name: PostSummariesResponse
  property_count: 2
  slug: asoatlas-com-post-summaries-response
- name: PostThreadMessagesRequest
  property_count: 2
  slug: asoatlas-com-post-thread-messages-request
- name: PostThreadsRequest
  property_count: 14
  slug: asoatlas-com-post-threads-request
- name: PostThreadsResponse
  property_count: 2
  slug: asoatlas-com-post-threads-response
- name: PostUnreadResponse
  property_count: 2
  slug: asoatlas-com-post-unread-response
jsonld:
- class_count: 11
  name: Asoatlas Com Context
  property_count: 19
  slug: asoatlas-com-context
layout: provider
modified: '2026-11-01'
name: ASO Atlas
nav: Providers
network: true
overview: 'ASO Atlas is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ASO, App Store, Keyword Research, Analytics, and Software-as-a-Service.


  The ASO Atlas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ASO Atlas'' developer surface includes authentication, pricing, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Asoatlas Com Plans Pricing
  plan_count: 2
  slug: asoatlas-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Asoatlas Com Rate Limits
  slug: asoatlas-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: ASO Atlas API Rules
  rule_count: 47
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 1
  slug: asoatlas-com-rules
scopes:
- name: Asoatlas Com Scopes
  scope_count: 0
  slug: asoatlas-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 38.2
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asoatlas Com Authentication
  slug: asoatlas-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Asoatlas Com Domain Security
  slug: asoatlas-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asoatlas-com
tags:
- ASO
- App Store
- Keyword Research
- Analytics
- Software-as-a-Service
website: https://asoatlas.com/
---
