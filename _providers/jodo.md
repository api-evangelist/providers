---
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: REST API for connecting an institute's ERP, finance or student-information system to Jodo fee collection. Covers user registration and hosted-flow access tokens, student master data and fee structures
  name: Jodo ERP Integrations API
  slug: jodo-erp-integrations-api
- description: Event delivery surface for the Jodo platform. Jodo POSTs 36 documented events across student master data, manual payments, Flex subscriptions/mandates/instalments, Pay collections and Cred education l
  name: Jodo Webhooks
  slug: jodo-webhooks
artifact_total: 7
asyncapis:
- description: Jodo delivers state changes for students, manual payments, Flex instalment plans, Pay collections and Cred education loans as HTTP POST webhooks to a URL the institute registers per event_code. PROVEN
  name: Jodo Webhooks
  slug: jodo-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.jodo.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jodo.in/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jodo.in/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jodo.in/getting-started/api-structure/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jodo.in/getting-started/introduction/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jodo-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jodo-sandbox.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jodo.in/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/jodo-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jodo-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jodo-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jodo-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jodo-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jodo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jodo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jodo-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/jodo-packages.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/jodo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jodo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jodo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.jodo.in/
- group: company
  title: ''
  type: Blog
  url: https://www.jodo.in/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jodohq
- group: operate
  title: ''
  type: Support
  url: https://www.jodo.in/contact-us/
- group: start
  title: ''
  type: Login
  url: https://app.jodo.in/institute/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jodo.in/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jodo.in/privacy-policy/
created: '2026-08-23'
description: 'Jodo is a Bengaluru-based fintech that automates fee collection for Indian educational institutes — schools, colleges, universities, coaching centres and skilling institutes. Founded in 2020 by Atulya Bhat, Raghav Nagarajan and Koustav Dey, the company says it serves 5,000+ institutes across 90+ cities and has processed over INR 30,000 crore in fees for 25 lakh+ students. Jodo ships three products on one platform: Flex (structured fees paid in instalments through an auto-debit mandate), Pay (student-linked collections, hosted checkout orders and shareable payment links) and Cred (education loans originated with NBFC lending partners). Its public ERP Integrations API lets an institute''s ERP, finance or student-information system register users and students, sync fee structures and discounts, reconcile manual payments, configure instalment schedules, create checkout orders and payment links, and manage webhook subscriptions. Jodo publishes a substantial developer reference at
  docs.jodo.in covering 25 REST operations and 36 webhook events, with documented UAT and production environments, Basic Auth, an error code registry, a retry and idempotency policy, HMAC SHA-256 webhook signatures and published source IP ranges — but no machine-readable OpenAPI or AsyncAPI document, and no public pricing.'
image: https://www.jodo.in/assets/images/icons/favicon.png
layout: provider
modified: '2026-08-23'
name: Jodo
nav: Providers
network: true
overview: 'Jodo publishes 2 APIs on the [APIs.io](https://apis.io/) network: ERP Integrations API and Webhooks. Tagged areas include Company, Payments, Education, Fintech, and Fee Collection.


  The Jodo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jodo''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 21 more developer resources.'
plans:
- name: Jodo Plans Pricing
  plan_count: 0
  slug: jodo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Jodo Rate Limits
  slug: jodo-rate-limits
score:
  band: strong
  composite: 56.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 63.0
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 28.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Jodo Authentication
  slug: jodo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jodo Domain Security
  slug: jodo-domain-security
  summary_line: TLSv1.3
slug: jodo
tags:
- Company
- Payments
- Education
- Fintech
- Fee Collection
- Lending
- India
- Webhooks
- ERP Integration
- Financial Services
website: https://www.jodo.in/
---
