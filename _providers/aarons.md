---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - scopes
  - rate-limits
  - security
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
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
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
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The AuthorizeSession API from Aaron's — 1 operation(s) for authorizesession.
  name: Aaron's Authorize Session API
  slug: aarons-authorizesession-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The AutoPayCustomerRetry API from Aaron's — 1 operation(s) for autopaycustomerretry.
  name: Aaron's Auto Pay Customer Retry API
  slug: aarons-autopaycustomerretry-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The CreateToken API from Aaron's — 1 operation(s) for createtoken.
  name: Aaron's Create Token API
  slug: aarons-createtoken-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The FiservPostback API from Aaron's — 1 operation(s) for fiservpostback.
  name: Aaron's Fiserv Postback API
  slug: aarons-fiservpostback-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The MemoryBearerToken API from Aaron's — 1 operation(s) for memorybearertoken.
  name: Aaron's Memory Bearer Token API
  slug: aarons-memorybearertoken-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The MemoryTokenGuid API from Aaron's — 1 operation(s) for memorytokenguid.
  name: Aaron's Memory Token Guid API
  slug: aarons-memorytokenguid-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The ping API from Aaron's — 2 operation(s) for ping.
  name: Aaron's Ping API
  slug: aarons-ping-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The RepayAuthPostback API from Aaron's — 1 operation(s) for repayauthpostback.
  name: Aaron's Repay Auth Postback API
  slug: aarons-repayauthpostback-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The RepayCardVaultPostback API from Aaron's — 1 operation(s) for repaycardvaultpostback.
  name: Aaron's Repay Card Vault Postback API
  slug: aarons-repaycardvaultpostback-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The SaveDeviceIntelligence API from Aaron's — 1 operation(s) for savedeviceintelligence.
  name: Aaron's Save Device Intelligence API
  slug: aarons-savedeviceintelligence-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The SaveToken API from Aaron's — 1 operation(s) for savetoken.
  name: Aaron's Save Token API
  slug: aarons-savetoken-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The UpdateCustomerRetryNotification API from Aaron's — 1 operation(s) for updatecustomerretrynotification.
  name: Aaron's Update Customer Retry Notification API
  slug: aarons-updatecustomerretrynotification-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The Create Session API from Aaron's — 1 operation(s) for create session.
  name: Aaron's Create Session API
  slug: aarons-create-session-api
- baseURL: https://api.aarons.com/onboarding
  baseurl_source: declared
  description: The CUSTOMER DATA API from Aaron's — 1 operation(s) for customer data.
  name: Aaron's CUSTOMER DATA API
  slug: aarons-customer-data-api
artifact_total: 47
asyncapis:
- description: ''
  name: Aarons Hpp Webhooks
  slug: aarons-hpp-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/aarons/finops/aarons-finops.yml
  title: ''
  type: FinOps
  url: finops/aarons-finops.yml
- group: docs
  href: https://artifacts.apis.io/aarons/openapi/_original/aarons-hpp-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/aarons-hpp-openapi.json
- group: agent
  href: https://artifacts.apis.io/aarons/well-known/aarons-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aarons-well-known.yml
- group: auth
  href: https://artifacts.apis.io/aarons/authentication/aarons-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aarons-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aarons/scopes/aarons-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aarons-scopes.yml
- group: design
  href: https://artifacts.apis.io/aarons/conformance/aarons-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aarons-conformance.yml
- group: design
  href: https://artifacts.apis.io/aarons/errors/aarons-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aarons-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aarons/lifecycle/aarons-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aarons-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aarons/conventions/aarons-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aarons-conventions.yml
- group: design
  href: https://artifacts.apis.io/aarons/data-model/aarons-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aarons-data-model.yml
- group: other
  href: https://artifacts.apis.io/aarons/overlays/aarons-hpp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aarons-hpp-overlay.yaml
- group: design
  href: https://artifacts.apis.io/aarons/asyncapi/aarons-hpp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aarons-hpp-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/aarons/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aarons/llms/aarons-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aarons-llms.txt
- group: build
  href: https://artifacts.apis.io/aarons/packages/aarons-packages.yml
  title: ''
  type: Packages
  url: packages/aarons-packages.yml
- group: commercial
  href: https://artifacts.apis.io/aarons/plans/aarons-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aarons-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aarons/rate-limits/aarons-rate-limits.yml
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
  href: https://artifacts.apis.io/aarons/security/aarons-domain-security.yml
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
- has_sources: true
  method: generated
  name: Aarons Finops
  primary_unit: ''
  service_category: Retail / Consumer Finance
  slug: aarons-finops
  template: false
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
modified: '2026-09-16'
name: Aaron's
nav: Providers
network: true
overview: 'Aaron''s publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorize Session API, Auto Pay Customer Retry API, Create Token API, and 14 more. Tagged areas include Lease-to-Own, Retail, Furniture, Electronics, and Appliances.


  The Aaron''s catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Aaron''s'' developer surface includes authentication, support, signup flow, and 22 more developer resources.'
plans:
- name: Aarons Plans Pricing
  plan_count: 0
  slug: aarons-plans-pricing
press:
- date: ''
  title: 'Harold Cohen: AARON'
  url: https://whitney.org/exhibitions/harold-cohen-aaron
- date: ''
  title: Salesforce Data Cloud Unifies Aaron's Retail ...
  url: https://www.salesforce.com/news/stories/aarons-customer-story/
- date: ''
  title: AI art history began in 1972 with Aaron's program
  url: https://www.facebook.com/groups/officialmidjourney/posts/456355219989381/
- date: ''
  title: The Aaron's Company, Inc.'s Post
  url: https://www.linkedin.com/posts/the-aaron%27s-company-inc._the-aarons-company-enters-into-definitive-activity-7208426161025024000-BpKq
- date: ''
  title: IQVentures Completes Acquisition of The Aaron's Company
  url: https://www.prnewswire.com/news-releases/iqventures-completes-acquisition-of-the-aarons-company-302267226.html
random_paper: 20
rate_limits:
- limit_count: 0
  name: Aarons Rate Limits
  slug: aarons-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Aaron's API Rules
  rule_count: 47
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 5
  slug: aarons-rules
scopes:
- name: Aarons Scopes
  scope_count: 0
  slug: aarons-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 27.6
    contract_governance: 31.8
    contract_quality: 55.3
    developer_ergonomics: 18.5
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 35.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aarons/aarons-2026-06-20T163019.png
security:
- kind: authentication
  name: Aarons Authentication
  slug: aarons-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aarons Domain Security
  slug: aarons-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: aarons-hpp-autopay-retry
  slug: aarons-hpp-autopay-retry
- name: aarons-hpp-gateway-postbacks
  slug: aarons-hpp-gateway-postbacks
- name: aarons-hpp-payment-session
  slug: aarons-hpp-payment-session
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
