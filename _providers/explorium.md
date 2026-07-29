---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Explorium Agentic Access
  operation_count: 17
  slug: explorium-agentic-access
  summary_line: 17 operations · 14 acting
api_count: 8
apis:
- description: 'Native remote Model Context Protocol server exposing the AgentSource data as 11 agent tools - match-business, fetch-businesses, fetch-businesses- statistics, fetch-businesses-events, enrich-business, '
  name: Explorium AgentSource MCP Server
  slug: explorium-agentsource-mcp-server
- description: Firmographic, technographic, financial, and operational company enrichments.
  name: Explorium Business Enrichments API
  slug: explorium-business-enrichments-api
- description: Match, fetch, stat, and autocomplete over the 150M+ company dataset.
  name: Explorium Businesses API
  slug: explorium-businesses-api
- description: Inspect the shared credit pool that meters all API usage.
  name: Explorium Credits API
  slug: explorium-credits-api
- description: Business and prospect event tracking plus enrollment management.
  name: Explorium Events API
  slug: explorium-events-api
- description: Contact information, profile, and social enrichments for people.
  name: Explorium Prospect Enrichments API
  slug: explorium-prospect-enrichments-api
- description: Match, fetch, stat, and autocomplete over the 800M+ people dataset.
  name: Explorium Prospects API
  slug: explorium-prospects-api
- description: Register endpoints that receive event notifications.
  name: Explorium Webhooks API
  slug: explorium-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: Explorium AgentSource API
  slug: open-explorium
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/explorium-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/explorium-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/explorium-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/explorium-ai
- group: company
  title: ''
  type: Website
  url: https://www.explorium.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.explorium.ai
- group: agent
  title: ''
  type: MCP
  url: https://developers.explorium.ai/mcp-docs/agentsource-mcp
- group: commercial
  title: ''
  type: Plans
  url: plans/explorium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/explorium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/explorium-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.explorium.ai/blog/
created: '2026-07-11'
description: Explorium is a B2B data foundation for AI agents and go-to-market teams. Its AgentSource API is a single external-data and enrichment platform - one API plus a native MCP server - that resolves, fetches, enriches, and monitors a business dataset of 150M+ companies and a prospect dataset of 800M+ people aggregated from 100+ external sources. Capabilities include entity matching, filtered fetch and market-sizing stats, autocomplete, 30+ firmographic / technographic / financial / prospect-contact enrichment endpoints (single and bulk up to 50 records), real-time business and prospect event tracking with webhooks, and a shared credit pool that meters all usage. The API is hosted at https://api.explorium.ai, authenticated with an API_KEY header, and gated behind an Explorium account with a free 100-credit developer tier.
finops:
- name: Explorium Finops
  service_category: Data and Analytics
  slug: explorium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/explorium.png
layout: provider
modified: '2026-07-11'
name: Explorium
nav: Providers
network: true
overview: 'Explorium publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Business Enrichments API, Businesses API, Credits API, and 4 more. Tagged areas include Data Enrichment, Web Intelligence, Reference Data, B2B Data, and Company Data.


  Explorium''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Explorium Plans Pricing
  plan_count: 3
  slug: explorium-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 4
  name: Explorium Rate Limits
  slug: explorium-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/explorium/refs/heads/main/screenshots/explorium-2026-07-25T213931.png
security:
- kind: authentication
  name: Explorium Authentication
  slug: explorium-authentication
  summary_line: apiKey · 1 scheme
slug: explorium
tags:
- Data Enrichment
- Web Intelligence
- Reference Data
- B2B Data
- Company Data
- AI Agents
- Prospect Enrichment
- Firmographics
- MCP
website: https://www.explorium.ai
---
