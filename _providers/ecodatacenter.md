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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ecodatacenter/refs/heads/main/hosts/ecodatacenter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecodatacenter-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ecodatacenter/refs/heads/main/vendors/ecodatacenter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecodatacenter-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://ecodatacenter.tech/about-ecodatacenter/management
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ecodatacenter/refs/heads/main/security/ecodatacenter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecodatacenter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecodatacenter.tech/
- group: start
  title: ''
  type: GettingStarted
  url: https://ecodatacenter.tech/taking-you-to-net-zero
- group: operate
  title: ''
  type: Support
  url: https://ecodatacenter.tech/contact
- group: company
  title: ''
  type: Blog
  url: https://ecodatacenter.tech/insights
- group: company
  title: ''
  type: Press
  url: https://ecodatacenter.tech/press
coverage:
  checked: '2026-10-15'
  detail: API documentation pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 404
    url: https://ecodatacenter.tech/redoc
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: EcoDataCenter is a European leader in sustainable compute infrastructure, operating high‑performance data centers across Sweden. Founded in Sweden, the company combines world‑class engineering with minimal climate impact, offering services that enable customers to achieve net‑zero goals while scaling seamlessly. EcoDataCenter focuses on efficiency, renewable energy use, and transparent sustainability reporting, positioning itself as a pioneer in green data center solutions for the European market.
layout: provider
modified: '2026-10-15'
name: EcoDataCenter
nav: Providers
network: true
overview: 'EcoDataCenter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DataCenter, Sustainability, Cloud, and Europe.


  EcoDataCenter''s developer surface includes getting-started guide, support, engineering blog, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
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
  name: Ecodatacenter Domain Security
  slug: ecodatacenter-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ecodatacenter
tags:
- Company
- DataCenter
- Sustainability
- Cloud
- Europe
website: https://ecodatacenter.tech/
---
