---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - '{''url'': ''https://www.becn.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.qxo.com/. RESOLVED 2026-09-04: this is an acquisition, not a stale domain — QXO, Inc. completed its acquisition of Beacon Roofing Supply on 2025-04-29 and folded the PRO+ web app into qxo.com. The API host did NOT move: https://beaconproplus.com/swagger/ and the /v1|/v2|/v3 REST bases still serve from the Beacon domain.''}'
  - '{''url'': ''https://go.qxo.com/qxoapi'', ''status'': 200, ''note'': ''API access is sales-gated: requester must already be a QXO customer and accept the API licence terms. No self-serve signup, no published price.''}'
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-09-16'
api_count: 21
apis:
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Add Multiple Items To Order API from Beacon Roofing Supply — 1 operation(s) for add multiple items to order.
  name: Beacon Roofing Supply Add Multiple Items To Order API
  slug: beacon-roofing-supply-add-multiple-items-to-order-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Beacon Stack (BASE URL:- https://beacon-api-x7xzzdp35a-uk.a.run.app) API from Beacon Roofing Supply — 2 operation(s) for beacon stack (base url:- https://beacon-api-x7xzzdp35a-uk.a.run.app).
  name: Beacon Roofing Supply Beacon Stack (BASE URL:- https://beacon-api-x7xzzdp35a-uk.a.run.app) API
  slug: beacon-roofing-supply-beacon-stack-base-url-https-beacon-api-x7xzzdp35a-uk-a-run-app-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Bill Trust Services API from Beacon Roofing Supply — 1 operation(s) for bill trust services.
  name: Beacon Roofing Supply Bill Trust Services API
  slug: beacon-roofing-supply-bill-trust-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Catalog ITEM Services API from Beacon Roofing Supply — 27 operation(s) for catalog item services.
  name: Beacon Roofing Supply Catalog ITEM Services API
  slug: beacon-roofing-supply-catalog-item-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Checkout API from Beacon Roofing Supply — 14 operation(s) for checkout.
  name: Beacon Roofing Supply Checkout API
  slug: beacon-roofing-supply-checkout-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Customer Services API from Beacon Roofing Supply — 4 operation(s) for customer services.
  name: Beacon Roofing Supply Customer Services API
  slug: beacon-roofing-supply-customer-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Delivery Tracking Service API from Beacon Roofing Supply — 9 operation(s) for delivery tracking service.
  name: Beacon Roofing Supply Delivery Tracking Service API
  slug: beacon-roofing-supply-delivery-tracking-service-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Eagle View Order API from Beacon Roofing Supply — 11 operation(s) for eagle view order.
  name: Beacon Roofing Supply Eagle View Order API
  slug: beacon-roofing-supply-eagle-view-order-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Eagle View Reports API from Beacon Roofing Supply — 3 operation(s) for eagle view reports.
  name: Beacon Roofing Supply Eagle View Reports API
  slug: beacon-roofing-supply-eagle-view-reports-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The EV Measurement to Order API from Beacon Roofing Supply — 12 operation(s) for ev measurement to order.
  name: Beacon Roofing Supply EV Measurement to Order API
  slug: beacon-roofing-supply-ev-measurement-to-order-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Favorites Services API from Beacon Roofing Supply — 4 operation(s) for favorites services.
  name: Beacon Roofing Supply Favorites Services API
  slug: beacon-roofing-supply-favorites-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The GAF Quick Measure Services API from Beacon Roofing Supply — 3 operation(s) for gaf quick measure services.
  name: Beacon Roofing Supply GAF Quick Measure Services API
  slug: beacon-roofing-supply-gaf-quick-measure-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Health Check API from Beacon Roofing Supply — 1 operation(s) for health check.
  name: Beacon Roofing Supply Health Check API
  slug: beacon-roofing-supply-health-check-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Hover Job Services API from Beacon Roofing Supply — 4 operation(s) for hover job services.
  name: Beacon Roofing Supply Hover Job Services API
  slug: beacon-roofing-supply-hover-job-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The IDP Token Services API from Beacon Roofing Supply — 1 operation(s) for idp token services.
  name: Beacon Roofing Supply IDP Token Services API
  slug: beacon-roofing-supply-idp-token-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Integration Services API from Beacon Roofing Supply — 1 operation(s) for integration services.
  name: Beacon Roofing Supply Integration Services API
  slug: beacon-roofing-supply-integration-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Integrations - Development API from Beacon Roofing Supply — 2 operation(s) for integrations - development.
  name: Beacon Roofing Supply Integrations - Development API
  slug: beacon-roofing-supply-integrations-development-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Invoiced Services API from Beacon Roofing Supply — 1 operation(s) for invoiced services.
  name: Beacon Roofing Supply Invoiced Services API
  slug: beacon-roofing-supply-invoiced-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Job Service API from Beacon Roofing Supply — 2 operation(s) for job service.
  name: Beacon Roofing Supply Job Service API
  slug: beacon-roofing-supply-job-service-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Journal Services API from Beacon Roofing Supply — 5 operation(s) for journal services.
  name: Beacon Roofing Supply Journal Services API
  slug: beacon-roofing-supply-journal-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Loyal Reward Services API from Beacon Roofing Supply — 1 operation(s) for loyal reward services.
  name: Beacon Roofing Supply Loyal Reward Services API
  slug: beacon-roofing-supply-loyal-reward-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The My Account Services API from Beacon Roofing Supply — 37 operation(s) for my account services.
  name: Beacon Roofing Supply My Account Services API
  slug: beacon-roofing-supply-my-account-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The OAuth Service API from Beacon Roofing Supply — 1 operation(s) for oauth service.
  name: Beacon Roofing Supply OAuth Service API
  slug: beacon-roofing-supply-oauth-service-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Order History Services API from Beacon Roofing Supply — 6 operation(s) for order history services.
  name: Beacon Roofing Supply Order History Services API
  slug: beacon-roofing-supply-order-history-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Perfect Order Services API from Beacon Roofing Supply — 4 operation(s) for perfect order services.
  name: Beacon Roofing Supply Perfect Order Services API
  slug: beacon-roofing-supply-perfect-order-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Pricing Services API from Beacon Roofing Supply — 2 operation(s) for pricing services.
  name: Beacon Roofing Supply Pricing Services API
  slug: beacon-roofing-supply-pricing-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Quote Order Services API from Beacon Roofing Supply — 8 operation(s) for quote order services.
  name: Beacon Roofing Supply Quote Order Services API
  slug: beacon-roofing-supply-quote-order-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Quote Services API from Beacon Roofing Supply — 13 operation(s) for quote services.
  name: Beacon Roofing Supply Quote Services API
  slug: beacon-roofing-supply-quote-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Rebate Services API from Beacon Roofing Supply — 10 operation(s) for rebate services.
  name: Beacon Roofing Supply Rebate Services API
  slug: beacon-roofing-supply-rebate-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Sales Order Hold Services API from Beacon Roofing Supply — 2 operation(s) for sales order hold services.
  name: Beacon Roofing Supply Sales Order Hold Services API
  slug: beacon-roofing-supply-sales-order-hold-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Saved Order Services API from Beacon Roofing Supply — 16 operation(s) for saved order services.
  name: Beacon Roofing Supply Saved Order Services API
  slug: beacon-roofing-supply-saved-order-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The SMS Services API from Beacon Roofing Supply — 1 operation(s) for sms services.
  name: Beacon Roofing Supply SMS Services API
  slug: beacon-roofing-supply-sms-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Submit Order Services API from Beacon Roofing Supply — 1 operation(s) for submit order services.
  name: Beacon Roofing Supply Submit Order Services API
  slug: beacon-roofing-supply-submit-order-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Suggestive Selling API from Beacon Roofing Supply — 1 operation(s) for suggestive selling.
  name: Beacon Roofing Supply Suggestive Selling API
  slug: beacon-roofing-supply-suggestive-selling-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The Template Services API from Beacon Roofing Supply — 11 operation(s) for template services.
  name: Beacon Roofing Supply Template Services API
  slug: beacon-roofing-supply-template-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The User Register Services API from Beacon Roofing Supply — 4 operation(s) for user register services.
  name: Beacon Roofing Supply User Register Services API
  slug: beacon-roofing-supply-user-register-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The User Tour Services API from Beacon Roofing Supply — 2 operation(s) for user tour services.
  name: Beacon Roofing Supply User Tour Services API
  slug: beacon-roofing-supply-user-tour-services-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The V1 API from Beacon Roofing Supply — 10 operation(s) for v1.
  name: Beacon Roofing Supply V1 API
  slug: beacon-roofing-supply-v1-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The V2 API from Beacon Roofing Supply — 126 operation(s) for v2.
  name: Beacon Roofing Supply V2 API
  slug: beacon-roofing-supply-v2-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The V3 API from Beacon Roofing Supply — 4 operation(s) for v3.
  name: Beacon Roofing Supply V3 API
  slug: beacon-roofing-supply-v3-api
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: The V4 API from Beacon Roofing Supply — 1 operation(s) for v4.
  name: Beacon Roofing Supply V4 API
  slug: beacon-roofing-supply-v4-api
artifact_total: 61
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/overlays/beacon-roofing-supply-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beacon-roofing-supply-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/overlays/beacon-roofing-supply-all-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beacon-roofing-supply-all-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/overlays/beacon-roofing-supply-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beacon-roofing-supply-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/overlays/beacon-roofing-supply-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beacon-roofing-supply-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/overlays/beacon-roofing-supply-oauth2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beacon-roofing-supply-oauth2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/overlays/beacon-roofing-supply-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beacon-roofing-supply-public-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/overlays/beacon-roofing-supply-internal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beacon-roofing-supply-internal-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/authentication/beacon-roofing-supply-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beacon-roofing-supply-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/security/beacon-roofing-supply-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beacon-roofing-supply-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beacon-building-products
- group: company
  title: ''
  type: Website
  url: https://www.becn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qxo.com/customapi
- group: docs
  title: ''
  type: Documentation
  url: https://beaconproplus.com/swagger/
- group: docs
  title: ''
  type: APIReference
  url: https://beaconproplus.com/swagger/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://go.qxo.com/qxoapi
- group: start
  title: ''
  type: SignUp
  url: https://www.qxo.com/open-an-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qxo.com/integrations/api-license-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qxo.com/privacy-policy-and-cookie-notice
- group: operate
  title: ''
  type: Support
  url: https://www.qxo.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.qxo.com/qxo-blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://beaconproplus.com/swagger/dev/index.html
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/changelog/beacon-roofing-supply-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beacon-roofing-supply-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/scopes/beacon-roofing-supply-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/beacon-roofing-supply-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/conventions/beacon-roofing-supply-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beacon-roofing-supply-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/errors/beacon-roofing-supply-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beacon-roofing-supply-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/errors/beacon-roofing-supply-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/beacon-roofing-supply-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/lifecycle/beacon-roofing-supply-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/beacon-roofing-supply-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/lifecycle/beacon-roofing-supply-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/beacon-roofing-supply-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/conformance/beacon-roofing-supply-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beacon-roofing-supply-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/data-model/beacon-roofing-supply-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beacon-roofing-supply-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/packages/beacon-roofing-supply-packages.yml
  title: ''
  type: Packages
  url: packages/beacon-roofing-supply-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/llms/beacon-roofing-supply-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beacon-roofing-supply-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/plans/beacon-roofing-supply-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beacon-roofing-supply-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/rate-limits/beacon-roofing-supply-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/beacon-roofing-supply-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/finops/beacon-roofing-supply-finops.yml
  title: ''
  type: FinOps
  url: finops/beacon-roofing-supply-finops.yml
created: '2026-03-23'
description: 'Beacon Roofing Supply (formerly NASDAQ: BECN) is one of the largest distributors of residential and non-residential roofing materials and complementary building products in North America, operating roughly 600 branches. QXO, Inc. completed its acquisition of Beacon on 2025-04-29 and the business now trades under the QXO brand. Its contractor commerce platform, Beacon PRO+, publishes an unusually complete REST surface: eleven OpenAPI 3.0 documents totalling 424 operations, indexed at https://beaconproplus.com/swagger/ and covering catalog search, account-specific real-time pricing, branch availability, cart and order submission, quotes and approval workflows, order history, delivery tracking, invoices, manufacturer rebates, permission management and the EagleView, GAF QuickMeasure and Hover measurement integrations, plus an OAuth 2.0 token service and a change log covering 72 releases. Access is sales-gated at https://www.qxo.com/customapi; contracts are public.'
features:
- description: Access live product inventory levels and pricing across Beacon locations for accurate contractor quoting.
  name: Real-Time Inventory and Pricing
- description: Place, manage, and track roofing material orders programmatically through the Beacon PRO+ API.
  name: Online Ordering
- description: Real-time delivery status updates and tracking for all Beacon material orders.
  name: Delivery Tracking
- description: Manage contractor account details, billing, and payment information through the API.
  name: Account Management
- description: Receive storm event notifications to proactively reach out to customers in affected areas.
  name: Storm Tracking Alerts
- description: Track manufacturer rebate programs and earned rebates through the API.
  name: Rebate Tracking
finops:
- name: Beacon Roofing Supply Finops
  service_category: Construction Distribution / E-Commerce APIs
  slug: beacon-roofing-supply-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beacon-roofing-supply.png
integrations:
- description: Roofing contractor management software with native Beacon PRO+ integration for material ordering.
  name: AccuLynx
- description: Contractor CRM and project management platform with Beacon PRO+ material order integration.
  name: JobNimbus
- description: Roofing manufacturer partnership enabling GAF product ordering through Beacon PRO+ e-commerce.
  name: GAF
- description: EDI integration service enabling electronic purchase orders, ASNs, and invoices with Beacon Roofing Supply.
  name: TrueCommerce EDI
layout: provider
modified: '2026-09-04'
name: Beacon Roofing Supply
nav: Providers
network: true
overview: 'Beacon Roofing Supply publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Add Multiple Items To Order API, Beacon Stack (BASE URL:- https://beacon-api-x7xzzdp35a-uk.a.run.app) API, Bill Trust Services API, and 38 more. Tagged areas include Construction, Distribution, Roofing, Building Materials, and E-Commerce.


  Beacon Roofing Supply''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 29 more developer resources.'
plans:
- name: Beacon Roofing Supply Plans Pricing
  plan_count: 0
  slug: beacon-roofing-supply-plans-pricing
press:
- date: '2026-05-25'
  title: QXO completes the acquisition of Beacon Roofing Supply ...
  url: https://news.mergerlinks.com/daily-review/qxo-completes-the-acquisition-of-beacon-roofing-supply-for-$-11bn
- date: '2026-05-25'
  title: BEACON ROOFING SUPPLY, INC. QUEEN MERGERCO, INC ...
  url: https://d18rn0p25nwr6d.cloudfront.net/CIK-0001124941/30855609-2f78-44b5-a21b-d4113cd5aee5.pdf
- date: '2026-05-25'
  title: 'In case you missed it: From private label roofing products ...'
  url: https://www.facebook.com/RoofingContractor/posts/in-case-you-missed-it-from-private-label-roofing-products-%EF%B8%8F-to-ai-powered-logist/1405757331590241/
- date: '2026-05-25'
  title: How QXO is Using AI to Streamline Distribution
  url: https://www.roofingcontractor.com/articles/101320-how-qxo-is-using-ai-to-streamline-distribution
- date: '2026-05-25'
  title: QXO launches $11 billion tender offer for Beacon Roofing ...
  url: https://www.investing.com/news/company-news/qxo-launches-11-billion-tender-offer-for-beacon-roofing-supply-93CH-3831708
random_paper: 13
rate_limits:
- limit_count: 0
  name: Beacon Roofing Supply Rate Limits
  slug: beacon-roofing-supply-rate-limits
scopes:
- name: Beacon Roofing Supply Scopes
  scope_count: 0
  slug: beacon-roofing-supply-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 23.7
  previous_composite: 43.8
  provenance:
    conformance: derived
    contracts:
      callable: 85.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/screenshots/beacon-roofing-supply-2026-06-20T173105.png
security:
- kind: authentication
  name: Beacon Roofing Supply Authentication
  slug: beacon-roofing-supply-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Beacon Roofing Supply Domain Security
  slug: beacon-roofing-supply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beacon-roofing-supply
tags:
- Construction
- Distribution
- Roofing
- Building Materials
- E-Commerce
- Fortune 1000
- Supply Chain
- Order
- Catalog
- Delivery
use_cases:
- description: Integrate Beacon PRO+ with AccuLynx, JobNimbus, or other contractor management platforms to enable in-app material ordering.
  name: Contractor Management Software Integration
- description: Connect enterprise ERP systems with Beacon ordering and inventory for automated procurement workflows.
  name: ERP Integration
- description: Build custom ordering interfaces for roofing contractors that pull live Beacon pricing and inventory.
  name: Custom Ordering Portals
- description: Integrate Beacon delivery tracking into construction project management and scheduling tools.
  name: Delivery Logistics
website: https://www.becn.com/
---
