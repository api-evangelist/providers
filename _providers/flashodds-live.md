---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Flash Props API provides player-props data and MCP services.
  name: Flash Props API
  slug: flash-props-api
- baseURL: https://sorqen.flashodds.live
  baseurl_source: declared
  description: Sorqen API is a sports fair-value API and MCP server by Flash AI Solutions, providing sportsbook-derived no-vig probabilities, confidence, provenance, history, and prediction-market reference pricing.
  name: Sorqen API API
  slug: sorqen-api-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/flashodds-live/rules/flashodds-live-rules.yml
  title: ''
  type: Spectral
  url: rules/flashodds-live-rules.yml
- group: design
  href: https://artifacts.apis.io/flashodds-live/json-ld/flashodds-live-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flashodds-live-context.jsonld
- group: design
  href: https://artifacts.apis.io/flashodds-live/vocabulary/flashodds-live-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flashodds-live-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/flashodds-live/conformance/flashodds-live-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flashodds-live-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/flashodds-live/plans/flashodds-live-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flashodds-live-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flashodds-live/data-model/flashodds-live-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flashodds-live-data-model.yml
- group: auth
  href: https://artifacts.apis.io/flashodds-live/authentication/flashodds-live-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flashodds-live-authentication.yml
- group: design
  href: https://artifacts.apis.io/flashodds-live/errors/flashodds-live-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flashodds-live-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/flashodds-live/llms/flashodds-live-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flashodds-live-llms.txt
- group: agent
  href: https://artifacts.apis.io/flashodds-live/well-known/flashodds-live-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flashodds-live-well-known.yml
- group: other
  href: https://artifacts.apis.io/flashodds-live/hosts/flashodds-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flashodds-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/flashodds-live/vendors/flashodds-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flashodds-live-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flashodds.live/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://api.flashodds.live/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flashodds.live/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://api.flashodds.live/pricing
- group: start
  title: ''
  type: Login
  url: https://flashodds.live/login
- group: docs
  title: ''
  type: Documentation
  url: https://api.flashodds.live/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://flashodds.live/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://api.flashodds.live/connect
- group: docs
  title: ''
  type: APIReference
  url: https://api.flashodds.live/reference
- group: auth
  href: https://artifacts.apis.io/flashodds-live/security/flashodds-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flashodds-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flashodds.live/
created: '2026-10-30'
description: FlashOdds Live provides real-time sports betting odds and analytics through a modern API, enabling developers to integrate live odds, event data, and betting market information into applications, websites, and platforms. The service offers comprehensive coverage of major sports, detailed market depth, and historical data, supporting use cases such as odds comparison, betting widgets, and automated trading strategies. It emphasizes low latency, high reliability, and clear documentation for seamless integration.
image: https://flashodds.live/og/site
json_schemas:
- name: FairValue
  property_count: 16
  slug: flashodds-live-fair-value
- name: GradeRequest
  property_count: 4
  slug: flashodds-live-grade-request
- name: GradeResponse
  property_count: 8
  slug: flashodds-live-grade-response
jsonld:
- class_count: 7
  name: Flashodds Live Context
  property_count: 42
  slug: flashodds-live-context
layout: provider
modified: '2026-10-30'
name: flashodds-live
nav: Providers
network: true
overview: 'flashodds-live publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Sorqen API API, and 1 more. Tagged areas include Sports, Betting, Odds, Real-time, and Analytics.


  The flashodds-live catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  flashodds-live''s developer surface includes authentication, pricing, documentation, getting-started guide, API reference, and 18 more developer resources.'
plans:
- name: Flashodds Live Plans Pricing
  plan_count: 4
  slug: flashodds-live-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: flashodds-live API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: flashodds-live-rules
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 63.6
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Flashodds Live Authentication
  slug: flashodds-live-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Flashodds Live Domain Security
  slug: flashodds-live-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flashodds-live
tags:
- Sports
- Betting
- Odds
- Real-time
- Analytics
- API
website: https://flashodds.live/
---
