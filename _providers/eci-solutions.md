---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-09-06'
api_count: 15
apis:
- baseURL: https://api-erp.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: A product-agnostic REST API for reading and writing data in ECI ERP products, currently supporting Deacom, M1, Macola and JobBOSS². The API user account determines which ERP product, customer and data
  name: ECI Manufacturing ERP API
  slug: eci-solutions-platform
- baseURL: https://api-jb2.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: The JobBOSS²-specific REST API for cloud-hosted JobBOSS² customers, covering orders and order line items, order routings, quotes and quote line items, customers, contacts, shipping addresses, estimate
  name: JobBOSS² Public API
  slug: eci-solutions-jobboss2
- baseURL: https://api-m1.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: The M1 ERP public REST API for hosted M1 customers, exposing roughly 1,200 operations across inventory, financial, CRM, production, quality, purchase orders, shipping, employee, sales orders, quotatio
  name: M1 Public API
  slug: eci-solutions-m1
- baseURL: https://api-user.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Management plane for the ECI Manufacturing Integration Engine: companies, API users and credentials, connections, integrations and integration settings, applications, devices, reports, telemetry and p'
  name: ECI MFG Integration Management API
  slug: eci-solutions-integration-management
- baseURL: https://api-user.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: Common authentication endpoints for every ECI Manufacturing Integration Engine API. Issues 60-minute OAuth 2.0 client-credentials access tokens for API users; there is no refresh token, so callers re-
  name: ECI Authentication API
  slug: eci-solutions-authentication
- baseURL: https://payments-api.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Credit card and ACH processing for ECI manufacturing products through the Paya payment gateway: payments, accounts, account vaults and contacts. Bearer tokens from the Integration Engine client-creden'
  name: ECI MFG Payment API
  slug: eci-solutions-payment
- baseURL: https://api-fin.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Accounting-system integration for ECI ERP products. v1 integrates QuickBooks Online, MYOB, Xero and Sage; v2 integrates Xero and ECI Financials and covers purchase, sales and general ledger flows. v2 '
  name: ECI Financial Integration API
  slug: eci-solutions-financial
- baseURL: https://api-ecommerce.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Integration surface for the EvolutionX B2B e-commerce platform: customers, products, product location quantities and EvoX synchronisation resources, used to keep catalogue, pricing and inventory in st'
  name: ECI EvolutionX Ecommerce API
  slug: eci-solutions-ecommerce
- baseURL: https://api-einvoice.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Electronic invoicing integration with the Avalara E-Invoicing & Live Reporting system: documents, input fields and country mandates, for ECI customers subject to statutory e-invoicing regimes.'
  name: ECI Einvoice API
  slug: eci-solutions-einvoice
- baseURL: https://api-ship.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: Shipment, package and label creation for ECI ERP products through EasyPost, plus carrier lists, address validation and unit-of-measure lookups.
  name: ECI Shipping API
  slug: eci-solutions-shipping
- baseURL: https://api-currency.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: Currency code and conversion-rate lookups used by the multi-currency fields in the ECI ERP and JobBOSS² contracts.
  name: ECI Currency Data API
  slug: eci-solutions-currency
- baseURL: https://api-commerce.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Accounts payable and accounts receivable invoice payment through Nuvei''s Commerce Portal: customers, vendors, customer payments and vendor payments, with top/skip paging.'
  name: ECI AP/AR Commerce Automation API
  slug: eci-solutions-apar-commerce
- baseURL: https://api-office.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Microsoft 365 integration for ECI products: drive files, mail and calendar for the signed-in user, with nextPageToken cursor paging.'
  name: ECI Office Integration API
  slug: eci-solutions-office
- baseURL: https://api-notification.integrations.ecimanufacturing.com
  baseurl_source: declared
  description: 'Message notification delivery for ECI products over email (AWS SES) and in-app REST or WebSocket channels. Uses two different token types: Integration Engine client-credentials tokens to create notifi'
  name: ECI Notification API
  slug: eci-solutions-notification
- baseURL: https://api.lassocrm.com/v1
  baseurl_source: declared
  description: The public API for Lasso CRM, ECI's new-home-sales CRM (acquired with Lasso Data Systems and sold under ecisolutions.com/products/lasso-crm). Manages registrants, their contact information, notes, que
  name: Lasso CRM API
  slug: eci-solutions-lasso-crm
