---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: Solve Intelligence's first-party remote Model Context Protocol server. A streamable-HTTP MCP endpoint, authorized with OAuth against the company's own authorization server, that exposes patent and non
  name: Solve MCP
  slug: solve-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/solve-intelligence-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solve-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solveintelligence.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.solveintelligence.com/blog/post/solve-intelligence-mcp-server-now-available-in-claude-2
- group: company
  title: ''
  type: Blog
  url: https://www.solveintelligence.com/blog
- group: start
  title: ''
  type: Login
  url: https://copilot.solveintelligence.com/
- group: operate
  title: ''
  type: Support
  url: https://www.solveintelligence.com/book-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solveintelligence.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solveintelligence.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.solveintelligence.com/security
- group: auth
  title: ''
  type: Compliance
  url: conformance/solve-intelligence-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/solve-intelligence-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/solve-intelligence-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solve-intelligence-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/solve-intelligence-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/solve-intelligence-plans-pricing.yml
created: '2026-08-28'
description: 'Solve Intelligence builds AI-native software for patent attorneys and intellectual property teams. Its Patent Copilot is an in-browser document editor, comparable to a word processor, with an AI assistant purpose-built for the patent lifecycle: application drafting, claim drafting, office action response and prosecution, invention harvesting and disclosure enhancement, claim and invalidity charting, prior-art and freedom-to-operate searching, infringement and validity analysis, standard-essential patent mapping, patent translation and proofreading. The company was founded by patent attorneys, AI researchers and software engineers, is used by hundreds of law firms and in-house IP teams across six continents, and has raised roughly $55M from Y Combinator, Microsoft, Thomson Reuters, 20VC, Operator Collective and Visionaries. Its public machine-readable surface is a first-party remote Model Context Protocol server, "Solve MCP", which brings global patent literature, non-patent
  literature, jurisdictional legal texts and case law, and SEP standard documentation into an agent session for subscribers.'
image: https://cdn.prod.website-files.com/6a3bc5ce3cbfe3ee9f91aa1c/6a8c37735149fe1094ae44a6_solveai-opengraph-2026-08.jpg
layout: provider
mcp_servers:
- description: Solve Intelligence publishes a first-party remote MCP server that exposes a slice of its Patent Copilot research surface to MCP clients. It is the only machine-callable API surface the company publish
  name: Solve MCP
  slug: solve-mcp
modified: '2026-08-28'
name: Solve Intelligence
nav: Providers
network: true
overview: 'Solve Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Tech, Intellectual Property, and Patents.


  Solve Intelligence''s developer surface includes documentation, engineering blog, support, and 13 more developer resources.'
plans:
- name: Solve Intelligence Plans Pricing
  plan_count: 0
  slug: solve-intelligence-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Solve Intelligence Rate Limits
  slug: solve-intelligence-rate-limits
scopes:
- name: Solve Intelligence Scopes
  scope_count: 0
  slug: solve-intelligence-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/solve-intelligence/refs/heads/main/screenshots/solve-intelligence-2026-09-02T160137.png
security:
- kind: authentication
  name: Solve Intelligence Authentication
  slug: solve-intelligence-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Solve Intelligence Domain Security
  slug: solve-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Solve Intelligence Trust Center
  slug: solve-intelligence-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: solve-intelligence
tags:
- Company
- Legal
- Legal Tech
- Intellectual Property
- Patents
- Artificial Intelligence
- Document Generation
- Search
- MCP
- Agents
website: https://www.solveintelligence.com/
---
