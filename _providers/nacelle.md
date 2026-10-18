---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Nacelle Agentic Access
  operation_count: 55
  slug: nacelle-agentic-access
  summary_line: 55 operations · 51 acting
api_count: 4
apis:
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The `allProducts` query on Nacelle's Storefront GraphQL API returns normalized product entries (variants, pricing, media, metafields) drawn from ingested Shopify or other commerce sources, with Relay-
  name: Nacelle Storefront Products API
  slug: nacelle-storefront-products-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The `allProductCollections` query returns merchandised collections of products (the normalized equivalent of Shopify collections) with their member product references, for building category and listin
  name: Nacelle Storefront Product Collections API
  slug: nacelle-storefront-product-collections-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The `allContent` query returns CMS content entries (pages, articles, marketing blocks, media) ingested from sources such as Contentful, with a configurable entryDepth for resolving nested content refe
  name: Nacelle Storefront Content API
  slug: nacelle-storefront-content-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: 'The `navigation` and `spaceProperties` queries return a space''s navigation groups (menus) and space-level configuration (locales, currency, metadata) used to render a headless storefront''s chrome and '
  name: Nacelle Storefront Navigation and Spaces API
  slug: nacelle-storefront-navigation-spaces-api
- baseURL: https://admin.api.nacelle.com/graphql
  baseurl_source: declared
  description: The Admin GraphQL API triggers and monitors the indexing / ingestion pipeline that pulls data from connected sources (Shopify, CMS) into a space - starting or resetting index jobs for a data source, e
  name: Nacelle Admin Indexing and Ingestion API
  slug: nacelle-admin-indexing-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The addresses API from Nacelle — 1 operation(s) for addresses.
  name: Nacelle Addresses API
  slug: nacelle-addresses-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The checkout API from Nacelle — 2 operation(s) for checkout.
  name: Nacelle Checkout API
  slug: nacelle-checkout-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The credentials API from Nacelle — 4 operation(s) for credentials.
  name: Nacelle Credentials API
  slug: nacelle-credentials-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The customers API from Nacelle — 3 operation(s) for customers.
  name: Nacelle Customers API
  slug: nacelle-customers-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The entries (ALPHA) API from Nacelle — 3 operation(s) for entries (alpha).
  name: Nacelle entries (ALPHA) API
  slug: nacelle-entries-alpha-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The entries API from Nacelle — 7 operation(s) for entries.
  name: Nacelle Entries API
  slug: nacelle-entries-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: Entry operations
  name: Nacelle entries (BETA) API
  slug: nacelle-entries-beta-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The fulfillments API from Nacelle — 2 operation(s) for fulfillments.
  name: Nacelle Fulfillments API
  slug: nacelle-fulfillments-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The index API from Nacelle — 4 operation(s) for index.
  name: Nacelle Index API
  slug: nacelle-index-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The multiorders API from Nacelle — 3 operation(s) for multiorders.
  name: Nacelle Multiorders API
  slug: nacelle-multiorders-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The orderitems API from Nacelle — 1 operation(s) for orderitems.
  name: Nacelle Orderitems API
  slug: nacelle-orderitems-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The payment API from Nacelle — 1 operation(s) for payment.
  name: Nacelle Payment API
  slug: nacelle-payment-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The paymentintent API from Nacelle — 5 operation(s) for paymentintent.
  name: Nacelle Paymentintent API
  slug: nacelle-paymentintent-api
- baseURL: https://storefront.api.nacelle.com/graphql/v1/spaces
  baseurl_source: declared
  description: The token API from Nacelle — 2 operation(s) for token.
  name: Nacelle Token API
  slug: nacelle-token-api
artifact_total: 44
collections:
- collection_type: open
  name: Nacelle GraphQL API
  slug: open-nacelle
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/agentic-access/nacelle-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nacelle-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/rules/nacelle-rules.yml
  title: ''
  type: Spectral
  url: rules/nacelle-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/json-ld/nacelle-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nacelle-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/vocabulary/nacelle-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nacelle-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/data-model/nacelle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nacelle-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://nacelle.com/terms-and-conditions
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/security/nacelle-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/nacelle-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/errors/nacelle-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nacelle-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/llms/nacelle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nacelle-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/hosts/nacelle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nacelle-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/vendors/nacelle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nacelle-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.nacelle.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nacelle.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://nacelle.com/pricing/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/scopes/nacelle-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/nacelle-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/authentication/nacelle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nacelle-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/security/nacelle-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nacelle-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/security/nacelle-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nacelle-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/security/nacelle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nacelle-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getnacelle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nacelle
- group: company
  title: ''
  type: Website
  url: https://nacelle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nacelle.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/plans/nacelle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nacelle-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/rate-limits/nacelle-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nacelle-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/finops/nacelle-finops.yml
  title: ''
  type: FinOps
  url: finops/nacelle-finops.yml
