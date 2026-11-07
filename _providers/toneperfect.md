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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Toneperfect Agentic Access
  operation_count: 5
  slug: toneperfect-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.toneperfect.app
  baseurl_source: spec
  description: The Assessment API from TonePerfect (Pronunciation Assessment API) — 1 operation(s) for assessment.
  name: TonePerfect (Pronunciation Assessment API) Assessment API
  slug: toneperfect-assessment-api
- baseURL: https://api.toneperfect.app
  baseurl_source: spec
  description: The Capabilities API from TonePerfect (Pronunciation Assessment API) — 1 operation(s) for capabilities.
  name: TonePerfect (Pronunciation Assessment API) Capabilities API
  slug: toneperfect-capabilities-api
- baseURL: https://api.toneperfect.app
  baseurl_source: spec
  description: The Utilities API from TonePerfect (Pronunciation Assessment API) — 3 operation(s) for utilities.
  name: TonePerfect (Pronunciation Assessment API) Utilities API
  slug: toneperfect-utilities-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/toneperfect/capabilities/toneperfect-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/toneperfect-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/toneperfect/agentic-access/toneperfect-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/toneperfect-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/toneperfect/plans/toneperfect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/toneperfect-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/toneperfect/rules/toneperfect-rules.yml
  title: ''
  type: Spectral
  url: rules/toneperfect-rules.yml
- group: design
  href: https://artifacts.apis.io/toneperfect/json-ld/toneperfect-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/toneperfect-context.jsonld
- group: design
  href: https://artifacts.apis.io/toneperfect/vocabulary/toneperfect-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/toneperfect-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/toneperfect/data-model/toneperfect-data-model.yml
  title: ''
  type: DataModel
  url: data-model/toneperfect-data-model.yml
- group: design
  href: https://artifacts.apis.io/toneperfect/conventions/toneperfect-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/toneperfect-conventions.yml
- group: design
  href: https://artifacts.apis.io/toneperfect/conventions/toneperfect-conventions.yml
  title: ''
  type: Conventions
  url: conventions/toneperfect-conventions.yml
- group: auth
  href: https://artifacts.apis.io/toneperfect/authentication/toneperfect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toneperfect-authentication.yml
- group: design
  href: https://artifacts.apis.io/toneperfect/errors/toneperfect-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/toneperfect-problem-types.yml
- group: design
  href: https://artifacts.apis.io/toneperfect/conformance/toneperfect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toneperfect-conformance.yml
- group: agent
  href: https://artifacts.apis.io/toneperfect/llms/toneperfect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toneperfect-llms.txt
- group: other
  href: https://artifacts.apis.io/toneperfect/hosts/toneperfect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toneperfect-hosts.yml
- group: other
  href: https://artifacts.apis.io/toneperfect/vendors/toneperfect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toneperfect-vendors.yml
- group: build
  href: https://artifacts.apis.io/toneperfect/packages/toneperfect-packages.yml
  title: ''
  type: Packages
  url: packages/toneperfect-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.toneperfect.app/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://api.toneperfect.app/status/
- group: auth
  title: ''
  type: Security
  url: https://api.toneperfect.app/security/
- group: build
  title: ''
  type: SDKs
  url: https://api.toneperfect.app/sdk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.toneperfect.app/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://api.toneperfect.app/pricing/
- group: start
  title: ''
  type: Login
  url: https://api.toneperfect.app/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.toneperfect.app/changelog/
- group: company
  title: ''
  type: Blog
  url: https://api.toneperfect.app/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.toneperfect.app/quickstart/
- group: auth
  href: https://artifacts.apis.io/toneperfect/security/toneperfect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toneperfect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.toneperfect.app
- group: docs
  title: ''
  type: Documentation
  url: https://api.toneperfect.app/docs
created: '2026-10-08'
description: TonePerfect offers an AI‑powered pronunciation assessment API for language learning applications. It supports ten languages and provides a single endpoint that returns a detailed score (0‑100) for the whole sentence, each word, and individual sounds, including tone information for Mandarin. The service includes free tier credits, transparent pricing, and robust error handling, making it suitable for developers integrating speech evaluation into apps.
finops:
- has_sources: true
  method: derived
  name: Toneperfect Finops
  primary_unit: seat
  service_category: ''
  slug: toneperfect-finops
  template: false
image: https://api.toneperfect.app/static/og-image.png
json_schemas:
- name: Assessment
  property_count: 19
  slug: toneperfect-assessment
- name: Capabilities
  property_count: 3
  slug: toneperfect-capabilities
- name: CompactAssessment
  property_count: 11
  slug: toneperfect-compact-assessment
- name: StatusWindow
  property_count: 6
  slug: toneperfect-status-window
jsonld:
- class_count: 11
  name: Toneperfect Context
  property_count: 62
  slug: toneperfect-context
layout: provider
modified: '2026-10-08'
name: TonePerfect (Pronunciation Assessment API)
nav: Providers
network: true
overview: 'TonePerfect (Pronunciation Assessment API) publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Assessment API, Capabilities API, and Utilities API. Tagged areas include Company, Artificial Intelligence, Speech, Language Learning, and Pronunciation.


  The TonePerfect (Pronunciation Assessment API) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TonePerfect (Pronunciation Assessment API)''s developer surface includes authentication, pricing, changelog, engineering blog, getting-started guide, documentation, and 23 more developer resources.'
plans:
- name: Toneperfect Plans Pricing
  plan_count: 3
  slug: toneperfect-plans-pricing
- name: Toneperfect Price Estimates
  plan_count: 0
  slug: toneperfect-price-estimates
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: TonePerfect (Pronunciation Assessment API) API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: toneperfect-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 60.5
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
    score: 0.0
screenshot: https://apis.io/screenshots/toneperfect/toneperfect-2026-11-03T144851.png
security:
- kind: authentication
  name: Toneperfect Authentication
  slug: toneperfect-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Toneperfect Domain Security
  slug: toneperfect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toneperfect
tags:
- Company
- Artificial Intelligence
- Speech
- Language Learning
- Pronunciation
website: https://api.toneperfect.app
---
