---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST API for programmatically sending digital gift cards, virtual prepaid Visa/Mastercard, e-gift cards, and other digital rewards instantly to recipients. Supports campaign management, recipient trac
  name: Rybbon Instant Rewards API
  slug: rybbon-instant-rewards-api
- description: 'REST API for integrating a points-based reward system, allowing platforms to allocate points to recipients which can then be redeemed for digital gift cards and prepaid rewards. Uses OAuth 2.0 client '
  name: Rybbon Points-to-Rewards API
  slug: rybbon-points-to-rewards-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rybbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bhnrewards.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bhnrewards.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bhnrewards
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bhnrewards
- group: company
  title: ''
  type: Blog
  url: https://www.bhnrewards.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bhnrewards.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rybbon.net/
- group: other
  title: ''
  type: X
  url: https://twitter.com/BHNrewards
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/rybbon/refs/heads/main/plans/rybbon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/rybbon/refs/heads/main/rate-limits/rybbon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/rybbon/refs/heads/main/finops/rybbon-finops.yml
created: 2026-06-13
description: Rybbon (now BHN Rewards) is a digital rewards management platform with a REST API for sending gift cards and prepaid virtual cards, managing reward campaigns, tracking recipient engagement, and accessing reward analytics. The platform supports both Instant Rewards and Points-to-Rewards integration models, authenticated via OAuth 2.0 client credentials, and serves marketing, market research, academic research, and employee incentive use cases globally.
finops:
- name: Rybbon Finops
  service_category: ''
  slug: rybbon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rybbon.png
layout: provider
modified: 2026-06-13
name: Rybbon
nav: Providers
network: true
overview: 'Rybbon publishes 1 API on the [APIs.io](https://apis.io/) network: Instant Rewards API. Tagged areas include Digital Rewards, Gift Cards, Prepaid Cards, Incentives, and Marketing.


  Rybbon''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Rybbon Plans Pricing
  plan_count: 2
  slug: rybbon-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Rybbon Rate Limits
  slug: rybbon-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 29.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rybbon/refs/heads/main/screenshots/rybbon-2026-06-20T193311.png
security:
- kind: domain-security
  name: Rybbon Domain Security
  slug: rybbon-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: rybbon
tags:
- Digital Rewards
- Gift Cards
- Prepaid Cards
- Incentives
- Marketing
- Employee Recognition
- Market Research
- Points
- Fintech
website: https://www.bhnrewards.com/
---
