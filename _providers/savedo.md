---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.savedo.de'', ''status'': 302, ''note'': ''declared website redirects to https://www.raisin.com/de-de/ueber-weltsparen/savedo/ — a different registrable domain (savedo.de -> raisin.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: company
  title: ''
  type: Website
  url: https://www.savedo.de
- group: company
  title: ''
  type: About
  url: https://www.raisin.com/de-de/ueber-weltsparen/savedo/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/savedo-domain-security.yml
created: '2026-07-17'
description: Savedo was a German fintech operating a consumer deposit marketplace that let savers in Germany open fixed-term and savings accounts across multiple European partner banks from a single portal. Backed by Point Nine, it was acquired by Deposit Solutions in 2017 and is now a subsidiary brand of Raisin SE (WeltSparen). The Savedo customer portal was deactivated on 31 March 2022 and the brand no longer accepts new customers; existing balances are administered via flatexDEGIRO Bank AG. Savedo published no public API, developer portal, or SDKs. This profile is retained as a network lead surfaced from the Point Nine portfolio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/savedo.png
layout: provider
modified: '2026-07-21'
name: Savedo
nav: Providers
network: true
overview: Savedo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Savings, and Deposits.
random_paper: 12
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
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
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
screenshot: https://raw.githubusercontent.com/api-evangelist/savedo/refs/heads/main/screenshots/savedo-2026-09-02T154454.png
security:
- kind: domain-security
  name: Savedo Domain Security
  slug: savedo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: savedo
tags:
- Company
- Fintech
- Banking
- Savings
- Deposits
- Financial-Services
- Germany
- Defunct
website: https://www.savedo.de
---
