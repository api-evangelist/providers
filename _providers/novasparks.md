---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://novasparks.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.exegy.com/ — a different registrable domain (novasparks.com -> exegy.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://novasparks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://novasparks.com/api_or_wireformat/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://novasparks.com/privacy-cookie-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novasparks-domain-security.yml
created: '2026-07-17'
description: NovaSparks builds ultra-low-latency FPGA market data solutions for banks, trading firms, and electronic markets. Its NovaTick ticker plant, delivered as a hardware appliance or PCIe card, normalizes and distributes real-time feeds across global equities, options (OPRA), and other asset classes with deterministic nanosecond latency. Integration is via a proprietary ultra-low-latency C++ Software API and the NovaSparks Wire Format (NSWF), a normalized message protocol whose full specification is provided to banks and trading firms under NDA rather than published publicly. NovaSparks is now part of Exegy. Surfaced as a portfolio company of Partech.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novasparks.png
layout: provider
modified: '2026-07-20'
name: NovaSparks
nav: Providers
network: true
overview: 'NovaSparks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure Saas, Financial-Services, Market Data, and FPGA.


  NovaSparks'' developer surface includes documentation and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 1.2
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Novasparks Domain Security
  slug: novasparks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: novasparks
tags:
- Company
- Infrastructure Saas
- Financial-Services
- Market Data
- FPGA
- Low Latency
- Trading
- Hardware
website: https://novasparks.com/
---
