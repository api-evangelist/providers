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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 90
  human_in_the_loop: 13
  name: Calc Engineer Agentic Access
  operation_count: 181
  slug: calc-engineer-agentic-access
  summary_line: 181 operations · 90 acting · 13 human-in-the-loop
api_count: 1
apis:
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The auth API from calc.engineer — 2 operation(s) for auth.
  name: calc.engineer Auth API
  slug: calc-engineer-auth-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The catalog API from calc.engineer — 1 operation(s) for catalog.
  name: calc.engineer Catalog API
  slug: calc-engineer-catalog-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The docs API from calc.engineer — 1 operation(s) for docs.
  name: calc.engineer Docs API
  slug: calc-engineer-docs-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The general API from calc.engineer — 23 operation(s) for general.
  name: calc.engineer General API
  slug: calc-engineer-general-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The homelab API from calc.engineer — 13 operation(s) for homelab.
  name: calc.engineer Homelab API
  slug: calc-engineer-homelab-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The mesh API from calc.engineer — 10 operation(s) for mesh.
  name: calc.engineer Mesh API
  slug: calc-engineer-mesh-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The pcb API from calc.engineer — 14 operation(s) for pcb.
  name: calc.engineer Pcb API
  slug: calc-engineer-pcb-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The power API from calc.engineer — 15 operation(s) for power.
  name: calc.engineer Power API
  slug: calc-engineer-power-api
- baseURL: https://calc.engineer
  baseurl_source: declared
  description: The rf API from calc.engineer — 13 operation(s) for rf.
  name: calc.engineer Rf API
  slug: calc-engineer-rf-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/calc-engineer/agentic-access/calc-engineer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/calc-engineer-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/calc-engineer/rules/calc-engineer-rules.yml
  title: ''
  type: Spectral
  url: rules/calc-engineer-rules.yml
- group: design
  href: https://artifacts.apis.io/calc-engineer/vocabulary/calc-engineer-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calc-engineer-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/calc-engineer/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/calc-engineer/errors/calc-engineer-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/calc-engineer-problem-types.yml
- group: design
  href: https://artifacts.apis.io/calc-engineer/conformance/calc-engineer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calc-engineer-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calc-engineer/llms/calc-engineer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calc-engineer-llms.txt
- group: other
  href: https://artifacts.apis.io/calc-engineer/hosts/calc-engineer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calc-engineer-hosts.yml
- group: other
  href: https://artifacts.apis.io/calc-engineer/vendors/calc-engineer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calc-engineer-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://calc.engineer/api/docs
- group: auth
  href: https://artifacts.apis.io/calc-engineer/security/calc-engineer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calc-engineer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calc.engineer/
created: '2026-11-03'
description: Calc.engineer provides a free in-browser SPICE circuit simulator, PCB autorouter, and 89 engineering calculators covering RF, LoRa, solar, PCB and homelab. It offers an MCP-native REST API for AI agents without signup, aiming to empower engineers with accessible simulation tools.
image: https://calc.engineer/og.jpg
layout: provider
modified: '2026-11-03'
name: calc.engineer
nav: Providers
network: true
overview: 'calc.engineer publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Catalog API, Docs API, and 6 more. Tagged areas include Company, Engineering, Simulation, and Calculator.


  The calc.engineer catalog on APIs.io includes 1 Spectral governance ruleset.


  calc.engineer''s developer surface includes API reference and 11 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: calc.engineer API Rules
  rule_count: 40
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 4
  slug: calc-engineer-rules
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 43.5
    developer_ergonomics: 5.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calc Engineer Domain Security
  slug: calc-engineer-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: calc-engineer-general-logarithm
  slug: calc-engineer-general-logarithm
slug: calc-engineer
tags:
- Company
- Engineering
- Simulation
- Calculator
website: https://calc.engineer/
---
