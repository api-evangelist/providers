---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bargo Congress Trades Api Agentic Access
  operation_count: 6
  slug: bargo-congress-trades-api-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: A focused Streamable HTTP MCP server exposing three read-only tools over the Congress Trades dataset — get_congress_trades, get_congress_member and get_congress_stats. The handshake and tools/list are
  name: Congress Trades MCP Server
  slug: congress-trades-mcp-server
- description: Members of Congress and their disclosure histories.
  name: Bargo Congress Trades API Members API
  slug: bargo-congress-trades-api-members-api
- description: Aggregate dataset statistics and freshness.
  name: Bargo Congress Trades API Statistics API
  slug: bargo-congress-trades-api-statistics-api
- description: Normalized House and Senate securities transactions.
  name: Bargo Congress Trades API Trades API
  slug: bargo-congress-trades-api-trades-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bargo-congress-trades-api-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bargo-congress-trades-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bargo-congress-trades-api-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bargo.ai/free-apis/congress
- group: docs
  title: ''
  type: Documentation
  url: https://www.bargo.ai/free-apis/congress
- group: docs
  title: ''
  type: APIReference
  url: https://www.bargo.ai/free-apis/congress/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bargo.ai/free-apis/congress
- group: start
  title: ''
  type: SignUp
  url: https://www.bargo.ai/free-apis/dash
- group: operate
  title: ''
  type: Support
  url: https://www.bargo.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bargo.ai/free-apis/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bargo.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bargo-ai
- group: company
  title: ''
  type: Blog
  url: https://www.bargo.ai/research
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bargo-congress-trades-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bargo-congress-trades-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bargo-congress-trades-api-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bargo-congress-trades-api-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/bargo-congress-trades-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bargo-congress-trades-api-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bargo-congress-trades-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bargo-congress-trades-api-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bargo-congress-trades-api-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bargo-congress-trades-api-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bargo-congress-trades-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bargo-congress-trades-api-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/bargo-congress-trades-api-components.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bargo-congress-trades-api-congress-trades-overlay.yaml
created: '2026-07-26'
description: A free JSON REST API and hosted MCP server from Bargo that normalizes U.S. House and Senate STOCK Act securities transaction disclosures into a queryable dataset — currently 42,000+ disclosed trades across 415 members and 4,100+ tickers. Six read-only GET operations cover trades (filterable by ticker, member, chamber, transaction type and date range), a member roster, per-member disclosure histories, aggregate statistics, and a dataset-freshness health check. Unusually for a free congressional-trading tracker, every row carries per-trade price performance — estimated price at the trade, latest price, and percent move since. Records are parsed and deduplicated from the official U.S. House Clerk Financial Disclosure reports and Senate eFD Periodic Transaction Reports, so disclosures lag transactions by up to ~45 days. Access is anonymous by default at a lower quota; a free no-card API key raises limits and unlocks a focused three-tool MCP server for agents. Open CORS, an embeddable
  browser widget, and first-party JavaScript and Python clients. Attribution is required; bulk redistribution of raw records is not permitted.
examples:
- key_count: 4
  name: Bargo Congress Trades Api Get Health Example
  slug: bargo-congress-trades-api-get-health-example
- key_count: 4
  name: Bargo Congress Trades Api Get Stats Example
  slug: bargo-congress-trades-api-get-stats-example
- key_count: 4
  name: Bargo Congress Trades Api List Trades By Ticker Example
  slug: bargo-congress-trades-api-list-trades-by-ticker-example
image: https://www.bargo.ai/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: bargo-congress-trades-api-mcp.yml
  slug: bargo-congress-trades-api-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-09'
name: Bargo Congress Trades API
nav: Providers
network: true
overview: 'Bargo Congress Trades API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Members API, Statistics API, and Trades API. Tagged areas include congress, finance, stocks, government, and stock-act.


  Bargo Congress Trades API''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 22 more developer resources.'
random_paper: 83
rate_limits:
- limit_count: 6
  name: Bargo Congress Trades Api Rate Limits
  slug: bargo-congress-trades-api-rate-limits
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 57.5
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Bargo Congress Trades Api Authentication
  slug: bargo-congress-trades-api-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Bargo Congress Trades Api Domain Security
  slug: bargo-congress-trades-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bargo-congress-trades-api
tags:
- congress
- finance
- stocks
- government
- stock-act
- mcp
- congressional-trading
- financial-disclosure
- market-data
- public-data
- free-api
- open-data
website: https://www.bargo.ai/free-apis/congress
---
