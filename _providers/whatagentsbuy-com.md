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
    agent_skills: unknown
    agentic_access: false
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Independent trust, discovery and delivery data for the APIs behind agentic commerce.
  name: What Agents Buy API
  slug: what-agents-buy-api
- baseURL: https://whatagentsbuy.com
  baseurl_source: declared
  description: Independent trust, discovery and delivery data for the APIs behind agentic commerce. Free JSON endpoints plus one paid x402 lookup. No key required for the free data.
  name: What Agents Buy API API
  slug: what-agents-buy-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/whatagentsbuy-com/rules/whatagentsbuy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/whatagentsbuy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/whatagentsbuy-com/conformance/whatagentsbuy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whatagentsbuy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/whatagentsbuy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/whatagentsbuy-com/errors/whatagentsbuy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whatagentsbuy-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/whatagentsbuy-com/llms/whatagentsbuy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whatagentsbuy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/whatagentsbuy-com/mcp/whatagentsbuy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/whatagentsbuy-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/whatagentsbuy-com/hosts/whatagentsbuy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whatagentsbuy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/whatagentsbuy-com/vendors/whatagentsbuy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whatagentsbuy-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/whatagentsbuy-com/security/whatagentsbuy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whatagentsbuy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whatagentsbuy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://whatagentsbuy.com/checklist
- group: start
  title: ''
  type: GettingStarted
  url: https://whatagentsbuy.com/grading
created: '2026-10-31'
description: What Agents Buy provides independent reviews and data on x402 APIs that power agentic commerce. It aggregates transaction data from multiple blockchain networks, offers a live dashboard of USDC payments, and publishes detailed receipts and analyses for developers and researchers. The platform aims to increase transparency in the emerging AI‑driven commerce ecosystem by delivering open data and insights.
image: https://whatagentsbuy.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at whatagentsbuy.com.
  name: whatagentsbuy-com MCP Server
  slug: whatagentsbuy-com-mcp-yml
modified: '2026-10-31'
name: whatagentsbuy-com
nav: Providers
network: true
overview: 'whatagentsbuy-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including What Agents Buy API API, and 1 more. Tagged areas include Artificial Intelligence, Commerce, Blockchain, Data, and Transparency.


  The whatagentsbuy-com catalog on APIs.io includes 1 Spectral governance ruleset.


  whatagentsbuy-com''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: whatagentsbuy-com API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: whatagentsbuy-com-rules
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 33.3
    developer_ergonomics: 17.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 21.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
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
  name: Whatagentsbuy Com Domain Security
  slug: whatagentsbuy-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: whatagentsbuy-com
tags:
- Artificial Intelligence
- Commerce
- Blockchain
- Data
- Transparency
website: https://whatagentsbuy.com/
---
