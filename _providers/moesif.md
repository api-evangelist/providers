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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 106
  human_in_the_loop: 0
  name: Moesif Agentic Access
  operation_count: 174
  slug: moesif-agentic-access
  summary_line: 174 operations · 106 acting
api_count: 16
apis:
- description: The Moesif Collector API is the high-volume ingestion endpoint that receives API event data from server, client, and gateway SDKs. It accepts HTTP API call records, user/company entity updates, and cu
  name: Moesif Collector API
  slug: collector
- description: The Applications API from Moesif — 2 operation(s) for applications.
  name: Moesif Applications API
  slug: moesif-applications-api
- description: The Balance Transactions API from Moesif — 1 operation(s) for balance transactions.
  name: Moesif Balance Transactions API
  slug: moesif-balance-transactions-api
- description: The Billing Meters API from Moesif — 2 operation(s) for billing meters.
  name: Moesif Billing Meters API
  slug: moesif-billing-meters-api
- description: The Billing Reports API from Moesif — 2 operation(s) for billing reports.
  name: Moesif Billing Reports API
  slug: moesif-billing-reports-api
- description: The Cohorts API from Moesif — 3 operation(s) for cohorts.
  name: Moesif Cohorts API
  slug: moesif-cohorts-api
- description: The Companies API from Moesif — 5 operation(s) for companies.
  name: Moesif Companies API
  slug: moesif-companies-api
- description: The Dashboards API from Moesif — 7 operation(s) for dashboards.
  name: Moesif Dashboards API
  slug: moesif-dashboards-api
- description: The Email Templates API from Moesif — 2 operation(s) for email templates.
  name: Moesif Email Templates API
  slug: moesif-email-templates-api
- description: The Governance Rules API from Moesif — 2 operation(s) for governance rules.
  name: Moesif Governance Rules API
  slug: moesif-governance-rules-api
- description: The Metrics API from Moesif — 4 operation(s) for metrics.
  name: Moesif Metrics API
  slug: moesif-metrics-api
- description: The Product Catalog API from Moesif — 4 operation(s) for product catalog.
  name: Moesif Product Catalog API
  slug: moesif-product-catalog-api
- description: The Properties API from Moesif — 7 operation(s) for properties.
  name: Moesif Properties API
  slug: moesif-properties-api
- description: The Subscriptions API from Moesif — 4 operation(s) for subscriptions.
  name: Moesif Subscriptions API
  slug: moesif-subscriptions-api
- description: The Users API from Moesif — 5 operation(s) for users.
  name: Moesif Users API
  slug: moesif-users-api
- description: The Workspaces API from Moesif — 8 operation(s) for workspaces.
  name: Moesif Workspaces API
  slug: moesif-workspaces-api
artifact_total: 25
collections:
- collection_type: open
  name: Management API
  slug: open-moesif
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moesif-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moesif-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moesif-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moesif-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moesif
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moesif
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/moesif
- group: company
  title: ''
  type: Website
  url: https://www.moesif.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.moesif.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.moesif.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moesif.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.moesif.com/wrap
- group: company
  title: ''
  type: Blog
  url: https://www.moesif.com/blog
- group: build
  title: ''
  type: SDKs
  url: https://www.moesif.com/docs/server-integration/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesifdjango
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesifwsgi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesiftornado
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesifpythonrequest
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-servlet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesifmiddleware-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-laravel
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-slim
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-rack
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-play-filter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-browser-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-aws-lambda-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-aws-lambda-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moesif/moesif-aws-lambda-go
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Moesif/moesif-cloudflare
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Moesif/kong-plugin-moesif
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Moesif/lua-resty-moesif
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Moesif/express-gateway-plugin-moesif
- group: build
  title: ''
  type: Tools
  url: https://github.com/Moesif/auth0-logs-to-moesif
- group: build
  title: ''
  type: Sample
  url: https://github.com/Moesif/moesif-developer-portal
created: '2025-01-08'
description: Moesif is an API analytics, monitoring, monetization, and governance platform for API and AI product teams. The platform unifies API observability (analytics, logs, metrics, traces via OpenTelemetry), usage-based monetization (billing meters, product catalog, prepaid credits, Stripe integration), quotas and governance (rate limiting, contract enforcement), and customer-experience tooling (behavioral cohorts, emails, embedded metrics, developer portal). Moesif has expanded into AI agent and LLM analytics with usage-based billing for AI apps, GenAI-powered "Ask AI" analytics queries, and content monetization for LLM training.
finops:
- name: Moesif Finops
  service_category: API
  slug: moesif-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moesif.png
layout: provider
modified: '2026-05-22'
name: Moesif
nav: Providers
network: true
overview: 'Moesif publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Balance Transactions API, Billing Meters API, and 12 more. Tagged areas include Analytics, Monitoring, Monetization, Governance, and Observability.


  The Moesif catalog on APIs.io includes 1 Spectral governance ruleset.


  Moesif''s developer surface includes authentication, documentation, API reference, pricing, signup flow, engineering blog, tooling, and 30 more developer resources.'
plans:
- name: Moesif Plans Pricing
  plan_count: 3
  slug: moesif-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Moesif Rate Limits
  slug: moesif-rate-limits
rules:
- name: Moesif API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: moesif-rules
scopes:
- name: Moesif Scopes
  scope_count: 71
  slug: moesif-scopes
  summary_line: 71 scopes · password
score:
  band: developing
  composite: 45.7
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.4
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moesif/refs/heads/main/screenshots/moesif-2026-06-20T185704.png
security:
- kind: authentication
  name: Moesif Authentication
  slug: moesif-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Moesif Domain Security
  slug: moesif-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moesif
tags:
- Analytics
- Monitoring
- Monetization
- Governance
- Observability
- Billing
- AI Agents
- LLM Analytics
- OpenTelemetry
- Developer Portal
- Platform
- Insights
website: https://www.moesif.com/
---
