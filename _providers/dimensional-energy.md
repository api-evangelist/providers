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
- group: agent
  href: https://artifacts.apis.io/dimensional-energy/llms/dimensional-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dimensional-energy-llms.txt
- group: other
  href: https://artifacts.apis.io/dimensional-energy/hosts/dimensional-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dimensional-energy-hosts.yml
- group: other
  href: https://artifacts.apis.io/dimensional-energy/vendors/dimensional-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dimensional-energy-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dimensional-energy/security/dimensional-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dimensional-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dimensionalenergy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.dimensionalenergy.com/blog
- group: company
  title: ''
  type: About
  url: https://www.dimensionalenergy.com/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.dimensionalenergy.com/contact-us
- group: company
  title: ''
  type: News
  url: https://www.dimensionalenergy.com/news
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.dimensionalenergy.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Dimensional Energy develops catalyst technologies for cleaner syngas and syncrude production, offering licensing and integration services. The company focuses on high‑value product offtake, partnering and investing in bankable projects, and provides news, blog updates, and contact resources through its website.
image: https://cdn.prod.website-files.com/68fb720b661dd4869c0f1073/69d8f1baa32921fd463841bd_DEOpenGraph.jpg
layout: provider
modified: '2026-10-23'
name: Dimensional Energy
nav: Providers
network: true
overview: 'Dimensional Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Cleantech, Catalysts, and Licensing.


  Dimensional Energy''s developer surface includes engineering blog, product news, and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dimensional Energy Domain Security
  slug: dimensional-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dimensional-energy
tags:
- Company
- Energy
- Cleantech
- Catalysts
- Licensing
- Investment
website: https://www.dimensionalenergy.com/
---
