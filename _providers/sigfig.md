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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sigfig-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sigfig-llms.txt
- group: company
  title: ''
  type: Website
  url: https://sigfig.com/home/
created: '2026-07-17'
description: 'SigFig is a San Francisco-based wealth management technology (fintech) company. It operates two lines: "Tandems," an enterprise platform that helps financial institutions deliver intelligent, personalized financial advice, and "SigFig Wealth Management," a consumer robo-advisory service that builds and manages tax-efficient, diversified investment portfolios tailored to each client''s goals. SigFig is backed by Bain Capital Ventures, DCM Ventures, and Union Square Ventures. As of the 2026-07-21 enrichment pass, SigFig publishes no public developer API, SDK, MCP server, or developer portal; its site is served behind a WAF and the developer/docs/api subdomains do not resolve.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sigfig.png
layout: provider
modified: '2026-07-21'
name: SigFig
nav: Providers
network: true
overview: SigFig is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Wealth Management, Robo-Advisor, and Investing.
random_paper: 33
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Sigfig Domain Security
  slug: sigfig-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sigfig
tags:
- Company
- Fintech
- Wealth Management
- Robo-Advisor
- Investing
- Financial Services
- WealthTech
website: https://sigfig.com/home/
---