artifact_total: 24
asyncapis:
- description: ''
  name: Eci Solutions Lasso Registrant Webhooks
  slug: eci-solutions-lasso-registrant-webhooks
common:
- group: build
  title: ''
  type: Packages
  url: packages/eci-solutions-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eci-solutions-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/eci-solutions-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eci-solutions-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/eci-solutions-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eci-solutions-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/eci-solutions-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eci-solutions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eci-solutions-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eci-solutions-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eci-solutions-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eci-solutions-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/eci-solutions-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eci-solutions-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eci-solutions-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eci-solutions-lasso-registrant-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eci-solutions-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eci-solutions-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eci-solutions-finops.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/eci-solutions-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eci-solutions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/eci-solutions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eci-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ecisolutions.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.ecimanufacturing.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.ecimanufacturing.com/
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.ecimanufacturing.com/api.html?family=erp
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.ecimanufacturing.com/authenticate.html
- group: other
  title: ''
  type: Products
  url: https://www.ecisolutions.com/products/
- group: other
  title: ''
  type: Industries
  url: https://www.ecisolutions.com/industries/
- group: operate
  title: ''
  type: Support
  url: https://www.ecisolutions.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.ecisolutions.com/lets-talk/
- group: company
  title: ''
  type: Blog
  url: https://www.ecisolutions.com/company/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ecisolutions.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecisolutions.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Trust
  url: https://trust.ecisolutions.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eci-software--solutions
created: '2025-03-01'
description: 'ECI Software Solutions (ECI Solutions) is a global provider of industry-specific cloud business management software for small and medium-sized manufacturers, building-supply and industrial distributors, residential construction and trade contractors, field service organizations, and office technology / managed print dealers. Its portfolio spans ERP (JobBOSS², M1, Deacom, Macola, ProfitKey, Ridder iQ, Bemet, Spruce, DDMSPLUS, RockSolid MAX, e-automate, Khameleon), e-commerce (EvolutionX, Spruce eCommerce), CRM (Lasso, Sales Simplicity), payments (NET1), analytics (Cognytics, Lojic, Acsellerate) and MES/APS. ECI publishes a real, anonymously readable API program: the ECI Manufacturing Integration Engine at integrations.ecimanufacturing.com serves seventeen OpenAPI 3.0.1 contracts covering a product-agnostic ERP API plus JobBOSS², M1, authentication, integration management, payments, financial, e-commerce, e-invoicing, shipping, currency, AP/AR commerce, Office 365 and notification
  services, and Lasso CRM publishes its own OpenAPI 3.0.2 contract at platform.lassocrm.com. API activation itself is gated behind an ECI account manager.'
finops:
- name: Eci Solutions Finops
  service_category: API
  slug: eci-solutions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eci-solutions.png
layout: provider
modified: '2026-09-06'
name: ECI Solutions
nav: Providers
network: true
overview: 'ECI Solutions publishes 15 APIs on the [APIs.io](https://apis.io/) network, including ECI Manufacturing ERP API, JobBOSS² Public API, M1 Public API, and 12 more. Tagged areas include Accounting, Building Supply, Business Management, CRM, and Construction.


  The ECI Solutions catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ECI Solutions'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 31 more developer resources.'
plans:
- name: Eci Solutions Plans Pricing
  plan_count: 0
  slug: eci-solutions-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Eci Solutions Rate Limits
  slug: eci-solutions-rate-limits
scopes:
- name: Eci Solutions Scopes
  scope_count: 1
  slug: eci-solutions-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 36.2
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 55.6
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 65.8
  previous_composite: 15.0
  provenance:
    conformance: derived
    contracts:
      callable: 11.1
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/eci-solutions/refs/heads/main/screenshots/eci-solutions-2026-06-20T180423.png
security:
- kind: authentication
  name: Eci Solutions Authentication
  slug: eci-solutions-authentication
  summary_line: http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Eci Solutions Domain Security
  slug: eci-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eci Solutions Vulnerability Disclosure
  slug: eci-solutions-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Eci Solutions Trust Center
  slug: eci-solutions-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: eci-solutions
tags:
- Accounting
- Building Supply
- Business Management
- CRM
- Construction
- Distribution
- E-Commerce
- ERP
- Field Service
- Inventory
- Manufacturing
- Payments
- Retail
- Shipping
website: https://www.ecisolutions.com/
---
