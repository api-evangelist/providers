---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The public REST API for Northmill Flo (formerly MoreFlo), Northmill Bank's point-of-sale and commerce platform for merchants. Swagger 2.0, 125 paths / 199 operations over articles and pricing, stock m
  name: Northmill Flo API
  slug: northmill-flo-api
- description: Northmill Bank's PSD2 third-party-provider interface, covering Account Information Services (AIS) and Confirmation of Available Funds (CBPII/CAF), with request signing via ES256/RS256 key pairs regist
  name: Northmill Bank Open Banking API for TPPs
  slug: northmill-bank-open-banking-api-for-tpps
artifact_total: 9
asyncapis:
- description: ''
  name: Northmill Flo Webhooks
  slug: northmill-flo-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/northmill-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northmill-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.northmill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.moreflo.com/swagger/ui/index
- group: docs
  title: ''
  type: APIReference
  url: https://api.moreflo.com/swagger/docs/v2
- group: operate
  title: ''
  type: Support
  url: https://www.northmill.com/se/foretag/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.northmill.com/se/foretag/hjalp/
- group: company
  title: ''
  type: Blog
  url: https://www.northmill.com/se/blogg/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.northmill.com/se/foretag/vara-priser/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.northmill.com/se/foretag/villkor/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.northmill.com/se/integritetspolicy/
- group: start
  title: ''
  type: SignUp
  url: https://www.northmill.com/se/foretag/app/portal/login
- group: operate
  title: ''
  type: StatusPage
  url: https://www.northmill.com/se/foretag/hjalp/uppdateringar/driftstatus/
- group: auth
  title: ''
  type: Compliance
  url: https://www.northmill.com/se-en/about-us/corporate-governance/
- group: auth
  title: ''
  type: Security
  url: https://www.northmill.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/northmill-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/northmill-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/northmill-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/northmill-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/northmill-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/northmill-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/northmill-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/northmill-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/northmill-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/northmill-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/northmill-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/northmill-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/northmill-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/northmill-llms.txt
created: '2026-08-26'
description: Northmill Bank AB is a Swedish technology-driven bank, founded in Stockholm in 2006 and licensed by Finansinspektionen in 2019, that serves roughly 600,000 private customers and 2,500 businesses across Sweden, Norway and Finland with savings accounts, cards, personal and business lending, business accounts, Swish and card acquiring. Through its Northmill Flo business unit (formerly MoreFlo, acquired and rebranded) it also ships point-of-sale, booking, checkout and e-commerce products for retail and hospitality merchants. Its public developer surface is the Flo API - a Swagger 2.0 REST contract published at api.moreflo.com with 199 operations over articles, stock, orders, receipts, customers, bookings, campaigns, vouchers, SMS and webhooks - alongside a PSD2 open-banking interface for third-party providers documented under the Northmill Bank brand and delivered on Token.io infrastructure.
image: https://www.northmill.com/icon.png
layout: provider
mcp_servers:
- description: Northmill ships NO Model Context Protocol server, hosted or local. The tool list below is a CANDIDATE derived one-to-one from the merchant-wide operations of the Flo API Swagger document; each tool in
  name: Northmill MCP Server
  slug: northmill-mcp-server
modified: '2026-08-26'
name: Northmill
nav: Providers
network: true
overview: 'Northmill publishes 1 API on the [APIs.io](https://apis.io/) network: Flo API. Tagged areas include Banking, Payments, Point of Sale, Retail, and Open Banking.


  The Northmill catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Northmill''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Northmill Plans Pricing
  plan_count: 16
  slug: northmill-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Northmill Rate Limits
  slug: northmill-rate-limits
score:
  band: strong
  composite: 58.7
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 16.7
    contract_quality: 49.7
    developer_ergonomics: 54.2
    discoverability: 79.6
    governance: 16.7
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Northmill Authentication
  slug: northmill-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Northmill Domain Security
  slug: northmill-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Northmill Vulnerability Disclosure
  slug: northmill-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: northmill
tags:
- Banking
- Payments
- Point of Sale
- Retail
- Open Banking
- Sweden
- Fintech
- Webhooks
- E-commerce
- Lending
- Nordics
website: https://www.northmill.com/
---
