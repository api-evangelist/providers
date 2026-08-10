---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Company profiles, funding rounds, SEC filings and fund formations, keyed to real-time business events.
  name: Fundz API
  slug: fundz-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.fundz.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fundz.net/fundz-api
- group: commercial
  title: ''
  type: Pricing
  url: https://fundz.net/pricing
- group: start
  title: ''
  type: Signup
  url: https://fundz.net/api-trial
- group: agent
  title: ''
  type: LlmsText
  url: https://app.fundz.net/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fundz-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fundz-plans.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fundz-authentication.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Fund-z/fundzwatch-mcp
created: '2026-08-03'
description: 'Fundz is an event-first business intelligence platform, founded 2015, tracking 200,000+ companies and surfacing funding rounds, executive changes, M&A activity, SEC filings (8-K, 10-K, 10-Q, Form D) and website modifications in real time. Rather than storing millions of static records it focuses on companies showing active signals, and scores them against each user''s criteria. The API exposes company profiles, fundings, SEC filings and fund formations from api.fundz.net with an API key in the Authorization header. It sits in the same category as Harmonic and Crunchbase, and competes explicitly on access: an API key is free and issued instantly with no card and no sales call, and pricing is published rather than quoted. Fundz also ships an MCP server listed on the official Model Context Protocol registry, and publishes an llms.txt.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fundz.png
layout: provider
mcp_servers:
- description: ''
  name: fundz-mcp.yml
  slug: fundz-mcpyml
modified: '2026-08-03'
name: Fundz
nav: Providers
network: true
overview: 'Fundz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Intelligence, Funding, Private Markets, Mergers And Acquisitions, and SEC Filings.


  Fundz''s developer surface includes documentation, pricing, signup flow, authentication, and 5 more developer resources.'
plans:
- name: Fundz Plans
  plan_count: 0
  slug: fundz-plans
random_paper: 87
score:
  band: emerging
  composite: 15.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.4
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Fundz Authentication
  slug: fundz-authentication
  summary_line: 1 scheme
slug: fundz
tags:
- Business Intelligence
- Funding
- Private Markets
- Mergers And Acquisitions
- SEC Filings
- Signals
- Sales Intelligence
- MCP
- Agents
website: https://www.fundz.net/
---
