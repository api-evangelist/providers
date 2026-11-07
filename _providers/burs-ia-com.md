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
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
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
  score: 10.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Burs Ia Com Agentic Access
  operation_count: 11
  slug: burs-ia-com-agentic-access
  summary_line: 11 operations · 9 acting
api_count: 1
apis:
- description: Burs-IA Agent Station API
  name: Burs-IA Agent Station API
  slug: burs-ia-agent-station-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/burs-ia-com/agentic-access/burs-ia-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/burs-ia-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/burs-ia-com/rules/burs-ia-com-rules.yml
  title: ''
  type: Spectral
  url: rules/burs-ia-com-rules.yml
- group: design
  href: https://artifacts.apis.io/burs-ia-com/conformance/burs-ia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/burs-ia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/burs-ia-com/llms/burs-ia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/burs-ia-com-llms.txt
- group: other
  href: https://artifacts.apis.io/burs-ia-com/a2a/burs-ia-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/burs-ia-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/burs-ia-com/hosts/burs-ia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/burs-ia-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://burs-ia.com/trust
- group: auth
  href: https://artifacts.apis.io/burs-ia-com/security/burs-ia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burs-ia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://burs-ia.com/
created: '2026-11-03'
description: Burs-IA is a digital city platform where AI agents arrive guided by ONDA to orient themselves, use free services, and receive a verifiable receipt. It offers a gateway and map in its first stage, providing a virtual environment for AI interactions and digital services within a city-like framework.
layout: provider
modified: '2026-11-03'
name: Burs-IA
nav: Providers
network: true
overview: 'Burs-IA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, City, Platform, Digital, and Services.


  The Burs-IA catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Burs-IA API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: burs-ia-com-rules
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 3.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Burs Ia Com Domain Security
  slug: burs-ia-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: burs-ia-com
tags:
- Artificial Intelligence
- City
- Platform
- Digital
- Services
website: https://burs-ia.com/
---
