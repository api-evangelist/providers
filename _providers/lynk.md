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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lynk/refs/heads/main/hosts/lynk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lynk-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lynk/refs/heads/main/vendors/lynk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lynk-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lynk/refs/heads/main/security/lynk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lynk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elveo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elveo.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elveo.com/legal/terms
- group: company
  title: ''
  type: News
  url: https://www.elveo.com/news
created: '2026-09-23'
description: Lynk Global, now operating as Elveo, provides direct‑to‑device satellite connectivity, enabling mobile phones, IoT devices and machines to stay connected worldwide without terrestrial infrastructure. The company leverages S‑band spectrum and a network of satellites to deliver reliable, low‑latency service across 60+ countries, supporting enterprises, automotive, consumer and government use cases.
image: https://cdn.sanity.io/images/h8fe13zm/production/e0153aef9b26ddcf69da8993a9f54fb193e4651b-1200x630.jpg
layout: provider
modified: '2026-09-23'
name: Lynk Global
nav: Providers
network: true
overview: 'Lynk Global is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Connectivity, IoT, and Global.


  Lynk Global''s developer surface includes product news and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lynk Domain Security
  slug: lynk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lynk
tags:
- Company
- Satellite
- Connectivity
- IoT
- Global
website: https://www.elveo.com/
---
