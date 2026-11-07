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
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference not publicly documented; no machine‑readable specification discovered.
  name: Burnes Atelier API
  slug: burnes-atelier-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/burnesatelier-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/burnesatelier-com/llms/burnesatelier-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/burnesatelier-com-llms.txt
- group: other
  href: https://artifacts.apis.io/burnesatelier-com/hosts/burnesatelier-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/burnesatelier-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/burnesatelier-com/vendors/burnesatelier-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/burnesatelier-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/burnesatelier-com/security/burnesatelier-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burnesatelier-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://burnesatelier.com/
coverage:
  checked: '2026-11-03'
  detail: Homepage returns readable HTML but no machine‑readable API documentation was found despite probing common spec locations.
  evidence:
  - status: 200
    url: https://burnesatelier.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Burnes Atelier provides governed implementation, automation, monitoring, evidence, and integration services. Their ΛXÏS platform delivers business outcomes through configurable workflows, risk review packages, AI visibility tools, and product development pilots. The company focuses on governed business execution, offering services such as private pilot builds, automation implementation, buyer‑signal monitoring, and carrier risk reviews, all backed by evidence‑based processes.
layout: provider
modified: '2026-11-03'
name: Burnes Atelier
nav: Providers
network: true
overview: Burnes Atelier is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business, Automation, Integration, Monitoring, and Risk Management.
random_paper: 9
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Burnesatelier Com Domain Security
  slug: burnesatelier-com-domain-security
  summary_line: TLSv1.3
slug: burnesatelier-com
tags:
- Business
- Automation
- Integration
- Monitoring
- Risk Management
website: https://burnesatelier.com/
---
