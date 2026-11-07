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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/redox-limited/well-known/redox-limited-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/redox-limited-well-known.yml
- group: other
  href: https://artifacts.apis.io/redox-limited/hosts/redox-limited-hosts.yml
  title: ''
  type: Hosts
  url: hosts/redox-limited-hosts.yml
- group: other
  href: https://artifacts.apis.io/redox-limited/vendors/redox-limited-vendors.yml
  title: ''
  type: Vendors
  url: vendors/redox-limited-vendors.yml
- group: auth
  href: https://artifacts.apis.io/redox-limited/security/redox-limited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redox-limited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redox.com/
- group: company
  title: ''
  type: About
  url: https://redox.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://redox.com/contact/
- group: company
  title: ''
  type: Newsroom
  url: https://redox.com/news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://redox.com/investor-centre/
- group: company
  title: ''
  type: Careers
  url: https://redox.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redox.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redox.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redox/
created: '2026-10-22'
description: Redox (Redox Ltd) is a chemical and ingredients distributor headquartered in Australia, supplying more than 1000 specialty and commodity products to customers in Australia, the USA, the UK, New Zealand, Malaysia and other markets. It serves food and beverage, personal care, human and animal health, crop protection, water treatment, coatings, plastics, mining and other industries. No public developer API, documentation or portal is published on redox.com.
image: https://redox.com/wp-content/themes/redox/img/apple-touch-icon.png
layout: provider
modified: '2026-10-22'
name: Redox
nav: Providers
network: true
overview: Redox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chemicals, Distribution, Ingredients, and Supply Chain.
random_paper: 15
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
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
  previous_composite: 9.9
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
screenshot: https://apis.io/screenshots/redox-limited/redox-limited-2026-11-03T142105.png
security:
- kind: domain-security
  name: Redox Limited Domain Security
  slug: redox-limited-domain-security
  summary_line: TLSv1.3 · DMARC
slug: redox-limited
tags:
- Company
- Chemicals
- Distribution
- Ingredients
- Supply Chain
- Australia
website: https://redox.com/
---
