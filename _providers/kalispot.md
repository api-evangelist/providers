---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kalispot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kalispot.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kalispot/
created: '2026-07-17'
description: KaliSpot is a fintech network operated by Outsource Monetic Group Inc. (OMG), an Atlanta-headquartered startup with legal presence in Senegal and Morocco. KaliSpots are Financial Inclusive Service Points (FISP) — ATM and interactive teller machine (ITM) locations running a brand-agnostic, "phygital" infrastructure that bridges physical cash and digital financial services. From a single access point, customers reach banks, mobile money operators, and fintechs for 24/7 cash-in/cash-out (CICO), positioning KaliSpot as an independent omnichannel ATM operator across Francophone West and Central Africa, with pilots launched in Senegal and Côte d'Ivoire. Founded 2021; pre-seed funding from 500 Global and Grenfell Holdings. No public developer API or documentation surface has been published to date.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kalispot.png
layout: provider
modified: '2026-07-19'
name: KaliSpot
nav: Providers
network: true
overview: KaliSpot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial-Services, Payments, and Financial Inclusion.
random_paper: 10
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 2
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
    - north-america
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kalispot/refs/heads/main/screenshots/kalispot-2026-07-25T223434.png
security:
- kind: domain-security
  name: Kalispot Domain Security
  slug: kalispot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kalispot
tags:
- Company
- Fintech
- Financial-Services
- Payments
- Financial Inclusion
- Mobile Money
- ATM Network
- Banking
- Africa
website: https://kalispot.com
---
