---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/causes/hosts/causes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/causes-hosts.yml
- group: other
  href: https://artifacts.apis.io/causes/vendors/causes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/causes-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.causes.com/feed/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.causes.com/privacypolicy
- group: company
  title: ''
  type: Newsroom
  url: https://www.causes.com/feed/news
- group: start
  title: ''
  type: Login
  url: https://www.causes.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.causes.com/feed/blog
- group: auth
  href: https://artifacts.apis.io/causes/security/causes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/causes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.causes.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.causes.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Causes is a technology-driven nonprofit platform that connects donors, volunteers, and organizations to create positive social impact. By aggregating data on charitable initiatives, Causes enables transparent giving, real-time tracking of contributions, and collaborative project management. The platform offers APIs for accessing cause listings, donation processing, volunteer coordination, and impact analytics, empowering developers to build applications that foster community engagement and measurable outcomes across a wide range of social sectors.
layout: provider
modified: '2026-10-22'
name: Causes
nav: Providers
network: true
overview: 'Causes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Nonprofit, API, Donations, Volunteers, and Impact.


  Causes'' developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Causes Domain Security
  slug: causes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: causes
tags:
- Nonprofit
- API
- Donations
- Volunteers
- Impact
website: https://www.causes.com/
---
