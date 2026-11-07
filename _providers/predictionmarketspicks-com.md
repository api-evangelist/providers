---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API providing free prediction market data and picks.
  name: Prediction Market Picks API
  slug: prediction-market-picks-api
- description: 'predictionmarketspicks-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: predictionmarketspicks-com API
  slug: predictionmarketspicks-com-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/predictionmarketspicks-com/plans/predictionmarketspicks-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/predictionmarketspicks-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/predictionmarketspicks-com/rules/predictionmarketspicks-com-rules.yml
  title: ''
  type: Spectral
  url: rules/predictionmarketspicks-com-rules.yml
- group: design
  href: https://artifacts.apis.io/predictionmarketspicks-com/json-ld/predictionmarketspicks-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/predictionmarketspicks-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/predictionmarketspicks-com/vocabulary/predictionmarketspicks-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/predictionmarketspicks-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/predictionmarketspicks-com/data-model/predictionmarketspicks-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/predictionmarketspicks-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/predictionmarketspicks-com/security/predictionmarketspicks-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/predictionmarketspicks-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/predictionmarketspicks-com/authentication/predictionmarketspicks-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/predictionmarketspicks-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/predictionmarketspicks-com/conformance/predictionmarketspicks-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/predictionmarketspicks-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/predictionmarketspicks-com/llms/predictionmarketspicks-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/predictionmarketspicks-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/predictionmarketspicks-com/well-known/predictionmarketspicks-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/predictionmarketspicks-com-security.txt
- group: agent
  href: https://artifacts.apis.io/predictionmarketspicks-com/well-known/predictionmarketspicks-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/predictionmarketspicks-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/predictionmarketspicks-com/hosts/predictionmarketspicks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/predictionmarketspicks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/predictionmarketspicks-com/vendors/predictionmarketspicks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/predictionmarketspicks-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://predictionmarketspicks.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://predictionmarketspicks.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://predictionmarketspicks.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://predictionmarketspicks.com/news
- group: start
  title: ''
  type: Login
  url: https://predictionmarketspicks.com/login
- group: other
  title: ''
  type: Leadership
  url: https://predictionmarketspicks.com/team
- group: docs
  title: ''
  type: Documentation
  url: https://predictionmarketspicks.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://predictionmarketspicks.com/mcp/setup
- group: auth
  href: https://artifacts.apis.io/predictionmarketspicks-com/security/predictionmarketspicks-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/predictionmarketspicks-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/predictionmarketspicks-com/security/predictionmarketspicks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/predictionmarketspicks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://predictionmarketspicks.com/
coverage:
  checked: '2026-10-29'
  detail: API documentation is served as a JavaScript‑rendered page without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://predictionmarketspicks.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Prediction Market Picks provides free prediction market picks across platforms like Kalshi, Polymarket, DraftKings, and FanDuel. It offers live edge calculations, an EV calculator, combo builder, and a weekly newsletter for traders, delivering analytical tools and market insights to help users make informed betting decisions.
image: https://predictionmarketspicks.com/og-image.png
json_schemas:
- name: GetApiPublicRecessionTrackerResponse
  property_count: 7
  slug: predictionmarketspicks-com-get-api-public-recession-tracker-response
- name: GetApiV1AlertsResponse
  property_count: 7
  slug: predictionmarketspicks-com-get-api-v1-alerts-response
jsonld:
- class_count: 2
  name: Predictionmarketspicks Com Context
  property_count: 7
  slug: predictionmarketspicks-com-context
layout: provider
modified: '2026-10-29'
name: predictionmarketspicks-com
nav: Providers
network: true
overview: 'predictionmarketspicks-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Prediction Markets, TradingTools, Analytics, and News.


  The predictionmarketspicks-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  predictionmarketspicks-com''s developer surface includes authentication, pricing, documentation, getting-started guide, and 20 more developer resources.'
plans:
- name: Predictionmarketspicks Com Plans Pricing
  plan_count: 4
  slug: predictionmarketspicks-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: predictionmarketspicks-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: predictionmarketspicks-com-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 20.4
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.1
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/predictionmarketspicks-com/predictionmarketspicks-com-2026-11-03T141434.png
security:
- kind: authentication
  name: Predictionmarketspicks Com Authentication
  slug: predictionmarketspicks-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Predictionmarketspicks Com Domain Security
  slug: predictionmarketspicks-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Predictionmarketspicks Com Vulnerability Disclosure
  slug: predictionmarketspicks-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: predictionmarketspicks-com
tags:
- Company
- Prediction Markets
- TradingTools
- Analytics
- News
website: https://predictionmarketspicks.com/
---
