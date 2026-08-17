---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/crayon-plans-pricing.yml
  - https://www.crayon.co/pricing
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: 'Hosted Model Context Protocol server exposing a customer''s curated Crayon competitive intelligence — battlecards, win/loss stories, competitor profiles, objection handling and customer proof points — '
  name: Crayon Competitive Intelligence MCP Server
  slug: mcp-server
- description: Crayon markets a Content API (battlecards, win/loss stories, competitor profiles, objection handling, customer proof points) and an Answers API (structured real-time answers) for pulling curated compe
  name: Crayon Content and Answers API
  slug: content-answers-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crayon-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crayon-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crayon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crayon-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crayon-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crayon-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crayon-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crayon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crayon-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/crayon-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crayon-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crayon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crayon.co
- group: company
  title: ''
  type: Blog
  url: https://www.crayon.co/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.crayon.co/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crayon.co/pricing
- group: start
  title: ''
  type: Login
  url: https://app.crayon.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crayon.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crayon.co/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crayon-co
created: '2026-05-11'
description: 'Crayon is a Boston-based competitive intelligence platform that automatically captures, analyzes and distributes competitor activity — website and pricing changes, product updates, social posts, news, reviews, job postings and review-site sentiment — and turns it into battlecards, competitor profiles, win/loss stories, objection handling and email digests for product marketing, sales enablement and go-to-market teams. Crayon AI adds automated summarization, dynamic battlecard updates and the 2026 ''Sparks'' feature, which reads a competitor''s strategic moves and writes them up for revenue teams. On 2026-09-04 Crayon shipped what it describes as the first competitive-intelligence MCP server, a hosted OAuth-protected Model Context Protocol endpoint that exposes a customer''s own curated Crayon content to Claude, ChatGPT, Glean, Microsoft Copilot, Google Gemini and internal Slack or Teams assistants. Crayon also markets a Content API and an Answers API, but publishes no developer
  portal, reference or machine-readable specification for either. NOTE: Crayon (crayon.co) is unrelated to Crayon Group ASA (crayon.com), the Norwegian Microsoft CSP.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crayon.png
layout: provider
mcp_servers:
- description: ''
  name: crayon-mcp.yml
  slug: crayon-mcpyml
modified: '2026-08-14'
name: Crayon
nav: Providers
network: true
overview: 'Crayon publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Competitive Intelligence, Market Intelligence, Sales Enablement, Battlecards, and Win-Loss Analysis.


  Crayon''s developer surface includes authentication, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Crayon Plans Pricing
  plan_count: 0
  slug: crayon-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 0
  name: Crayon Rate Limits
  slug: crayon-rate-limits
scopes:
- name: Crayon Scopes
  scope_count: 1
  slug: crayon-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 24.6
  delta: -4.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 8.1
    developer_ergonomics: 21.7
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crayon/refs/heads/main/screenshots/crayon-2026-06-20T175221.png
security:
- kind: authentication
  name: Crayon Authentication
  slug: crayon-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Crayon Domain Security
  slug: crayon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crayon
tags:
- Competitive Intelligence
- Market Intelligence
- Sales Enablement
- Battlecards
- Win-Loss Analysis
- Product Marketing
- AI
- MCP
website: https://www.crayon.co
---
