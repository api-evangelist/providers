---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.scalapay.com
  baseurl_source: declared
  description: The Instore API from Scalapay — 6 operation(s) for instore.
  name: Scalapay Instore API
  slug: scalapay-instore-api
- baseURL: https://api.scalapay.com
  baseurl_source: declared
  description: The Orders API from Scalapay — 8 operation(s) for orders.
  name: Scalapay Orders API
  slug: scalapay-orders-api
- baseURL: https://api.scalapay.com
  baseurl_source: declared
  description: The Reporting API from Scalapay — 6 operation(s) for reporting.
  name: Scalapay Reporting API
  slug: scalapay-reporting-api
artifact_total: 10
asyncapis:
- description: ''
  name: Scalapay Webhooks
  slug: scalapay-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scalapay Instore API
  slug: open-scalapay-instore-api
- collection_type: open
  name: Scalapay Orders API
  slug: open-scalapay-orders-api
- collection_type: open
  name: Scalapay Reporting API
  slug: open-scalapay-reporting-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/scalapay-capability-edges.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/scalapay-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/scalapay-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.scalapay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.scalapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.scalapay.com/docs/get-started-with-scalapay
- group: docs
  title: ''
  type: APIReference
  url: https://developers.scalapay.com/reference/api-architecture
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.scalapay.com/docs/get-started-with-scalapay
- group: operate
  title: ''
  type: Support
  url: https://help.scalapay.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://merchant-help.scalapay.com/
- group: start
  title: ''
  type: SignUp
  url: https://portal.scalapay.com/signup
- group: start
  title: ''
  type: Login
  url: https://partner.scalapay.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scalapay.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scalapay.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.scalapay.com/legals
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scalapay.com/
- group: build
  title: ''
  type: SourceCode
  url: https://bitbucket.org/scalapay
- group: auth
  title: ''
  type: Authentication
  url: authentication/scalapay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scalapay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/scalapay-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/scalapay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/scalapay-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/scalapay-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/scalapay-components.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scalapay-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/scalapay-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scalapay-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/scalapay-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scalapay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scalapay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/scalapay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scalapay-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scalapay-domain-security.yml
created: '2026-08-02'
description: 'Scalapay is an Italian buy-now-pay-later (BNPL) payment provider that lets shoppers split a purchase into instalments — pay in 3, pay in 4, or pay later — while the merchant is settled by Scalapay. Its REST API is a compact, order-centric surface: create an instalment order, redirect the shopper to Scalapay Checkout, then capture, delay, void or refund against the order token, with a parallel in-store and offline pay-by-link family authenticated by a device-scoped key, plus reporting endpoints for reconciling orders, refunds, payouts and disputes against Scalapay''s bank transfers. Merchants integrate through a CDN-loaded web component (the Scalapay Suite Widget) on the product, cart and checkout pages, or through prebuilt modules for Magento, WooCommerce, PrestaShop, Shopify, Shopware, BigCommerce, VTEX, Salesforce and others. Scalapay operates in EUR across 14 authorised European territories.'
image: https://cdn.prod.website-files.com/614b9948e0cc06785c60efe7/67c9cc48ae95dd9c93be62c3_favicon-256.png
layout: provider
modified: '2026-08-02'
name: Scalapay
nav: Providers
network: true
overview: 'Scalapay publishes 3 APIs on the [APIs.io](https://apis.io/) network: Instore API, Orders API, and Reporting API. Tagged areas include Payments, Buy Now Pay Later, BNPL, Instalments, and E-Commerce.


  The Scalapay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scalapay''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 27 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 61.1
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 48.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scalapay/refs/heads/main/screenshots/scalapay-2026-08-17T081726.png
security:
- kind: authentication
  name: Scalapay Authentication
  slug: scalapay-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Scalapay Domain Security
  slug: scalapay-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: scalapay
tags:
- Payments
- Buy Now Pay Later
- BNPL
- Instalments
- E-Commerce
- Checkout
- Financial-Services
- Point-of-Sale
- Reconciliation
- Europe
- Company
website: https://www.scalapay.com/
---
