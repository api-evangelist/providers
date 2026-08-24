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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.3
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.sava.health/
- group: company
  title: ''
  type: Blog
  url: https://www.sava.health/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.sava.health/waiting-list
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sava.health/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sava.health/privacy-notice
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sava-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sava-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sava-domain-security.yml
created: '2026-07-17'
description: SAVA (sava.health) is a health-monitoring company developing a minimally invasive, continuous multi-molecule biosensor worn just beneath the skin. The platform is designed to capture real-time molecular data - glucose, lactate, ketones, sodium, histamine, urea, alcohol, and cortisol - and surface it through a connected mobile app, aiming to shift healthcare toward preventative monitoring and personal wellness. The company is early stage and pre-launch, operating a waiting-list model for early access to its device rather than a public product. It publishes no first-party developer API or health-data API; its marketing site is built on Wix and exposes the Wix Site MCP endpoint and a published llms.txt for agentic access to public site content only. Backed by Balderton Capital.
image: https://static.wixstatic.com/media/aaa55f_2da7a13e2e4f419c87e476acfc59b6a7~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: SAVA Site MCP (Wix)
  slug: sava-site-mcp-wix
modified: '2026-07-21'
name: SAVA
nav: Providers
network: true
overview: 'SAVA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Biosensor, and Wearables.


  SAVA''s developer surface includes engineering blog, signup flow, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.9
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Sava Domain Security
  slug: sava-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sava
tags:
- Company
- Health
- Digital Health
- Biosensor
- Wearables
- Continuous Monitoring
- Preventative Health
- Health Tech
- MCP
website: https://www.sava.health/
---
