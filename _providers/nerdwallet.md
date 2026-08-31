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
  scored_at: '2026-08-30'
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
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
