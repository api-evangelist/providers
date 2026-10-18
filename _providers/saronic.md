---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/saronic/refs/heads/main/plans/saronic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/saronic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/saronic/refs/heads/main/rate-limits/saronic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/saronic-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/saronic/refs/heads/main/finops/saronic-finops.yml
  title: ''
  type: FinOps
  url: finops/saronic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.saronic.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/saronic/refs/heads/main/security/saronic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saronic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saronic.com/
- group: other
  title: ''
  type: Vessels
  url: https://www.saronic.com/vessels
- group: company
  title: ''
  type: About
  url: https://www.saronic.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.saronic.com/careers
- group: company
  title: ''
  type: News
  url: https://www.saronic.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.saronic.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saronic-technologies/
created: '2026-05-23'
description: Saronic Technologies designs, manufactures, and deploys AI-enabled autonomous surface vessels (ASVs) for maritime security, domain awareness, reconnaissance, logistics, and payload delivery. The Austin-based company sells to the U.S. Navy, allied defense forces, and select commercial and government customers. Vessel models include Spyglass, Cutlass, Corsair, and Marauder, ranging from 6 to 150 feet. The Echelon software platform provides mission planning, high-fidelity simulation, fleet command-and-control, and open architecture for third-party payload integration (ISR sensors, EW, comms, weapons). Saronic does not publish a public, self-service developer API; integrations are arranged through partnership and are subject to U.S. export controls (ITAR/EAR).
finops:
- has_sources: false
  method: generated
  name: Saronic Finops
  primary_unit: ''
  service_category: API
  slug: saronic-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saronic.png
layout: provider
modified: '2026-10-06'
name: Saronic Technologies
nav: Providers
network: true
overview: 'Saronic Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Defense, Maritime, Autonomous Surface Vessels, ASV, and Echelon.


  Saronic Technologies'' developer surface includes engineering blog, product news, and 10 more developer resources.'
plans:
- name: Saronic Plans Pricing
  plan_count: 1
  slug: saronic-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Saronic Rate Limits
  slug: saronic-rate-limits
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 5.3
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/saronic/refs/heads/main/screenshots/saronic-2026-06-20T193437.png
security:
- kind: domain-security
  name: Saronic Domain Security
  slug: saronic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: saronic
tags:
- Defense
- Maritime
- Autonomous Surface Vessels
- ASV
- Echelon
- Command and Control
- Mission Software
- Unmanned Systems
- ITAR
- Naval
website: https://www.saronic.com/
---
