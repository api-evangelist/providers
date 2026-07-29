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
- acting_count: 12
  human_in_the_loop: 1
  name: Atomic Fi Agentic Access
  operation_count: 30
  slug: atomic-fi-agentic-access
  summary_line: 30 operations · 12 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The Access Tokens API from Atomic — 2 operation(s) for access tokens.
  name: Atomic Access Tokens API
  slug: atomic-fi-access-tokens-api
- description: The Company API from Atomic — 3 operation(s) for company.
  name: Atomic Company API
  slug: atomic-fi-company-api
- description: The Data API from Atomic — 7 operation(s) for data.
  name: Atomic Data API
  slug: atomic-fi-data-api
- description: The Linked Accounts API from Atomic — 2 operation(s) for linked accounts.
  name: Atomic Linked Accounts API
  slug: atomic-fi-linked-accounts-api
- description: The PayLink API from Atomic — 2 operation(s) for paylink.
  name: Atomic PayLink API
  slug: atomic-fi-paylink-api
- description: The Secrets API from Atomic — 2 operation(s) for secrets.
  name: Atomic Secrets API
  slug: atomic-fi-secrets-api
- description: The Tasks API from Atomic — 5 operation(s) for tasks.
  name: Atomic Tasks API
  slug: atomic-fi-tasks-api
- description: The Users API from Atomic — 3 operation(s) for users.
  name: Atomic Users API
  slug: atomic-fi-users-api
- description: The Webhooks API from Atomic — 2 operation(s) for webhooks.
  name: Atomic Webhooks API
  slug: atomic-fi-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: Atomic API
  slug: open-atomic-fi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/atomic-fi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atomic-fi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atomic-fi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atomicfi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atomicfi
- group: company
  title: ''
  type: Website
  url: https://atomicfi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atomicfi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/atomic-fi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atomic-fi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/atomic-fi-finops.yml
created: '2026-07-01'
description: Atomic is a payroll and financial connectivity platform. Through user-permissioned access to payroll, HR, and merchant accounts, Atomic lets applications switch direct deposit, verify income and employment, retrieve payroll data, and update payment methods on file. The Transact SDK is an embedded, hosted front-end that drives these workflows on top of Atomic's backend REST API.
finops:
- name: Atomic Fi Finops
  service_category: Financial Services
  slug: atomic-fi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atomic-fi.png
layout: provider
modified: '2026-07-01'
name: Atomic
nav: Providers
network: true
overview: 'Atomic publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Company API, Data API, and 6 more. Tagged areas include Fintech, Payroll, Direct Deposit, Income Verification, and Employment Verification.


  Atomic''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Atomic Fi Plans Pricing
  plan_count: 2
  slug: atomic-fi-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Atomic Fi Rate Limits
  slug: atomic-fi-rate-limits
score:
  band: thin
  composite: 35.0
  delta: -2.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atomic-fi/refs/heads/main/screenshots/atomic-fi-2026-07-25T201606.png
security:
- kind: authentication
  name: Atomic Fi Authentication
  slug: atomic-fi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Atomic Fi Domain Security
  slug: atomic-fi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: atomic-fi
tags:
- Fintech
- Payroll
- Direct Deposit
- Income Verification
- Employment Verification
- Financial Connectivity
- Embedded Finance
website: https://atomicfi.com
---
