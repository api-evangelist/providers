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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voxox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voxox.com/
coverage:
  checked: '2026-09-04'
  detail: voxox.com served a real Voxox site through 2025-11-16 and has since been a GoDaddy parking lander — a 114-byte JavaScript redirect to /lander whose catch-all answers HTTP 200 for every path including /openapi.json and all of /.well-known/ — with no MX record and with every developer, docs, api, assist, support, my, app and portal subdomain gone from DNS.
  evidence:
  - status: 200
    url: https://voxox.com/
  - status: 200
    url: https://voxox.com/lander
  - status: 200
    url: https://voxox.com/sitemap.xml
  - status: 200
    url: https://voxox.com/.well-known/security.txt
  - status: 200
    url: https://voxox.com/openapi.json
  reason: defunct
  state: none
created: '2026-09-04'
description: 'Voxox is the trade name of Telcentris, Inc., a San Diego, California cloud communications provider founded in 2006 by Bryan, Kevin and Robert Hertz. It sold hosted business phone service (Voxox Cloud Phone), wholesale SIP voice termination and A2P/wholesale SMS messaging, the latter offered to carriers and resellers over an HTTP API and SMPP. The developer surface was never published openly: the wholesale SMS API reference was issued privately by an account manager rather than posted as a public reference or machine-readable specification. As of December 2025 voxox.com resolves to a registrar parking page, the domain carries no MX record, and every developer, docs, support and application subdomain the company operated has stopped resolving.'
layout: provider
modified: '2026-09-04'
name: Voxox
nav: Providers
network: true
overview: Voxox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Communications, Cloud Communications, and VoIP.
random_paper: 13
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Voxox Domain Security
  slug: voxox-domain-security
  summary_line: TLSv1.3
slug: voxox
tags:
- Company
- Telecommunications
- Communications
- Cloud Communications
- VoIP
- SMS
- Messaging
- CPaaS
website: https://voxox.com/
---
