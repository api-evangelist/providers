---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.chinacarapi.com
  baseurl_source: spec
  description: ChinaCarAPI provides used‑car listings from Dongchedi and Che168.
  name: ChinaCarAPI
  slug: china-car-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/chinacarapi-com/well-known/chinacarapi-com-apify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chinacarapi-com-apify-security.txt
- group: commercial
  href: https://artifacts.apis.io/chinacarapi-com/plans/chinacarapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chinacarapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chinacarapi-com/vocabulary/chinacarapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chinacarapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/chinacarapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/chinacarapi-com/authentication/chinacarapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chinacarapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/chinacarapi-com/conformance/chinacarapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chinacarapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chinacarapi-com/llms/chinacarapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chinacarapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/chinacarapi-com/well-known/chinacarapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chinacarapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chinacarapi-com/hosts/chinacarapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chinacarapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chinacarapi-com/vendors/chinacarapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chinacarapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/chinacarapi-com/packages/chinacarapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/chinacarapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/chinacarapi-com/packages/chinacarapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/chinacarapi-com-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.chinacarapi.com`
- group: auth
  href: https://artifacts.apis.io/chinacarapi-com/security/chinacarapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chinacarapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chinacarapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://chinacarapi.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://chinacarapi.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://chinacarapi.com/start-china-import
- group: commercial
  title: ''
  type: Pricing
  url: https://chinacarapi.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://t.me/innqtech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThatMojo
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://t.me/api/mcp
  - status: 200
    url: https://chinacarapi.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: ChinaCarAPI provides developers with comprehensive data from China's used‑car marketplaces Dongchedi and Che168. The API delivers listings, prices, inspection reports, export eligibility, and detailed vehicle information in both English and original Chinese. Data is refreshed twice daily, with change‑feed support for incremental updates. Plans include a 5‑day trial and tiered pricing for starters, businesses, and scale users, with cryptocurrency payment options.
image: https://chinacarapi.com/en/opengraph-image?8009b09eac73d78c
layout: provider
modified: '2026-10-30'
name: chinacarapi-com
nav: Providers
network: true
overview: 'chinacarapi-com is listed with 1 API on the [APIs.io](https://apis.io/) network: ChinaCarAPI. Tagged areas include Automotive, Data, China, and Used Cars.


  chinacarapi-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 15 more developer resources.'
plans:
- name: Chinacarapi Com Plans Pricing
  plan_count: 4
  slug: chinacarapi-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Chinacarapi Com Rate Limits
  slug: chinacarapi-com-rate-limits
scopes:
- name: Chinacarapi Com Scopes
  scope_count: 0
  slug: chinacarapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 40.3
    catalog_earned_first_party: 12.0
    catalog_gap: 74.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 36.8
    contract_governance: 8.3
    contract_quality: 30.5
    developer_ergonomics: 46.9
    discoverability: 48.2
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 40.2
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chinacarapi-com/chinacarapi-com-2026-11-03T124024.png
security:
- kind: authentication
  name: Chinacarapi Com Authentication
  slug: chinacarapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chinacarapi Com Domain Security
  slug: chinacarapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chinacarapi-com
tags:
- Automotive
- Data
- China
- Used Cars
website: https://chinacarapi.com/
---
