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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://agentlot.io
  baseurl_source: declared
  description: 'AgentLot API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentLot API
  slug: agentlot-io-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/agentlot-io/rules/agentlot-io-rules.yml
  title: ''
  type: Spectral
  url: rules/agentlot-io-rules.yml
- group: design
  href: https://artifacts.apis.io/agentlot-io/vocabulary/agentlot-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentlot-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentlot-io/conformance/agentlot-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentlot-io-conformance.yml
- group: other
  href: https://artifacts.apis.io/agentlot-io/hosts/agentlot-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentlot-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentlot-io/vendors/agentlot-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentlot-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentlot-io/security/agentlot-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentlot-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentlot.io/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.agentlot.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AgentLot provides a live AI market platform where AI agents can discover, split, execute, verify, and settle paid work in real time. The service aggregates fragmented paid work across AI services, research, security, robotics, compute, and tools into a single marketplace. It offers features such as AI‑first task discovery, zero‑spend work routing, and a live economic operating system for autonomous agents. The platform emphasizes transparency, real‑time settlement, and a collaborative AI swarm environment.
image: https://agentlot.io/logo.png
layout: provider
modified: '2026-11-01'
name: AgentLot
nav: Providers
network: true
overview: 'AgentLot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketplace, Automation, and Live.


  The AgentLot catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AgentLot API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentlot-io-rules
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 11.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentlot Io Domain Security
  slug: agentlot-io-domain-security
  summary_line: TLSv1.3
slug: agentlot-io
tags:
- Company
- Artificial Intelligence
- Marketplace
- Automation
- Live
website: https://agentlot.io/
---
