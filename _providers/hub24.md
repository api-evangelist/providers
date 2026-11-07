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
api_count: 1
apis:
- description: HUB24's developer centre (developer.hub24.com.au) provides an API library for developers integrating with HUB24 infrastructure, with support available; access to the library requires registering or lo
  name: HUB24 API Library
  slug: hub24-api-library
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/hub24/well-known/hub24-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hub24-status-security.txt
- group: agent
  href: https://artifacts.apis.io/hub24/well-known/hub24-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hub24-well-known.yml
- group: other
  href: https://artifacts.apis.io/hub24/hosts/hub24-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hub24-hosts.yml
- group: other
  href: https://artifacts.apis.io/hub24/vendors/hub24-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hub24-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hub24/security/hub24-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hub24-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hub24.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hub24.com.au/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hub24.com.au/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hub24.com.au/
created: '2026-10-21'
description: HUB24 Limited is an ASX-listed (ASX:HUB) Australian wealth-technology company that describes itself as a provider of integrated platform, technology and data solutions for the Australian wealth industry. Its group includes the HUB24 investment and superannuation Platform (managed portfolios and a broad range of investment options for financial advisers and their clients), Class (SMSF administration, trust accounting and portfolio management software), NowInfinity (legal documentation and corporate compliance) and myprosperity. HUB24 runs a developer centre at developer.hub24.com.au where registered users can access its API library. Its public sites sit behind an Incapsula bot challenge, so this profile is built from search-indexed company material.
layout: provider
modified: '2026-10-21'
name: HUB24
nav: Providers
network: true
overview: HUB24 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Investment Platform, Superannuation, and Financial Services.
random_paper: 13
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hub24 Domain Security
  slug: hub24-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hub24
tags:
- Company
- Wealth Management
- Investment Platform
- Superannuation
- Financial Services
- Fintech
- Australia
website: https://www.hub24.com.au/
---
