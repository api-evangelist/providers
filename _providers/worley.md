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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/worley/llms/worley-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/worley-llms.txt
- group: agent
  href: https://artifacts.apis.io/worley/well-known/worley-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/worley-well-known.yml
- group: other
  href: https://artifacts.apis.io/worley/hosts/worley-hosts.yml
  title: ''
  type: Hosts
  url: hosts/worley-hosts.yml
- group: other
  href: https://artifacts.apis.io/worley/vendors/worley-vendors.yml
  title: ''
  type: Vendors
  url: vendors/worley-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.worley.com/support
- group: auth
  href: https://artifacts.apis.io/worley/security/worley-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/worley-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://worley.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.worley.com/en/insights/our-news
- group: company
  title: ''
  type: Blog
  url: https://www.worley.com/en/insights/our-thinking
- group: company
  title: ''
  type: AboutUs
  url: https://www.worley.com/en/about-us
- group: other
  title: ''
  type: Leadership
  url: https://www.worley.com/en/about-us/our-people/leadership
- group: operate
  title: ''
  type: Contact
  url: https://www.worley.com/en/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.worley.com/en/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.worley.com/en/investor-relations
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.worley.com/en/site-services/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/worley/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Worley_ECR
created: '2026-10-22'
description: Worley is an ASX-listed global professional services company that describes itself as an accountable partner for EPCM (engineering, procurement and construction management) and project delivery, supporting energy, chemicals and resources customers from concept to operational readiness. Its site says it is more than 40,000 energy, chemicals and resources experts in over 40 countries, offering full project delivery, Worley Consulting, and specialist technology businesses such as Worley Chemetics and Worley Comprimo. Surfaced via the australia-apidays-2026 harvest; no public developer portal or API documentation was found on worley.com.
image: https://www.worley.com/-/media/images/worley/logos/worley_logo_pos_brandmark.png
layout: provider
modified: '2026-10-22'
name: Worley
nav: Providers
network: true
overview: 'Worley is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Engineering, Energy, Chemicals, and Resources.


  Worley''s developer surface includes support, engineering blog, and 15 more developer resources.'
plans:
- name: Worley Plans Pricing
  plan_count: 0
  slug: worley-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Worley Rate Limits
  slug: worley-rate-limits
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
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
  previous_composite: 9.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/worley/worley-2026-11-03T150245.png
security:
- kind: domain-security
  name: Worley Domain Security
  slug: worley-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: worley
tags:
- Company
- Engineering
- Energy
- Chemicals
- Resources
- Construction
- Consulting
- Professional Services
- Australia
website: https://worley.com/
---
