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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Brex Agentic Access
  operation_count: 17
  slug: brex-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 3
apis:
- description: The Budget Programs API from Brex — 2 operation(s) for budget programs.
  name: Brex Budget Programs API
  slug: brex-budget-programs-api
- description: The Budgets API from Brex — 6 operation(s) for budgets.
  name: Brex Budgets API
  slug: brex-budgets-api
- description: The Spend Limits API from Brex — 3 operation(s) for spend limits.
  name: Brex Spend Limits API
  slug: brex-spend-limits-api
artifact_total: 13
asyncapis:
- description: 'AsyncAPI 2.6 description of the Brex Webhooks surface. Brex uses webhooks to deliver real-time notifications when events happen in the accounts that you manage. Subscribers register an HTTPS callback '
  name: Brex Webhooks API
  slug: brex-webhooks-asyncapi
collections:
- collection_type: open
  name: Brex Budgets API
  slug: open-brex
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brex-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brexhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brexhq
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.brex.com/llms.txt
created: '2024-11-12'
description: Brex is the first fully unified spend platform with global corporate cards, expense management, reimbursements, travel, and bill pay. Brex makes it easy for finance teams to control all of their spend, all in one place. Using the Brex API, you can power your internal tools and create custom workflows.
finops:
- name: Brex Finops
  service_category: API
  slug: brex-finops
graphqls:
- description: Brex is a financial stack for startups and enterprises covering corporate cards, business accounts, bill pay, and expense management. The API covers accounts, cards, transactions, statements, expenses
  name: Brex GraphQL API
  slug: brex-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brex.png
layout: provider
modified: '2026-05-30'
name: Brex
nav: Providers
network: true
overview: 'Brex publishes 3 APIs on the [APIs.io](https://apis.io/) network: Budget Programs API, Budgets API, and Spend Limits API. Tagged areas include Bill Pay, Corporate Cards, Expenses, Reimbursements, and Spending.


  The Brex catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Brex''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Brex Plans Pricing
  plan_count: 3
  slug: brex-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Brex Rate Limits
  slug: brex-rate-limits
rules:
- name: Brex API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: brex-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.8
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brex/refs/heads/main/screenshots/brex-2026-06-20T173653.png
security:
- kind: authentication
  name: Brex Authentication
  slug: brex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brex Domain Security
  slug: brex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brex
tags:
- Bill Pay
- Corporate Cards
- Expenses
- Reimbursements
- Spending
---
