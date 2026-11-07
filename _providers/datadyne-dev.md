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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DataDyne's Pulse KPI dashboard, providing access to shop performance data.
  name: Pulse API
  slug: pulse-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/datadyne-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/datadyne-dev/llms/datadyne-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datadyne-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/datadyne-dev/hosts/datadyne-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datadyne-dev-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datadyne.dev/privacy/
- group: auth
  href: https://artifacts.apis.io/datadyne-dev/security/datadyne-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datadyne-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datadyne.dev/
coverage:
  checked: '2026-11-05'
  detail: Documentation site returns HTML shells for OpenAPI URLs, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.datadyne.dev/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: DataDyne provides PULSE, a real‑time KPI dashboard for automotive repair shops. The platform delivers live performance metrics such as profitability, close ratio, labor rates and technician output to owners, managers, service advisors and technicians. PULSE integrates with shop‑management systems like Tekmetric, Shop‑Ware and Google Maps Platform and supports multi‑shop operators.
image: https://www.datadyne.dev/images/og-default.png
layout: provider
modified: '2026-11-04'
name: DataDyne
nav: Providers
network: true
overview: DataDyne is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include automotive repair, KPI dashboard, Shop Management, and Multi-Location.
random_paper: 6
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datadyne Dev Domain Security
  slug: datadyne-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: datadyne-dev
tags:
- automotive repair
- KPI dashboard
- Shop Management
- Multi-Location
website: https://datadyne.dev/
---
