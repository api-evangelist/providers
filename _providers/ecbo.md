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
    mcp_server: false
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ecbo/vendors/ecbo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecbo-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/ecbo/plans/ecbo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ecbo-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ecbo/llms/ecbo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecbo-llms.txt
- group: auth
  href: https://artifacts.apis.io/ecbo/well-known/ecbo-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ecbo-help-security.txt
- group: agent
  href: https://artifacts.apis.io/ecbo/well-known/ecbo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecbo-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecbo/hosts/ecbo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecbo-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.ecbo.io/ja/
- group: company
  title: ''
  type: Newsroom
  url: https://ecbo.io/news
- group: docs
  title: ''
  type: Documentation
  url: https://help.ecbo.io/
- group: auth
  href: https://artifacts.apis.io/ecbo/security/ecbo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecbo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecbo.io
coverage:
  checked: '2026-10-25'
  detail: The ecbo website provides no developer documentation or API endpoints.
  evidence:
  - status: 200
    url: https://ecbo.io
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Ecbo株式会社 (ecbo Inc.) is a Japanese startup offering shared luggage storage and pickup services through its ecbo cloak platform. It operates a network of urban hubs where users can securely drop off and retrieve items, aiming to redefine ownership and enable flexible, on‑demand access to personal belongings. The company partners with major logistics and retail firms, emphasizing convenience, sustainability, and innovative sharing economy solutions.
image: https://ecbo.io/wp-content/themes/kon/src/img/meta.jpg
layout: provider
modified: '2026-10-24'
name: Ecbo
nav: Providers
network: true
overview: 'Ecbo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Ecbo''s developer surface includes support, documentation, and 9 more developer resources.'
plans:
- name: Ecbo Plans Pricing
  plan_count: 2
  slug: ecbo-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 41.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ecbo Domain Security
  slug: ecbo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ecbo
tags:
- Company
website: https://ecbo.io
---