created: '2026-07-01'
description: Nacelle is a headless / composable commerce data platform that ingests, normalizes, and indexes commerce and content data (Shopify, Contentful and other CMS sources) and serves it back to headless storefronts through a single, fast GraphQL Storefront API. The company has since pivoted toward an AI personalization engine, and the headless commerce Storefront API is now a legacy / maintenance-mode product rather than an actively expanding platform.
finops:
- has_sources: true
  method: generated
  name: Nacelle Finops
  primary_unit: ''
  service_category: Commerce and Content Infrastructure
  slug: nacelle-finops
  template: false
graphqls:
- description: Nacelle is a headless / composable commerce data platform. It ingests and normalizes
  name: Nacelle GraphQL APIs
  slug: nacelle-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nacelle.png
json_schemas:
- name: AddressCreate
  property_count: 13
  slug: nacelle-address-create
- name: CredentialsRequest represents the request to create a new credentials.
  property_count: 2
  slug: nacelle-credentials-request
- name: Credentials holds information about client credentials.
  property_count: 6
  slug: nacelle-credentials
- name: FulfillmentCreate represents the details of a fulfillment.
  property_count: 15
  slug: nacelle-fulfillment-create
- name: FulfillmentUpdate represents the details of a fulfillment.
  property_count: 15
  slug: nacelle-fulfillment-update
- name: PayloadJWT represents the request to create a new public token.
  property_count: 3
  slug: nacelle-issue-request
- name: JWTResponse represents the structure of a JWT token response.
  property_count: 2
  slug: nacelle-issue-response
- name: MultiOrderCheckout represents the details of a multi-order/multi-cart.
  property_count: 20
  slug: nacelle-multi-order-checkout
- name: OrderCheckout represents the details of an order/order-checkout.
  property_count: 26
  slug: nacelle-order-checkout
- name: OrderItemUpdate represents the details of an order item.
  property_count: 13
  slug: nacelle-order-item-update
- name: TokenRequest represents the request to create a new token.
  property_count: 4
  slug: nacelle-token-request
- name: Token represents the structure of an access token.
  property_count: 2
  slug: nacelle-token
jsonld:
- class_count: 50
  name: Nacelle Context
  property_count: 127
  slug: nacelle-context
layout: provider
modified: '2026-07-01'
name: Nacelle
nav: Providers
network: true
overview: 'Nacelle publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Storefront Products API, Storefront Product Collections API, Storefront Content API, and 16 more. Tagged areas include Commerce, Headless Commerce, Composable Commerce, GraphQL, and Content.


  The Nacelle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nacelle''s developer surface includes support, pricing, authentication, documentation, and 22 more developer resources.'
plans:
- name: Nacelle Plans Pricing
  plan_count: 1
  slug: nacelle-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Nacelle Rate Limits
  slug: nacelle-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Nacelle API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 2
  slug: nacelle-rules
scopes:
- name: Nacelle Scopes
  scope_count: 2
  slug: nacelle-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.8
    catalog_earned_first_party: 0.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.7
  facets:
    access_clarity: 31.6
    contract_governance: 17.4
    contract_quality: 66.0
    developer_ergonomics: 32.9
    discoverability: 78.6
    operational_transparency: 36.8
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/nacelle/refs/heads/main/screenshots/nacelle-2026-08-07T184601.png
security:
- kind: authentication
  name: Nacelle Authentication
  slug: nacelle-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nacelle Domain Security
  slug: nacelle-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Nacelle Vulnerability Disclosure
  slug: nacelle-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Nacelle Trust Center
  slug: nacelle-trust-center
  summary_line: SOC 2, GDPR
slug: nacelle
tags:
- Commerce
- Headless Commerce
- Composable Commerce
- GraphQL
- Content
- Data Indexing
website: https://nacelle.com/
---
