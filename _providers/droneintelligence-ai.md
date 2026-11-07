---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
- description: API for Drone Intelligence data and services
  name: Drone Intelligence API
  slug: drone-intelligence-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/droneintelligence-ai/plans/droneintelligence-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/droneintelligence-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/droneintelligence-ai/llms/droneintelligence-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/droneintelligence-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/droneintelligence-ai/hosts/droneintelligence-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/droneintelligence-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/droneintelligence-ai/vendors/droneintelligence-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/droneintelligence-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://droneintelligence.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://droneintelligence.ai/privacy
- group: auth
  href: https://artifacts.apis.io/droneintelligence-ai/security/droneintelligence-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/droneintelligence-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://droneintelligence.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://droneintelligence.ai/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://droneintelligence.ai/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://droneintelligence.ai/pricing
- group: company
  title: ''
  type: About
  url: https://droneintelligence.ai/about
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found despite MCP endpoint being public.
  evidence:
  - status: 0
    url: https://api.droneintelligence.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Drone Intelligence provides independent research and intelligence on the global drone and autonomous systems market. It publishes briefings, reports, market maps, and data-driven analyses covering defence procurement, commercial logistics, aviation regulation, and emerging technologies. The service aims to deliver source‑traced, commercially relevant insights for investors, strategists, and industry stakeholders.
image: https://droneintelligence.ai/api/og?title=Intelligence+for+the+drone+economy.&category=INDEPENDENT+RESEARCH
layout: provider
modified: '2026-11-06'
name: Drone Intelligence
nav: Providers
network: true
overview: 'Drone Intelligence is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drone, Intelligence, Research, and Markets.


  Drone Intelligence''s developer surface includes documentation, pricing, and 10 more developer resources.'
plans:
- name: Droneintelligence Ai Plans Pricing
  plan_count: 3
  slug: droneintelligence-ai-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Droneintelligence Ai Domain Security
  slug: droneintelligence-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: droneintelligence-ai
tags:
- Company
- Drone
- Intelligence
- Research
- Markets
- Analytics
website: https://droneintelligence.ai/
---
