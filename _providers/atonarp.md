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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atonarp/refs/heads/main/llms/atonarp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atonarp-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atonarp/refs/heads/main/hosts/atonarp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atonarp-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atonarp/refs/heads/main/vendors/atonarp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atonarp-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://atonarp.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atonarp/refs/heads/main/security/atonarp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atonarp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atonarp.com/
- group: company
  title: ''
  type: About
  url: https://atonarp.com/about/
- group: other
  title: ''
  type: Products
  url: https://atonarp.com/products/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atonarp.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://atonarp.com/contact/
coverage:
  checked: 2026-09-26
  detail: API host https://api.atonarp.com returned no usable OpenAPI or GraphQL spec despite probing common endpoints.
  evidence:
  - status: error
    url: https://api.atonarp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atonarp Inc. develops advanced digital molecular profiling technologies for semiconductor manufacturing, industrial process control, pharmaceutical production, and EV battery fabrication. Their in‑situ, high‑speed, high‑sensitivity mass spectrometry platforms enable real‑time monitoring and decision‑making, improving efficiency, reducing waste, and lowering costs across multiple industries.
layout: provider
modified: '2026-09-26'
name: Atonarp
nav: Providers
network: true
overview: Atonarp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Molecular Profiling, Industrial Automation, and Pharmaceuticals.
random_paper: 9
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 6
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
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atonarp Domain Security
  slug: atonarp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atonarp
tags:
- Company
- Semiconductors
- Molecular Profiling
- Industrial Automation
- Pharmaceuticals
website: https://atonarp.com/
---
