---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Topi Agentic Access
  operation_count: 31
  slug: topi-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 1
apis:
- baseURL: https://seller-api.topi.eu
  baseurl_source: declared
  description: Topi catalog for sellers
  name: Topi Catalog API
  slug: topi-catalog-api
- baseURL: https://seller-api.topi.eu
  baseurl_source: declared
  description: 'Provides operations to handle offers for end-customers. ## Webhooks ### OfferUpdates We will ping the URL provided whenever an offer has changed its status to: `"accepted"`, `"declined"`, `"voided"`, '
  name: Topi Offer API
  slug: topi-offer-api
- baseURL: https://seller-api.topi.eu
  baseurl_source: declared
  description: 'Provides operations to handle orders for end-customers. ## Webhooks We will ping the URL provided whenever an order has changed its status to: `"created"`, `"completed"`, or `"canceled"`. **Payload**:'
  name: Topi Order API
  slug: topi-order-api
- baseURL: https://seller-api.topi.eu
  baseurl_source: declared
  description: '#### Assets without serial numbers Some assets might not have a serial number (e.g. accessories). In order to send them with the shipment, explicitly pass an empty string `""` as the `serial_number` f'
  name: Topi Shipment API
  slug: topi-shipment-api
- baseURL: https://seller-api.topi.eu
  baseurl_source: declared
  description: Provides operations to handle shipping-related tasks.
  name: Topi Shipping Method API
  slug: topi-shipping-method-api
artifact_total: 19
asyncapis:
- description: ''
  name: Topi Webhooks
  slug: topi-webhooks
collections:
- collection_type: open
  name: topi Seller catalog API
  slug: open-topi-catalog-api
- collection_type: open
  name: topi Seller catalog offer API
  slug: open-topi-offer-api
- collection_type: open
  name: topi Seller catalog order API
  slug: open-topi-order-api
- collection_type: open
  name: topi Seller catalog shipment API
  slug: open-topi-shipment-api
- collection_type: open
  name: topi Seller catalog shippingMethod API
  slug: open-topi-shippingmethod-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.topi.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.topi.eu/docs/get-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.topi.eu/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.topi.eu/docs/get-started/introduction
- group: operate
  title: ''
  type: Support
  url: https://www.topi.eu/en/faqs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.topi.eu/en/privacy-policy
- group: docs
  href: https://artifacts.apis.io/topi/openapi/_original/topi-seller-api-openapi-original.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/topi-seller-api-openapi-original.yaml
- group: auth
  href: https://artifacts.apis.io/topi/authentication/topi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/topi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/topi/scopes/topi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/topi-scopes.yml
- group: agent
  href: https://artifacts.apis.io/topi/agentic-access/topi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/topi-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/topi/security/topi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/topi-domain-security.yml
- group: design
  href: https://artifacts.apis.io/topi/errors/topi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/topi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/topi/conventions/topi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/topi-conventions.yml
- group: design
  href: https://artifacts.apis.io/topi/lifecycle/topi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/topi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/topi/conformance/topi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/topi-conformance.yml
- group: design
  href: https://artifacts.apis.io/topi/data-model/topi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/topi-data-model.yml
- group: start
  href: https://artifacts.apis.io/topi/sandbox/topi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/topi-sandbox.yml
- group: design
  href: https://artifacts.apis.io/topi/components/topi-components.yml
  title: ''
  type: Components
  url: components/topi-components.yml
- group: design
  href: https://artifacts.apis.io/topi/asyncapi/topi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/topi-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/topi/mcp/topi-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/topi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/topi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/topi/llms/topi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/topi-llms.txt
- group: other
  href: https://artifacts.apis.io/topi/overlays/topi-seller-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/topi-seller-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.topi.eu/en/
created: '2026-07-17'
description: topi is a European hardware-as-a-service (HaaS) fintech that lets B2B sellers and retailers offer tech devices, IT hardware, and equipment as flexible monthly rental subscriptions instead of one-off purchases, across eCommerce, telesales, and point-of-sale channels. Merchants embed topi rentals into their checkout through the OAuth2-secured topi Seller API (catalog, offers, orders, shipments, and shipping methods) and the topi Elements embeddable web components, with a dedicated sandbox for end-to-end testing. Backed by Creandum.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/topi.png
layout: provider
modified: '2026-07-21'
name: Topi
nav: Providers
network: true
overview: 'Topi publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Offer API, Order API, and 2 more. Tagged areas include Company, Fintech, Hardware as a Service, Rentals, and Embedded Finance.


  The Topi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Topi''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Topi API Rules
  rule_count: 65
  severity_counts:
    error: 53
    hint: 0
    info: 4
    warn: 8
  slug: topi-rules
scopes:
- name: Topi Scopes
  scope_count: 13
  slug: topi-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 58.7
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/topi/topi-2026-08-17T082405.png
security:
- kind: authentication
  name: Topi Authentication
  slug: topi-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Topi Domain Security
  slug: topi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create and manage a rental offer
  slug: topi-create-rental-offer
- name: Accept and fulfill a topi order
  slug: topi-fulfill-order
- name: Sync a product catalog to topi
  slug: topi-sync-catalog
slug: topi
tags:
- Company
- Fintech
- Hardware as a Service
- Rentals
- Embedded Finance
- B2B Payments
- Financing
- Checkout
- Germany
website: https://www.topi.eu/en/
---
