---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aiculus/llms/aiculus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiculus-llms.txt
- group: other
  href: https://artifacts.apis.io/aiculus/hosts/aiculus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiculus-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiculus/vendors/aiculus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiculus-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aiculus.co/privacy-policy
- group: auth
  href: https://artifacts.apis.io/aiculus/security/aiculus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiculus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiculus.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://aiculus.co/mcp
  - status: 403
    url: https://www.aiculus.co/mcp
  - status: 200
    url: https://aiculus.co/
  reason: no-developer-program
  state: none
created: '2026-10-19'
description: Aiculus provides AI‑driven API security solutions, helping organisations detect and respond to API threats in real time. Their platform offers visibility, privacy, and comprehensive threat detection across all API traffic, enabling stronger defence‑in‑depth strategies. Services include consulting, advisory, and tailored security implementations for enterprises seeking to secure third‑party API integrations and protect against emerging vulnerabilities.
image: https://static.wixstatic.com/media/74e05b_639ab63a22dc4c308f0e95c3b11dd68b%7Emv2.png/v1/fit/w_2500,h_1330,al_c/74e05b_639ab63a22dc4c308f0e95c3b11dd68b%7Emv2.png
layout: provider
modified: '2026-10-19'
name: Aiculus
nav: Providers
network: true
overview: Aiculus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Security, Artificial Intelligence, Threat Detection, and Consulting.
random_paper: 14
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 6.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aiculus/aiculus-2026-11-03T120501.png
security:
- kind: domain-security
  name: Aiculus Domain Security
  slug: aiculus-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aiculus
tags:
- Company
- API Security
- Artificial Intelligence
- Threat Detection
- Consulting
website: https://aiculus.co/
---
