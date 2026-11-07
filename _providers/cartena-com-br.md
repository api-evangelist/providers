---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cartena-com-br/plans/cartena-com-br-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cartena-com-br-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/cartena-com-br/hosts/cartena-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cartena-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/cartena-com-br/vendors/cartena-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cartena-com-br-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://cartena.com.br/help
- group: commercial
  title: ''
  type: Pricing
  url: https://cartena.com.br/plans
- group: start
  title: ''
  type: Login
  url: https://cartena.com.br/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cartena-tecnologia
- group: auth
  href: https://artifacts.apis.io/cartena-com-br/security/cartena-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cartena-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cartena.com.br/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cartena.com.br/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cartena.com.br/terms
coverage:
  checked: '2026-11-03'
  detail: No public API specification or developer documentation was found on cartena.com.br.
  evidence:
  - status: 404
    url: https://cartena.com.br/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Cartena provides a platform for managing investment portfolios, tracking dividends, and visualizing performance. It offers tools for organizing investments, monitoring earnings, and generating evolution charts, helping users stay on top of their financial assets with comprehensive insights and easy-to-use interfaces.
image: https://cartena.com.br/img/og-default.jpg
layout: provider
modified: '2026-11-03'
name: Cartena
nav: Providers
network: true
overview: 'Cartena is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Investment, Portfolio, Dividends, and Brazil.


  Cartena''s developer surface includes support, pricing, and 9 more developer resources.'
plans:
- name: Cartena Com Br Plans Pricing
  plan_count: 3
  slug: cartena-com-br-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cartena Com Br Domain Security
  slug: cartena-com-br-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cartena-com-br
tags:
- Finance
- Investment
- Portfolio
- Dividends
- Brazil
website: https://cartena.com.br/
---
