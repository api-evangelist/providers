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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/wirescan/hosts/wirescan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wirescan-hosts.yml
- group: other
  href: https://artifacts.apis.io/wirescan/vendors/wirescan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wirescan-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.wirescan.no/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.wirescan.no/
- group: company
  title: ''
  type: Blog
  url: https://www.wirescan.no/blog
- group: auth
  href: https://artifacts.apis.io/wirescan/security/wirescan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wirescan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wirescan.no
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.wirescan.no
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Wirescan, founded in 2003 by technologist Paolo Franco Fantoni, provides digital solutions for cable monitoring using its proprietary LIRA® Technology. Based in Norway, the company offers a suite of products and services for infrastructure monitoring, data analytics, and resource management, serving utilities and industrial clients worldwide.
image: http://static1.squarespace.com/static/5f903866e8c9924e679b44a8/t/5fb537c60a166e3f6e833d20/1605711817021/WIRESCAN_wave.png?format=1500w
layout: provider
modified: '2026-10-21'
name: Wirescan
nav: Providers
network: true
overview: 'Wirescan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Infrastructure, DataAnalytics, and Norway.


  Wirescan''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
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
  name: Wirescan Domain Security
  slug: wirescan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wirescan
tags:
- Company
- Monitoring
- Infrastructure
- DataAnalytics
- Norway
website: https://www.wirescan.no
---
