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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Shippingeasy Agentic Access
  operation_count: 8
  slug: shippingeasy-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://app.shippingeasy.com/api
  baseurl_source: declared
  description: Order create, look up, status update, and cancellation.
  name: ShippingEasy Orders API
  slug: shippingeasy-orders-api
- baseURL: https://app.shippingeasy.com/api
  baseurl_source: declared
  description: API-enabled stores configured in the ShippingEasy account.
  name: ShippingEasy Stores API
  slug: shippingeasy-stores-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShippingEasy Customer API
  slug: open-shippingeasy-customer-api
- collection_type: open
  name: ShippingEasy Customer Orders API
  slug: open-shippingeasy-orders-api
- collection_type: open
  name: ShippingEasy Customer Orders Stores API
  slug: open-shippingeasy-stores-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shippingeasy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shippingeasy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shippingeasy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://shippingeasy.com
- group: commercial
  title: ''
  type: Pricing
  url: https://shippingeasy.com/pricing/
- group: other
  title: ''
  type: ShippingAPI
  url: https://shippingeasy.com/shipping-api/
- group: docs
  title: ''
  type: Documentation
  url: https://shippingeasy.readme.io/reference/getting-started
- group: start
  title: ''
  type: Signup
  url: https://app.shippingeasy.com/customer/new
- group: start
  title: ''
  type: Login
  url: https://app.shippingeasy.com/login
- group: other
  title: ''
  type: APICredentials
  url: https://app.shippingeasy.com/settings/api_credentials
- group: operate
  title: ''
  type: Support
  url: https://support.shippingeasy.com
- group: company
  title: ''
  type: Blog
  url: https://shippingeasy.com/blog/
- group: company
  title: ''
  type: Careers
  url: https://shippingeasy.com/careers/
- group: other
  title: ''
  type: Parent
  url: https://auctane.com
- group: other
  title: ''
  type: SisterBrand
  url: https://www.shipengine.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShippingEasy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ShippingEasy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shippingeasy
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ShippingEasy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/ShippingEasy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shippingeasy.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shippingeasy.com/privacy-policy/
created: '2026-05-25'
description: ShippingEasy is an Austin, Texas shipping software platform for online merchants, providing multi-carrier label printing with discounted USPS, UPS, FedEx, and DHL rates, automated order import and workflow rules, inventory and product management, branded tracking, customer email marketing, and reporting. ShippingEasy was acquired by Stamps.com in 2016 and is part of the Auctane portfolio of shipping brands, which also includes ShipStation, ShipEngine, ShipWorks, MetaPack, Packlink, and Endicia. The company exposes a public Customer API focused on sending orders into ShippingEasy from custom marketplaces or storefronts not already covered by the built-in integration catalog; for fuller multi-carrier label, rate, and tracking APIs, ShippingEasy directs developers to sister brand ShipEngine.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippingeasy.png
layout: provider
modified: '2026-05-25'
name: ShippingEasy
nav: Providers
network: true
overview: 'ShippingEasy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Stores API. Tagged areas include Shipping, Logistics, Multi-Carrier, Labels, and Order Management.


  ShippingEasy''s developer surface includes authentication, pricing, documentation, signup flow, support, engineering blog, YouTube channel, and 15 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.9
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
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shippingeasy/refs/heads/main/screenshots/shippingeasy-2026-06-20T193821.png
security:
- kind: authentication
  name: Shippingeasy Authentication
  slug: shippingeasy-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Shippingeasy Domain Security
  slug: shippingeasy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippingeasy
tags:
- Shipping
- Logistics
- Multi-Carrier
- Labels
- Order Management
- E-Commerce
- Auctane
- Stamps.com
website: https://shippingeasy.com
---
