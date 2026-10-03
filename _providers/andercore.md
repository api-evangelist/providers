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
api_count: 1
apis:
- description: API for Andercore's industrial trade platform
  name: Andercore API
  slug: andercore-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/andercore/refs/heads/main/llms/andercore-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/andercore-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andercore/refs/heads/main/hosts/andercore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andercore-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andercore/refs/heads/main/vendors/andercore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andercore-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.andercore.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.andercore.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.andercore.com/press/andercore-secures-40m-series-b-for-ai-driven-industrial-trade-platform
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/andercore/refs/heads/main/security/andercore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andercore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.andercore.com
coverage:
  checked: 2026-09-24
  detail: API endpoints require authentication, returning 401 for OpenAPI discovery attempts.
  evidence:
  - status: 401
    url: https://api.andercore.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-24'
description: Andercore is a Europe‑based AI‑native supplier of industrial materials, operating a platform that unifies supply, demand, and capital for global industrial trade. The company offers real‑time inventory access, dynamic pricing, managed logistics, and embedded financing, aiming to replace fragmented manual processes with speed, transparency, and reliability across multiple languages and regions.
image: https://cdn.prod.website-files.com/6953b66cfe49c7eee28420b2/6a99516a12b43d612c5bbfae_opengraph_english.png
layout: provider
modified: '2026-09-24'
name: Andercore
nav: Providers
network: true
overview: Andercore publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Industrial Trade, Supply Chain, Fintech, and Europe.
random_paper: 1
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Andercore Domain Security
  slug: andercore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andercore
tags:
- Artificial Intelligence
- Industrial Trade
- Supply Chain
- Fintech
- Europe
website: https://www.andercore.com
---
