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
    agent_card: flavored
    agent_skills: false
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
  score: 7.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agentiscript Com Agentic Access
  operation_count: 4
  slug: agentiscript-com-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: Public API for AgentiScript concepts and data.
  name: AgentiScript Public API
  slug: agentiscript-public-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/agentiscript-com/agentic-access/agentiscript-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentiscript-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentiscript-com/rules/agentiscript-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentiscript-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentiscript-com/errors/agentiscript-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentiscript-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentiscript-com/conformance/agentiscript-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentiscript-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentiscript-com/llms/agentiscript-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentiscript-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentiscript-com/a2a/agentiscript-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentiscript-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/agentiscript-com/hosts/agentiscript-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentiscript-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentiscript-com/vendors/agentiscript-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentiscript-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentiscript.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentiscript.com/legal/privacy/
- group: docs
  title: ''
  type: APIReference
  url: https://agentiscript.com/developers/
- group: auth
  href: https://artifacts.apis.io/agentiscript-com/security/agentiscript-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentiscript-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentiscript.com/
created: '2026-11-01'
description: AgentiScript provides an open visual language for the agentic economy, enabling shared meaning for concepts, ideas, processes, and relationships. It offers tokenization and agentification to give digital form and precise identity to intangible assets, supporting both humans and AI agents to discover, understand, and use them together. The platform is built as a public good, integrating with the XRP Ledger for payments while remaining open and extensible.
layout: provider
modified: '2026-11-01'
name: AgentiScript
nav: Providers
network: true
overview: 'AgentiScript is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source, Visual Language, AgenticEconomy, Tokenization, and Artificial Intelligence.


  The AgentiScript catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentiScript''s developer surface includes API reference and 12 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: AgentiScript API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: agentiscript-com-rules
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 14.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
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
  name: Agentiscript Com Domain Security
  slug: agentiscript-com-domain-security
  summary_line: TLSv1.3
slug: agentiscript-com
tags:
- Open Source
- Visual Language
- AgenticEconomy
- Tokenization
- Artificial Intelligence
website: https://agentiscript.com/
---
