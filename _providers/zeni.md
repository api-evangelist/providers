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
- description: 'Zeni MCP is a hosted, remote Model Context Protocol server that lets AI assistants (Claude, OpenAI Codex, Google Antigravity) read a company''s live Zeni financials. It exposes ~20 read-only tools and '
  name: Zeni MCP Server
  slug: zeni-mcp-server
modified: '2026-07-21'
name: Zeni
nav: Providers
network: true
overview: 'Zeni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Bookkeeping, Accounting, and Financial Operations.


  Zeni''s developer surface includes documentation, pricing, engineering blog, signup flow, authentication, and 12 more developer resources.'
random_paper: 18
screenshot: https://raw.githubusercontent.com/api-evangelist/zeni/refs/heads/main/screenshots/zeni-2026-09-02T171607.png
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
