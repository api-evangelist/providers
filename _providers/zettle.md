---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Zettle Agentic Access
  operation_count: 3
  slug: zettle-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: OAuth 2.0 authentication and authorisation for Zettle APIs. Supports authorisation code grant with PKCE for mobile and partner-hosted apps.
  name: Zettle OAuth API
  slug: zettle-oauth-api
- description: Retrieve purchase transaction history, individual purchase records, and refund data for a merchant account.
  name: Zettle Purchase API
  slug: zettle-purchase-api
- description: Manage the merchant product catalogue including products, variants, prices, and categories.
  name: Zettle Product Library API
  slug: zettle-product-library-api
- description: Track stock levels and inventory movements across merchant locations. Default rate limit is 4 requests per second.
  name: Zettle Inventory API
  slug: zettle-inventory-api
- description: Upload and manage product images used in the Zettle product library and POS display.
  name: Zettle Image API
  slug: zettle-image-api
- description: Issue, redeem, and manage gift cards for Zettle merchants.
  name: Zettle Giftcard API
  slug: zettle-giftcard-api
- description: The accounts API from Zettle — 2 operation(s) for accounts.
  name: Zettle accounts API
  slug: zettle-accounts-api
- description: The payout API from Zettle — 1 operation(s) for payout.
  name: Zettle payout API
  slug: zettle-payout-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Finance accounts API
  slug: open-zettle-accounts-api
- collection_type: open
  name: Finance accounts payout API
  slug: open-zettle-payout-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zettle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zettle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zettle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zettle-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zettle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zettle.com/docs/get-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/izettle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zettle/
- group: company
  title: ''
  type: Blog
  url: https://www.zettle.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zettle.com/gb/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zettle.com/
- group: other
  title: ''
  type: X
  url: https://x.com/Zettle
- group: commercial
  title: ''
  type: Plans
  url: plans/zettle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zettle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zettle-finops.yml
created: 2026-06-13
description: Zettle by PayPal is a cloud-based point-of-sale platform (formerly iZettle) that provides REST APIs for managing product inventory, processing card payments, tracking purchases, handling refunds, and accessing merchant financial and account data.
examples:
- key_count: 3
  name: Zettle Get Account Balance Example
  slug: zettle-get-account-balance-example
- key_count: 3
  name: Zettle Get Payout Info Example
  slug: zettle-get-payout-info-example
- key_count: 3
  name: Zettle Get Transactions Example
  slug: zettle-get-transactions-example
finops:
- name: Zettle Finops
  service_category: ''
  slug: zettle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zettle.png
json_schemas:
- name: Zettle Account Balance
  property_count: 2
  slug: zettle-account-balance
- name: Zettle Payout Info
  property_count: 5
  slug: zettle-payout-info
- name: Zettle Transaction
  property_count: 4
  slug: zettle-transaction
jsonld:
- class_count: 4
  name: Zettle Context
  property_count: 13
  slug: zettle-context
layout: provider
modified: 2026-06-13
name: Zettle
nav: Providers
network: true
overview: 'Zettle publishes 2 APIs on the [APIs.io](https://apis.io/) network: accounts API and payout API. Tagged areas include Point-of-Sale, POS, Payments, Inventory, and Finance.


  The Zettle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zettle''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Zettle Plans Pricing
  plan_count: 1
  slug: zettle-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 6
  name: Zettle Rate Limits
  slug: zettle-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zettle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zettle-jsonschema-spectral-rules
scopes:
- name: Zettle Scopes
  scope_count: 1
  slug: zettle-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 61.2
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zettle/refs/heads/main/screenshots/zettle-2026-06-20T201853.png
security:
- kind: authentication
  name: Zettle Authentication
  slug: zettle-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zettle Domain Security
  slug: zettle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zettle
tags:
- Point-of-Sale
- POS
- Payments
- Inventory
- Finance
- PayPal
- Card Payments
- Merchant Services
website: https://www.zettle.com/
---
