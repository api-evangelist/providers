---
access_model:
  confidence: high
  label: Public contract, retired runtime
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  - lifecycle
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'REST API for the full Cacheflow quote-to-cash surface: proposals (quotes) and proposal items, product catalog and versioning, customers and contacts, subscriptions and change/renewal proposals, billin'
  name: Cacheflow API
  slug: cacheflow-api
artifact_total: 7
asyncapis:
- description: ''
  name: Cacheflow Webhooks
  slug: cacheflow-webhooks
common:
- group: company
  title: ''
  type: Website
  url: http://www.getcacheflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.getcacheflow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.getcacheflow.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://developer.getcacheflow.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.getcacheflow.com/reference/create-an-api-token-copy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getcacheflow
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cacheflow-api-openapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cacheflow-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cacheflow-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cacheflow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cacheflow-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cacheflow-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cacheflow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cacheflow-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cacheflow-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cacheflow-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/cacheflow-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cacheflow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cacheflow-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cacheflow-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cacheflow-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cacheflow-domain-security.yml
created: '2026-07-17'
description: 'Cacheflow was a B2B SaaS billing, CPQ (configure-price-quote), and subscription-management platform that let software companies build interactive deal rooms, automate quote-to-cash, and offer buyers flexible payment and financing options. Founded in 2020 and backed by GGV Capital and GV, Cacheflow was acquired by HubSpot in 2024 and folded into HubSpot Commerce / HubSpot CPQ. The company shipped a substantial REST API — 305 paths and 400 operations across proposals, products, customers, subscriptions, billing schedules, usage, invoices, payments, refunds, approvals, e-signature and CRM/accounting integrations — and that contract is still publicly published: developer.getcacheflow.com serves a live ReadMe developer portal with an llms.txt and an OpenAPI 3.0.1 definition. The runtime is gone. As of 2026-08-13 api.getcacheflow.com, api.sandbox.getcacheflow.com, checkout, status and help all return NXDOMAIN, and getcacheflow.com 301-redirects to HubSpot''s Commerce CPQ page. This
  profile therefore records a rare shape: a fully published, machine-readable API contract that outlived the API it described.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cacheflow.png
layout: provider
mcp_servers:
- description: ''
  name: cacheflow-mcp.yml
  slug: cacheflow-mcpyml
modified: '2026-08-13'
name: Cacheflow
nav: Providers
network: true
overview: 'Cacheflow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Billing, Subscriptions, and CPQ.


  The Cacheflow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cacheflow''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 18 more developer resources.'
plans:
- name: Cacheflow Plans Pricing
  plan_count: 0
  slug: cacheflow-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 0
  name: Cacheflow Rate Limits
  slug: cacheflow-rate-limits
score:
  band: thin
  composite: 35.5
  delta: 29.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 47.0
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 5.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cacheflow/refs/heads/main/screenshots/cacheflow-2026-07-25T204205.png
security:
- kind: authentication
  name: Cacheflow Authentication
  slug: cacheflow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cacheflow Domain Security
  slug: cacheflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cacheflow
tags:
- Company
- Fintech
- Billing
- Subscriptions
- CPQ
- Quote-to-Cash
- Payments
- SaaS
- Invoicing
- Revenue Operations
- E-Signature
- Retired API
website: http://www.getcacheflow.com/
---
