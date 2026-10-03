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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for Beijing Institute of Technology Genshu Technology
  name: API
  slug: api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beijinginstituteoftechnologygenshutechnology/refs/heads/main/well-known/beijinginstituteoftechnologygenshutechnology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beijinginstituteoftechnologygenshutechnology-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beijinginstituteoftechnologygenshutechnology/refs/heads/main/hosts/beijinginstituteoftechnologygenshutechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beijinginstituteoftechnologygenshutechnology-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://lggs.tech/web/news/index.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beijinginstituteoftechnologygenshutechnology/refs/heads/main/security/beijinginstituteoftechnologygenshutechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beijinginstituteoftechnologygenshutechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lggs.tech/
coverage:
  checked: '2026-09-27'
  detail: The developer portal returns a JavaScript shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://api.lggs.tech/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beijing Institute of Technology Genshu Technology Co., Ltd. (北京理工亘舒科技有限公司) was founded in December 2016. It focuses on the commercialization of aerospace biomedical technology, offering high-end cold chain equipment, space microfluidic medical testing, smart traditional Chinese medicine platforms, space payload services, and STEAM education. Backed by Beijing Institute of Technology and collaborations with aerospace academies, it operates as a specialized high‑tech enterprise.
layout: provider
modified: '2026-09-27'
name: Beijinginstituteoftechnologygenshutechnology
nav: Providers
network: true
overview: Beijinginstituteoftechnologygenshutechnology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Biomedical, Cold Chain, and Education.
random_paper: 8
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beijinginstituteoftechnologygenshutechnology Domain Security
  slug: beijinginstituteoftechnologygenshutechnology-domain-security
  summary_line: TLSv1.2
slug: beijinginstituteoftechnologygenshutechnology
tags:
- Company
- Aerospace
- Biomedical
- Cold Chain
- Education
website: https://lggs.tech/
---
