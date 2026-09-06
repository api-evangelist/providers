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
  url: security/efishery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://efishery.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/efishery
created: '2026-07-17'
description: 'eFishery is an Indonesian aquaculture technology ("fishtech") company founded in 2013 in Bandung by Gibran Huzaifah and Chrisna Aditya. Its platform combined an IoT smart auto-feeder (eFeeder) that dispenses feed to fish and shrimp ponds and streams pond telemetry to a smartphone app, with an integrated services layer: eFisheryKu / eFarm farm-management software, eFund (including the Kabayan "pay later" financing product) linking smallholder farmers to lenders, and eFresh / eMart marketplaces connecting farmers to feed suppliers and downstream buyers. The company raised a $90M Series C (2022) and a $200M Series D (2023) at a unicorn valuation, backed by investors including 500 Global, Aqua-Spark, SoftBank Vision Fund 2, Temasek, and Northstar. In late 2024 an audit alleged large-scale financial-statement fraud dating to 2018; both founders resigned and the company underwent multiple rounds of layoffs and restructuring through 2025. This record was surfaced as a 500 Global portfolio
  company and enriched by the API Evangelist pipeline; eFishery exposes no public developer API or developer portal, and its primary efishery.com domain currently resolves to a parked/forwarding host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/efishery.png
layout: provider
modified: '2026-07-19'
name: eFishery
nav: Providers
network: true
overview: eFishery is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aquaculture, AgriTech, FishTech, and IoT.
random_paper: 2
score:
  band: minimal
  composite: 5.3
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/efishery/refs/heads/main/screenshots/efishery-2026-07-25T212946.png
security:
- kind: domain-security
  name: Efishery Domain Security
  slug: efishery-domain-security
  summary_line: DMARC
slug: efishery
tags:
- Company
- Aquaculture
- AgriTech
- FishTech
- IoT
- Fintech
- Marketplace
- Smart Feeder
- Indonesia
website: https://efishery.com
---
