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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Basis Theory Agentic Access
  operation_count: 49
  slug: basis-theory-agentic-access
  summary_line: 49 operations · 30 acting
api_count: 10
apis:
- description: Create and authenticate 3D Secure sessions.
  name: Basis Theory 3D Secure API
  slug: basis-theory-3d-secure-api
- description: Manage API credentials, permissions, and access rules.
  name: Basis Theory Applications API
  slug: basis-theory-applications-api
- description: List audit logs of platform activity.
  name: Basis Theory Logs API
  slug: basis-theory-logs-api
- description: Manage pre-configured proxies and invoke the detokenizing Proxy.
  name: Basis Theory Proxy API
  slug: basis-theory-proxy-api
- description: Manage and invoke serverless Reactor functions.
  name: Basis Theory Reactors API
  slug: basis-theory-reactors-api
- description: Manage the current tenant, usage reports, and security contact.
  name: Basis Theory Tenants API
  slug: basis-theory-tenants-api
- description: Short-lived intents that capture data before conversion to a token.
  name: Basis Theory Token Intents API
  slug: basis-theory-token-intents-api
- description: Batch tokenization and detokenization.
  name: Basis Theory Tokenize / Detokenize API
  slug: basis-theory-tokenize-detokenize-api
- description: Create, retrieve, search, update, and delete tokens.
  name: Basis Theory Tokens API
  slug: basis-theory-tokens-api
- description: Register webhook URLs and subscribe to event types.
  name: Basis Theory Webhooks API
  slug: basis-theory-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Basis Theory API
  slug: open-basis-theory
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/basis-theory-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/basis-theory-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basis-theory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/basis-theory-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Basis-Theory
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/basis-theory
- group: company
  title: ''
  type: Website
  url: https://basistheory.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.basistheory.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/basis-theory-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/basis-theory-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/basis-theory-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.basistheory.com/rss.xml
created: '2026-06-20'
description: Basis Theory is a PCI Level 1 compliant tokenization and data vault platform. Its API-first product lets developers tokenize, store, and use sensitive data - cardholder data, PII, PHI, and bank account numbers - without that data ever touching their own systems, using tokens, a detokenizing Proxy, serverless Reactors, and 3D Secure authentication.
finops:
- name: Basis Theory Finops
  service_category: Security and Compliance
  slug: basis-theory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basis-theory.png
layout: provider
modified: '2026-06-20'
name: Basis Theory
nav: Providers
network: true
overview: 'Basis Theory publishes 10 APIs on the [APIs.io](https://apis.io/) network, including 3D Secure API, Applications API, Logs API, and 7 more. Tagged areas include Tokenization, Data Vault, PCI Compliance, Payments, and Security.


  Basis Theory''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Basis Theory Plans Pricing
  plan_count: 4
  slug: basis-theory-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 4
  name: Basis Theory Rate Limits
  slug: basis-theory-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basis-theory/refs/heads/main/screenshots/basis-theory-2026-06-20T173050.png
security:
- kind: authentication
  name: Basis Theory Authentication
  slug: basis-theory-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Basis Theory Domain Security
  slug: basis-theory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Basis Theory Trust Center
  slug: basis-theory-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: basis-theory
tags:
- Tokenization
- Data Vault
- PCI Compliance
- Payments
- Security
website: https://basistheory.com/
---
