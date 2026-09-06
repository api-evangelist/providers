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
  url: security/mintifi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mintifi.com
created: '2026-07-17'
description: Mintifi is an Indian supply-chain financing platform that provides inventory and working-capital financing to SMEs, distributors, and dealers across manufacturer distribution networks. Its products include checkout and inventory financing, an Electronic Invoice Presentment and Payment (EIPP) solution for ERP-integrated invoice settlement and reconciliation, WhatsApp-based inventory financing, and Mintifi Collect for payment collection with Tally integration. The company exposes ERP-integration APIs to partners and is backed by Norwest Venture Partners. No public developer portal, OpenAPI, or self-serve API documentation is currently published; the docs host is access-gated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mintifi.png
layout: provider
modified: '2026-07-20'
name: Mintifi
nav: Providers
network: true
overview: Mintifi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Lending, Supply Chain Finance, and Fintech.
random_paper: 17
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
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mintifi/refs/heads/main/screenshots/mintifi-2026-08-07T183654.png
security:
- kind: domain-security
  name: Mintifi Domain Security
  slug: mintifi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mintifi
tags:
- Company
- Financial-Services
- Lending
- Supply Chain Finance
- Fintech
- SME
- Payments
- India
website: https://mintifi.com
---
