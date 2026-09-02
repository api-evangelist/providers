---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Cart API from Passport — 1 operation(s) for cart.
  name: Passport Cart API
  slug: passport-cart-api
- description: The Healthcheck API from Passport — 1 operation(s) for healthcheck.
  name: Passport Healthcheck API
  slug: passport-healthcheck-api
- description: The Order API from Passport — 1 operation(s) for order.
  name: Passport Order API
  slug: passport-order-api
- description: The Product Price API from Passport — 1 operation(s) for product price.
  name: Passport Product Price API
  slug: passport-product-price-api
- description: The Rate API from Passport — 1 operation(s) for rate.
  name: Passport Rate API
  slug: passport-rate-api
- description: The Ship API from Passport — 1 operation(s) for ship.
  name: Passport Ship API
  slug: passport-ship-api
- description: The Tax And Duty API from Passport — 1 operation(s) for tax and duty.
  name: Passport Tax And Duty API
  slug: passport-tax-and-duty-api
- description: The Void API from Passport — 1 operation(s) for void.
  name: Passport Void API
  slug: passport-void-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Getting Started with Passport Global Cart API
  slug: open-passport-cart-api
- collection_type: open
  name: Getting Started with Passport Global Healthcheck API
  slug: open-passport-healthcheck-api
- collection_type: open
  name: Getting Started with Passport Global Order API
  slug: open-passport-order-api
- collection_type: open
  name: Getting Started with Passport Global Product Price API
  slug: open-passport-product-price-api
- collection_type: open
  name: Getting Started with Passport Global Rate API
  slug: open-passport-rate-api
- collection_type: open
  name: Getting Started with Passport Global Ship API
  slug: open-passport-ship-api
- collection_type: open
  name: Getting Started with Passport Global Tax And Duty API
  slug: open-passport-tax-and-duty-api
- collection_type: open
  name: Getting Started with Passport Global Void API
  slug: open-passport-void-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/passport-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://passportglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.passportglobal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.passportglobal.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.passportglobal.com/
- group: operate
  title: ''
  type: Support
  url: https://passportglobal.com/contact-sales/
- group: company
  title: ''
  type: Blog
  url: https://passportglobal.com/news-and-articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://passportglobal.com/feed/
- group: start
  title: ''
  type: Login
  url: https://portal.passportglobal.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://passportglobal.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://passportglobal.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://passportglobal.com/gdpr/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.passportglobal.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/passport-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/passport-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/passport-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/passport-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/passport-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/passport-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/passport-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/passport-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/passport-public-api-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/passport-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/passport-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/passport-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/passport-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: Passport (Passport Global, Inc.) is a cross-border ecommerce logistics and compliance platform founded in 2017 that helps direct-to-consumer brands sell and ship internationally to 190+ markets. The company combines its own international parcel network (Passport Shipping) with in-country enablement, marketplace management, trade and fiscal compliance, seller/merchant-of-record services, duty drawback, and returns. Its public REST API — the Passport Global API, currently version 3.15 — exposes landed-cost rating, shipping label generation and voiding, order submission and management, cart-level duty and tax quoting, currency-converted product pricing, and a tax-and-duty calculator, authenticated with an X-Access-Token API key issued by the Passport onboarding team.
image: https://passportglobal.com/wp-content/uploads/2024/12/passport-international-shipping-compliance-localization.png
layout: provider
mcp_servers:
- description: ''
  name: Passport MCP Server
  slug: passport-mcp-server
modified: '2026-08-04'
name: Passport
nav: Providers
network: true
overview: 'Passport publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Healthcheck API, Order API, and 5 more. Tagged areas include Company, Shipping, Logistics, Cross-border eCommerce, and International Shipping.


  Passport''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 21 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 44.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passport/refs/heads/main/screenshots/passport-2026-08-07T191541.png
security:
- kind: authentication
  name: Passport Authentication
  slug: passport-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Passport Domain Security
  slug: passport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: passport
tags:
- Company
- Shipping
- Logistics
- Cross-border eCommerce
- International Shipping
- Customs Compliance
- Landed Cost
- duties-and-taxes
- Parcel Delivery
- E-Commerce
- Merchant of Record
- Trade Compliance
website: https://passportglobal.com/
---
