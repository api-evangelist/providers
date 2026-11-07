---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dimatrix/hosts/dimatrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dimatrix-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diamatrix.com/about/privacy-terms-and-conditions/
- group: company
  title: ''
  type: Newsroom
  url: https://diamatrix.com/news/
- group: auth
  href: https://artifacts.apis.io/dimatrix/security/dimatrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dimatrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diamatrix.com
coverage:
  checked: '2026-10-23'
  detail: No API documentation or machine-readable contracts were found on the company's website.
  evidence:
  - status: 200
    url: https://diamatrix.com
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Dimatrix Ltd is a provider of ophthalmic surgical instruments, knives, sutures and related medical devices. Founded in 1993, the company offers a range of high‑quality products for eye surgeons, including diamond‑coated knives, stainless‑steel instruments, iris speculum devices, and suture solutions. Their portfolio emphasizes innovation, precision, and patient outcomes, serving hospitals and eye‑care facilities worldwide.
layout: provider
modified: '2026-10-23'
name: Dimatrix
nav: Providers
network: true
overview: Dimatrix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical, Ophthalmology, Surgical Instruments, Healthcare, and Devices.
random_paper: 2
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 6.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dimatrix/dimatrix-2026-11-03T130732.png
security:
- kind: domain-security
  name: Dimatrix Domain Security
  slug: dimatrix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dimatrix
tags:
- Medical
- Ophthalmology
- Surgical Instruments
- Healthcare
- Devices
website: https://diamatrix.com
---
