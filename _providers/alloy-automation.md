---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 9
  human_in_the_loop: 0
  name: Alloy Automation Agentic Access
  operation_count: 27
  slug: alloy-automation-agentic-access
  summary_line: 27 operations · 9 acting
api_count: 10
apis:
- description: Discover resources/actions and execute typed actions.
  name: Alloy Automation Connectivity API
  slug: alloy-automation-connectivity-api
- description: Third-party connections held by a user, plus credential metadata.
  name: Alloy Automation Credentials API
  slug: alloy-automation-credentials-api
- description: Execution events and observability.
  name: Alloy Automation Events API
  slug: alloy-automation-events-api
- description: Available connectors and a user's enabled integrations.
  name: Alloy Automation Integrations API
  slug: alloy-automation-integrations-api
- description: Raw proxied requests to a provider via a stored credential.
  name: Alloy Automation Passthrough API
  slug: alloy-automation-passthrough-api
- description: Normalized accounting objects (accounts, invoices).
  name: Alloy Automation Unified Accounting API
  slug: alloy-automation-unified-accounting-api
- description: Normalized commerce objects (products, orders, customers).
  name: Alloy Automation Unified Commerce API
  slug: alloy-automation-unified-commerce-api
- description: Normalized CRM objects (contacts, companies, deals).
  name: Alloy Automation Unified CRM API
  slug: alloy-automation-unified-crm-api
- description: Per-user JWTs for rendering the embedded frontend.
  name: Alloy Automation User Tokens API
  slug: alloy-automation-user-tokens-api
- description: End-user records that scope credentials, integrations, and executions.
  name: Alloy Automation Users API
  slug: alloy-automation-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Alloy Automation Embedded & Unified API
  slug: open-alloy-automation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alloy-automation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alloy-automation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alloy-automation-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alloy-automation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alloy-automation
- group: company
  title: ''
  type: Website
  url: https://runalloy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runalloy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/alloy-automation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alloy-automation-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alloy-automation-finops.yml
created: '2026-07-01'
description: Alloy Automation (runalloy.com) is an embedded integration platform (iPaaS) and Unified API for SaaS products. Its Embedded product lets you drop white-labeled, end-user-facing integrations into your app, while the Connectivity and Unified API provide a single REST interface for connecting to hundreds of third-party platforms across commerce, CRM, and accounting. All APIs use dated versioning (2024-03), a Bearer API key, and per-user credentials/tokens.
finops:
- name: Alloy Automation Finops
  service_category: Integration Platform
  slug: alloy-automation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alloy-automation.png
layout: provider
modified: '2026-07-01'
name: Alloy Automation
nav: Providers
network: true
overview: 'Alloy Automation publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Connectivity API, Credentials API, Events API, and 7 more. Tagged areas include iPaaS, Integration, Unified API, Embedded, and SaaS.


  Alloy Automation''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Alloy Automation Plans Pricing
  plan_count: 3
  slug: alloy-automation-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 4
  name: Alloy Automation Rate Limits
  slug: alloy-automation-rate-limits
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Alloy Automation Authentication
  slug: alloy-automation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alloy Automation Domain Security
  slug: alloy-automation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alloy-automation
tags:
- iPaaS
- Integration
- Unified API
- Embedded
- SaaS
- Automation
website: https://runalloy.com
---
