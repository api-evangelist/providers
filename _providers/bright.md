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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.thinkbright.mx/
- group: company
  title: ''
  type: About
  url: https://www.thinkbright.mx/sobrenosotros
- group: operate
  title: ''
  type: Support
  url: https://www.thinkbright.mx/contacto
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thinkbright.mx/aviso-privacidad
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bright-mexico/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/joinbright/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/joinbright/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bright-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bright-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bright-domain-security.yml
created: '2026-07-17'
description: Bright is Mexico's leading residential and commercial solar energy provider, founded in 2014 (Y Combinator W15) by Jonah Greenberger. Often described as "Sunrun for the developing world," Bright combines financing and software to let homeowners and businesses adopt rooftop solar and battery energy storage (BESS) at no upfront cost. The company operates a marketplace connecting a network of local installers, distributors, and retail promoters with customers, and offers financing models such as solar PPAs and leasing schemes. Bright's public web presence is a Wix-hosted marketing site (thinkbright.mx) covering its industrial, commercial, and home solutions, success cases, and 24/7 energy monitoring technology. It exposes an agent-facing surface via an llms.txt and a hosted Wix Site MCP endpoint, but publishes no first-party developer/REST API.
image: https://static.wixstatic.com/media/248b1d_f91dfc1bc971452080cea17e73bcc327~mv2.png/v1/fill/w_2500,h_2500,al_c/248b1d_f91dfc1bc971452080cea17e73bcc327~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: bright-mcp.yml
  slug: bright-mcpyml
modified: '2026-07-18'
name: Bright
nav: Providers
network: true
overview: 'Bright is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar Energy, Renewable Energy, Energy Storage, and FinTech.


  Bright''s developer surface includes support and 9 more developer resources.'
random_paper: 75
score:
  band: minimal
  composite: 11.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.6
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bright/refs/heads/main/screenshots/bright-2026-07-25T203828.png
security:
- kind: domain-security
  name: Bright Domain Security
  slug: bright-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bright
tags:
- Company
- Solar Energy
- Renewable Energy
- Energy Storage
- FinTech
- Climate
- Mexico
- Y Combinator
website: https://www.thinkbright.mx/
---
