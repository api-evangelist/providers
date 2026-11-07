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
  href: https://artifacts.apis.io/the-lottery-corporation/well-known/the-lottery-corporation-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/the-lottery-corporation-security.txt
- group: agent
  href: https://artifacts.apis.io/the-lottery-corporation/well-known/the-lottery-corporation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/the-lottery-corporation-well-known.yml
- group: other
  href: https://artifacts.apis.io/the-lottery-corporation/hosts/the-lottery-corporation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-lottery-corporation-hosts.yml
- group: other
  href: https://artifacts.apis.io/the-lottery-corporation/vendors/the-lottery-corporation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-lottery-corporation-vendors.yml
- group: auth
  href: https://artifacts.apis.io/the-lottery-corporation/security/the-lottery-corporation-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-lottery-corporation-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/the-lottery-corporation/security/the-lottery-corporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-lottery-corporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thelotterycorporation.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.thelotterycorporation.com/news-and-media/news
- group: operate
  title: ''
  type: Support
  url: https://www.thelotterycorporation.com/contact-us
- group: auth
  title: ''
  type: Security
  url: https://www.thelotterycorporation.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thelotterycorporation.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thelotterycorporation.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.thelotterycorporation.com/work-with-us/tech-careers
- group: company
  title: ''
  type: Investors
  url: https://www.thelotterycorporation.com/investors
created: '2026-10-22'
description: The Lottery Corporation Limited (ASX:TLC) is an Australian lottery and Keno operator, the home of The Lott and Keno brands, running Australia's biggest lottery games in every state and territory except Western Australia and describing itself as one of the world's top-performing lottery businesses, now evolving into a digitally led entertainment company. Its corporate site (thelotterycorporation.com) covers its brands, investors, ESG, careers (including tech careers) and news; no public developer API or documentation is published there.
image: https://www.thelotterycorporation.com/content/dam/projects/tlc/page/TLC_Social-Share-FB_1200x630.png
layout: provider
modified: '2026-10-22'
name: The Lottery Corporation
nav: Providers
network: true
overview: 'The Lottery Corporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lottery, Gaming, Entertainment, and Keno.


  The Lottery Corporation''s developer surface includes support and 13 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 9
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
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 5.3
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
screenshot: https://apis.io/screenshots/the-lottery-corporation/the-lottery-corporation-2026-11-03T144542.png
security:
- kind: domain-security
  name: The Lottery Corporation Domain Security
  slug: the-lottery-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: The Lottery Corporation Vulnerability Disclosure
  slug: the-lottery-corporation-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: the-lottery-corporation
tags:
- Company
- Lottery
- Gaming
- Entertainment
- Keno
- Australia
- ASX Listed
website: https://www.thelotterycorporation.com/
---
