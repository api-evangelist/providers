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
  url: security/stake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getyourstake.com/
- group: company
  title: ''
  type: Blog
  url: https://getyourstake.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getyourstake.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getyourstake.com/legal/terms-of-use
created: '2026-07-17'
description: 'Stake (Stake Technologies, Inc., NMLS #2535498) operates the "Return on Rent" cash-back network for renters. Renters earn cash back on their rent payments, build credit history through on-time payments, unlock exclusive local deals, and access banking services including an FDIC-insured checking account and debit card provided through banking partner Midland States Bank. Co-founded by Rowland Hobbs and Jimmy Jacobson, the platform reports more than 550,000 homes in its network and over $50M in cash back earned by renters, averaging roughly $350 per renter annually. Stake is a consumer-facing fintech product; it does not publish a public developer API, SDK, or documentation surface at this time. Added to the API Evangelist network as a VC-portfolio lead (surfaced under Battery Ventures).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stake.png
layout: provider
modified: '2026-07-21'
name: '@Stake'
nav: Providers
network: true
overview: '@Stake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Real-Estate, PropTech, and Renters.


  @Stake''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.7
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stake/refs/heads/main/screenshots/stake-2026-09-02T160723.png
security:
- kind: domain-security
  name: Stake Domain Security
  slug: stake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stake
tags:
- Company
- Fintech
- Real-Estate
- PropTech
- Renters
- Cashback
- Banking
- Rewards
website: https://getyourstake.com/
---
