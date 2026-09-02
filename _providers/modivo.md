---
access_model:
  confidence: medium
  label: Public storefront commerce API, no developer program
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  - openapi
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: The GraphQL endpoint that powers the MODIVO storefront and mobile applications, exposed at https://modivo.pl/graphql with introspection left open to anonymous callers. The schema carries 770 types, 11
  name: MODIVO Storefront GraphQL API
  slug: modivo-storefront-graphql-api
- description: MODIVO's third-party marketplace runs on a Mirakl tenant at modivo.mirakl.net. Sellers automate offers, stock, prices, orders and tracking numbers through the standard Mirakl Marketplace Seller API on
  name: MODIVO Marketplace Seller API (Mirakl)
  slug: modivo-marketplace-seller-api-mirakl
- description: Interface which provides product renders information for products.
  name: MODIVO Catalog Product Render List V1 API
  slug: modivo-catalogproductrenderlistv1-api
- description: The chatbotOrderRestApiOrderRestApiServiceV1 API from MODIVO — 2 operation(s) for chatbotorderrestapiorderrestapiservicev1.
  name: MODIVO Chatbot Order Rest API Order Rest API Service V1 API
  slug: modivo-chatbotorderrestapiorderrestapiservicev1-api
- description: Interface for managing guest payment information
  name: MODIVO Checkout Guest Payment Information Management V1 API
  slug: modivo-checkoutguestpaymentinformationmanagementv1-api
- description: Interface for managing guest shipping address information
  name: MODIVO Checkout Guest Shipping Information Management V1 API
  slug: modivo-checkoutguestshippinginformationmanagementv1-api
- description: Interface for guest quote totals calculation
  name: MODIVO Checkout Guest Totals Information Management V1 API
  slug: modivo-checkoutguesttotalsinformationmanagementv1-api
- description: Interface for managing customers accounts.
  name: MODIVO Customer Account Management V1 API
  slug: modivo-customeraccountmanagementv1-api
- description: Country information acquirer interface
  name: MODIVO Directory Country Information Acquirer V1 API
  slug: modivo-directorycountryinformationacquirerv1-api
- description: Currency information acquirer interface
  name: MODIVO Directory Currency Information Acquirer V1 API
  slug: modivo-directorycurrencyinformationacquirerv1-api
- description: Interface HttpServiceInterface
  name: MODIVO Eob JWT HTTP Service V1 API
  slug: modivo-eobjwthttpservicev1-api
- description: The eobMyReturnsWebhookWebhookV1 API from MODIVO — 1 operation(s) for eobmyreturnswebhookwebhookv1.
  name: MODIVO Eob My Returns Webhook Webhook V1 API
  slug: modivo-eobmyreturnswebhookwebhookv1-api
- description: The eobPlaceOrderOrderManagementV1 API from MODIVO — 1 operation(s) for eobplaceorderordermanagementv1.
  name: MODIVO Eob Place Order Order Management V1 API
  slug: modivo-eobplaceorderordermanagementv1-api
- description: The eobTrustmateIntegrationDisplayApiV1 API from MODIVO — 1 operation(s) for eobtrustmateintegrationdisplayapiv1.
  name: MODIVO Eob Trustmate Integration Display API V1 API
  slug: modivo-eobtrustmateintegrationdisplayapiv1-api
- description: Interface GuestCartRepositoryInterface
  name: MODIVO Gift Message Guest Cart Repository V1 API
  slug: modivo-giftmessageguestcartrepositoryv1-api
- description: Interface GuestItemRepositoryInterface
  name: MODIVO Gift Message Guest Item Repository V1 API
  slug: modivo-giftmessageguestitemrepositoryv1-api
- description: Interface providing token generation for Admins
  name: MODIVO Integration Admin Token Service V1 API
  slug: modivo-integrationadmintokenservicev1-api
- description: Interface providing token generation for Customers
  name: MODIVO Integration Customer Token Service V1 API
  slug: modivo-integrationcustomertokenservicev1-api
