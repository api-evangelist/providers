---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocean-aero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oceanaero.com
- group: company
  title: ''
  type: About
  url: https://www.oceanaero.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.oceanaero.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oceanaero.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oceanaero.com/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/ocean-aero-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocean-aero-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ocean-aero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ocean-aero-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Ocean Aero's entire web presence is a 13-page Squarespace marketing site for the Triton AUSV with no developer, docs or API section; fleets are run from the company's own proprietary mission-control GUI, and api./developer./docs./portal./data.oceanaero.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://www.oceanaero.com/sitemap.xml
  - status: 404
    url: https://www.oceanaero.com/openapi.json
  - status: 404
    url: https://www.oceanaero.com/llms.txt
  - status: 404
    url: https://www.oceanaero.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Ocean Aero is a Gulfport, Mississippi maritime robotics manufacturer that designs, builds and operates the Triton, an environmentally powered Autonomous Underwater and Surface Vehicle (AUSV) that can both sail on the surface and submerge to collect data above and below the waterline and relay it back to shore. The 14-foot platform harvests wind and solar energy, carries pre-packaged or custom payloads for defense, ocean research and offshore energy missions, and is managed through Ocean Aero's own proprietary mission-control GUI with fleet-wide waypoint and payload management. As of this profile Ocean Aero sells vehicles, payloads and mission services — it publishes no public developer program, no API reference and no machine-readable API contract.
image: https://static1.squarespace.com/static/6a563a75f3daa06a8c545fa3/t/6a5643493543696e32b268b7/1784038217324/Option_5.png?format=1500w
layout: provider
modified: '2026-08-26'
name: Ocean Aero
nav: Providers
network: true
overview: 'Ocean Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Maritime, Autonomous Vehicles, Uncrewed Systems, and Robotics.


  Ocean Aero''s developer surface includes support and 9 more developer resources.'
plans:
- name: Ocean Aero Plans Pricing
  plan_count: 0
  slug: ocean-aero-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Ocean Aero Rate Limits
  slug: ocean-aero-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocean-aero/refs/heads/main/screenshots/ocean-aero-2026-09-02T150821.png
security:
- kind: domain-security
  name: Ocean Aero Domain Security
  slug: ocean-aero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ocean-aero
tags:
- Company
- Maritime
- Autonomous Vehicles
- Uncrewed Systems
- Robotics
- Ocean Data
- Defense
- Hardware
website: https://www.oceanaero.com
---
