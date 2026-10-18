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
  href: https://raw.githubusercontent.com/api-evangelist/circuity/refs/heads/main/llms/circuity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/circuity-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circuity/refs/heads/main/hosts/circuity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circuity-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/circuity/refs/heads/main/security/circuity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circuity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://circuity.com
coverage:
  checked: '2026-10-08'
  detail: The company's website returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://circuity.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Circuity is a private‑market technology platform that enables the buying, selling, and management of pre‑IPO company shares. It offers liquidity solutions, settlement services, and equity administration tools for investors, employees, and private companies. The platform integrates with secondary‑market venues and provides a mobile app for real‑time trading and portfolio management, aiming to democratize access to private‑company equity.
layout: provider
modified: '2026-10-08'
name: Circuity
nav: Providers
network: true
overview: Circuity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Private-Market, Equity, Liquidity, and Fintech.
random_paper: 18
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
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
  name: Circuity Domain Security
  slug: circuity-domain-security
  summary_line: TLSv1.3
slug: circuity
tags:
- Company
- Private-Market
- Equity
- Liquidity
- Fintech
website: https://circuity.com
---
