---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Autonet Work Agentic Access
  operation_count: 5
  slug: autonet-work-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: Network intelligence API with Community (1,000 req/mo) and Architect (50,000 req/mo) tiers. Authenticate with X-Autonet-Token.
  name: Autonet Network Probe API
  slug: autonet-network-probe-api
- baseURL: https://autonet.work
  baseurl_source: declared
  description: The Utils API from Autonet — 2 operation(s) for utils.
  name: Autonet Utils API
  slug: autonet-work-utils-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/autonet-work/agentic-access/autonet-work-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/autonet-work-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/autonet-work/rate-limits/autonet-work-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/autonet-work-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/autonet-work/plans/autonet-work-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autonet-work-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/autonet-work/rules/autonet-work-rules.yml
  title: ''
  type: Spectral
  url: rules/autonet-work-rules.yml
- group: agent
  href: https://artifacts.apis.io/autonet-work/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/autonet-work/conventions/autonet-work-conventions.yml
  title: ''
  type: Conventions
  url: conventions/autonet-work-conventions.yml
- group: start
  href: https://artifacts.apis.io/autonet-work/sandbox/autonet-work-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/autonet-work-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/autonet-work/authentication/autonet-work-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autonet-work-authentication.yml
- group: design
  href: https://artifacts.apis.io/autonet-work/errors/autonet-work-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autonet-work-problem-types.yml
- group: design
  href: https://artifacts.apis.io/autonet-work/conformance/autonet-work-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autonet-work-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autonet-work/llms/autonet-work-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autonet-work-llms.txt
- group: build
  href: https://artifacts.apis.io/autonet-work/mcp/autonet-work-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/autonet-work-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/autonet-work/mcp/autonet-work-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autonet-work-mcp.yml
- group: other
  href: https://artifacts.apis.io/autonet-work/hosts/autonet-work-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autonet-work-hosts.yml
- group: auth
  href: https://artifacts.apis.io/autonet-work/security/autonet-work-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autonet-work-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autonet.work/
- group: docs
  title: ''
  type: Documentation
  url: https://autonet.work/utils/docs
- group: docs
  title: ''
  type: APIReference
  url: https://autonet.work/utils/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://autonet.work/utils/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://autonet.work/utils/docs
created: '2026-11-02'
description: Autonet provides internet utilities for software agents, offering temporary callback inboxes, network diagnostics, endpoint monitoring, and coin‑based usage limits. Agents can receive webhooks, check DNS and TLS, trace network paths, and track liveness without deploying servers. The service is free‑beta with a credit system and a REST + MCP API documented at https://autonet.work/utils/docs and described by an OpenAPI schema.
json_schemas:
- name: AgentRegistration
  property_count: 11
  slug: autonet-work-agent-registration
- name: ClaimCode
  property_count: 4
  slug: autonet-work-claim-code
- name: TokenResponse
  property_count: 7
  slug: autonet-work-token-response
jsonld:
- class_count: 5
  name: Autonet Work Context
  property_count: 21
  slug: autonet-work-context
layout: provider
mcp_servers:
- description: Remote MCP server at autonet.work.
  name: Autonet MCP Server
  slug: autonet-work-mcp-yml
modified: '2026-11-02'
name: Autonet
nav: Providers
network: true
overview: 'Autonet publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Utils API, and 1 more. Tagged areas include Internet, Utilities, Agents, and Monitoring.


  The Autonet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Autonet''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Autonet Work Plans Pricing
  plan_count: 1
  slug: autonet-work-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Autonet Work Rate Limits
  slug: autonet-work-rate-limits
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Autonet API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: autonet-work-rules
scopes:
- name: Autonet Work Scopes
  scope_count: 0
  slug: autonet-work-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 61.5
    catalog_earned_first_party: 16.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 49.1
    developer_ergonomics: 39.8
    discoverability: 53.3
    operational_transparency: 21.1
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Autonet Work Authentication
  slug: autonet-work-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Autonet Work Domain Security
  slug: autonet-work-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: autonet-work-agent-health
  slug: autonet-work-agent-health
- name: autonet-work-agent
  slug: autonet-work-agent
slug: autonet-work
tags:
- Internet
- Utilities
- Agents
- Monitoring
website: https://autonet.work/
---
