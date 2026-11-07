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
  href: https://artifacts.apis.io/santos/well-known/santos-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/santos-security.txt
- group: auth
  href: https://artifacts.apis.io/santos/well-known/santos-santos-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/santos-santos-security.txt
- group: agent
  href: https://artifacts.apis.io/santos/well-known/santos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/santos-well-known.yml
- group: other
  href: https://artifacts.apis.io/santos/hosts/santos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/santos-hosts.yml
- group: other
  href: https://artifacts.apis.io/santos/vendors/santos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/santos-vendors.yml
- group: auth
  href: https://artifacts.apis.io/santos/security/santos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/santos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.santos.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.santos.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.santos.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.santos.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://www.santos.com/careers/
- group: company
  title: ''
  type: Investors
  url: https://www.santos.com/investors/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10716
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SantosLtd
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/santosltd
created: '2026-10-22'
description: 'Santos Ltd is an Australian-headquartered global energy company with oil and gas operations across Australia, Papua New Guinea, Timor-Leste and the United States. Its website describes it as providing reliable, affordable energy for progress while seeking to provide lower carbon energy over time. Santos was surfaced via the API Evangelist harvest backlog (source: australia-apidays-2026); its public site (santos.com) publishes corporate, investor, news and careers information and no public developer portal or API documentation was found.'
image: https://www.santos.com/wp-content/uploads/2023/04/cropped-android-chrome-512x512-1.png
layout: provider
modified: '2026-10-22'
name: Santos
nav: Providers
network: true
overview: 'Santos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Natural Gas, and LNG.


  Santos'' developer surface includes support, YouTube channel, and 13 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
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
  previous_composite: 8.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/santos/santos-2026-11-03T142746.png
security:
- kind: domain-security
  name: Santos Domain Security
  slug: santos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: santos
tags:
- Company
- Energy
- Oil and Gas
- Natural Gas
- LNG
- Australia
website: https://www.santos.com/
---
