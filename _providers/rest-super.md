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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/rest-super/hosts/rest-super-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rest-super-hosts.yml
- group: build
  href: https://artifacts.apis.io/rest-super/integrations/rest-super-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/rest-super-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/rest-super/vendors/rest-super-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rest-super-vendors.yml
- group: auth
  href: https://artifacts.apis.io/rest-super/security/rest-super-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rest-super-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rest.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://rest.com.au/employer/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://rest.com.au/super/manage/getting-started
- group: start
  title: ''
  type: Login
  url: https://rest.com.au/employer/login
- group: company
  title: ''
  type: Newsroom
  url: https://rest.com.au/why-rest/about-rest/news
- group: operate
  title: ''
  type: Support
  url: https://rest.com.au/why-rest/about-rest/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rest.com.au/why-rest/about-rest/fund-details/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rest.com.au/why-rest/about-rest/fund-details/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://rest.com.au/super/manage/memberaccess/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rest-super/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/RESTindustrySuper
created: '2026-10-22'
description: Rest Super is the brand of the Retail Employees Superannuation Trust (Rest), an Australian profit-to-member superannuation fund serving around 2 million members, with Retail Employees Superannuation Pty Limited (ABN 39 001 987 739, AFSL 240003) as trustee. It offers Rest Super, Rest Corporate and Rest Pension products, retirement and advice services, and the Rest Pay employer contribution platform with published user guides. Its public web presence (rest.com.au) has no published developer API or portal; it was surfaced via the API Evangelist harvest backlog (australia-apidays-2026).
image: https://rest.com.au/getmedia/b5815433-e6b8-4557-be3d-06a4a29d0e64/rest-reps-man-woman-2-mb.jpg?width=860&height=488&ext=.jpg
layout: provider
modified: '2026-10-22'
name: Rest Super
nav: Providers
network: true
overview: 'Rest Super is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Superannuation, Financial Services, Retirement, and Pensions.


  Rest Super''s developer surface includes documentation, getting-started guide, support, YouTube channel, and 11 more developer resources.'
plans:
- name: Rest Super Plans Pricing
  plan_count: 0
  slug: rest-super-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Rest Super Rate Limits
  slug: rest-super-rate-limits
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
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
  previous_composite: 18.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rest Super Domain Security
  slug: rest-super-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rest-super
tags:
- Company
- Superannuation
- Financial Services
- Retirement
- Pensions
- Australia
- Investment
website: https://rest.com.au/
---
