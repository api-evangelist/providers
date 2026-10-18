---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Extend Agentic Access
  operation_count: 43
  slug: extend-agentic-access
  summary_line: 43 operations · 26 acting
api_count: 11
apis:
- description: 'Extend''s REST API for product and shipping protection: manage offers, contracts, orders and line items, refunds, claims, service orders, and leads. Header-based date versioning; OAuth2 client-credenti'
  name: Extend API
  slug: extend-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Claims Management API from Extend — 2 operation(s) for claims management.
  name: Extend Claims Management API
  slug: extend-claims-management-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Contracts API from Extend — 2 operation(s) for contracts.
  name: Extend Contracts API
  slug: extend-contracts-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Leads API from Extend — 3 operation(s) for leads.
  name: Extend Leads API
  slug: extend-leads-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Offers API from Extend — 1 operation(s) for offers.
  name: Extend Offers API
  slug: extend-offers-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Orders API from Extend — 13 operation(s) for orders.
  name: Extend Orders API
  slug: extend-orders-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Products API from Extend — 2 operation(s) for products.
  name: Extend Products API
  slug: extend-products-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Refunds API from Extend — 1 operation(s) for refunds.
  name: Extend Refunds API
  slug: extend-refunds-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Service Orders API from Extend — 10 operation(s) for service orders.
  name: Extend Service Orders API
  slug: extend-service-orders-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Dynamic Return Policy API from Extend — 1 operation(s) for dynamic return policy.
  name: Extend Dynamic Return Policy API
  slug: extend-dynamic-return-policy-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Line Items API from Extend — 7 operation(s) for line items.
  name: Extend Line Items API
  slug: extend-line-items-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The ShippingOffers API from Extend — 3 operation(s) for shippingoffers.
  name: Extend Shipping Offers API
  slug: extend-shippingoffers-api
- baseURL: https://api.helloextend.com
  baseurl_source: declared
  description: The Webhooks API from Extend — 1 operation(s) for webhooks.
  name: Extend Webhooks API
  slug: extend-webhooks-api
artifact_total: 18
asyncapis:
- description: ''
  name: Extend Webhooks
  slug: extend-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/agentic-access/extend-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/extend-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/rules/extend-rules.yml
  title: ''
  type: Spectral
  url: rules/extend-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/vocabulary/extend-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/extend-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/lifecycle/extend-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/extend-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/errors/extend-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/extend-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/hosts/extend-hosts.yml
  title: ''
  type: Hosts
  url: hosts/extend-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/vendors/extend-vendors.yml
  title: ''
  type: Vendors
  url: vendors/extend-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.extend.com/press
- group: company
  title: ''
  type: Website
  url: https://www.extend.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/security/extend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/extend-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.extend.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.extend.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.extend.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.extend.com/docs/getting-started-with-extends-api
- group: operate
  title: ''
  type: Support
  url: https://www.extend.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.extend.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helloextend
- group: start
  title: ''
  type: Login
  url: https://merchants.extend.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.extend.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.extend.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.extend.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.extend.com/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/authentication/extend-authentication.yml
  title: ''
  type: Authentication
  url: authentication/extend-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/conventions/extend-conventions.yml
  title: ''
  type: Conventions
  url: conventions/extend-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/conventions/extend-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/extend-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/llms/extend-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/extend-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/well-known/extend-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/extend-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/mcp/extend-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/extend-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/conformance/extend-conformance.yml
  title: ''
  type: Conformance
  url: conformance/extend-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/lifecycle/extend-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/extend-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/sandbox/extend-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/extend-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/asyncapi/extend-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/extend-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/data-model/extend-data-model.yml
  title: ''
  type: DataModel
  url: data-model/extend-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/components/extend-components.yml
  title: ''
  type: Components
  url: components/extend-components.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/packages/extend-packages.yml
  title: ''
  type: Packages
  url: packages/extend-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/packages/extend-packages.yml
  title: ''
  type: SDKs
  url: packages/extend-packages.yml
created: '2026-07-17'
description: Extend is a product and shipping protection platform for merchants and ecommerce brands. Its API lets merchants surface extended-warranty and shipping-protection offers at checkout and post-purchase, create and manage protection contracts, process orders and line items, file and track claims, and manage service orders, refunds, and leads. Extend provides separate demo (sandbox) and production environments, header-based date versioning, OAuth2 client-credentials authentication with short-lived access tokens, idempotency keys on writes, and webhooks for claim and service-order status changes, alongside client-side SDKs and prebuilt commerce-platform integrations for Shopify, BigCommerce, Magento, WooCommerce, and Salesforce Commerce Cloud.
image: https://avatars.githubusercontent.com/u/46018312?v=4
layout: provider
modified: '2026-07-19'
name: Extend
nav: Providers
network: true
overview: 'Extend publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Claims Management API, Contracts API, Leads API, and 10 more. Tagged areas include Company, Consumer, Product Protection, Extended Warranty, and Shipping Protection.


  The Extend catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Extend''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 29 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Extend API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: extend-rules
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.2
  facets:
    access_clarity: 27.6
    contract_governance: 35.6
    contract_quality: 55.0
    developer_ergonomics: 52.4
    discoverability: 80.4
    operational_transparency: 42.1
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/extend/refs/heads/main/screenshots/extend-2026-07-25T213943.png
security:
- kind: authentication
  name: Extend Authentication
  slug: extend-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Extend Domain Security
  slug: extend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: extend
tags:
- Company
- Consumer
- Product Protection
- Extended Warranty
- Shipping Protection
- E-Commerce
- Warranty
- Claims
- Contracts
- Retail
- Insurance
website: https://www.extend.com/
---
