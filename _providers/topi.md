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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Topi Agentic Access
  operation_count: 31
  slug: topi-agentic-access
  summary_line: 31 operations · 20 acting
api_count: 1
apis:
- description: Topi catalog for sellers
  name: Topi catalog API
  slug: topi-catalog-api
- description: 'Provides operations to handle offers for end-customers. ## Webhooks ### OfferUpdates We will ping the URL provided whenever an offer has changed its status to: `"accepted"`, `"declined"`, `"voided"`, '
  name: Topi offer API
  slug: topi-offer-api
- description: 'Provides operations to handle orders for end-customers. ## Webhooks We will ping the URL provided whenever an order has changed its status to: `"created"`, `"completed"`, or `"canceled"`. **Payload**:'
  name: Topi order API
  slug: topi-order-api
- description: '#### Assets without serial numbers Some assets might not have a serial number (e.g. accessories). In order to send them with the shipment, explicitly pass an empty string `""` as the `serial_number` f'
  name: Topi shipment API
  slug: topi-shipment-api
- description: Provides operations to handle shipping-related tasks.
  name: Topi shippingMethod API
  slug: topi-shippingmethod-api
artifact_total: 17
asyncapis:
- description: ''
  name: Topi Webhooks
  slug: topi-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: OpenAPI
  url: openapi/_original/topi-seller-api-openapi-original.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/topi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/topi-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/topi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/topi-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/topi-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/topi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/topi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/topi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/topi-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/topi-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/topi-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/topi-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/topi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/topi-llms.txt
- group: other
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
mcp_servers:
- description: ''
  name: Topi MCP Server
  slug: topi-mcp-server
modified: '2026-07-21'
name: Topi
nav: Providers
network: true
overview: 'Topi publishes 5 APIs on the [APIs.io](https://apis.io/) network, including catalog API, offer API, order API, and 2 more. Tagged areas include Company, Fintech, Hardware as a Service, Rentals, and Embedded Finance.


  The Topi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Topi''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 3
scopes:
- name: Topi Scopes
  scope_count: 13
  slug: topi-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 66.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 42.9
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
    score: 48.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/topi/refs/heads/main/screenshots/topi-2026-08-17T082405.png
security:
- kind: authentication
  name: Topi Authentication
  slug: topi-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Topi Domain Security
  slug: topi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
