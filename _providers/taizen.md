---
access_model:
  confidence: medium
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://usetaizen.com/book
  - plans/taizen-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Taizen's remote Model Context Protocol server — the company's only machine-callable surface. Per the provider's own manifest it lets an agent connect once instead of wiring fifteen-plus individual MCP
  name: Taizen MCP Server
  slug: taizen-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://usetaizen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usetaizen.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usetaizen.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://usetaizen.com/book
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usetaizen.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usetaizen.com/privacy
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://usetaizen.com/dpa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taizen-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/taizenai
- group: auth
  title: ''
  type: TrustCenter
  url: security/taizen-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.usetaizen.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taizen-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taizen-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/taizen-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/taizen-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/taizen-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taizen-lifecycle.yml
created: '2026-07-17'
description: 'Taizen is a managed agentic AI platform for go-to-market teams that automates win/loss analysis, competitive intelligence and sales-asset production. Its agents continuously read recorded sales calls (Gong, Fireflies, tl;dv, Granola, Genesys Cloud), CRM deal data (Salesforce, HubSpot, Attio, Clari), survey and review signal (Typeform, SurveyMonkey, G2) and existing collateral (Google Drive, SharePoint) to detect recurring objections and competitor moves, then auto-generate battlecards, rep-training drills and AI-roleplay scenarios, and deliver them into Slack. Taizen also books and runs AI-led interviews with lost buyers. Its machine surface is not a REST API but an agent surface: a remote, OAuth-protected MCP server at eu.mcp.usetaizen.com positioned as one connection in place of fifteen-plus individual MCP connectors, and a first-party open-source Claude plugin of thirty GTM Agent Skills. Backed by Techstars, the company emphasizes built-in governance, no model-vendor lock-in,
  SOC 2 / ISO 27001 / GDPR posture with an EU data region, and open sources supporting retrieval tooling on GitHub.'
image: https://usetaizen.com/assets/taizen.svg
layout: provider
mcp_servers:
- description: Taizen's hosted MCP server. Per the provider's own manifest it exists to "connect once instead of 15+ individual MCP connectors" — it indexes the customer's Gong calls, CRM records and documents so an
  name: Taizen MCP Server
  slug: taizen-mcp-server
modified: '2026-08-14'
name: Taizen
nav: Providers
network: true
overview: 'Taizen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Win-Loss Analysis, Competitive Intelligence, Sales Enablement, and Revenue Intelligence.


  Taizen''s developer surface includes documentation, getting-started guide, signup flow, and 15 more developer resources.'
plans:
- name: Taizen Plans Pricing
  plan_count: 0
  slug: taizen-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Taizen Rate Limits
  slug: taizen-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Taizen Authentication
  slug: taizen-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Taizen Domain Security
  slug: taizen-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Taizen Trust Center
  slug: taizen-trust-center
  summary_line: SOC 2, ISO 27001
slug: taizen
tags:
- Company
- Win-Loss Analysis
- Competitive Intelligence
- Sales Enablement
- Revenue Intelligence
- Go-To-Market
- AI Agents
- Battlecards
- Sales
- MCP
- Agent Skills
- Conversation Intelligence
- Product Marketing
website: https://usetaizen.com/
---
