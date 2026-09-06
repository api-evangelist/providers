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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.t2pco.com/en
- group: auth
  title: ''
  type: TrustCenter
  url: security/t2p-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.t2pco.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/t2p-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/t2p-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.t2pco.com/en/t2p-privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.t2pco.com/en/contact-us-t2p
created: '2026-07-17'
description: T2P Co., Ltd. (DeepPocket) is a Bangkok, Thailand fintech founded in 2011 that provides comprehensive payment solutions for enterprises of all sizes. Its products include a payment gateway (cards, mobile wallets, in-store), a white-label digital wallet platform, corporate and prepaid card issuance, spend management with real-time controls, business escrow, the DeepBlok loyalty program, and the DeepPocket consumer e-wallet app for top-ups, payments, and global money transfers. T2P is backed by 500 Global, Benchachinda Holding, DTAC Accelerate, and J Ventures, and reports serving 10M+ customers and 30+ corporate clients. T2P holds PCI DSS compliance but publishes no public developer API surface; integrations are arranged directly with the company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/t2p.png
layout: provider
modified: '2026-07-21'
name: T2P
nav: Providers
network: true
overview: 'T2P is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payment Gateway, and Digital Wallet.


  T2P''s developer surface includes support and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/t2p/refs/heads/main/screenshots/t2p-2026-09-02T161656.png
security:
- kind: domain-security
  name: T2P Domain Security
  slug: t2p-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: T2P Trust Center
  slug: t2p-trust-center
  summary_line: PCI DSS
slug: t2p
tags:
- Company
- Fintech
- Payments
- Payment Gateway
- Digital Wallet
- Card Issuing
- E-Wallet
- Escrow
- Financial-Services
- Thailand
website: https://www.t2pco.com/en
---
