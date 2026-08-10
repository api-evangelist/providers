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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'Dovetail Public API for building custom integrations against a Dovetail workspace: manage projects, folders, docs, insights, data (notes), highlights, tags, themes, channels, topics, contacts, users, '
  name: Dovetail API
  slug: dovetail-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://dovetail.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dovetail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dovetail.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dovetail.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dovetail.com/docs/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/dovetail-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://dovetail.com/signup/
- group: start
  title: ''
  type: Login
  url: https://app.dovetail.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dovetail.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://docs.dovetail.com/help/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.dovetail.com/help/
- group: company
  title: ''
  type: Blog
  url: https://dovetail.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dovetail.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dovetail.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://dovetail.com/changelog/dovetail-api/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dovetail-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dovetail.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dovetail.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dovetail-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dovetail-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dovetail-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dovetail-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dovetail-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dovetail-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dovetail-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dovetail-domain-security.yml
created: '2026-07-17'
description: Dovetail is a customer intelligence platform that aggregates customer feedback from sales calls, support tickets, user-research sessions, surveys and other channels, then uses AI to transcribe, analyze, tag and structure it into a searchable research repository. Teams across product, design, research, customer experience, sales and marketing turn that signal into insights, docs, dashboards and automated agents. The Dovetail Public API (base https://dovetail.com/api/v1) exposes projects, folders, docs, insights, data (notes), highlights, tags, themes, channels, topics, contacts, users, custom fields, files, comments and transcripts, plus Magic Search, Search V2 and Magic Summarize, and an official hosted MCP server for AI agents. Backed by Accel and Felicis.
image: https://dovetail.com/media/Social_Meta1.png
layout: provider
mcp_servers:
- description: ''
  name: dovetail-mcp.yml
  slug: dovetail-mcpyml
modified: '2026-07-18'
name: Dovetail
nav: Providers
network: true
overview: 'Dovetail publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Customer Research, User Research, and Customer Insights.


  Dovetail''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, pricing, support, and 19 more developer resources.'
random_paper: 44
rate_limits:
- limit_count: 1
  name: Dovetail Rate Limits
  slug: dovetail-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 38.2
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dovetail/refs/heads/main/screenshots/dovetail-2026-07-25T212327.png
security:
- kind: authentication
  name: Dovetail Authentication
  slug: dovetail-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Dovetail Domain Security
  slug: dovetail-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dovetail
tags:
- Company
- Consumer
- Customer Research
- User Research
- Customer Insights
- Customer Feedback
- Research Repository
- Analytics
- AI
- Product Management
website: https://dovetail.com/
---
