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
api_count: 1
apis:
- description: AI‑driven analytics API for querying data warehouses
  name: Bicycle API
  slug: bicycle-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bicycle/llms/bicycle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bicycle-llms.txt
- group: other
  href: https://artifacts.apis.io/bicycle/hosts/bicycle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bicycle-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://bicycle.ai:443/newsroom
- group: auth
  href: https://artifacts.apis.io/bicycle/security/bicycle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bicycle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bicycle.io
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's documented hosts.
  evidence:
  - status: 0
    url: https://api.bicycle.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Bicycle provides AI‑driven analytics agents that enable revenue‑critical teams to query, detect, explain, and act on data directly within their data warehouses such as Snowflake and BigQuery. The platform offers a natural‑language interface, ontology‑based signal patterns, and actionable insights across retail, travel, and Shopify use‑cases, helping businesses replace static dashboards with interactive AI assistants.
image: https://bicycle.ai/shared/og-card.png
layout: provider
modified: '2026-10-29'
name: Bicycle
nav: Providers
network: true
overview: Bicycle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Data Warehouse, Retail, and Travel.
random_paper: 11
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bicycle/bicycle-2026-11-03T121712.png
security:
- kind: domain-security
  name: Bicycle Domain Security
  slug: bicycle-domain-security
  summary_line: TLSv1.2
slug: bicycle
tags:
- Artificial Intelligence
- Analytics
- Data Warehouse
- Retail
- Travel
- Shopify
website: https://bicycle.io
---
