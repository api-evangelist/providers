---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 4.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentreader Xyz Agentic Access
  operation_count: 1
  slug: agentreader-xyz-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Read URLs and PDFs via REST endpoints
  name: AgentReader API
  slug: agentreader-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/agentreader-xyz/agentic-access/agentreader-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentreader-xyz-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentreader-xyz/plans/agentreader-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentreader-xyz-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentreader-xyz/rules/agentreader-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/agentreader-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/agentreader-xyz/vocabulary/agentreader-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentreader-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentreader-xyz/conformance/agentreader-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentreader-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentreader-xyz/llms/agentreader-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentreader-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentreader-xyz/well-known/agentreader-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentreader-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentreader-xyz/hosts/agentreader-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentreader-xyz-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentreader.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentreader.xyz/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: auth
  href: https://artifacts.apis.io/agentreader-xyz/authentication/agentreader-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentreader-xyz-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agentreader-xyz/security/agentreader-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentreader-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentreader.xyz/
created: '2026-11-01'
description: AgentReader provides a service that reads any URL or PDF and returns clean Markdown or JSON, optimized for developers and AI agents. It offers a REST and MCP interface, supports JavaScript rendering, handles cookie walls, and includes pricing tiers with free daily reads. The platform emphasizes privacy, logging only hostnames, and offers payment via credit cards or USDC on Base.
layout: provider
modified: '2026-11-01'
name: AgentReader
nav: Providers
network: true
overview: 'AgentReader is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Processing, PDF, Markdown, and Agent Tools.


  The AgentReader catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentReader''s developer surface includes pricing, authentication, and 12 more developer resources.'
plans:
- name: Agentreader Xyz Plans Pricing
  plan_count: 3
  slug: agentreader-xyz-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AgentReader API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: agentreader-xyz-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentreader Xyz Authentication
  slug: agentreader-xyz-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agentreader Xyz Domain Security
  slug: agentreader-xyz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentreader-xyz
tags:
- Artificial Intelligence
- Data Processing
- PDF
- Markdown
- Agent Tools
website: https://agentreader.xyz/
---
