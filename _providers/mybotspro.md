---
access_model:
  confidence: high
  label: Self-service SaaS, no public API
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://mybots.pro/#pricing
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: 'The myBots identity provider, running OpenIddict. This is the only surface in the estate that publishes a complete, anonymous, machine-readable contract: RFC 8414 authorization-server metadata and an '
  name: myBots Identity (OAuth 2.0 / OpenID Connect)
  slug: mybots-identity-oauth-20-openid-connect
- description: 'The anonymous configuration API behind the embeddable Mia AI web-chat widget. A single published operation, GET /api/IntegrationApp/public/webchat/{channel}/config, returns the launcher accent color, '
  name: myBots Web Chat Public API
  slug: mybots-web-chat-public-api
- description: 'The bearer-gated REST API the Mia AI application calls to operate a tenant''s agents, subscription and channels. Confirmed live — /api/Subscribe/program answers HTTP 401 with www-authenticate: Bearer, '
  name: myBots Tenant API
  slug: mybots-tenant-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://mybots.pro
- group: operate
  title: ''
  type: Support
  url: mailto:service@mybots.pro
- group: commercial
  title: ''
  type: Pricing
  url: https://mybots.pro/#pricing
- group: start
  title: ''
  type: Login
  url: https://mia.mybots.pro/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mybots.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mybots.pro/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/mybotsjp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mybots-pro
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/mybots.pro
- group: other
  title: ''
  type: Telegram
  url: https://t.me/mybots_probot
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mybotspro-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mybotspro-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.mybots.pro/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/mybotspro-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mybotspro-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mybotspro-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mybotspro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mybotspro-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mybotspro-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mybotspro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mybotspro-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/mybotspro-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/mybotspro-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mybotspro-llms.txt
created: '2026-07-17'
description: 'myBots (operated by Global AI Group, Inc.) builds enterprise AI sales and support agents for messaging channels — WhatsApp, Instagram, Telegram, LinkedIn and web chat, under the Mia AI product name. Each agent qualifies inbound leads, answers questions from the business''s own knowledge base in its brand voice, books appointments on a connected calendar, recommends products from a live catalog, and syncs contacts and deals to HubSpot, Bitrix, Pipedrive, amoCRM or Google Sheets. It is a no-developer SaaS aimed at business teams, priced per message rather than per seat. myBots publishes no developer portal, no API reference and no machine-readable API specification of any kind — no OpenAPI, AsyncAPI, GraphQL SDL, Postman collection, MCP server or A2A agent card exists on any of its hosts. It does run real, reachable API infrastructure behind the product: a live OAuth 2.0 / OpenID Connect authorization server at auth.mybots.pro that serves complete anonymous discovery metadata,
  a bearer-gated tenant API at client.mybots.pro, and one anonymous public operation at notification.mybots.pro that configures the embeddable web-chat widget. Surfaced as a portfolio company of 500 Global and added to the API Evangelist network.'
image: https://mybots.pro/og-image.png
layout: provider
modified: '2026-08-14'
name: Mybots.pro
nav: Providers
network: true
overview: 'Mybots.pro publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Conversational AI, Messaging, and Chatbots.


  Mybots.pro''s developer surface includes support, pricing, authentication, and 21 more developer resources.'
plans:
- name: Mybotspro Plans Pricing
  plan_count: 5
  slug: mybotspro-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Mybotspro Rate Limits
  slug: mybotspro-rate-limits
scopes:
- name: Mybotspro Scopes
  scope_count: 6
  slug: mybotspro-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials/password
score:
  band: emerging
  composite: 22.4
  delta: -6.7
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mybotspro/refs/heads/main/screenshots/mybotspro-2026-08-07T184510.png
security:
- kind: authentication
  name: Mybotspro Authentication
  slug: mybotspro-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Mybotspro Domain Security
  slug: mybotspro-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mybotspro
tags:
- Company
- AI Agents
- Conversational AI
- Messaging
- Chatbots
- Customer Support
- Sales Automation
- WhatsApp
- Telegram
- Instagram
- Omnichannel
- Lead Qualification
- OpenID Connect
website: https://mybots.pro
---