- description: 'Get Pickup Locations filtered by provided Search Request. Pickup Location entities are Immutable object and can not be changed after creation. All modification of Pickup Location must be done through '
  name: MODIVO Inventory In Store Pickup API Get Pickup Locations V1 API
  slug: modivo-inventoryinstorepickupapigetpickuplocationsv1-api
- description: The marketplacePlaceOrderOrderManagementV1 API from MODIVO — 1 operation(s) for marketplaceplaceorderordermanagementv1.
  name: MODIVO Marketplace Place Order Order Management V1 API
  slug: modivo-marketplaceplaceorderordermanagementv1-api
- description: The modivoMyReturnsWebhookWebhookV1 API from MODIVO — 1 operation(s) for modivomyreturnswebhookwebhookv1.
  name: MODIVO Modivo My Returns Webhook Webhook V1 API
  slug: modivo-modivomyreturnswebhookwebhookv1-api
- description: The paymentServicesPaypalCompleteOrderV1 API from MODIVO — 1 operation(s) for paymentservicespaypalcompleteorderv1.
  name: MODIVO Payment Services Paypal Complete Order V1 API
  slug: modivo-paymentservicespaypalcompleteorderv1-api
- description: The paymentServicesPaypalPaymentConfigRequestV1 API from MODIVO — 5 operation(s) for paymentservicespaypalpaymentconfigrequestv1.
  name: MODIVO Payment Services Paypal Payment Config Request V1 API
  slug: modivo-paymentservicespaypalpaymentconfigrequestv1-api
- description: An interface for the REST WebAPI request to create an order
  name: MODIVO Payment Services Paypal Payment Order Request V1 API
  slug: modivo-paymentservicespaypalpaymentorderrequestv1-api
- description: An interface for the REST WebAPI to get payment sdk urls
  name: MODIVO Payment Services Paypal Payment SDK Request V1 API
  slug: modivo-paymentservicespaypalpaymentsdkrequestv1-api
- description: Interface AuthInterface
  name: MODIVO Pay Pal Braintree Auth V1 API
  slug: modivo-paypalbraintreeauthv1-api
- description: Billing address management interface for guest carts.
  name: MODIVO Quote Guest Billing Address Management V1 API
  slug: modivo-quoteguestbillingaddressmanagementv1-api
- description: Cart Item repository interface for guest carts.
  name: MODIVO Quote Guest Cart Item Repository V1 API
  slug: modivo-quoteguestcartitemrepositoryv1-api
- description: Cart Management interface for guest carts.
  name: MODIVO Quote Guest Cart Management V1 API
  slug: modivo-quoteguestcartmanagementv1-api
- description: Cart Repository interface for guest carts.
  name: MODIVO Quote Guest Cart Repository V1 API
  slug: modivo-quoteguestcartrepositoryv1-api
- description: Bundled API to collect totals for cart based on shipping/payment methods and additional data.
  name: MODIVO Quote Guest Cart Total Management V1 API
  slug: modivo-quoteguestcarttotalmanagementv1-api
- description: Cart totals repository interface for guest carts.
  name: MODIVO Quote Guest Cart Total Repository V1 API
  slug: modivo-quoteguestcarttotalrepositoryv1-api
- description: Coupon management interface for guest carts.
  name: MODIVO Quote Guest Coupon Management V1 API
  slug: modivo-quoteguestcouponmanagementv1-api
- description: Payment method management interface for guest carts.
  name: MODIVO Quote Guest Payment Method Management V1 API
  slug: modivo-quoteguestpaymentmethodmanagementv1-api
- description: Interface GuestShipmentEstimationInterface
  name: MODIVO Quote Guest Shipment Estimation V1 API
  slug: modivo-quoteguestshipmentestimationv1-api
- description: Shipping method management interface for guest carts.
  name: MODIVO Quote Guest Shipping Method Management V1 API
  slug: modivo-quoteguestshippingmethodmanagementv1-api
- description: Search API for all requests
  name: MODIVO Search V1 API
  slug: modivo-searchv1-api
