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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudeats/refs/heads/main/llms/cloudeats-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudeats-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudeats/refs/heads/main/hosts/cloudeats-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudeats-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudeats/refs/heads/main/vendors/cloudeats-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudeats-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cloudeats.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.cloudeats.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudeats/refs/heads/main/security/cloudeats-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudeats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudeats.com
coverage:
  checked: '2026-10-09'
  detail: The provider's website is a Wix‑generated JavaScript‑rendered site with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.cloudeats.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: CloudEats is a pioneer cloud restaurant company creating next‑generation digital brands and proprietary cloud kitchen technology. Based in Manila, it operates cloud kitchens across Southeast Asia, building persona‑driven online‑optimized brands and offering API integration with leading food delivery platforms for real‑time menu control and high conversion rates.
image: https://static.wixstatic.com/media/c23c75_25326d8211a34793a75486cf7cc52a9a%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/c23c75_25326d8211a34793a75486cf7cc52a9a%7Emv2.jpg
layout: provider
modified: '2026-10-09'
name: Cloudeats
nav: Providers
network: true
overview: 'Cloudeats is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Kitchen, Southeast Asia, API Integration, and Food Delivery.


  Cloudeats'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 4.8
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
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudeats Domain Security
  slug: cloudeats-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloudeats
tags:
- Company
- Cloud Kitchen
- Southeast Asia
- API Integration
- Food Delivery
- Startups
website: https://www.cloudeats.com
---
