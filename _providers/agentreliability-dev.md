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
  score: 5.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentreliability Dev Agentic Access
  operation_count: 1
  slug: agentreliability-dev-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Read-only API providing access to the Agent Reliability knowledge corpus and metrics.
  name: Agent Reliability API
  slug: agent-reliability-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/agentreliability-dev/agentic-access/agentreliability-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentreliability-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentreliability-dev/rules/agentreliability-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentreliability-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentreliability-dev/vocabulary/agentreliability-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentreliability-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentreliability-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentreliability-dev/conformance/agentreliability-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentreliability-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentreliability-dev/llms/agentreliability-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentreliability-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentreliability-dev/hosts/agentreliability-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentreliability-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentreliability-dev/vendors/agentreliability-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentreliability-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentreliability.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentreliability.dev/privacy
- group: auth
  href: https://artifacts.apis.io/agentreliability-dev/security/agentreliability-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentreliability-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentreliability.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://agentreliability.dev/openapi.json
created: '2026-11-01'
description: Agent Reliability provides testing, benchmarking, and auditing tools for autonomous AI agents. It offers a public knowledge corpus, open data, and APIs for accessing evidence, metrics, and evaluation results, supporting developers to improve agent reliability and transparency.
layout: provider
modified: '2026-11-01'
name: Agent Reliability
nav: Providers
network: true
overview: 'Agent Reliability is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, Reliability, Benchmarking, and Testing.


  The Agent Reliability catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Reliability''s developer surface includes API reference and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Agent Reliability API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agentreliability-dev-rules
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 5.4
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 15.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentreliability Dev Domain Security
  slug: agentreliability-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-llms
  slug: agentreliability-dev-get-llms
slug: agentreliability-dev
tags:
- Artificial Intelligence
- Agents
- Reliability
- Benchmarking
- Testing
website: https://agentreliability.dev/
---
