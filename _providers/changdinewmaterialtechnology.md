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
  href: https://raw.githubusercontent.com/api-evangelist/changdinewmaterialtechnology/refs/heads/main/hosts/changdinewmaterialtechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changdinewmaterialtechnology-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/changdinewmaterialtechnology/refs/heads/main/security/changdinewmaterialtechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changdinewmaterialtechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cdmaterial.com
- group: operate
  title: ''
  type: Support
  url: https://www.cdmaterial.com/contactus.html
coverage:
  checked: '2026-10-08'
  detail: The site is served via Firebase with JavaScript rendering, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.cdmaterial.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Changdinewmaterialtechnology, also known as Changdi New Material Technology (Shanghai) Co., Ltd., is a Chinese high‑tech enterprise specializing in the research, development, production and sales of optical and electronic nanomaterials. The company offers a range of products such as nano‑ceramic thermal insulation materials, nano‑nickel slurry, BOPET optical films and privacy‑screen films, serving industries like electronics displays, finance, automotive and construction. It positions itself as an innovative “little giant” with strong R&D capabilities and national‑level specialized technology recognition.
layout: provider
modified: '2026-10-08'
name: Changdinewmaterialtechnology
nav: Providers
network: true
overview: 'Changdinewmaterialtechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Changdinewmaterialtechnology''s developer surface includes support and 3 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 35.7
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
  name: Changdinewmaterialtechnology Domain Security
  slug: changdinewmaterialtechnology-domain-security
  summary_line: TLSv1.2
slug: changdinewmaterialtechnology
tags:
- Company
website: https://www.cdmaterial.com
---
