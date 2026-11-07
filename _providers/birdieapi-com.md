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
    agent_skills: derived
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Birdieapi Com Agentic Access
  operation_count: 14
  slug: birdieapi-com-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://mcp.birdieapi.com
  baseurl_source: declared
  description: The Basic lookup API from birdieapi-com — 4 operation(s) for basic lookup.
  name: birdieapi-com Basic lookup API
  slug: birdieapi-com-basic-lookup-api
- baseURL: https://mcp.birdieapi.com
  baseurl_source: declared
  description: The Static reference API from birdieapi-com — 3 operation(s) for static reference.
  name: birdieapi-com Static reference API
  slug: birdieapi-com-static-reference-api
- baseURL: https://mcp.birdieapi.com
  baseurl_source: declared
  description: The Stats + aggregation API from birdieapi-com — 6 operation(s) for stats + aggregation.
  name: birdieapi-com Stats + aggregation API
  slug: birdieapi-com-stats-aggregation-api
- baseURL: https://mcp.birdieapi.com
  baseurl_source: declared
  description: The Time-series API from birdieapi-com — 1 operation(s) for time-series.
  name: birdieapi-com Time Series API
  slug: birdieapi-com-time-series-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/birdieapi-com/agentic-access/birdieapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/birdieapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/birdieapi-com/plans/birdieapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/birdieapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/birdieapi-com/rules/birdieapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/birdieapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/birdieapi-com/vocabulary/birdieapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/birdieapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/birdieapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/birdieapi-com/errors/birdieapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/birdieapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/birdieapi-com/conformance/birdieapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/birdieapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/birdieapi-com/llms/birdieapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/birdieapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/birdieapi-com/well-known/birdieapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/birdieapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/birdieapi-com/hosts/birdieapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/birdieapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/birdieapi-com/vendors/birdieapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/birdieapi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://birdieapi.com/terms
- group: operate
  title: ''
  type: Support
  url: https://birdieapi.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://birdieapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://birdieapi.com/dashboard/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://birdieapi.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://birdieapi.com/pricing
- group: start
  title: ''
  type: Login
  url: https://birdieapi.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://birdieapi.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://birdieapi.com/for/developers
- group: docs
  title: ''
  type: APIReference
  url: https://birdieapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/birdieapi-com/authentication/birdieapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/birdieapi-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/birdieapi-com/security/birdieapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birdieapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://birdieapi.com/
created: '2026-10-30'
description: BirdieAPI offers a comprehensive golf data API providing historical and current PGA Tour, LPGA, and other professional golf tournament statistics. The service includes leaderboards, hole-by-hole scores, player performance metrics, course ratings, and odds for major winners. With tiered pricing, free credits, and detailed documentation, developers can integrate real-time golf data into apps, analytics platforms, and fantasy sports services. The API emphasizes reliability, extensive coverage of tours, and clear rate‑limit policies.
image: https://birdieapi.com/opengraph-image?8a6b7f7b7786f567
layout: provider
modified: '2026-10-30'
name: birdieapi-com
nav: Providers
network: true
overview: 'birdieapi-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basic lookup API, Static reference API, Stats + aggregation API, and 1 more. Tagged areas include Company, Bird Tracking, Migration Analytics, Open Data, and Conservation.


  The birdieapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  birdieapi-com''s developer surface includes support, sandbox, pricing, documentation, API reference, authentication, and 18 more developer resources.'
plans:
- name: Birdieapi Com Plans Pricing
  plan_count: 4
  slug: birdieapi-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: birdieapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: birdieapi-com-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/birdieapi-com/birdieapi-com-2026-11-03T121743.png
security:
- kind: authentication
  name: Birdieapi Com Authentication
  slug: birdieapi-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Birdieapi Com Domain Security
  slug: birdieapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: list-tournaments
  slug: birdieapi-com-list_tournaments
slug: birdieapi-com
tags:
- Company
- Bird Tracking
- Migration Analytics
- Open Data
- Conservation
website: https://birdieapi.com/
---
