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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity API
  slug: open-alloy-automation-connectivity-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Credentials API
  slug: open-alloy-automation-credentials-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Events API
  slug: open-alloy-automation-events-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Integrations API
  slug: open-alloy-automation-integrations-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Passthrough API
  slug: open-alloy-automation-passthrough-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Unified Accounting API
  slug: open-alloy-automation-unified-accounting-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Unified Commerce API
  slug: open-alloy-automation-unified-commerce-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Unified CRM API
  slug: open-alloy-automation-unified-crm-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity User Tokens API
  slug: open-alloy-automation-user-tokens-api
- collection_type: open
  name: Alloy Automation Embedded & Unified Connectivity Users API
  slug: open-alloy-automation-users-api
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
random_paper: 20
rate_limits:
- limit_count: 4
  name: Alloy Automation Rate Limits
  slug: alloy-automation-rate-limits
score:
  band: thin
  composite: 37.0
  delta: -0.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alloy-automation/refs/heads/main/screenshots/alloy-automation-2026-07-25T195811.png
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
