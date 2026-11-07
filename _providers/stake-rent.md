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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/stake-rent/well-known/stake-rent-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stake-rent-status-security.txt
- group: agent
  href: https://artifacts.apis.io/stake-rent/llms/stake-rent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stake-rent-llms.txt
- group: agent
  href: https://artifacts.apis.io/stake-rent/well-known/stake-rent-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stake-rent-well-known.yml
- group: other
  href: https://artifacts.apis.io/stake-rent/hosts/stake-rent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stake-rent-hosts.yml
- group: other
  href: https://artifacts.apis.io/stake-rent/vendors/stake-rent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stake-rent-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stake.rent/
- group: auth
  href: https://artifacts.apis.io/stake-rent/security/stake-rent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stake-rent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stake.rent/
- group: company
  title: ''
  type: Blog
  url: https://stake.rent/blog.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stake.rent/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stake.rent/terms.html
coverage:
  checked: '2026-10-29'
  detail: No API documentation or machine‑readable contract was found on the provider’s site.
  evidence:
  - status: 200
    url: https://stake.rent/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Stake provides cash back rewards for renters, helping them earn money back on moving, renting, and saving. The platform partners with over 600,000 renters in the Renter Network, offering cash back on eligible transactions and services. Stake aims to accelerate renter wealth through a mission-driven approach, leveraging partnerships with financial services and merchants to deliver real financial benefits to its users.
image: https://stake.rent/og.png
layout: provider
modified: '2026-10-29'
name: '@Stake'
nav: Providers
network: true
overview: '@Stake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Cashback, Renters, and Financial Services.


  @Stake''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 18.4
  previous_composite: 13.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stake-rent/stake-rent-2026-11-03T143722.png
security:
- kind: domain-security
  name: Stake Rent Domain Security
  slug: stake-rent-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: stake-rent
tags:
- Company
- Fintech
- Cashback
- Renters
- Financial Services
website: https://stake.rent/
---
