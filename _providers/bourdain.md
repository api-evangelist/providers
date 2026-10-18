---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-17'
api_count: 6
apis:
- baseURL: https://bourdain.io
  baseurl_source: spec
  description: The Acp Checkout API from Bourdain — 1 operation(s) for acp checkout.
  name: Bourdain Acp Checkout API
  slug: bourdain-acp-checkout-api
- baseURL: https://bourdain.io
  baseurl_source: spec
  description: The Acp Confirm API from Bourdain — 1 operation(s) for acp confirm.
  name: Bourdain Acp Confirm API
  slug: bourdain-acp-confirm-api
- baseURL: https://bourdain.io
  baseurl_source: spec
  description: The Acp Payment API from Bourdain — 1 operation(s) for acp payment.
  name: Bourdain Acp Payment API
  slug: bourdain-acp-payment-api
- baseURL: https://bourdain.io
  baseurl_source: spec
  description: The Acp Product API from Bourdain — 1 operation(s) for acp product.
  name: Bourdain Acp Product API
  slug: bourdain-acp-product-api
- baseURL: https://bourdain.io
  baseurl_source: spec
  description: The Acp Products API from Bourdain — 1 operation(s) for acp products.
  name: Bourdain Acp Products API
  slug: bourdain-acp-products-api
- baseURL: https://bourdain.io
  baseurl_source: spec
  description: The Mcp Server API from Bourdain — 1 operation(s) for mcp server.
  name: Bourdain Mcp Server API
  slug: bourdain-mcp-server-api
artifact_total: 18
asyncapis:
- description: ''
  name: Bourdain Webhooks
  slug: bourdain-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/rate-limits/bourdain-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bourdain-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/rules/bourdain-rules.yml
  title: ''
  type: Spectral
  url: rules/bourdain-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/json-ld/bourdain-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bourdain-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/vocabulary/bourdain-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bourdain-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/asyncapi/bourdain-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bourdain-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/data-model/bourdain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bourdain-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/authentication/bourdain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bourdain-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/conformance/bourdain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bourdain-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/llms/bourdain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bourdain-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/hosts/bourdain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bourdain-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/vendors/bourdain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bourdain-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bourdain/refs/heads/main/security/bourdain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bourdain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bourdain.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bourdain.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.bourdain.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bourdain.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.bourdain.io/help
- group: company
  title: ''
  type: Blog
  url: https://www.bourdain.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bourdain.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bourdain.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bourdain.io/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://www.bourdain.io/roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bourdain.io/status
coverage:
  checked: '2026-10-16'
  detail: API documentation is HTML with no machine‑readable OpenAPI/GraphQL/AsyncAPI spec available.
  evidence:
  - status: 200
    url: https://www.bourdain.io/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Bourdain operates an agentic trading card marketplace that enables users to browse, buy, sell, and price trading cards such as Pokémon and One Piece. The platform offers AI‑driven search and filtering, seller analytics, and a roadmap for future features. It provides a modern web interface with pricing, terms, privacy, and support pages, aiming to bring confidence to card collectors and traders.
image: https://bourdain.io/og-image.png
json_schemas:
- name: GetAcpProductIdResponse
  property_count: 2
  slug: bourdain-get-acp-product-id-response
- name: GetAcpProductsResponse
  property_count: 5
  slug: bourdain-get-acp-products-response
- name: PostAcpCheckoutRequest
  property_count: 3
  slug: bourdain-post-acp-checkout-request
- name: PostAcpCheckoutResponse
  property_count: 3
  slug: bourdain-post-acp-checkout-response
- name: PostAcpPaymentRequest
  property_count: 3
  slug: bourdain-post-acp-payment-request
- name: PostMcpServerRequest
  property_count: 4
  slug: bourdain-post-mcp-server-request
jsonld:
- class_count: 9
  name: Bourdain Context
  property_count: 19
  slug: bourdain-context
layout: provider
modified: '2026-10-16'
name: Bourdain
nav: Providers
network: true
overview: 'Bourdain is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Acp Checkout API, Acp Confirm API, Acp Payment API, and 3 more. Tagged areas include Company, Marketplace, Trading Cards, Artificial Intelligence, and E-Commerce.


  The Bourdain catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bourdain''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 10
  name: Bourdain Rate Limits
  slug: bourdain-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Bourdain API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: bourdain-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 33.4
    developer_ergonomics: 47.6
    discoverability: 69.6
    operational_transparency: 60.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bourdain Authentication
  slug: bourdain-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bourdain Domain Security
  slug: bourdain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bourdain
tags:
- Company
- Marketplace
- Trading Cards
- Artificial Intelligence
- E-Commerce
- Collectibles
website: https://bourdain.io/
---
