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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Deskfeed Dev Agentic Access
  operation_count: 5
  slug: deskfeed-dev-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://deskfeed.dev
  baseurl_source: declared
  description: The Bsc Alerts API from deskfeed — 1 operation(s) for bsc alerts.
  name: deskfeed Bsc Alerts API
  slug: deskfeed-dev-bsc-alerts-api
- baseURL: https://deskfeed.dev
  baseurl_source: declared
  description: The Bsc Pool Autopsy API from deskfeed — 1 operation(s) for bsc pool autopsy.
  name: deskfeed Bsc Pool Autopsy API
  slug: deskfeed-dev-bsc-pool-autopsy-api
- baseURL: https://deskfeed.dev
  baseurl_source: declared
  description: The Bsc Verdict API from deskfeed — 1 operation(s) for bsc verdict.
  name: deskfeed Bsc Verdict API
  slug: deskfeed-dev-bsc-verdict-api
- baseURL: https://deskfeed.dev
  baseurl_source: declared
  description: The Events API from deskfeed — 1 operation(s) for events.
  name: deskfeed Events API
  slug: deskfeed-dev-events-api
- baseURL: https://deskfeed.dev
  baseurl_source: declared
  description: The Market State API from deskfeed — 1 operation(s) for market state.
  name: deskfeed Market State API
  slug: deskfeed-dev-market-state-api
artifact_total: 10
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zw-onemaker-ai
- group: agent
  href: https://artifacts.apis.io/deskfeed-dev/agentic-access/deskfeed-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deskfeed-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/deskfeed-dev/plans/deskfeed-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deskfeed-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deskfeed-dev/rules/deskfeed-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/deskfeed-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/deskfeed-dev/errors/deskfeed-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deskfeed-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deskfeed-dev/conformance/deskfeed-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deskfeed-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deskfeed-dev/llms/deskfeed-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deskfeed-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/deskfeed-dev/a2a/deskfeed-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deskfeed-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/deskfeed-dev/mcp/deskfeed-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deskfeed-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/deskfeed-dev/hosts/deskfeed-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deskfeed-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/deskfeed-dev/vendors/deskfeed-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deskfeed-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/deskfeed-dev/security/deskfeed-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deskfeed-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deskfeed.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://deskfeed.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://deskfeed.dev/agent/
- group: operate
  title: ''
  type: Contact
  url: https://deskfeed.dev/
created: '2026-11-05'
description: Deskfeed is an autonomous economic agent platform that provides real market‑data services via on‑chain payments. It offers five API endpoints for data retrieval, integrates with USDC on Base, and showcases projects like Autonomous Economic Agent, AgentGate, and OneMaker Pipeline. The site includes documentation, an OpenAPI spec, and links to GitHub repositories, emphasizing AI‑driven agent reliability and open‑source tooling.
image: https://deskfeed.dev/images/og.png?v=3
layout: provider
mcp_servers:
- description: Remote MCP server at deskfeed.dev.
  name: deskfeed MCP Server
  slug: deskfeed-dev-mcp-yml
modified: '2026-11-05'
name: deskfeed
nav: Providers
network: true
overview: 'deskfeed publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bsc Alerts API, Bsc Pool Autopsy API, Bsc Verdict API, and 2 more. Tagged areas include Artificial Intelligence, Autonomous Agents, Data Services, Blockchain, and Open Source.


  The deskfeed catalog on APIs.io includes 1 Spectral governance ruleset.


  deskfeed''s developer surface includes API reference, getting-started guide, and 14 more developer resources.'
plans:
- name: Deskfeed Dev Plans Pricing
  plan_count: 3
  slug: deskfeed-dev-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: deskfeed API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: deskfeed-dev-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deskfeed Dev Domain Security
  slug: deskfeed-dev-domain-security
  summary_line: TLSv1.3
slug: deskfeed-dev
tags:
- Artificial Intelligence
- Autonomous Agents
- Data Services
- Blockchain
- Open Source
website: https://deskfeed.dev/
---
