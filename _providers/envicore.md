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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.4
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envicore-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/envicore-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/envicore-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/envicore-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://envicoreinc.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.envicoreinc.com/privacy-policy
created: '2026-07-17'
description: 'EnviCore is a Calgary, Alberta based sustainability and materials-technology company, backed by Techstars, that produces low-carbon supplementary cementitious materials for the mining and construction industries. Its low-temperature process repurposes industrial waste, mine tailings, clays, and pozzolans into valuable cement replacements, reducing CO2 emissions and supporting a circular economy. EnviCore does not publish a developer API, but its public website exposes an agentic surface: a published llms.txt and a live Wix Site MCP endpoint for AI-agent access to public site content.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envicore.png
layout: provider
mcp_servers:
- description: ''
  name: EnviCore Site MCP (Wix)
  slug: envicore-site-mcp-wix
modified: '2026-07-19'
name: EnviCore
nav: Providers
network: true
overview: EnviCore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sustainability, CleanTech, Construction Materials, and Cement.
random_paper: 69
score:
  band: minimal
  composite: 10.7
  delta: 0.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/envicore/refs/heads/main/screenshots/envicore-2026-07-25T213447.png
security:
- kind: domain-security
  name: Envicore Domain Security
  slug: envicore-domain-security
  summary_line: TLSv1.3 · HSTS
slug: envicore
tags:
- Company
- Sustainability
- CleanTech
- Construction Materials
- Cement
- Mining
- Circular Economy
- Carbon Reduction
- MCP
website: https://envicoreinc.com/
---
