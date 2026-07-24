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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Formance Agentic Access
  operation_count: 95
  slug: formance-agentic-access
  summary_line: 95 operations · 46 acting
api_count: 8
apis:
- description: OAuth2 / OIDC authorization server, clients, and users.
  name: Formance Auth API
  slug: formance-auth-api
- description: Programmable double-entry ledger (v2).
  name: Formance Ledger API
  slug: formance-ledger-api
- description: Flows workflows, instances, and triggers (v2).
  name: Formance Orchestration API
  slug: formance-orchestration-api
- description: Unified payments connectivity, connectors, and transfers.
  name: Formance Payments API
  slug: formance-payments-api
- description: Reconciliation policies and runs.
  name: Formance Reconciliation API
  slug: formance-reconciliation-api
- description: Cross-module search.
  name: Formance Search API
  slug: formance-search-api
- description: White-label wallets, balances, and holds.
  name: Formance Wallets API
  slug: formance-wallets-api
- description: Webhook subscription configuration.
  name: Formance Webhooks API
  slug: formance-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: Formance Platform API
  slug: open-formance
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formance-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/formance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/formance-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/formancehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formance
- group: company
  title: ''
  type: Website
  url: https://www.formance.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formance.com
- group: commercial
  title: ''
  type: Plans
  url: plans/formance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formance-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/formance-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.formance.com/blog/rss.xml
created: '2026-07-01'
description: Formance builds open-source financial infrastructure for money movement. The platform pairs a programmable double-entry Ledger (with the Numscript DSL) with a unified Payments connectivity layer and Flows orchestration, plus Wallets, Reconciliation, Auth, and Webhooks. It is delivered as open-source components and as a managed multi-tenant Formance Cloud, exposing REST APIs secured with OAuth2 client-credentials Bearer tokens.
finops:
- name: Formance Finops
  service_category: Financial Infrastructure
  slug: formance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formance.png
layout: provider
modified: '2026-07-01'
name: Formance
nav: Providers
network: true
overview: 'Formance publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Ledger API, Orchestration API, and 5 more. Tagged areas include Financial Infrastructure, Ledger, Double-Entry Accounting, Payments, and Orchestration.


  Formance''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Formance Plans Pricing
  plan_count: 3
  slug: formance-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 3
  name: Formance Rate Limits
  slug: formance-rate-limits
scopes:
- name: Formance Scopes
  scope_count: 6
  slug: formance-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: thin
  composite: 40.3
  delta: 3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.5
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.6
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 60.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Formance Authentication
  slug: formance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Formance Domain Security
  slug: formance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Formance Vulnerability Disclosure
  slug: formance-vulnerability-disclosure
  summary_line: disclosure policy published
slug: formance
tags:
- Financial Infrastructure
- Ledger
- Double-Entry Accounting
- Payments
- Orchestration
- Money Movement
- Open Source
- Fintech
website: https://www.formance.com
---
