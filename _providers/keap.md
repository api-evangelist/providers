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
- acting_count: 10
  human_in_the_loop: 0
  name: Keap Agentic Access
  operation_count: 26
  slug: keap-agentic-access
  summary_line: 26 operations · 10 acting
api_count: 9
apis:
- description: Keap REST Hooks webhook surface. Subscribers register a `hookUrl` and `eventKey` via the v1 REST API (`POST /rest/v1/hooks`), complete an `X-Hook-Secret` verification handshake, then receive HTTP POST
  name: Keap REST Hooks
  slug: rest-hooks
- description: Read marketing campaigns.
  name: Keap Campaigns API
  slug: keap-campaigns-api
- description: Manage company records.
  name: Keap Companies API
  slug: keap-companies-api
- description: Manage Keap contacts.
  name: Keap Contacts API
  slug: keap-contacts-api
- description: Manage sales opportunities.
  name: Keap Opportunities API
  slug: keap-opportunities-api
- description: Manage e-commerce orders.
  name: Keap Orders API
  slug: keap-orders-api
- description: Manage catalog products.
  name: Keap Products API
  slug: keap-products-api
- description: Manage tags and tag categories.
  name: Keap Tags API
  slug: keap-tags-api
- description: Manage tasks and follow-ups.
  name: Keap Tasks API
  slug: keap-tasks-api
artifact_total: 16
asyncapis:
- description: AsyncAPI 2.6 description of the Keap (formerly Infusionsoft) REST Hooks webhook surface. Keap REST Hooks are subscriptions that are created and managed via the v1 REST API (`POST /rest/v1/hooks`). Onc
  name: Keap REST Hooks
  slug: keap-resthooks-asyncapi
collections:
- collection_type: open
  name: Keap REST API
  slug: open-keap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/keap-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keap-growing
- group: company
  title: ''
  type: Website
  url: https://keap.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.infusionsoft.com/
- group: start
  title: ''
  type: Signup
  url: https://keap.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://keap.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.infusionsoft.com/
- group: auth
  title: ''
  type: OAuth
  url: https://developer.infusionsoft.com/getting-started-oauth-keys/
- group: company
  title: ''
  type: Blog
  url: https://keap.com/small-business-automation-blog
created: '2026-05-11'
description: Keap (formerly Infusionsoft) is a customer relationship management (CRM), sales, and marketing automation platform for small businesses that combines contact management, email marketing, e-commerce, and pipeline automation. The Keap REST API provides programmatic access to contacts, companies, opportunities, orders, products, tasks, campaigns, and tags using OAuth 2.0 or Personal Access Tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keap.png
layout: provider
modified: '2026-05-30'
name: Keap
nav: Providers
network: true
overview: 'Keap publishes 9 APIs on the [APIs.io](https://apis.io/) network, including REST Hooks, Campaigns API, Companies API, and 6 more. Tagged areas include CRM, Sales, Marketing Automation, Small Business, and E-Commerce.


  The Keap catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Keap''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 7 more developer resources.'
random_paper: 17
rules:
- name: Keap API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: keap-asyncapi-spectral-rules
scopes:
- name: Keap Scopes
  scope_count: 1
  slug: keap-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.5
  delta: -3.5
  facets:
    commercial_clarity: 10.5
    contract_quality: 63.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 0.0
  previous_composite: 40.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/keap/refs/heads/main/screenshots/keap-2026-06-20T183931.png
security:
- kind: authentication
  name: Keap Authentication
  slug: keap-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Keap Domain Security
  slug: keap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: keap
tags:
- CRM
- Sales
- Marketing Automation
- Small Business
- E-Commerce
- Contacts
website: https://keap.com
---
