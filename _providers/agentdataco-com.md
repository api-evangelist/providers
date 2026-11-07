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
  band: agent-aware
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
    error_semantics: documented
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
  score: 10.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentdataco Com Agentic Access
  operation_count: 1
  slug: agentdataco-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Structured daily JSON feeds on the AI ecosystem.
  name: Agent Data Co API
  slug: agent-data-co-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/agentdataco-com/agentic-access/agentdataco-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentdataco-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentdataco-com/plans/agentdataco-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentdataco-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentdataco-com/rules/agentdataco-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdataco-com-rules.yml
- group: auth
  href: https://artifacts.apis.io/agentdataco-com/authentication/agentdataco-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentdataco-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentdataco-com/errors/agentdataco-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdataco-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentdataco-com/conformance/agentdataco-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdataco-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentdataco-com/llms/agentdataco-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdataco-com-llms.txt
- group: build
  href: https://artifacts.apis.io/agentdataco-com/mcp/agentdataco-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentdataco-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentdataco-com/mcp/agentdataco-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdataco-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentdataco-com/well-known/agentdataco-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdataco-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentdataco-com/hosts/agentdataco-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdataco-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentdataco-com/vendors/agentdataco-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentdataco-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://agentdataco.com/mcp/com.goodmorningmaldives/newsroom
- group: auth
  href: https://artifacts.apis.io/agentdataco-com/security/agentdataco-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdataco-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdataco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentdataco.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://agentdataco.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentdataco.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentdataco.com/privacy
created: '2026-10-31'
description: Agent Data Co provides AI ecosystem data feeds for agents and analysts, offering structured JSON from public APIs covering AI agents, MCP servers, launches, pricing changes, and app reviews. Their services include live data feeds, pricing monitoring, and trend analysis, available via REST and MCP endpoints, with free and paid tiers.
image: https://agentdataco.com/og.svg
layout: provider
mcp_servers:
- description: Remote MCP server at agentdataco.com requiring an API key.
  name: Agent Data Co MCP Server
  slug: agentdataco-com-mcp-yml
modified: '2026-10-31'
name: Agent Data Co
nav: Providers
network: true
overview: 'Agent Data Co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data, Feed, Analytics, and Software-as-a-Service.


  The Agent Data Co catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Data Co''s developer surface includes authentication, documentation, pricing, and 16 more developer resources.'
plans:
- name: Agentdataco Com Plans Pricing
  plan_count: 4
  slug: agentdataco-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Agent Data Co API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agentdataco-com-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 47.4
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.8
    operational_transparency: 10.5
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
  name: Agentdataco Com Authentication
  slug: agentdataco-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentdataco Com Domain Security
  slug: agentdataco-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentdataco-com
tags:
- Artificial Intelligence
- Data
- Feed
- Analytics
- Software-as-a-Service
- Company
website: https://agentdataco.com/
---
