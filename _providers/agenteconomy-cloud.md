---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agenteconomy Cloud Agentic Access
  operation_count: 12
  slug: agenteconomy-cloud-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://agentery.com/api/v1
  baseurl_source: declared
  description: The aepi API from agenteconomy.cloud — 3 operation(s) for aepi.
  name: agenteconomy.cloud Aepi API
  slug: agenteconomy-cloud-aepi-api
- baseURL: https://agentery.com/api/v1
  baseurl_source: declared
  description: The discovery API from agenteconomy.cloud — 4 operation(s) for discovery.
  name: agenteconomy.cloud Discovery API
  slug: agenteconomy-cloud-discovery-api
- baseURL: https://agentery.com/api/v1
  baseurl_source: declared
  description: The market API from agenteconomy.cloud — 4 operation(s) for market.
  name: agenteconomy.cloud Market API
  slug: agenteconomy-cloud-market-api
- baseURL: https://agentery.com/api/v1
  baseurl_source: declared
  description: The pricing API from agenteconomy.cloud — 2 operation(s) for pricing.
  name: agenteconomy.cloud Pricing API
  slug: agenteconomy-cloud-pricing-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/agenteconomy-cloud/agentic-access/agenteconomy-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenteconomy-cloud-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/agenteconomy-cloud/rate-limits/agenteconomy-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agenteconomy-cloud-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agenteconomy-cloud/plans/agenteconomy-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenteconomy-cloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agenteconomy-cloud/rules/agenteconomy-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/agenteconomy-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/agenteconomy-cloud/vocabulary/agenteconomy-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenteconomy-cloud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agenteconomy-cloud/errors/agenteconomy-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenteconomy-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agenteconomy-cloud/conformance/agenteconomy-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenteconomy-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenteconomy-cloud/llms/agenteconomy-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenteconomy-cloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/agenteconomy-cloud/mcp/agenteconomy-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenteconomy-cloud-mcp.yml
- group: other
  href: https://artifacts.apis.io/agenteconomy-cloud/hosts/agenteconomy-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenteconomy-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenteconomy-cloud/vendors/agenteconomy-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenteconomy-cloud-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agenteconomy-cloud/security/agenteconomy-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenteconomy-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenteconomy.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://agenteconomy.cloud/guides/use-our-data
- group: docs
  title: ''
  type: APIReference
  url: https://agenteconomy.cloud/api/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agenteconomy.cloud/guides/use-our-data
- group: company
  title: ''
  type: Blog
  url: https://agenteconomy.cloud/pulse
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Onnson/agenteconomy-mcp
created: '2026-10-31'
description: What AI agents buy, sell and pay for, explained for newcomers, with market numbers you can recompute from public chain data. Weekly Pulse, seller rankings, protocol guides, and an MCP server that checks sellers before an agent pays.
image: https://agenteconomy.cloud/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.agenteconomy.cloud.
  name: agenteconomy.cloud MCP Server
  slug: agenteconomy-cloud-mcp-yml
modified: '2026-11-01'
name: agenteconomy.cloud
nav: Providers
network: true
overview: 'agenteconomy.cloud publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aepi API, Discovery API, Market API, and 1 more. Tagged areas include Artificial Intelligence, Agents, Economy, Data, and Marketplace.


  The agenteconomy.cloud catalog on APIs.io includes 1 Spectral governance ruleset.


  agenteconomy.cloud''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Agenteconomy Cloud Plans Pricing
  plan_count: 5
  slug: agenteconomy-cloud-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Agenteconomy Cloud Rate Limits
  slug: agenteconomy-cloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: agenteconomy.cloud API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: agenteconomy-cloud-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 43.5
    developer_ergonomics: 15.5
    discoverability: 65.0
    operational_transparency: 23.7
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
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
  name: Agenteconomy Cloud Domain Security
  slug: agenteconomy-cloud-domain-security
  summary_line: TLSv1.3
slug: agenteconomy-cloud
tags:
- Artificial Intelligence
- Agents
- Economy
- Data
- Marketplace
website: https://agenteconomy.cloud/
---
