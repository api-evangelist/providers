---
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
    mcp_server: platform
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fundmomentum Agentic Access
  operation_count: 1
  slug: fundmomentum-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://fundmomentum.vc
  baseurl_source: spec
  description: The Api API from Fund Momentum — 1 operation(s) for api.
  name: Fund Momentum API
  slug: fundmomentum-api-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/fundmomentum/agentic-access/fundmomentum-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fundmomentum-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fundmomentum/rules/fundmomentum-rules.yml
  title: ''
  type: Spectral
  url: rules/fundmomentum-rules.yml
- group: design
  href: https://artifacts.apis.io/fundmomentum/errors/fundmomentum-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fundmomentum-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fundmomentum/conformance/fundmomentum-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fundmomentum-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fundmomentum/llms/fundmomentum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fundmomentum-llms.txt
- group: build
  href: https://artifacts.apis.io/fundmomentum/mcp/fundmomentum-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fundmomentum-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fundmomentum/mcp/fundmomentum-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fundmomentum-mcp.yml
- group: other
  href: https://artifacts.apis.io/fundmomentum/hosts/fundmomentum-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fundmomentum-hosts.yml
- group: other
  href: https://artifacts.apis.io/fundmomentum/vendors/fundmomentum-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fundmomentum-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://fundmomentum.vc/press
- group: start
  title: ''
  type: Login
  url: https://fundmomentum.vc/login
- group: auth
  href: https://artifacts.apis.io/fundmomentum/security/fundmomentum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fundmomentum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fundmomentum.vc/
- group: docs
  title: ''
  type: Documentation
  url: https://fundmomentum.vc/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://fundmomentum.vc/_api/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://fundmomentum.vc/for-agents
- group: company
  title: ''
  type: Blog
  url: https://fundmomentum.vc/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fundmomentum.vc/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fundmomentum.vc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fundmomentum.vc/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/fundmomentum/workspace
created: '2026-10-17'
description: Fund Momentum provides agentic fundraising intelligence, offering verified profiles of over 2,700 VC partners across 950+ funds, real-time fund closing data, and LP radar tools. Their platform enables founders and emerging managers to query fund and LP information via a simple MCP API, integrating with AI assistants for personalized insights.
image: https://fundmomentum.vc/_api/og-image-png?title=The%20agentic%20pulse%20of%20Venture%20Capital.&kicker=For%20founders%20and%20emerging%20fund%20managers
layout: provider
mcp_servers:
- description: Remote MCP server at fundmomentum.vc.
  name: Fund Momentum MCP Server
  slug: fundmomentum-mcp-yml
modified: '2026-10-17'
name: Fund Momentum
nav: Providers
network: true
overview: 'Fund Momentum publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fundraising, Venture Capital, Data Intelligence, and AI Agents.


  The Fund Momentum catalog on APIs.io includes 1 Spectral governance ruleset.


  Fund Momentum''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Fund Momentum API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: fundmomentum-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 35.7
    discoverability: 58.3
    operational_transparency: 0.0
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fundmomentum Domain Security
  slug: fundmomentum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fundmomentum
tags:
- Company
- Fundraising
- Venture Capital
- Data Intelligence
- AI Agents
website: https://fundmomentum.vc/
---
