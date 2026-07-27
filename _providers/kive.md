---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 31.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'The Kive MCP server is Kive''s programmable interface: an OAuth 2.1 protected Model Context Protocol endpoint that lets an authorized agent browse Kive workspaces, saved products, trained models, studi'
  name: Kive MCP Server
  slug: mcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.kive.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kive.ai/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://kive.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://kive.ai/docs/introduction-getting-started/start-here.md
- group: operate
  title: ''
  type: Support
  url: https://kive.ai/docs/troubleshooting-faqs/contact-support.md
- group: company
  title: ''
  type: Blog
  url: https://kive.ai/news
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kive-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://kive.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://kive.ai/signup
- group: start
  title: ''
  type: Login
  url: https://kive.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kive.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kive.ai/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kive-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kive-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kive-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kive-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kive-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kive-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kive-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kive.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/kive-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.kive.ai/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.kive.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kive-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kive-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kive-rate-limits.yml
- group: other
  title: ''
  type: Enterprise
  url: https://kive.ai/enterprise
- group: other
  title: ''
  type: Customers
  url: https://kive.ai/customers
- group: company
  title: ''
  type: Careers
  url: https://kiveai.notion.site/Work-at-Kive-304f5135e42c8078ac44df36a1ba72b8
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getkive
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@kiveai
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/kive.ai
- group: company
  title: ''
  type: Facebook
  url: https://facebook.com/kiveai
created: '2026-07-17'
description: Kive is an AI product photography and campaign content platform for e-commerce brands, built by TO LABS AB and used by more than 10,000 brands. It generates accurate product shots, lifestyle scenes, campaign imagery and product videos from a brand's own assets, using a large catalogue of professionally curated visual presets ("studios") tuned to categories such as fashion, cosmetics, skincare, jewellery and footwear. The platform pairs generation with a creative asset library, AI-powered search, boards, custom-trained subject models, bulk catalogue generation and editing tools (background removal and replacement, canvas extension, upscaling). Kive publishes no public REST API; its programmable surface is an OAuth-protected Model Context Protocol server at mcp.kive.ai that lets agents browse workspaces and products and create images and videos on the user's credits.
image: https://mcp.kive.ai/kive_logo_192.png
layout: provider
mcp_servers:
- description: ''
  name: kive-mcp.yml
  slug: kive-mcpyml
modified: '2026-07-19'
name: Kive
nav: Providers
network: true
overview: 'Kive publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Artificial Intelligence, Generative AI, and Creative.


  Kive''s developer surface includes documentation, getting-started guide, support, engineering blog, changelog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Kive Plans
  plan_count: 4
  slug: kive-plans
random_paper: 23
rate_limits:
- limit_count: 0
  name: Kive Rate Limits
  slug: kive-rate-limits
scopes:
- name: Kive Scopes
  scope_count: 2
  slug: kive-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kive/refs/heads/main/screenshots/kive-2026-07-25T223918.png
security:
- kind: authentication
  name: Kive Authentication
  slug: kive-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Kive Domain Security
  slug: kive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kive Vulnerability Disclosure
  slug: kive-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Kive Trust Center
  slug: kive-trust-center
  summary_line: ISO/IEC 27001:2022
slug: kive
tags:
- Company
- SaaS
- Artificial Intelligence
- Generative AI
- Creative
- Product Photography
- Digital Asset Management
- E-Commerce
- Images
- Video
- MCP
website: https://www.kive.ai/
---
