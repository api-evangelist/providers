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
  band: agent-aware
  dimensions:
    agent_card: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentconnectors Dev Agentic Access
  operation_count: 3
  slug: agentconnectors-dev-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Public directory API providing listings of MCP servers.
  name: Agent Connectors API
  slug: agent-connectors-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/agentconnectors-dev/agentic-access/agentconnectors-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentconnectors-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentconnectors-dev/plans/agentconnectors-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentconnectors-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentconnectors-dev/rules/agentconnectors-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentconnectors-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentconnectors-dev/errors/agentconnectors-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentconnectors-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentconnectors-dev/conformance/agentconnectors-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentconnectors-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentconnectors-dev/llms/agentconnectors-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentconnectors-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentconnectors-dev/well-known/agentconnectors-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentconnectors-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentconnectors-dev/hosts/agentconnectors-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentconnectors-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentconnectors-dev/vendors/agentconnectors-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentconnectors-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://agentconnectors.dev/categories/security
- group: company
  title: ''
  type: Newsroom
  url: https://agentconnectors.dev/categories/media
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentconnectors.dev/categories/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentconnectors.dev/changelog
- group: auth
  href: https://artifacts.apis.io/agentconnectors-dev/security/agentconnectors-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentconnectors-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentconnectors.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentconnectors.dev/about
- group: docs
  title: ''
  type: APIReference
  url: https://agentconnectors.dev/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://agentconnectors.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentconnectors.dev/terms
- group: operate
  title: ''
  type: Contact
  url: https://agentconnectors.dev/contact
created: '2026-11-01'
description: Agent Connectors is an independent public directory of Model Context Protocol (MCP) servers and AI agent connectors. It provides a searchable listing of MCP servers, each with source citations, and offers JSON and Markdown representations for agents. The site also runs a free read‑only MCP server for querying listings. It is not a connector platform and does not host or run connectors itself.
image: https://agentconnectors.dev/opengraph-image?b34e10c01bcb3d0f
layout: provider
modified: '2026-11-01'
name: Agent Connectors
nav: Providers
network: true
overview: 'Agent Connectors is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Directory, MCP, Artificial Intelligence, Open Data, and Public.


  The Agent Connectors catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Connectors'' developer surface includes changelog, documentation, API reference, pricing, and 16 more developer resources.'
plans:
- name: Agentconnectors Dev Plans Pricing
  plan_count: 4
  slug: agentconnectors-dev-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Agent Connectors API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agentconnectors-dev-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 38.6
    developer_ergonomics: 13.1
    discoverability: 67.0
    operational_transparency: 13.2
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentconnectors Dev Domain Security
  slug: agentconnectors-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentconnectors-dev
tags:
- Directory
- MCP
- Artificial Intelligence
- Open Data
- Public
website: https://agentconnectors.dev/
---
