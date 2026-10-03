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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ariacv/refs/heads/main/hosts/ariacv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ariacv-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ariacv/refs/heads/main/vendors/ariacv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ariacv-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://broadviewventures.org/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://broadviewventures.org/news/
- group: other
  title: ''
  type: Leadership
  url: https://broadviewventures.org/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ariacv/refs/heads/main/security/ariacv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ariacv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://broadviewventures.org/portfolio/aria-cv/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on the API host.
  evidence:
  - status: 0
    url: https://api.broadviewventures.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aria CV, Inc. is developing a medical device to treat pulmonary hypertension, a life‑threatening disease with limited therapeutic options. The company aims to provide a less invasive, cost‑effective solution compared to expensive drug therapies, addressing a significant unmet medical need.
image: https://broadviewventures.org/wp-content/uploads/2021/01/ariacv.jpg
layout: provider
modified: '2026-09-26'
name: Ariacv
nav: Providers
network: true
overview: Ariacv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Pulmonary Hypertension, Healthcare, and Biotechnology.
random_paper: 14
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ariacv Domain Security
  slug: ariacv-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ariacv
tags:
- Company
- Medical Devices
- Pulmonary Hypertension
- Healthcare
- Biotechnology
website: https://broadviewventures.org/portfolio/aria-cv/
---
