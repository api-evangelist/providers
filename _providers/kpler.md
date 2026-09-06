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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kpler Agentic Access
  operation_count: 4
  slug: kpler-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: MarineTraffic data services API (property of Kpler) for real-time and historical vessel tracking - current vessel positions and fleet positions, historical vessel tracks, port calls and berth calls, e
  name: MarineTraffic API
  slug: marinetraffic-api
- description: GraphQL API for vessel intelligence on 220,000+ vessels - technical particulars, dimensions, and capacity plus six levels of ownership (beneficial owner, registered owner, commercial manager, operator
  name: MarineTraffic Vessels API
  slug: marinetraffic-vessels-api
- description: Global vessel-position data feed launched September 2025 (replacing MarineTraffic AIS and the acquired Spire Maritime feeds) combining terrestrial, satellite, and roaming AIS from a 9,000+ station net
  name: Kpler AIS Data Feed
  slug: kpler-ais-data-feed
- baseURL: https://api.kpler.com
  baseurl_source: declared
  description: Flows and other aggregated series.
  name: Kpler Aggregations API
  slug: kpler-aggregations-api
- baseURL: https://api.kpler.com
  baseurl_source: declared
  description: The Authentication API from Kpler — 1 operation(s) for authentication.
  name: Kpler Authentication API
  slug: kpler-authentication-api
- baseURL: https://api.kpler.com
  baseurl_source: declared
  description: Trades, vessels, and other observed fact data.
  name: Kpler Facts API
  slug: kpler-facts-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kpler Direct Access Aggregations API
  slug: open-kpler-aggregations-api
- collection_type: open
  name: Kpler Direct Access Aggregations Authentication API
  slug: open-kpler-authentication-api
- collection_type: open
  name: Kpler Direct Access Aggregations Facts API
  slug: open-kpler-facts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kpler-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kpler-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kpler-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kpler.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kpler
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kpler.com/
- group: build
  title: ''
  type: SDK
  url: https://python-sdk.dev.kpler.com/
- group: build
  title: ''
  type: PostmanPublicWorkspace
  url: https://www.postman.com/kplerdev
- group: commercial
  title: ''
  type: Plans
  url: plans/kpler-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kpler-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kpler-finops.yml
created: '2026-07-11'
description: Kpler is a commodities intelligence and maritime data platform that tracks cargoes, vessels, and trade flows across oil, refined products, LNG, LPG, and dry bulk markets. Kpler owns MarineTraffic and FleetMon (acquired 2023) and acquired Spire's maritime AIS business (2025), giving it one of the largest terrestrial and satellite AIS vessel tracking networks in the world. Its Direct Access REST APIs deliver trades, flows, vessels, port calls, freight metrics, and inventories per commodity platform, while MarineTraffic APIs deliver live vessel positions, port calls, voyages, and vessel particulars. API access is customer-gated behind an enterprise subscription, but the documentation, Python SDK, and endpoint surface are publicly published.
finops:
- name: Kpler Finops
  service_category: Analytics and Market Data
  slug: kpler-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kpler.png
layout: provider
modified: '2026-07-11'
name: Kpler
nav: Providers
network: true
overview: 'Kpler publishes 3 APIs on the [APIs.io](https://apis.io/) network: Aggregations API, Authentication API, and Facts API. Tagged areas include Vessel Tracking, Maritime, Commodities, Supply Chain, and AIS.


  Kpler''s developer surface includes authentication, documentation, SDKs, and 8 more developer resources.'
plans:
- name: Kpler Plans Pricing
  plan_count: 3
  slug: kpler-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Kpler Rate Limits
  slug: kpler-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kpler/refs/heads/main/screenshots/kpler-2026-07-25T224256.png
security:
- kind: authentication
  name: Kpler Authentication
  slug: kpler-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Kpler Domain Security
  slug: kpler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kpler
tags:
- Vessel Tracking
- Maritime
- Commodities
- Supply Chain
- AIS
- Trade Flows
- Shipping
- Energy
website: https://www.kpler.com
---
