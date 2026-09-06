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
  url: security/nerdwallet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nerdwallet.com
- group: company
  title: ''
  type: Blog
  url: https://www.nerdwallet.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.nerdwallet.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nerdwallet.com/p/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nerdwallet.com/p/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nerdwallet
created: '2026-07-17'
description: 'NerdWallet is a personal finance company that helps consumers make smarter money decisions across credit cards, banking, investing, loans, mortgages, insurance, and taxes. Through its website and mobile apps it offers comparison tools, product marketplaces, educational content, and free credit-score monitoring. Founded in 2009 and headquartered in San Francisco, NerdWallet is publicly traded (NASDAQ: NRDS) and was surfaced in the API Evangelist network as a portfolio company of ivp. As of this enrichment pass NerdWallet publishes no public developer API, developer portal, or well-known API discovery surface; this profile captures its public identity and domain-security posture.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nerdwallet.png
layout: provider
modified: '2026-07-20'
name: NerdWallet
nav: Providers
network: true
overview: 'NerdWallet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Personal Finance, Consumer Finance, and Financial-Services.


  NerdWallet''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Nerdwallet Domain Security
  slug: nerdwallet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nerdwallet
tags:
- Company
- Fintech
- Personal Finance
- Consumer Finance
- Financial-Services
- Credit Cards
- Comparison
website: https://www.nerdwallet.com
---
