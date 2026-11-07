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
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/endeavour-group/security/endeavour-group-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/endeavour-group-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/endeavour-group/hosts/endeavour-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/endeavour-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/endeavour-group/vendors/endeavour-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/endeavour-group-vendors.yml
- group: auth
  href: https://artifacts.apis.io/endeavour-group/security/endeavour-group-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/endeavour-group-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/endeavour-group/security/endeavour-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endeavour-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.endeavourgroup.com.au/
- group: company
  title: ''
  type: About
  url: https://www.endeavourgroup.com.au/about
- group: company
  title: ''
  type: Newsroom
  url: https://www.endeavourgroup.com.au/news-and-media
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.endeavourgroup.com.au/investor-relations
- group: company
  title: ''
  type: Careers
  url: https://www.endeavourgroup.com.au/careers
- group: operate
  title: ''
  type: Support
  url: https://www.endeavourgroup.com.au/contact
- group: other
  title: ''
  type: Sustainability
  url: https://www.endeavourgroup.com.au/sustainability
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.endeavourpartnerportal.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.endeavourgroup.com.au/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.endeavourgroup.com.au/privacy-at-endeavour-group/privacy-policy
created: '2026-10-21'
description: Endeavour Group is an Australian drinks retailer and hospitality company headquartered in Australia and listed on the ASX. It operates the Dan Murphy's and BWS retail drinks networks and ALH Group's 350+ licensed hotels (pubs), along with Pinnacle Drinks, Langtons, MixIn, endeavourX and the DELIVERY by endeavour and FULFILLED by endeavour services, and runs the Endeavour Partner Portal (supplier dashboard) for its retail suppliers. No public developer API, API documentation or developer portal was found on its site (endeavourgroup.com.au, checked 2026-10-21). Surfaced via the API Evangelist harvest backlog (australia-apidays-2026).
image: https://cdn.prod.website-files.com/69411b50da307126bedceb2b/698301d9474b08287d009fa3_Endeavour%20Group.jpg
layout: provider
modified: '2026-10-21'
name: Endeavour Group
nav: Providers
network: true
overview: 'Endeavour Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Drinks, Liquor, and Hospitality.


  Endeavour Group''s developer surface includes support and 14 more developer resources.'
plans:
- name: Endeavour Group Plans Pricing
  plan_count: 0
  slug: endeavour-group-plans-pricing
random_paper: 11
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 11
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
screenshot: https://apis.io/screenshots/endeavour-group/endeavour-group-2026-11-03T131510.png
security:
- kind: domain-security
  name: Endeavour Group Domain Security
  slug: endeavour-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Endeavour Group Vulnerability Disclosure
  slug: endeavour-group-vulnerability-disclosure
  summary_line: no policy recorded
slug: endeavour-group
tags:
- Company
- Retail
- Drinks
- Liquor
- Hospitality
- Hotels
- Australia
- ASX Listed
website: https://www.endeavourgroup.com.au/
---
