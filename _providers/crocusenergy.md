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
  href: https://raw.githubusercontent.com/api-evangelist/crocusenergy/refs/heads/main/hosts/crocusenergy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crocusenergy-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crocusenergy/refs/heads/main/security/crocusenergy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crocusenergy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crocusenergy.com
coverage:
  checked: '2026-10-11'
  detail: No API documentation or developer program is publicly available on the company's website.
  evidence:
  - status: 200
    url: https://crocusenergy.com
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Crocusenergy is an emerging renewable energy company focused on developing solar and wind power projects across the United States. The firm provides clean energy solutions, engages in project financing, and offers operational services for sustainable power generation. Through its innovative technology and strategic partnerships, Crocusenergy aims to accelerate the transition to low‑carbon energy sources while delivering reliable electricity to communities and businesses.
image: https://img1.wsimg.com/isteam/videos/uA41GmyyG8IMaxXdb
layout: provider
modified: '2026-10-11'
name: Crocusenergy
nav: Providers
network: true
overview: Crocusenergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Renewable Energy, Solar, Wind, and Cleantech.
random_paper: 7
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crocusenergy Domain Security
  slug: crocusenergy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crocusenergy
tags:
- Company
- Renewable Energy
- Solar
- Wind
- Cleantech
website: https://crocusenergy.com
---
