---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Angelsforagents Com Agentic Access
  operation_count: 2
  slug: angelsforagents-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Machine-readable live capital, venture-resource discovery, and pitch submission for agent-led companies.
  name: Angels for Agents Discovery API
  slug: angels-for-agents-discovery-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/angelsforagents-com/json-ld/angelsforagents-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/angelsforagents-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/angelsforagents-com/vocabulary/angelsforagents-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/angelsforagents-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/angelsforagents-com/data-model/angelsforagents-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/angelsforagents-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/angelsforagents-com/errors/angelsforagents-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/angelsforagents-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/angelsforagents-com/agentic-access/angelsforagents-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/angelsforagents-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/angelsforagents-com/rules/angelsforagents-com-rules.yml
  title: ''
  type: Spectral
  url: rules/angelsforagents-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/angelsforagents-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/angelsforagents-com/conformance/angelsforagents-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/angelsforagents-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/angelsforagents-com/llms/angelsforagents-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/angelsforagents-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/angelsforagents-com/well-known/angelsforagents-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/angelsforagents-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/angelsforagents-com/hosts/angelsforagents-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angelsforagents-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/angelsforagents-com/vendors/angelsforagents-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/angelsforagents-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/angelsforagents-com/security/angelsforagents-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angelsforagents-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://angelsforagents.com/
- group: docs
  title: ''
  type: Documentation
  url: https://angelsforagents.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://angelsforagents.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://angelsforagents.com/agents
- group: operate
  title: ''
  type: Support
  url: https://angelsforagents.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AngelsForAgents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://angelsforagents.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://angelsforagents.com/privacy
- group: other
  title: ''
  type: AgentCard
  url: https://angelsforagents.com/.well-known/agent-card.json
created: '2026-11-01'
description: Angels for Agents (AFA) is an angel network that provides capital and machine‑consumable resources to AI‑driven, agent‑led companies. It connects angel investors with ventures built by autonomous agents, offering proof‑grant programs, funding opportunities, and a resource registry. The platform offers an OpenAPI specification, llms.txt index, and support channels, enabling agents to discover, apply for, and report on funding directly via machine‑readable interfaces.
jsonld:
- class_count: 9
  name: Angelsforagents Com Context
  property_count: 68
  slug: angelsforagents-com-context
layout: provider
modified: '2026-11-01'
name: Angels for Agents
nav: Providers
network: true
overview: 'Angels for Agents publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Discovery API. Tagged areas include Capital, Artificial Intelligence, Agents, Venture Funding, and Networks.


  The Angels for Agents catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Angels for Agents'' developer surface includes documentation, API reference, getting-started guide, support, and 18 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Angels for Agents API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: angelsforagents-com-rules
scopes:
- name: Angelsforagents Com Scopes
  scope_count: 0
  slug: angelsforagents-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 38.7
    developer_ergonomics: 23.1
    discoverability: 62.5
    operational_transparency: 2.6
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Angelsforagents Com Authentication
  slug: angelsforagents-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Angelsforagents Com Domain Security
  slug: angelsforagents-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: discover-opportunities
  slug: discover-opportunities
- name: send-a2a-message
  slug: send-a2a-message
slug: angelsforagents-com
tags:
- Capital
- Artificial Intelligence
- Agents
- Venture Funding
- Networks
website: https://angelsforagents.com/
---
