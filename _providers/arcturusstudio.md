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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcturusstudio/refs/heads/main/hosts/arcturusstudio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcturusstudio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcturusstudio/refs/heads/main/vendors/arcturusstudio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcturusstudio-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.arcturus.studio/PrivacyPolicyStatements.html
- group: company
  title: ''
  type: Newsroom
  url: https://arcturus.studio/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcturusstudio/refs/heads/main/security/arcturusstudio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcturusstudio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcturus.studio
coverage:
  checked: 2026-09-25
  detail: No developer program or API documentation was found for arcturusstudio.
  evidence:
  - status: 0
    url: https://api.arcturus.studio/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Arcturusstudio, operating as Arcturus Studio, delivers real‑time 3D volumetric video of sports events using computer vision and AI. Their platform enables broadcasters, teams, leagues, and venues to provide immersive, interactive experiences across 2D broadcast, social media, and AR/VR devices. The company also offers data products derived from player and game analytics, supporting coaches and analysts with actionable insights.
layout: provider
modified: '2026-09-25'
name: Arcturusstudio
nav: Providers
network: true
overview: Arcturusstudio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, 3DVideo, Artificial Intelligence, and Broadcasting.
random_paper: 13
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arcturusstudio Domain Security
  slug: arcturusstudio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arcturusstudio
tags:
- Company
- Sports
- 3DVideo
- Artificial Intelligence
- Broadcasting
- Data Analytics
website: https://arcturus.studio
---
