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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Basis Theory Agentic Access
  operation_count: 49
  slug: basis-theory-agentic-access
  summary_line: 49 operations · 30 acting
api_count: 1
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
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Basis Theory 3D Secure API
  slug: open-basis-theory-3d-secure-api
- collection_type: open
  name: Basis Theory 3D Secure Applications API
  slug: open-basis-theory-applications-api
- collection_type: open
  name: Basis Theory 3D Secure Logs API
  slug: open-basis-theory-logs-api
- collection_type: open
  name: Basis Theory 3D Secure Proxy API
  slug: open-basis-theory-proxy-api
- collection_type: open
  name: Basis Theory 3D Secure Reactors API
  slug: open-basis-theory-reactors-api
- collection_type: open
  name: Basis Theory 3D Secure Tenants API
  slug: open-basis-theory-tenants-api
- collection_type: open
  name: Basis Theory 3D Secure Token Intents API
  slug: open-basis-theory-token-intents-api
- collection_type: open
  name: Basis Theory 3D Secure Tokenize / Detokenize API
  slug: open-basis-theory-tokenize-detokenize-api
- collection_type: open
  name: Basis Theory 3D Secure Tokens API
  slug: open-basis-theory-tokens-api
- collection_type: open
  name: Basis Theory 3D Secure Webhooks API
  slug: open-basis-theory-webhooks-api
- collection_type: open
  name: Basis Theory API
  slug: open-basis-theory
common:
- group: auth
  title: ''
  type: Security
  url: https://basistheory.com/security
- group: build
  title: ''
  type: SDKs
  url: https://developers.basistheory.com/docs/sdks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.basistheory.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://basistheory.com/resources/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://basistheory.com/resources/terms-of-service
- group: commercial
  title: ''
  type: Pricing
  url: https://basistheory.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://portal.basistheory.com/register
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


  Basis Theory''s developer surface includes pricing, signup flow, authentication, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Basis Theory Plans Pricing
  plan_count: 4
  slug: basis-theory-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Basis Theory Rate Limits
  slug: basis-theory-rate-limits
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 56.7
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 55.6
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
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
