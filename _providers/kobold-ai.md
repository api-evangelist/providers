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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation placeholder; no machine-readable contract discovered.
  name: KoBold AI API
  slug: kobold-ai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/kobold-ai/hosts/kobold-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kobold-ai-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.kobold.ai/category/news/
- group: auth
  href: https://artifacts.apis.io/kobold-ai/security/kobold-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kobold-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kobold.ai
coverage:
  checked: '2026-10-25'
  detail: Docs pages return HTML shells with no machine‑readable spec, despite being publicly accessible.
  evidence:
  - status: 200
    url: https://www.kobold.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: KoBold AI provides accessible artificial intelligence solutions for businesses and non‑experts, offering self‑service AI products, marketing tools, data quality enhancements, and consulting services. The company emphasizes GDPR compliance, high security, and ease of integration without requiring deep technical expertise, aiming to democratize AI across various industries.
image: https://www.kobold.ai/wp-content/uploads/2022/11/logo_wide_orange.png
layout: provider
modified: '2026-10-25'
name: KoBold Metals
nav: Providers
network: true
overview: KoBold Metals is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, SaaS, Marketing, and DataQuality.
random_paper: 18
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kobold Ai Domain Security
  slug: kobold-ai-domain-security
  summary_line: TLSv1.3
slug: kobold-ai
tags:
- Company
- AI
- SaaS
- Marketing
- DataQuality
website: https://kobold.ai
---
