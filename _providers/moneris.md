---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Moneris Agentic Access
  operation_count: 54
  slug: moneris-agentic-access
  summary_line: 54 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform 3D Secure authentications against payment methods
  name: Moneris 3D Secure API
  slug: moneris-3d-secure-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage customers
  name: Moneris Customers API
  slug: moneris-customers-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage Disputes
  name: Moneris Disputes API
  slug: moneris-disputes-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage Installments
  name: Moneris Installments API
  slug: moneris-installments-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage Kount risk assessment inquiries
  name: Moneris Kount API
  slug: moneris-kount-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Manage Merchants onboarding
  name: Moneris Merchant Onboarding API
  slug: moneris-merchant-onboarding-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Retrieve Multi-Currency Pricing Rate Lookups
  name: Moneris Multi-Currency Pricing Rate Lookup API
  slug: moneris-multi-currency-pricing-rate-lookup-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Create and Manage payment methods
  name: Moneris Payment Methods API
  slug: moneris-payment-methods-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage payments
  name: Moneris Payments API
  slug: moneris-payments-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Product recommendations
  name: Moneris Products API
  slug: moneris-products-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage payment refunds
  name: Moneris Refunds API
  slug: moneris-refunds-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage Subscriptions
  name: Moneris Subscriptions API
  slug: moneris-subscriptions-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: The Surcharge Lookup API from Moneris — 1 operation(s) for surcharge lookup.
  name: Moneris Surcharge Lookup API
  slug: moneris-surcharge-lookup-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Manage Moneris Terminal & Service Orders
  name: Moneris Terminal & Service Orders API
  slug: moneris-terminal-service-orders-api
- baseURL: https://api.moneris.io
  baseurl_source: declared
  description: Perform and Manage card validations
  name: Moneris Validations API
  slug: moneris-validations-api
artifact_total: 29
asyncapis:
- description: ''
  name: Moneris Subscriptions Webhooks
  slug: moneris-subscriptions-webhooks
collections:
- collection_type: open
  name: Moneris API
  slug: open-moneris-unified-api
common:
- group: commercial
  href: https://artifacts.apis.io/moneris/plans/moneris-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moneris-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/moneris/capabilities/moneris-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/moneris-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/moneris/overlays/moneris-unified-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moneris-unified-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/moneris/security/moneris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moneris-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/moneris/agentic-access/moneris-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moneris-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/moneris/scopes/moneris-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/moneris-scopes.yml
- group: auth
  href: https://artifacts.apis.io/moneris/authentication/moneris-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moneris-authentication.yml
- group: agent
  href: https://artifacts.apis.io/moneris/mcp/moneris-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moneris-mcp.yml
- group: design
  href: https://artifacts.apis.io/moneris/conventions/moneris-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moneris-conventions.yml
- group: design
  href: https://artifacts.apis.io/moneris/conventions/moneris-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/moneris-conventions.yml
- group: design
  href: https://artifacts.apis.io/moneris/errors/moneris-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moneris-problem-types.yml
- group: build
  href: https://artifacts.apis.io/moneris/errors/moneris-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/moneris-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/moneris/lifecycle/moneris-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moneris-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moneris.com
- group: design
  href: https://artifacts.apis.io/moneris/conformance/moneris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moneris-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.moneris.com/en/support/compliance-and-security/pci-data-security
- group: design
  href: https://artifacts.apis.io/moneris/asyncapi/moneris-subscriptions-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/moneris-subscriptions-webhooks.yml
- group: design
  href: https://artifacts.apis.io/moneris/data-model/moneris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moneris-data-model.yml
- group: start
  href: https://artifacts.apis.io/moneris/sandbox/moneris-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/moneris-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/moneris/well-known/moneris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moneris-well-known.yml
- group: agent
  href: https://artifacts.apis.io/moneris/llms/moneris-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moneris-llms.txt
