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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is behind a login portal requiring authentication.
  name: Alfa Laval API
  slug: alfa-laval-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/alfalaval/hosts/alfalaval-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alfalaval-hosts.yml
- group: other
  href: https://artifacts.apis.io/alfalaval/vendors/alfalaval-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alfalaval-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.alfalaval.com/media/newsandstories/?category=news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.alfalaval.com/Util/login.aspx?ReturnUrl=%2f
- group: docs
  title: ''
  type: Documentation
  url: https://dev.alfalaval.com/
- group: auth
  href: https://artifacts.apis.io/alfalaval/security/alfalaval-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alfalaval-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alfalaval.com
- group: company
  title: ''
  type: Blog
  url: https://www.alfalaval.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.alfalaval.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alfalaval.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alfalaval.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlfaLaval
coverage:
  checked: '2026-11-01'
  detail: Developer portal requires login, blocking access to API documentation.
  evidence:
  - status: 200
    url: https://dev.alfalaval.com/Util/login.aspx?ReturnUrl=%2f
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Alfa Laval is a leading global provider of heat transfer, separation and fluid handling solutions, serving the Energy, Food, Water and Marine industries. Founded in 1878, the company pioneers sustainable technologies that improve efficiency and reduce waste across a wide range of applications, from power generation to dairy processing and maritime transport.
image: https://www.alfalaval.com/ui/css/img/logo-alfalaval.svg
layout: provider
modified: '2026-11-01'
name: Alfa Laval
nav: Providers
network: true
overview: 'Alfa Laval is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Heat Transfer, Separation, Fluid Handling, Energy, and Food.


  Alfa Laval''s developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alfalaval Domain Security
  slug: alfalaval-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: alfalaval
tags:
- Heat Transfer
- Separation
- Fluid Handling
- Energy
- Food
- Water
- Marine
website: https://www.alfalaval.com
---
