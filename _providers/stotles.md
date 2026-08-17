---
access_model:
  confidence: high
  label: Requires approval
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.stotles.com/pricing
  - https://www.stotles.com/integrations
  - https://api.stotles.com/v1/openapi.json
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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: 'REST API giving programmatic access to UK and Ireland public sector procurement data — notices, buyers, suppliers and framework agreements — as JSON over HTTPS. Eight read-only operations across four '
  name: Stotles Public API
  slug: stotles-public-api
- description: Hosted, remote Model Context Protocol server exposing Stotles public sector market data to AI chat tools and agents. Streamable-HTTP transport at api.stotles.com/mcp, authenticated with the same x-api
  name: Stotles MCP Server
  slug: stotles-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.stotles.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.stotles.com/
- group: operate
  title: ''
  type: Support
  url: https://help.stotles.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.stotles.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://app.stotles.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://app.stotles.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.stotles.com/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stotles.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.stotles.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stotles.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stotles.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.eu.vanta.com/stotles.com/trust/xpcnkioxgcvk0i3qd7fm
- group: auth
  title: ''
  type: Compliance
  url: https://app.eu.vanta.com/stotles.com/trust/xpcnkioxgcvk0i3qd7fm
- group: design
  title: ''
  type: Conformance
  url: conformance/stotles-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stotles-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stotles-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.stotles.com/llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/stotles-trust-center.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stotles
- group: build
  title: ''
  type: Packages
  url: packages/stotles-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stotles-plans-pricing.yml
created: '2026-07-17'
description: 'Stotles is a B2G (business-to-government) public sector procurement and sales intelligence platform for the UK and Ireland. It aggregates procurement notices, contract awards, framework agreements, buyer spend history, and verified decision-maker contacts from public sources such as Find a Tender, Contracts Finder, Digital Marketplace, TED, and Public Contracts Scotland, then layers tender discovery, market intelligence, AI-assisted bid qualification (Bid Studio), account targeting (Sales Studio), and pipeline management on top so suppliers can find, qualify, and win government contracts. Delivered as a SaaS web application at app.stotles.com, and — since 2026 — as a programmable surface: the Stotles Public API is a documented OpenAPI 3.1.0 REST service at api.stotles.com/v1 covering notices, buyers, suppliers and framework agreements, alongside a hosted Model Context Protocol server at api.stotles.com/mcp that brings the same market data into AI chat tools and agents. Both
  authenticate with a static x-api-key header; keys are issued by a Customer Success Manager rather than self-serve, and MCP access is in beta behind a waitlist.'
image: https://cdn.prod.website-files.com/67caf809eabcc3eb572f7bc7/68149b136c8bcfe66f0b8b2f_SEO%20Image%20-%20Homepage.jpg
layout: provider
mcp_servers:
- description: ''
  name: stotles-mcp.yml
  slug: stotles-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-14'
name: Stotles
nav: Providers
network: true
overview: 'Stotles publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Procurement, Public Sector, Government, and Tenders.


  Stotles'' developer surface includes documentation, support, getting-started guide, signup flow, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Stotles Plans Pricing
  plan_count: 11
  slug: stotles-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 2
  name: Stotles Rate Limits
  slug: stotles-rate-limits
score:
  band: developing
  composite: 51.4
  delta: 23.9
  facets:
    commercial_clarity: 92.1
    contract_quality: 61.9
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 27.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 44.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Stotles Authentication
  slug: stotles-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stotles Domain Security
  slug: stotles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stotles Trust Center
  slug: stotles-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: stotles
tags:
- Company
- Procurement
- Public Sector
- Government
- Tenders
- Sales Intelligence
- B2G
- Market Intelligence
- API
- OpenAPI
- MCP
- Agent Native
- Contract Awards
- Framework Agreements
- CPV
- United Kingdom
- Ireland
- GovTech
website: https://www.stotles.com
---
