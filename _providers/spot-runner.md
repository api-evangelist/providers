---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 10.8
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.spotrunner.com/
- group: start
  title: ''
  type: Login
  url: https://advertiser.spotrunner.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spotrunner.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spotrunner.com/terms-and-coniditions
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spot-runner-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spot-runner-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spot-runner-domain-security.yml
created: '2026-07-17'
description: Spot Runner is an AI-driven advertising technology company (backed by Battery Ventures) focused on contextual media planning for Connected TV (CTV) and online video. Its platform uses proprietary MicroModeling AI through tools such as ContextPlanner and ContextDeals to match advertiser creative to the most relevant, brand-suitable premium video ad opportunities across leading streaming networks, publishers, and TV OEMs, and to send Deal IDs directly to a buyer's DSP seat. Spot Runner also markets an "Agentic Agency" of multi-agent creative tooling for SMBs and DTC brands. The public surface is a marketing site plus an advertiser login portal; there is no published developer API, OpenAPI, or SDK. The site does expose a hosted Wix Site MCP endpoint for agentic AI access, advertised via its /llms.txt.
image: https://static.wixstatic.com/ficons/875226_5f83093056974a87a56d1050e1e3ee01~mv2.ico
layout: provider
mcp_servers:
- description: ''
  name: Spot Runner Wix Site MCP
  slug: spot-runner-wix-site-mcp
modified: '2026-07-21'
name: Spot Runner
nav: Providers
network: true
overview: Spot Runner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Connected TV, and CTV.
random_paper: 5
score:
  band: emerging
  composite: 14.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.3
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Spot Runner Domain Security
  slug: spot-runner-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spot-runner
tags:
- Company
- Advertising
- AdTech
- Connected TV
- CTV
- Online Video
- Contextual Advertising
- Agentic AI
- Media Planning
website: https://www.spotrunner.com/
---
