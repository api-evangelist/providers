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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/compound-finance/well-known/compound-finance-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/compound-finance-clarity-security.txt
- group: agent
  href: https://artifacts.apis.io/compound-finance/well-known/compound-finance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/compound-finance-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://artifacts.apis.io/compound-finance/hosts/compound-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compound-finance-hosts.yml
- group: other
  href: https://artifacts.apis.io/compound-finance/vendors/compound-finance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compound-finance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.compound.xyz/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.compound.xyz/privacy-policy
- group: auth
  href: https://artifacts.apis.io/compound-finance/security/compound-finance-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/compound-finance-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/compound-finance/security/compound-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compound-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://compoundlabs.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.compound.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://api.compound.xyz/
- group: company
  title: ''
  type: Blog
  url: https://blog.compound.xyz/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.compound.xyz
  - status: 200
    url: https://www.hiive.com/securities/compound-finance-stock
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Compound Finance is a decentralized finance (DeFi) protocol that enables users to earn interest on crypto assets by supplying them to liquidity pools and to borrow assets against collateral. It operates on multiple blockchains, offering transparent, algorithmic interest rates and governance through COMP token holders. The platform provides a suite of APIs for market data, account management, and protocol interactions, supporting developers building DeFi applications.
image: https://framerusercontent.com/images/bnPNZFQ54oKYRQG78PxAAYin8A.jpg
layout: provider
modified: '2026-10-10'
name: Compound Finance
nav: Providers
network: true
overview: 'Compound Finance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Finance, Lending, Cryptocurrency, and Blockchain.


  Compound Finance''s developer surface includes documentation, API reference, engineering blog, and 10 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 14.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/compound-finance/compound-finance-2026-11-03T125015.png
security:
- kind: domain-security
  name: Compound Finance Domain Security
  slug: compound-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Compound Finance Vulnerability Disclosure
  slug: compound-finance-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: compound-finance
tags:
- DeFi
- Finance
- Lending
- Cryptocurrency
- Blockchain
website: https://compoundlabs.xyz
---
