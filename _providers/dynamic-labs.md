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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Dynamic Labs Agentic Access
  operation_count: 22
  slug: dynamic-labs-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Gate authentication with allowlists.
  name: Dynamic Allowlists API
  slug: dynamic-labs-allowlists-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Retrieve aggregate environment analytics.
  name: Dynamic Analytics API
  slug: dynamic-labs-analytics-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Create and revoke environment-scoped API tokens.
  name: Dynamic API Tokens API
  slug: dynamic-labs-api-tokens-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Provision MPC-TSS embedded wallets for users.
  name: Dynamic Embedded Wallets API
  slug: dynamic-labs-embedded-wallets-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Retrieve and update environment (project) configuration.
  name: Dynamic Environments API
  slug: dynamic-labs-environments-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Download data exports.
  name: Dynamic Exports API
  slug: dynamic-labs-exports-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Fetch the JSON Web Key Set used to verify Dynamic JWTs.
  name: Dynamic JWKS API
  slug: dynamic-labs-jwks-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: List and manage end users authenticated into an environment.
  name: Dynamic Users API
  slug: dynamic-labs-users-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: View and manage wallets linked to users.
  name: Dynamic Wallets API
  slug: dynamic-labs-wallets-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Manage webhook endpoints for event notifications.
  name: Dynamic Webhooks API
  slug: dynamic-labs-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dynamic Allowlists API
  slug: open-dynamic-labs-allowlists-api
- collection_type: open
  name: Dynamic Allowlists Analytics API
  slug: open-dynamic-labs-analytics-api
- collection_type: open
  name: Dynamic Allowlists API Tokens API
  slug: open-dynamic-labs-api-tokens-api
- collection_type: open
  name: Dynamic Allowlists Embedded Wallets API
  slug: open-dynamic-labs-embedded-wallets-api
- collection_type: open
  name: Dynamic Allowlists Environments API
  slug: open-dynamic-labs-environments-api
- collection_type: open
  name: Dynamic Allowlists Exports API
  slug: open-dynamic-labs-exports-api
- collection_type: open
  name: Dynamic Allowlists JWKS API
  slug: open-dynamic-labs-jwks-api
- collection_type: open
  name: Dynamic Allowlists Users API
  slug: open-dynamic-labs-users-api
- collection_type: open
  name: Dynamic Allowlists Wallets API
  slug: open-dynamic-labs-wallets-api
- collection_type: open
  name: Dynamic Allowlists Webhooks API
  slug: open-dynamic-labs-webhooks-api
- collection_type: open
  name: Dynamic API
  slug: open-dynamic-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dynamic-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dynamic-labs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynamic-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dynamic-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dynamic-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dynamic-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dynamic-labs-financial
- group: company
  title: ''
  type: Website
  url: https://www.dynamic.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dynamic.xyz
- group: commercial
  title: ''
  type: Plans
  url: plans/dynamic-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dynamic-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dynamic-labs-finops.yml
created: '2026-07-01'
description: Dynamic is a web3 authentication and embedded wallet platform. It provides multi-chain login, embedded and smart wallets secured with MPC-TSS, onramps, and end-to-end user management through a developer dashboard, client SDKs, and an environment-scoped REST API for programmatically managing users, wallets, projects, webhooks, and token verification.
finops:
- name: Dynamic Labs Finops
  service_category: Identity and Access Management
  slug: dynamic-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dynamic-labs.png
layout: provider
modified: '2026-07-01'
name: Dynamic
nav: Providers
network: true
overview: 'Dynamic publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Allowlists API, Analytics API, API Tokens API, and 7 more. Tagged areas include Web3, Authentication, Embedded Wallets, Wallets, and MPC.


  Dynamic''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Dynamic Labs Plans Pricing
  plan_count: 3
  slug: dynamic-labs-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Dynamic Labs Rate Limits
  slug: dynamic-labs-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.7
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
    score: 35.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/screenshots/dynamic-labs-2026-07-25T212555.png
security:
- kind: authentication
  name: Dynamic Labs Authentication
  slug: dynamic-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dynamic Labs Domain Security
  slug: dynamic-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dynamic Labs Vulnerability Disclosure
  slug: dynamic-labs-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Dynamic Labs Trust Center
  slug: dynamic-labs-trust-center
  summary_line: SOC 2
slug: dynamic-labs
tags:
- Web3
- Authentication
- Embedded Wallets
- Wallets
- MPC
- Onboarding
- Crypto
website: https://www.dynamic.xyz
---
