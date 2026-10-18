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
api_count: 1
apis:
- description: API documentation for Cloudwise platform
  name: Cloudwise API
  slug: cloudwise-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudwise/refs/heads/main/hosts/cloudwise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudwise-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://cloudwise.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudwise.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cloudwise.ai/news
- group: other
  title: ''
  type: Leadership
  url: https://cloudwise.ai/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://cloudwise.ai/documentation/itam-manual
- group: start
  title: ''
  type: GettingStarted
  url: https://cloudwise.ai/documentation/castrel-setup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudwise/refs/heads/main/security/cloudwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudwise.ai
coverage:
  checked: '2026-10-09'
  detail: Main documentation site renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://cloudwise.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cloudwise provides AI‑driven observability, autonomous incident resolution, and unified IT operations for enterprises. Its platform combines AIOps, ITSM, CMDB, and monitoring to reduce MTTR, improve service reliability, and automate workflows across cloud and on‑prem environments. The company serves over 2,000 enterprises worldwide, focusing on digital transformation, proactive alert triage, and intelligent automation for IT teams.
image: https://cloudwise.ai/og/home.png
layout: provider
modified: '2026-10-09'
name: Cloudwise
nav: Providers
network: true
overview: 'Cloudwise is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Operations, Observability, Incident Management, ITSM, and Enterprise Infrastructure.


  Cloudwise''s developer surface includes support, documentation, getting-started guide, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 60.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudwise Domain Security
  slug: cloudwise-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cloudwise
tags:
- AI Operations
- Observability
- Incident Management
- ITSM
- Enterprise Infrastructure
website: https://cloudwise.ai
---
