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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Crayon Agentic Access
  operation_count: 22
  slug: crayon-agentic-access
  summary_line: 22 operations · 8 acting
api_count: 10
apis:
- description: REST API providing programmatic access to Crayon competitive intelligence content, battlecards, and AI-generated answers for integration into CRMs, enterprise search, and chat platforms. SDKs, Swagger
  name: Crayon Content and Answers API
  slug: content-answers-api
- description: Model Context Protocol server (Competitive Data Platform) that exposes Crayon competitive intelligence to AI assistants and tools such as ChatGPT, Glean, Copilot, Slack, and CRM systems.
  name: Crayon Competitive Intelligence MCP Server
  slug: mcp-server
- description: The Agreements API from Crayon — 1 operation(s) for agreements.
  name: Crayon Agreements API
  slug: crayon-agreements-api
- description: The Authentication API from Crayon — 1 operation(s) for authentication.
  name: Crayon Authentication API
  slug: crayon-authentication-api
- description: The Billing API from Crayon — 2 operation(s) for billing.
  name: Crayon Billing API
  slug: crayon-billing-api
- description: The Clients API from Crayon — 2 operation(s) for clients.
  name: Crayon Clients API
  slug: crayon-clients-api
- description: The CustomerTenants API from Crayon — 2 operation(s) for customertenants.
  name: Crayon CustomerTenants API
  slug: crayon-customertenants-api
- description: The Organizations API from Crayon — 3 operation(s) for organizations.
  name: Crayon Organizations API
  slug: crayon-organizations-api
- description: The Subscriptions API from Crayon — 2 operation(s) for subscriptions.
  name: Crayon Subscriptions API
  slug: crayon-subscriptions-api
- description: The Users API from Crayon — 2 operation(s) for users.
  name: Crayon Users API
  slug: crayon-users-api
artifact_total: 15
collections:
- collection_type: open
  name: Crayon API
  slug: open-crayon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crayon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crayon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crayon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crayon-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crayon-group
- group: company
  title: ''
  type: Website
  url: https://www.crayon.co
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.crayon.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crayon.co/request-a-demo
- group: start
  title: ''
  type: Signup
  url: https://www.crayon.co/request-a-demo
- group: company
  title: ''
  type: Blog
  url: https://www.crayon.co/blog/rss.xml
created: '2026-05-11'
description: Crayon is a competitive intelligence platform that automates the gathering, analysis, and distribution of competitor data from websites, social media, news, reviews, and other digital sources to power battlecards, win/loss analysis, and sales enablement. Its 2026 'Sparks' AI feature analyzes competitors' strategic moves and generates summaries for go-to-market teams. Crayon offers Content and Answers APIs plus a Competitive Intelligence MCP Server for integrating competitor insights into platforms like ChatGPT, Glean, Copilot, Slack, and CRMs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crayon.png
layout: provider
modified: '2026-05-11'
name: Crayon
nav: Providers
network: true
overview: 'Crayon publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agreements API, Authentication API, Billing API, and 5 more. Tagged areas include Competitive Intelligence, Market Intelligence, Sales Enablement, Battlecards, and Win-Loss Analysis.


  Crayon''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 36
scopes:
- name: Crayon Scopes
  scope_count: 1
  slug: crayon-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: emerging
  composite: 27.2
  delta: -2.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crayon/refs/heads/main/screenshots/crayon-2026-06-20T175221.png
security:
- kind: authentication
  name: Crayon Authentication
  slug: crayon-authentication
  summary_line: http/oauth2 · 2 schemes
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
- AI
- MCP
website: https://www.crayon.co
---
