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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/stockland/well-known/stockland-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stockland-www-security.txt
- group: auth
  href: https://artifacts.apis.io/stockland/security/stockland-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/stockland-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stockland/well-known/stockland-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stockland-security.txt
- group: agent
  href: https://artifacts.apis.io/stockland/well-known/stockland-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stockland-well-known.yml
- group: other
  href: https://artifacts.apis.io/stockland/hosts/stockland-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stockland-hosts.yml
- group: other
  href: https://artifacts.apis.io/stockland/vendors/stockland-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stockland-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.stockland.com.au:443/logistics/news
- group: auth
  href: https://artifacts.apis.io/stockland/security/stockland-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stockland-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stockland/security/stockland-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stockland-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stockland.com.au/
- group: company
  title: ''
  type: About
  url: https://www.stockland.com.au/about-stockland
- group: operate
  title: ''
  type: Support
  url: https://www.stockland.com.au/contact-stockland
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.stockland.com.au/investor-centre
- group: company
  title: ''
  type: Careers
  url: https://www.stockland.com.au/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stockland.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stockland.com.au/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stockland
created: '2026-10-22'
description: Stockland is one of Australia's largest diversified property groups (ASX-listed), describing itself as "Australia's largest community creator". It owns, manages and develops retail town centres, workplace and logistics assets, and residential and land lease communities (including Halcyon), with more than $17.9 billion of real estate assets according to its own About page. It was surfaced via the API Evangelist harvest backlog (australia-apidays-2026); no public developer portal or API documentation was found on stockland.com.au.
image: https://www.stockland.com.au/contentassets/dc8ad9373bcb4f25a11b4cd5ad90c282/stockland-logo-long-update.svg
layout: provider
modified: '2026-10-22'
name: Stockland
nav: Providers
network: true
overview: 'Stockland is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Property Development, Retail, and Logistics.


  Stockland''s developer surface includes support and 16 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 10.5
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
  previous_composite: 12.2
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stockland Domain Security
  slug: stockland-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Stockland Vulnerability Disclosure
  slug: stockland-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stockland
tags:
- Company
- Real Estate
- Property Development
- Retail
- Logistics
- Residential
- Australia
website: https://www.stockland.com.au/
---
