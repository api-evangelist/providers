---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Midpage Agentic Access
  operation_count: 3
  slug: midpage-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 4
apis:
- description: Remote Model Context Protocol server (OAuth-authenticated) that gives AI assistants like Claude, ChatGPT, and Perplexity source-grounded legal research tools - search, findInOpinion, analyzeOpinion, a
  name: Midpage MCP Server
  slug: mcp
- description: The Opinions API from Midpage — 1 operation(s) for opinions.
  name: Midpage Opinions API
  slug: midpage-opinions-api
- description: The Search API from Midpage — 1 operation(s) for search.
  name: Midpage Search API
  slug: midpage-search-api
- description: The User API from Midpage — 1 operation(s) for user.
  name: Midpage User API
  slug: midpage-user-api
artifact_total: 11
collections:
- collection_type: open
  name: Midpage Legal Database API
  slug: open-midpage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/midpage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/midpage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/midpage-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/midpage
- group: company
  title: ''
  type: Website
  url: https://www.midpage.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://midpage-docs.apidocumentation.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/midpage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/midpage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/midpage-finops.yml
created: '2026-06-21'
description: Midpage is an AI-powered legal research and drafting platform built on its own US legal database of millions of court opinions, statutes, and regulations spanning federal and state jurisdictions. Its developer products expose this corpus through a REST case-law API (semantic, keyword, and hybrid search; opinion retrieval; citator treatments), a Model Context Protocol (MCP) server for AI agents, and direct SQL read-replica access.
finops:
- name: Midpage Finops
  service_category: Legal Technology
  slug: midpage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/midpage.png
layout: provider
modified: '2026-06-21'
name: Midpage
nav: Providers
network: true
overview: 'Midpage publishes 3 APIs on the [APIs.io](https://apis.io/) network: Opinions API, Search API, and User API. Tagged areas include Legal, Case Law, Legal Research, Search, and AI.


  Midpage''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Midpage Plans Pricing
  plan_count: 4
  slug: midpage-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Midpage Rate Limits
  slug: midpage-rate-limits
score:
  band: thin
  composite: 39.2
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Midpage Authentication
  slug: midpage-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Midpage Domain Security
  slug: midpage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: midpage
tags:
- Legal
- Case Law
- Legal Research
- Search
- AI
website: https://www.midpage.ai/
---
