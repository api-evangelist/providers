---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Shirabe Dev Agentic Access
  operation_count: 5
  slug: shirabe-dev-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://shirabe.dev
  baseurl_source: declared
  description: 暦情報の取得
  name: shirabe-dev Calendar API
  slug: shirabe-dev-calendar-api
- baseURL: https://shirabe.dev
  baseurl_source: declared
  description: 複合正規化（住所・人名・法人番号・暦を 1 コールで横断）
  name: shirabe-dev Hub API
  slug: shirabe-dev-hub-api
- baseURL: https://shirabe.dev
  baseurl_source: declared
  description: システム情報
  name: shirabe-dev System API
  slug: shirabe-dev-system-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/shirabe-dev/agentic-access/shirabe-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shirabe-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/shirabe-dev/plans/shirabe-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shirabe-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shirabe-dev/rules/shirabe-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/shirabe-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/shirabe-dev/json-ld/shirabe-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shirabe-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/shirabe-dev/vocabulary/shirabe-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shirabe-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/shirabe-dev/data-model/shirabe-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shirabe-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/shirabe-dev/errors/shirabe-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shirabe-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shirabe-dev/conformance/shirabe-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shirabe-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shirabe-dev/llms/shirabe-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shirabe-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/shirabe-dev/well-known/shirabe-dev-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shirabe-dev-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/shirabe-dev/well-known/shirabe-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shirabe-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/shirabe-dev/hosts/shirabe-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shirabe-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/shirabe-dev/vendors/shirabe-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shirabe-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/shirabe-dev/packages/shirabe-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/shirabe-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/shirabe-dev/packages/shirabe-dev-packages.yml
  title: ''
  type: Packages
  url: packages/shirabe-dev-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/techwell-inc-jp
- group: docs
  title: ''
  type: APIReference
  url: https://shirabe.dev/llms.txt
- group: auth
  href: https://artifacts.apis.io/shirabe-dev/authentication/shirabe-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shirabe-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/shirabe-dev/security/shirabe-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shirabe-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shirabe.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://shirabe.dev/calendar/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://shirabe.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shirabe.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shirabe.dev/privacy
created: '2026-10-31'
description: 'Shirabe is an API platform providing deterministic Japanese data via four REST APIs: calendar, address normalization, Japanese text processing, and corporate number verification. It guarantees consistent JSON schema responses, low cost per call, and includes attribution to public data sources. The service offers free tier usage without registration and targets AI agents needing reliable factual data.'
image: https://shirabe.dev/og-default.svg
json_schemas:
- name: BestDaysResponse
  property_count: 4
  slug: shirabe-dev-best-days-response
- name: CalendarRangeResponse
  property_count: 3
  slug: shirabe-dev-calendar-range-response
- name: CalendarResponse
  property_count: 10
  slug: shirabe-dev-calendar-response
- name: EnrichRequest
  property_count: 2
  slug: shirabe-dev-enrich-request
- name: EnrichResponse
  property_count: 2
  slug: shirabe-dev-enrich-response
- name: HealthResponse
  property_count: 3
  slug: shirabe-dev-health-response
jsonld:
- class_count: 21
  name: Shirabe Dev Context
  property_count: 48
  slug: shirabe-dev-context
layout: provider
modified: '2026-10-31'
name: shirabe-dev
nav: Providers
network: true
overview: 'shirabe-dev publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Calendar API, Hub API, and System API. Tagged areas include API Platform, Japanese Data, Free Tier, and AI Integration.


  The shirabe-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  shirabe-dev''s developer surface includes API reference, authentication, documentation, pricing, and 20 more developer resources.'
plans:
- name: Shirabe Dev Plans Pricing
  plan_count: 3
  slug: shirabe-dev-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: shirabe-dev API Rules
  rule_count: 19
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 1
  slug: shirabe-dev-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 67.9
    developer_ergonomics: 27.4
    discoverability: 57.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shirabe-dev/shirabe-dev-2026-11-03T143132.png
security:
- kind: authentication
  name: Shirabe Dev Authentication
  slug: shirabe-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shirabe Dev Domain Security
  slug: shirabe-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shirabe-dev
tags:
- API Platform
- Japanese Data
- Free Tier
- AI Integration
website: https://shirabe.dev/
---
