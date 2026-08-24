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
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: http://percolata.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/percolata
- group: agent
  title: ''
  type: MCPServer
  url: mcp/percolata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/percolata-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/percolata-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.percolata.com/contact-form
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.percolata.com/terms-of-policy
created: '2026-07-17'
description: Percolata is a Palo Alto, California predictive-analytics company that applies machine learning to help retailers optimize labor scheduling and marketing spend. Its platform forecasts hourly sales, in-store traffic, and takeout demand to drive staffing optimization and marketing budget allocation, with published claims of 4x higher forecast accuracy, 10-20% same-store sales lift, and a forecast-accuracy guarantee. Named customers include 7-Eleven, Uniqlo, and Telefonica. The company is backed by Andreessen Horowitz (a16z) and Google Ventures (GV). Percolata does not publish a public developer portal or REST API reference; its retail platform is delivered as a managed product with custom application integration. The percolata.com marketing site is now served by Wix, which provisions a live, first-party Model Context Protocol (MCP) endpoint and an llms.txt for agentic access to public site content.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/percolata.png
layout: provider
mcp_servers:
- description: ''
  name: Percolata MCP Server
  slug: percolata-mcp-server
modified: '2026-07-20'
name: Percolata
nav: Providers
network: true
overview: 'Percolata is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Analytics, Machine-Learning, and Predictive Analytics.


  Percolata''s developer surface includes support and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.1
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.1
  provenance:
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Percolata Domain Security
  slug: percolata-domain-security
  summary_line: TLSv1.3 · HSTS
slug: percolata
tags:
- Company
- Retail
- Analytics
- Machine-Learning
- Predictive Analytics
- Workforce Optimization
- Marketing Optimization
website: http://percolata.com
---
