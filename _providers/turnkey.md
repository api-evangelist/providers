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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Turnkey Agentic Access
  operation_count: 21
  slug: turnkey-agentic-access
  summary_line: 21 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.turnkey.com/public/v1
  baseurl_source: declared
  description: Root organization and sub-organization management.
  name: Turnkey Organizations API
  slug: turnkey-organizations-api
- baseURL: https://api.turnkey.com/public/v1
  baseurl_source: declared
  description: Standalone raw private keys.
  name: Turnkey Private Keys API
  slug: turnkey-private-keys-api
- baseURL: https://api.turnkey.com/public/v1
  baseurl_source: declared
  description: Transaction and raw payload signing activities.
  name: Turnkey Signing API
  slug: turnkey-signing-api
- baseURL: https://api.turnkey.com/public/v1
  baseurl_source: declared
  description: Users, authenticators, API keys, and the policy engine.
  name: Turnkey Users & Policies API
  slug: turnkey-users-policies-api
- baseURL: https://api.turnkey.com/public/v1
  baseurl_source: declared
  description: HD wallets and wallet accounts.
  name: Turnkey Wallets API
  slug: turnkey-wallets-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Turnkey Organizations API
  slug: open-turnkey-organizations-api
- collection_type: open
  name: Turnkey Organizations Private Keys API
  slug: open-turnkey-private-keys-api
- collection_type: open
  name: Turnkey Organizations Signing API
  slug: open-turnkey-signing-api
- collection_type: open
  name: Turnkey Organizations Users & Policies API
  slug: open-turnkey-users-policies-api
- collection_type: open
  name: Turnkey Organizations Wallets API
  slug: open-turnkey-wallets-api
- collection_type: open
  name: Turnkey API
  slug: open-turnkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turnkey-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/turnkey-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turnkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turnkey-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tkhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turnkeyhq
- group: company
  title: ''
  type: Website
  url: https://www.turnkey.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.turnkey.com
- group: commercial
  title: ''
  type: Plans
  url: plans/turnkey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turnkey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turnkey-finops.yml
created: '2026-06-20'
description: Turnkey is secure wallet infrastructure and a key-management / signing platform for crypto. Its API-first platform runs private key generation and signing inside verifiable secure enclaves (TEEs), exposing an RPC-style REST API for organizations and sub-organizations, wallets and wallet accounts, raw private keys, users, policies, and authenticators. Every request is cryptographically stamped (P-256 / API-key or passkey signature) and verified before execution.
finops:
- name: Turnkey Finops
  service_category: Security and Identity
  slug: turnkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turnkey.png
layout: provider
modified: '2026-06-20'
name: Turnkey
nav: Providers
network: true
overview: 'Turnkey publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Organizations API, Private Keys API, Signing API, and 2 more. Tagged areas include Crypto, Wallets, Key Management, Signing, and Secure Enclaves.


  Turnkey''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Turnkey Plans Pricing
  plan_count: 4
  slug: turnkey-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Turnkey Rate Limits
  slug: turnkey-rate-limits
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.3
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turnkey/refs/heads/main/screenshots/turnkey-2026-06-20T195835.png
security:
- kind: authentication
  name: Turnkey Authentication
  slug: turnkey-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Turnkey Domain Security
  slug: turnkey-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Turnkey Vulnerability Disclosure
  slug: turnkey-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: turnkey
tags:
- Crypto
- Wallets
- Key Management
- Signing
- Secure Enclaves
website: https://www.turnkey.com
---
