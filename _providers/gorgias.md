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
    asyncapi_events: true
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
  score: 32.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Gorgias Agentic Access
  operation_count: 49
  slug: gorgias-agentic-access
  summary_line: 49 operations · 26 acting
api_count: 14
apis:
- description: Outbound webhook surface delivered through Gorgias HTTP Integrations. When configured triggers fire on a Gorgias account, Gorgias sends an HTTP request to the URL set on the TicketHttpIntegration, wit
  name: Gorgias Webhooks
  slug: webhooks
- description: The Account API from Gorgias — 2 operation(s) for account.
  name: Gorgias Account API
  slug: gorgias-account-api
- description: The Customers API from Gorgias — 2 operation(s) for customers.
  name: Gorgias Customers API
  slug: gorgias-customers-api
- description: The Integrations API from Gorgias — 2 operation(s) for integrations.
  name: Gorgias Integrations API
  slug: gorgias-integrations-api
- description: The Macros API from Gorgias — 2 operation(s) for macros.
  name: Gorgias Macros API
  slug: gorgias-macros-api
- description: The Messages API from Gorgias — 1 operation(s) for messages.
  name: Gorgias Messages API
  slug: gorgias-messages-api
- description: The Rules API from Gorgias — 2 operation(s) for rules.
  name: Gorgias Rules API
  slug: gorgias-rules-api
- description: The Surveys API from Gorgias — 1 operation(s) for surveys.
  name: Gorgias Surveys API
  slug: gorgias-surveys-api
- description: The Tags API from Gorgias — 3 operation(s) for tags.
  name: Gorgias Tags API
  slug: gorgias-tags-api
- description: The Teams API from Gorgias — 1 operation(s) for teams.
  name: Gorgias Teams API
  slug: gorgias-teams-api
- description: The Tickets API from Gorgias — 2 operation(s) for tickets.
  name: Gorgias Tickets API
  slug: gorgias-tickets-api
- description: The Users API from Gorgias — 2 operation(s) for users.
  name: Gorgias Users API
  slug: gorgias-users-api
- description: The Views API from Gorgias — 2 operation(s) for views.
  name: Gorgias Views API
  slug: gorgias-views-api
- description: The Widgets API from Gorgias — 2 operation(s) for widgets.
  name: Gorgias Widgets API
  slug: gorgias-widgets-api
artifact_total: 22
asyncapis:
- description: Best-effort AsyncAPI 2.6 description of the Gorgias webhook surface, delivered through Gorgias HTTP Integrations. When the configured triggers fire inside a Gorgias account, Gorgias performs an HTTP r
  name: Gorgias Webhooks (HTTP Integrations)
  slug: gorgias-asyncapi
collections:
- collection_type: open
  name: Gorgias REST API
  slug: open-gorgias
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gorgias-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gorgias-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gorgias-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gorgias-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gorgias-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gorgias.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gorgias
- group: company
  title: ''
  type: Website
  url: https://www.gorgias.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gorgias.com
- group: operate
  title: ''
  type: Help Center
  url: https://docs.gorgias.com/en-US
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gorgias.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.gorgias.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gorgias.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.gorgias.com/changelog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gorgiasio
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.gorgias.com/llms.txt
created: '2026-05-11'
description: Gorgias is a customer support and helpdesk platform purpose-built for ecommerce brands, with deep native integrations into Shopify, BigCommerce, Magento, and other commerce stacks to unify email, chat, social, SMS, and voice conversations alongside order data. The platform automates repetitive support tasks with AI agents and macros, surfaces revenue attribution for support interactions, and powers self-service flows on storefronts. The Gorgias REST API provides full CRUD access to tickets, customers, macros, integrations, and widgets using HTTP Basic authentication or OAuth2 for public apps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gorgias.png
layout: provider
modified: '2026-05-30'
name: Gorgias
nav: Providers
network: true
overview: 'Gorgias publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Account API, Customers API, and 11 more. Tagged areas include Customer Support, Helpdesk, Ecommerce, Shopify, and Tickets.


  The Gorgias catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Gorgias'' developer surface includes authentication, engineering blog, documentation, pricing, signup flow, changelog, and 10 more developer resources.'
random_paper: 28
rules:
- name: Gorgias API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: gorgias-asyncapi-spectral-rules
scopes:
- name: Gorgias Scopes
  scope_count: 6
  slug: gorgias-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 38.6
  delta: -3.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 60.2
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gorgias/refs/heads/main/screenshots/gorgias-2026-06-20T182307.png
security:
- kind: authentication
  name: Gorgias Authentication
  slug: gorgias-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gorgias Domain Security
  slug: gorgias-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gorgias Vulnerability Disclosure
  slug: gorgias-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gorgias
tags:
- Customer Support
- Helpdesk
- Ecommerce
- Shopify
- Tickets
- Conversations
website: https://www.gorgias.com
---