artifact_total: 44
asyncapis:
- description: ''
  name: Modivo Webhooks
  slug: modivo-webhooks
collections:
- collection_type: open
  name: MODIVO Commerce REST API
  slug: open-modivo-commerce-rest-api
- collection_type: open
  name: eobuwie Commerce REST API
  slug: open-modivo-eobuwie-commerce-rest-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/modivo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/modivo-commerce-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/modivo-eobuwie-commerce-rest-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://modivo.pl/
- group: other
  title: ''
  type: Company
  url: https://modivoplatform.com/en
- group: operate
  title: ''
  type: Support
  url: https://modivo.pl/b/centrum-pomocy
- group: operate
  title: ''
  type: HelpCenter
  url: https://modivo.pl/b/centrum-pomocy
- group: start
  title: ''
  type: SignUp
  url: https://modivo.pl/login
- group: start
  title: ''
  type: Login
  url: https://modivo.pl/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modivo.pl/b/regulamin-sklepu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modivo.pl/b/regulamin_prywatnosci
- group: company
  title: ''
  type: Blog
  url: https://advertising.modivo.com/news
- group: other
  title: ''
  type: Advertising
  url: https://advertising.modivo.com/
- group: company
  title: ''
  type: Careers
  url: https://praca.modivo.pl/technologia-i-produkt
- group: company
  title: ''
  type: InvestorRelations
  url: https://modivoplatform.com/en/investors
- group: auth
  title: ''
  type: Authentication
  url: authentication/modivo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modivo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modivo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modivo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/modivo-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modivo-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/modivo-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/modivo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modivo-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/modivo-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modivo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modivo-domain-security.yml
created: '2026-07-17'
description: 'MODIVO is a Polish multibrand fashion and lifestyle retailer that operates one of the largest fashion e-commerce platforms in Central and Eastern Europe, selling clothing, footwear, accessories, beauty and home products from more than a thousand brands across Poland, the Czech Republic, Slovakia, Romania, Hungary, Ukraine, the Baltics and Western Europe. MODIVO S.A. is the listed parent of the former CCC Group (renamed MODIVO S.A. in February 2026) and the group behind the eobuwie.pl, CCC, HalfPrice, worldbox and DeeZee retail brands; the MODIVO storefront company itself is the former eobuwie.pl S.A., a consumer-technology investment of SoftBank Vision Fund. MODIVO does not run a developer portal, but its storefront is an Adobe Commerce (Magento 2.4) deployment that serves two live, publicly readable machine contracts from its own domain: a self-describing Swagger 2.0 REST schema at https://modivo.pl/rest/all/schema?services=all and an openly introspectable GraphQL endpoint
  at https://modivo.pl/graphql. Third-party sellers integrate through a Mirakl-hosted marketplace tenant, and brands buy sponsored placements through MODIVO Ads, the group''s retail-media platform spanning MODIVO and eobuwie.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modivo.png
layout: provider
modified: '2026-08-12'
name: MODIVO
nav: Providers
network: true
overview: 'MODIVO publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Catalog Product Render List V1 API, Chatbot Order Rest API Order Rest API Service V1 API, Checkout Guest Payment Information Management V1 API, and 32 more. Tagged areas include Company, Consumer, Fashion, E-Commerce, and Retail.


  The MODIVO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MODIVO''s developer surface includes support, signup flow, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: Modivo Plans Pricing
  plan_count: 0
  slug: modivo-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Modivo Rate Limits
  slug: modivo-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 59.3
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modivo/refs/heads/main/screenshots/modivo-2026-08-07T184029.png
security:
- kind: authentication
  name: Modivo Authentication
  slug: modivo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Modivo Domain Security
  slug: modivo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modivo
tags:
- Company
- Consumer
- Fashion
- E-Commerce
- Retail
- Marketplace
- Retail Media
- Commerce
- Checkout
- Catalog
- GraphQL
- Adobe Commerce
- Magento
- Poland
- Central Europe
website: https://modivo.pl/
---
