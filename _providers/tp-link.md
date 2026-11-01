---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tp-link/hosts/tp-link-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tp-link-hosts.yml
- group: other
  href: https://artifacts.apis.io/tp-link/vendors/tp-link-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tp-link-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.tp-link.com/us/support/
- group: start
  title: ''
  type: SignUp
  url: https://community.tp-link.com/us/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.tp-link.com/web/official/privacy-policy?region=US
- group: company
  title: ''
  type: Newsroom
  url: https://www.tp-link.com/press/news/
- group: company
  title: ''
  type: Blog
  url: https://www.tp-link.com/us/blog/
- group: auth
  href: https://artifacts.apis.io/tp-link/security/tp-link-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tp-link-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tp-link.com/
created: '2026-10-28'
description: TP-Link (Omada) is a global provider of networking hardware and cloud‑based management solutions. The company offers a range of products including routers, Wi‑Fi access points, switches, and the Omada SD‑WAN and Wi‑Fi management platform for businesses. Its public website (tp‑link.com) presents product information, support resources, and corporate details, but does not expose a dedicated developer portal or public API documentation.
image: https://static.tp-link.com/assets/images/icon/open_graph_logo.png
layout: provider
modified: '2026-10-28'
name: TP-Link (Omada)
nav: Providers
network: true
overview: 'TP-Link (Omada) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Hardware, Cloud, and Business.


  TP-Link (Omada)''s developer surface includes support, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
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
  name: Tp Link Domain Security
  slug: tp-link-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tp-link
tags:
- Company
- Networking
- Hardware
- Cloud
- Business
- IoT
website: https://tp-link.com/
---
