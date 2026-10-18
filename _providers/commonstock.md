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
  href: https://raw.githubusercontent.com/api-evangelist/commonstock/refs/heads/main/hosts/commonstock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commonstock-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commonstock/refs/heads/main/security/commonstock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commonstock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://share.commonstock.com/
coverage:
  checked: '2026-10-09'
  detail: The share.commonstock.com site serves only HTML shells and requires rendering to access any API information.
  evidence:
  - status: 200
    url: https://share.commonstock.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: CommonStock is a social investing platform acquired by Yahoo! in 2023. It enables users to share insights, track portfolios, and discuss stock ideas within a community. Founded in 2017 and based in San Francisco, the service integrates with brokerage accounts to provide real‑time performance data. The platform offers a web app and mobile apps for iOS and Android, focusing on collaborative investment research and education.
layout: provider
modified: '2026-10-09'
name: CommonStock
nav: Providers
network: true
overview: CommonStock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 9
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Commonstock Domain Security
  slug: commonstock-domain-security
  summary_line: TLSv1.3
slug: commonstock
tags:
- Company
website: https://share.commonstock.com/
---