- group: agent
  href: https://artifacts.apis.io/moneris/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.moneris.com/moneris-api/docs/getting-started-guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.moneris.com/changelog
- group: start
  title: ''
  type: SignUp
  url: https://developer.moneris.com/login
- group: company
  title: ''
  type: Website
  url: https://www.moneris.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moneris.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moneris.com/moneris-api/docs/introduction
- group: other
  title: ''
  type: Registration
  url: https://developer.moneris.com/login
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/moneris
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moneris
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moneris
- group: company
  title: ''
  type: Blog
  url: https://www.moneris.com/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moneris.com/en/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneris.com/en/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.moneris.com/en/support/contact
created: '2026-07-23'
description: 'Moneris (Moneris Solutions Corporation) is Canada''s largest payment processor and merchant-acquiring company, founded in December 2000 as a joint venture equally owned by Royal Bank of Canada (RBC) and Bank of Montreal (BMO). It is a payment-technology and card-acquiring company rather than a deposit-taking Schedule I bank, sitting in the payments-infrastructure layer of Canadian financial services: it serves roughly 325,000 points of commerce, processes close to five billion transactions a year, and handles on the order of one in three Canadian card transactions. In 2025-2026 RBC and BMO explored a sale of the venture, with Francisco Partners (owner of Verifone) reported as the lead buyer. Unlike its bank owners, Moneris is not subject to Canada''s coming Consumer-Driven Banking framework; its "open" surface is a commercial, self-serve first-party developer program. Moneris runs a real, public developer portal at developer.moneris.com documenting the Moneris Unified API (REST,
  OpenAPI 3.0.3, hosts api.moneris.io production / api.sb.moneris.io sandbox) covering payments, tokenized payment methods, refunds, recurring billing/subscriptions, 3-D Secure, Kount fraud/risk, disputes, multi-currency pricing, and third-party merchant onboarding, secured with OAuth 2.0 client credentials and API keys, with a published Postman workspace.'
finops:
- has_sources: true
  method: derived
  name: Moneris Finops
  primary_unit: successful credit card transaction
  service_category: ''
  slug: moneris-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.moneris.io over HTTP; 19 tools listed.
  name: Moneris MCP Server
  slug: moneris
modified: '2026-07-23'
name: Moneris
nav: Providers
network: true
overview: 'Moneris publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including 3D Secure API, Customers API, Disputes API, and 12 more. Tagged areas include Financial Services, Payments, Payment Processing, Card Payments, and Merchant Services.


  The Moneris catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Moneris'' developer surface includes authentication, sandbox, getting-started guide, changelog, signup flow, documentation, engineering blog, and 29 more developer resources.'
plans:
- name: Moneris Plans Pricing
  plan_count: 3
  slug: moneris-plans-pricing
- name: Moneris Price Estimates
  plan_count: 0
  slug: moneris-price-estimates
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Moneris API Rules
  rule_count: 68
  severity_counts:
    error: 54
    hint: 0
    info: 5
    warn: 9
  slug: moneris-rules
scopes:
- name: Moneris Scopes
  scope_count: 14
  slug: moneris-scopes
  summary_line: 14 scopes · clientCredentials
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.4
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 61.0
    developer_ergonomics: 68.5
    discoverability: 75.0
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moneris/moneris-2026-08-07T184149.png
security:
- kind: authentication
  name: Moneris Authentication
  slug: moneris-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Moneris Domain Security
  slug: moneris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create a customer and charge them
  slug: moneris-create-customer-and-charge
- name: Pre-authorize, complete, and refund a payment
  slug: moneris-preauth-complete-refund
- name: Create and manage a recurring subscription
  slug: moneris-recurring-subscription
slug: moneris
tags:
- Financial Services
- Payments
- Payment Processing
- Card Payments
- Merchant Services
- Acquiring
- Canada
- Fintech
- Infrastructure
website: https://www.moneris.com
---
