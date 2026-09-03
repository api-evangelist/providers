---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Aaron's online lease application and approval system enabling customers to apply for lease-to-own financing before shopping. Provides instant approval decisions and leasing power discovery for furnitu
  name: Aaron's Lease Application
  slug: aarons-lease-application
- description: Aaron's online account management portal for customers to manage their lease accounts, make payments, set up EZPay automatic payments, track orders, and manage lease and payment information.
  name: Aaron's Account Management
  slug: aarons-account-management
- description: Aaron's lease-to-own product catalog covering furniture (bedroom, living room, dining), electronics (TVs, laptops, gaming), and appliances (washers, dryers, refrigerators) from top brands including As
  name: Aaron's Product Catalog
  slug: aarons-product-catalog
- baseURL: https://hpp.aarons.com
  baseurl_source: declared
  description: Aaron's Hosted Payment Page service — the only surface on the Aaron's estate that publishes a machine-readable API contract. A Swagger 2.0 document is served anonymously at https://hpp.aarons.com/open
  name: Aaron's Hosted Payment Page (HPP)
  slug: aarons-hpp
artifact_total: 30
asyncapis:
- description: ''
  name: Aarons Hpp Webhooks
  slug: aarons-hpp-webhooks
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/aarons-hpp-openapi.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aarons-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aarons-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aarons-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aarons-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aarons-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aarons-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aarons-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aarons-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aarons-hpp-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aarons-hpp-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aarons-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/aarons-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aarons-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aarons-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aarons.com/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aarons.com/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.aarons.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.aarons.com/FAQ
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aarons-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aarons.com
- group: start
  title: ''
  type: Login
  url: https://login.aarons.com
- group: start
  title: ''
  type: Signup
  url: https://www.aarons.com/apply
created: '2026-04-19'
description: Aaron's is a lease-to-own retailer of furniture, consumer electronics, home appliances, and accessories serving customers across the United States and Canada. They provide flexible payment options including rent-to-own leasing with instant approval, online account management, and EZPay automatic payments.
features:
- description: Online lease application with instant approval for customers to discover their leasing power before shopping in-store or online.
  name: Instant Lease Approval
- description: Automatic payment setup (EZPay) for convenient, scheduled lease payment processing without manual intervention.
  name: EZPay Automatic Payments
- description: Online payment portal for customers to make one-time or recurring lease payments through the Aaron's website.
  name: Online Payment Processing
- description: Express delivery in 2-3 days for eligible products to customer homes, with professional installation and setup.
  name: Express Delivery
- description: Store locator to find nearby Aaron's locations for in-store shopping, pickup, and customer service.
  name: Store Locator
- description: Online account portal for tracking orders, managing lease details, viewing payment history, and saving favorite products.
  name: Account Management Portal
- description: Clearance and previously leased product inventory available at reduced lease rates for budget-conscious customers.
  name: Previously Leased Inventory
finops:
- name: Aarons Finops
  service_category: Retail / Consumer Finance
  slug: aarons-finops
image: /assets/icons/aarons.png
integrations:
- description: The Aaron's Company subsidiary BrandsMart USA, providing consumer electronics and appliance retail with lease-to-own financing.
  name: BrandsMart USA
- description: The aarons.com storefront runs on Salesforce B2C Commerce. Its Open Commerce API (OCAPI) 21.3 Shop surface is live at /s/Aarons/dw/shop/v21_3/ and returns a standard OCAPI fault when called without a client ID. Probed 2026-08-29.
  name: Salesforce B2C Commerce (Demandware)
- description: Customer identity runs on Okta at login.aarons.com (custom domain), serving anonymous OpenID Connect and RFC 8414 discovery documents. Probed 2026-08-29.
  name: Okta
- description: api.aarons.com is an Azure API Management gateway fronting the account, home, ezpay, onboarding, support and Acadia service bases named in Aaron's own customer application bundle. Live and undocumented. Probed 2026-08-29.
  name: Azure API Management
- description: Payment gateway. Aaron's Hosted Payment Page publishes an inbound /FiservPostback receiver with a typed authorisation-result payload in its own Swagger contract.
  name: Fiserv
- description: Payment gateway and card vault. Aaron's HPP publishes inbound /RepayAuthPostback and /RepayCardVaultPostback receivers with versioned event envelopes.
  name: Repay
- description: Analytics and tracking integration via Google Tag Manager for website behavior analysis and marketing optimization.
  name: Google Tag Manager
layout: provider
modified: '2026-08-29'
name: Aaron's
nav: Providers
network: true
overview: 'Aaron''s publishes 1 API on the [APIs.io](https://apis.io/) network: Hosted Payment Page (HPP). Tagged areas include Lease-to-Own, Retail, Furniture, Electronics, and Appliances.


  The Aaron''s catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aaron''s'' developer surface includes authentication, support, signup flow, and 21 more developer resources.'
plans:
- name: Aarons Plans Pricing
  plan_count: 0
  slug: aarons-plans-pricing
press:
- date: '2026-05-25'
  title: 'Harold Cohen: AARON'
  url: https://whitney.org/exhibitions/harold-cohen-aaron
- date: '2026-05-25'
  title: Salesforce Data Cloud Unifies Aaron's Retail ...
  url: https://www.salesforce.com/news/stories/aarons-customer-story/
- date: '2026-05-25'
  title: AI art history began in 1972 with Aaron's program
  url: https://www.facebook.com/groups/officialmidjourney/posts/456355219989381/
- date: '2026-05-25'
  title: The Aaron's Company, Inc.'s Post
  url: https://www.linkedin.com/posts/the-aaron%27s-company-inc._the-aarons-company-enters-into-definitive-activity-7208426161025024000-BpKq
- date: '2026-05-25'
  title: IQVentures Completes Acquisition of The Aaron's Company
  url: https://www.prnewswire.com/news-releases/iqventures-completes-acquisition-of-the-aarons-company-302267226.html
random_paper: 14
rate_limits:
- limit_count: 0
  name: Aarons Rate Limits
  slug: aarons-rate-limits
scopes:
- name: Aarons Scopes
  scope_count: 0
  slug: aarons-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.6
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 18.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 31.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aarons/refs/heads/main/screenshots/aarons-2026-06-20T163019.png
security:
- kind: authentication
  name: Aarons Authentication
  slug: aarons-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aarons Domain Security
  slug: aarons-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aarons
tags:
- Lease-to-Own
- Retail
- Furniture
- Electronics
- Appliances
- Consumer Finance
- Fortune 1000
use_cases:
- description: Customers acquiring bedroom sets, sofas, sectionals, and dining furniture through flexible lease-to-own payment plans.
  name: Furniture Lease-to-Own
- description: Consumers accessing TVs, laptops, gaming consoles, and audio equipment through affordable weekly or monthly lease payments.
  name: Electronics Access
- description: Households obtaining washers, dryers, refrigerators, and ranges through lease-to-own options with delivery and installation.
  name: Appliance Leasing
- description: Consumers with limited or poor credit history accessing household goods through Aaron's flexible lease-to-own programs.
  name: Credit-Challenged Consumer Financing
- description: Short-term furniture and appliance needs for relocating individuals or temporary housing situations via lease agreements.
  name: Temporary Furnishing
website: https://www.aarons.com
---
