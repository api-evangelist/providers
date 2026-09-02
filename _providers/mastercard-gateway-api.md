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
    auth_clarity: bound
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
  score: 24.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Mastercard Gateway Api Agentic Access
  operation_count: 14
  slug: mastercard-gateway-api-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 1
apis:
- description: The Mastercard Payment Gateway API provides a comprehensive interface for integrating payments into applications, supporting multiple payment methods, currencies, and transaction types for merchants w
  name: Mastercard Gateway API
  slug: mastercard-gateway-api
- description: The Merchant API from Mastercard Gateway API — 10 operation(s) for merchant.
  name: Mastercard Gateway API Merchant API
  slug: mastercard-gateway-api-merchant-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mastercard Payment Gateway REST Merchant API
  slug: open-mastercard-gateway-api-merchant-api
- collection_type: open
  name: Mastercard Payment Gateway REST API
  slug: open-mastercard-gateway-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mastercard-gateway-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mastercard-gateway-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mastercard-gateway-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mastercard-Gateway
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/mastercardgateway
- group: start
  title: ''
  type: Portal
  url: https://developer.mastercard.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.mastercard.com/account/sign-up
- group: start
  title: ''
  type: Login
  url: https://developer.mastercard.com/account/log-in
- group: operate
  title: ''
  type: Support
  url: https://developer.mastercard.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.mastercard.com/terms-of-use
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.mastercard.com/llms.txt
created: '2024-11-28'
description: The Mastercard Payment Gateway provides a robust, developer-friendly REST API for integrating payment processing into applications. It supports a wide range of payment methods, currencies, and transaction types for merchants and payment service providers.
finops:
- name: Mastercard Gateway Api Finops
  service_category: API
  slug: mastercard-gateway-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mastercard-gateway-api.png
layout: provider
modified: '2026-04-28'
name: Mastercard Gateway API
nav: Providers
network: true
overview: 'Mastercard Gateway API publishes 1 API on the [APIs.io](https://apis.io/) network: Merchant API. Tagged areas include Credit Cards, Gateway, Payment Processing, and Payments.


  Mastercard Gateway API''s developer surface includes authentication, developer portal, signup flow, support, and 7 more developer resources.'
plans:
- name: Mastercard Gateway Api Plans Pricing
  plan_count: 3
  slug: mastercard-gateway-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Mastercard Gateway Api Rate Limits
  slug: mastercard-gateway-api-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mastercard-gateway-api/refs/heads/main/screenshots/mastercard-gateway-api-2026-06-20T185023.png
security:
- kind: authentication
  name: Mastercard Gateway Api Authentication
  slug: mastercard-gateway-api-authentication
  summary_line: http/mutualTLS · 2 schemes
- kind: domain-security
  name: Mastercard Gateway Api Domain Security
  slug: mastercard-gateway-api-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: mastercard-gateway-api
tags:
- Credit Cards
- Gateway
- Payment Processing
- Payments
website: https://developer.mastercard.com/
---
