---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 19.8
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://zeni.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zeni.ai/product/zeni-mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zeni.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.zeni.ai/blog
- group: start
  title: ''
  type: Login
  url: https://app.zeni.ai/
- group: start
  title: ''
  type: SignUp
  url: https://www.zeni.ai/demo/request
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zeni.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zeni.ai/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.zeni.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.zeni.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/zeni-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zeni-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zeni-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zeni-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeni-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zeni-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeni-domain-security.yml
created: '2026-07-17'
description: Zeni is an AI-powered bookkeeping and finance platform for startups and growing businesses, combining machine-learning automation with a dedicated human finance team. It connects to bank accounts, credit cards, payment platforms, and accounting systems to automatically capture and categorize transactions, reconcile accounts, and produce real-time financial dashboards and reports. Alongside AI bookkeeping, Zeni offers bill pay, employee reimbursements, business checking accounts and credit cards, payroll, tax accounting, and fractional CFO services. Zeni also ships a hosted, read-only MCP (Model Context Protocol) server that lets AI assistants such as Claude, OpenAI Codex, and Google Antigravity securely read a company's live Zeni financials via OAuth. The company reports managing more than $20B in transactions annually.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeni.png
layout: provider
mcp_servers:
- description: ''
  name: zeni-mcp.yml
  slug: zeni-mcpyml
modified: '2026-07-21'
name: Zeni
nav: Providers
network: true
overview: 'Zeni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Bookkeeping, Accounting, and Financial Operations.


  Zeni''s developer surface includes documentation, pricing, engineering blog, signup flow, authentication, and 12 more developer resources.'
random_paper: 140
score:
  band: emerging
  composite: 27.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 27.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Zeni Authentication
  slug: zeni-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zeni Domain Security
  slug: zeni-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Zeni Trust Center
  slug: zeni-trust-center
  summary_line: SOC 2 Type II
slug: zeni
tags:
- Company
- Fintech
- Bookkeeping
- Accounting
- Financial Operations
- Startups
- MCP
- AI Agents
website: https://zeni.ai/
---
