---
access_model:
  confidence: high
  label: No public API — aggregator-only (Plaid)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - review
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
- group: start
  title: ''
  type: Signup
  url: https://dave.com/register
- group: company
  title: ''
  type: Website
  url: https://dave.com
- group: company
  title: ''
  type: Blog
  url: https://dave.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.dave.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://dave.com/no-hidden-fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dave.com/terms-and-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dave.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dave-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dave-inc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dave-domain-security.yml
created: '2026-07-17'
description: 'Dave is a U.S. consumer financial-technology company (Nasdaq: DAVE), founded in 2016 and headquartered in Los Angeles, that operates a mobile banking app serving roughly 14 million members. Its products include ExtraCash short-term cash advances of up to $500 (underwritten with its CashAI cash-flow model rather than credit scores), an FDIC-insured Dave Checking account with early direct deposit and Round-Up savings, and a Goals savings account. Banking services are provided through partner banks such as Coastal Community Bank. Dave is a consumer app and does not publish a first-party public developer API, SDKs, or a developer portal: there is no developer.dave.com / docs.dave.com, and api.dave.com is the app''s private, undocumented mobile backend. Programmatic access to Dave-held consumer data is aggregator-mediated — Dave both consumes Plaid (to let members link external accounts) and is reachable as a supported institution through open-finance aggregators. This profile captures
  its public identity, aggregator-only open-finance posture, commercial link surface, and domain-security posture.'
image: https://dave.com/icons/icon-512.png
layout: provider
modified: '2026-07-23'
name: Dave
nav: Providers
network: true
overview: 'Dave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Neobank, and Personal Finance.


  Dave''s developer surface includes signup flow, engineering blog, support, pricing, and 6 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dave/refs/heads/main/screenshots/dave-2026-07-25T211429.png
security:
- kind: domain-security
  name: Dave Domain Security
  slug: dave-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dave
tags:
- Company
- Fintech
- Banking
- Neobank
- Personal Finance
- Cash Advance
- Financial-Services
- Mobile Banking
- United States
- Open Finance
- Aggregator Access
- Plaid
website: https://dave.com
---
