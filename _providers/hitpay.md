---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: half
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Hitpay Agentic Access
  operation_count: 92
  slug: hitpay-agentic-access
  summary_line: 92 operations · 49 acting
api_count: 1
apis:
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Account Status API from HitPay — 1 operation(s) for account status.
  name: HitPay Account Status API
  slug: hitpay-account-status-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Balances API from HitPay — 3 operation(s) for balances.
  name: HitPay Balances API
  slug: hitpay-balances-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Beneficiaries API from HitPay — 3 operation(s) for beneficiaries.
  name: HitPay Beneficiaries API
  slug: hitpay-beneficiaries-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Charge API from HitPay — 1 operation(s) for charge.
  name: HitPay Charge API
  slug: hitpay-charge-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Charges API from HitPay — 4 operation(s) for charges.
  name: HitPay Charges API
  slug: hitpay-charges-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Customers API from HitPay — 2 operation(s) for customers.
  name: HitPay Customers API
  slug: hitpay-customers-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Invoices API from HitPay — 2 operation(s) for invoices.
  name: HitPay Invoices API
  slug: hitpay-invoices-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Notifications API from HitPay — 1 operation(s) for notifications.
  name: HitPay Notifications API
  slug: hitpay-notifications-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Orders API from HitPay — 2 operation(s) for orders.
  name: HitPay Orders API
  slug: hitpay-orders-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Payment Requests API from HitPay — 4 operation(s) for payment requests.
  name: HitPay Payment Requests API
  slug: hitpay-payment-requests-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Product Category API from HitPay — 1 operation(s) for product category.
  name: HitPay Product Category API
  slug: hitpay-product-category-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Products API from HitPay — 2 operation(s) for products.
  name: HitPay Products API
  slug: hitpay-products-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Readers API from HitPay — 2 operation(s) for readers.
  name: HitPay Readers API
  slug: hitpay-readers-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Recurring Billing API from HitPay — 5 operation(s) for recurring billing.
  name: HitPay Recurring Billing API
  slug: hitpay-recurring-billing-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Refund API from HitPay — 2 operation(s) for refund.
  name: HitPay Refund API
  slug: hitpay-refund-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Remitters API from HitPay — 2 operation(s) for remitters.
  name: HitPay Remitters API
  slug: hitpay-remitters-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Staffs API from HitPay — 2 operation(s) for staffs.
  name: HitPay Staffs API
  slug: hitpay-staffs-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Static Qr API from HitPay — 2 operation(s) for static qr.
  name: HitPay Static Qr API
  slug: hitpay-static-qr-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Subscription Plan API from HitPay — 2 operation(s) for subscription plan.
  name: HitPay Subscription Plan API
  slug: hitpay-subscription-plan-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Transfers API from HitPay — 3 operation(s) for transfers.
  name: HitPay Transfers API
  slug: hitpay-transfers-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Virtual Accounts API from HitPay — 2 operation(s) for virtual accounts.
  name: HitPay Virtual Accounts API
  slug: hitpay-virtual-accounts-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Webhook Events API from HitPay — 2 operation(s) for webhook events.
  name: HitPay Webhook Events API
  slug: hitpay-webhook-events-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Location API from HitPay — 2 operation(s) for location.
  name: HitPay Location API
  slug: hitpay-location-api
- baseURL: https://api.hit-pay.com/v1
  baseurl_source: declared
  description: The Payouts API from HitPay — 3 operation(s) for payouts.
  name: HitPay Payouts API
  slug: hitpay-payouts-api
artifact_total: 88
asyncapis:
- description: ''
  name: Hitpay Events Webhooks
  slug: hitpay-events-webhooks
collections:
- collection_type: postman
  name: HitPay Account Status API
  slug: postman-hitpay-account-status-api
- collection_type: postman
  name: HitPay Account Status Balances API
  slug: postman-hitpay-balances-api
- collection_type: postman
  name: HitPay Account Status Beneficiaries API
  slug: postman-hitpay-beneficiaries-api
- collection_type: postman
  name: HitPay Account Status Charge API
  slug: postman-hitpay-charge-api
- collection_type: postman
  name: HitPay Account Status Charges API
  slug: postman-hitpay-charges-api
- collection_type: postman
  name: HitPay Account Status Customers API
  slug: postman-hitpay-customers-api
- collection_type: postman
  name: HitPay Account Status Invoices API
  slug: postman-hitpay-invoices-api
- collection_type: postman
  name: HitPay Account Status Notifications API
  slug: postman-hitpay-notifications-api
- collection_type: postman
  name: HitPay Account Status Orders API
  slug: postman-hitpay-orders-api
- collection_type: postman
  name: HitPay Account Status Payment Requests API
  slug: postman-hitpay-payment-requests-api
- collection_type: postman
  name: HitPay Account Status Product Category API
  slug: postman-hitpay-product-category-api
- collection_type: postman
  name: HitPay Account Status Products API
  slug: postman-hitpay-products-api
- collection_type: postman
  name: HitPay Account Status Readers API
  slug: postman-hitpay-readers-api
- collection_type: postman
  name: HitPay Account Status Recurring Billing API
  slug: postman-hitpay-recurring-billing-api
- collection_type: postman
  name: HitPay Account Status Refund API
  slug: postman-hitpay-refund-api
- collection_type: postman
  name: HitPay Account Status Refunds API
  slug: postman-hitpay-refunds-api
- collection_type: postman
  name: HitPay Account Status Remitters API
  slug: postman-hitpay-remitters-api
- collection_type: postman
  name: HitPay Account Status Staffs API
  slug: postman-hitpay-staffs-api
- collection_type: postman
  name: HitPay Account Status Static Qr API
  slug: postman-hitpay-static-qr-api
- collection_type: postman
  name: HitPay Account Status Subscription Plan API
  slug: postman-hitpay-subscription-plan-api
- collection_type: postman
  name: HitPay Account Status Subscription Plans API
  slug: postman-hitpay-subscription-plans-api
- collection_type: postman
  name: HitPay Account Status Transfers API
  slug: postman-hitpay-transfers-api
- collection_type: postman
  name: HitPay Account Status Virtual Accounts API
  slug: postman-hitpay-virtual-accounts-api
- collection_type: postman
  name: HitPay Account Status Webhook Events API
  slug: postman-hitpay-webhook-events-api
- collection_type: open
  name: HitPay Account Status API
  slug: open-hitpay-account-status-api
- collection_type: open
  name: HitPay Account Status Balances API
  slug: open-hitpay-balances-api
- collection_type: open
  name: HitPay Account Status Beneficiaries API
  slug: open-hitpay-beneficiaries-api
- collection_type: open
  name: HitPay Account Status Charge API
  slug: open-hitpay-charge-api
- collection_type: open
  name: HitPay Account Status Charges API
  slug: open-hitpay-charges-api
- collection_type: open
  name: HitPay Account Status Customers API
  slug: open-hitpay-customers-api
- collection_type: open
  name: HitPay Account Status Invoices API
  slug: open-hitpay-invoices-api
- collection_type: open
  name: HitPay Account Status Notifications API
  slug: open-hitpay-notifications-api
- collection_type: open
  name: HitPay Account Status Orders API
  slug: open-hitpay-orders-api
- collection_type: open
  name: HitPay Account Status Payment Requests API
  slug: open-hitpay-payment-requests-api
- collection_type: open
  name: HitPay Account Status Product Category API
  slug: open-hitpay-product-category-api
- collection_type: open
  name: HitPay Account Status Products API
  slug: open-hitpay-products-api
- collection_type: open
  name: HitPay Account Status Readers API
  slug: open-hitpay-readers-api
- collection_type: open
  name: HitPay Account Status Recurring Billing API
  slug: open-hitpay-recurring-billing-api
- collection_type: open
  name: HitPay Account Status Refund API
  slug: open-hitpay-refund-api
- collection_type: open
  name: HitPay Account Status Refunds API
  slug: open-hitpay-refunds-api
- collection_type: open
  name: HitPay Account Status Remitters API
  slug: open-hitpay-remitters-api
- collection_type: open
  name: HitPay Account Status Staffs API
  slug: open-hitpay-staffs-api
- collection_type: open
  name: HitPay Account Status Static Qr API
  slug: open-hitpay-static-qr-api
- collection_type: open
  name: HitPay Account Status Subscription Plan API
  slug: open-hitpay-subscription-plan-api
- collection_type: open
  name: HitPay Account Status Subscription Plans API
  slug: open-hitpay-subscription-plans-api
- collection_type: open
  name: HitPay Account Status Transfers API
  slug: open-hitpay-transfers-api
- collection_type: open
  name: HitPay Account Status Virtual Accounts API
  slug: open-hitpay-virtual-accounts-api
- collection_type: open
  name: HitPay Account Status Webhook Events API
  slug: open-hitpay-webhook-events-api
common:
- group: other
  href: https://artifacts.apis.io/hitpay/capabilities/hitpay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hitpay-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hitpay/overview
- group: agent
  href: https://artifacts.apis.io/hitpay/agentic-access/hitpay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hitpay-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hitpay/security/hitpay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hitpay-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hitpay/security/hitpay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hitpay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hitpay/security/hitpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hitpay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hitpay/authentication/hitpay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hitpay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hit-pay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hit-pay
- group: company
  title: ''
  type: Website
  url: https://www.hitpayapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hitpayapp.com/apis
- group: commercial
  href: https://artifacts.apis.io/hitpay/plans/hitpay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hitpay-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hitpay/rate-limits/hitpay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hitpay-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hitpay/finops/hitpay-finops.yml
  title: ''
  type: FinOps
  url: finops/hitpay-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hitpayapp.com/blog
- group: docs
  href: https://artifacts.apis.io/hitpay/openapi/_original/hitpay-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/hitpay-openapi-original.json
- group: agent
  href: https://artifacts.apis.io/hitpay/mcp/hitpay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hitpay-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hitpay/llms/hitpay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hitpay-llms.txt
- group: build
  href: https://artifacts.apis.io/hitpay/packages/hitpay-packages.yml
  title: ''
  type: Packages
  url: packages/hitpay-packages.yml
- group: build
  href: https://artifacts.apis.io/hitpay/cli/hitpay-cli.yml
  title: ''
  type: CLI
  url: cli/hitpay-cli.yml
- group: start
  href: https://artifacts.apis.io/hitpay/sandbox/hitpay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hitpay-sandbox.yml
- group: design
  href: https://artifacts.apis.io/hitpay/conventions/hitpay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hitpay-conventions.yml
- group: operate
  href: https://artifacts.apis.io/hitpay/changelog/hitpay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hitpay-changelog.yml
- group: design
  href: https://artifacts.apis.io/hitpay/lifecycle/hitpay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hitpay-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hitpay/conformance/hitpay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hitpay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.hitpayapp.com/security
- group: design
  href: https://artifacts.apis.io/hitpay/components/hitpay-components.yml
  title: ''
  type: Components
  url: components/hitpay-components.yml
- group: design
  href: https://artifacts.apis.io/hitpay/data-model/hitpay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hitpay-data-model.yml
- group: design
  href: https://artifacts.apis.io/hitpay/errors/hitpay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hitpay-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hitpay/asyncapi/hitpay-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hitpay-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/hitpay/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/hitpay/overlays/hitpay-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hitpay-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hitpayapp.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hitpayapp.com/apis/overview
- group: operate
  title: ''
  type: Support
  url: https://hitpay.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://hitpayapp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.hit-pay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hitpayapp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hitpayapp.com/privacy-policy
created: '2026-07-17'
description: HitPay is a Singapore-headquartered all-in-one payments platform for small and medium businesses across Asia-Pacific, unifying online checkout, point of sale, and B2B billing. Its REST API creates hosted Payment Requests, runs Recurring Billing on saved cards, and issues Refunds, with first-class Southeast Asian local methods (PayNow, GrabPay, WeChat Pay, Alipay, ShopeePay, Atome) alongside cards. Requests authenticate with the X-BUSINESS-API-KEY header.
finops:
- has_sources: true
  method: derived
  name: Hitpay Finops
  primary_unit: transaction
  service_category: ''
  slug: hitpay-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hitpay.png
layout: provider
mcp_servers:
- description: Remote MCP server at hitpay-mcp.vercel.app over HTTP; 39 tools listed.
  name: HitPay MCP Server
  slug: hitpay-api
modified: '2026-07-17'
name: HitPay
nav: Providers
network: true
overview: 'HitPay publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Status API, Balances API, Beneficiaries API, and 21 more. Tagged areas include Payments, Fintech, PayNow, Southeast Asia, and Small Business.


  The HitPay catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  HitPay''s developer surface includes authentication, documentation, engineering blog, CLI, sandbox, changelog, getting-started guide, and 32 more developer resources.'
plans:
- name: Hitpay Plans Pricing
  plan_count: 12
  slug: hitpay-plans-pricing
- name: Hitpay Price Estimates
  plan_count: 0
  slug: hitpay-price-estimates
random_paper: 7
rate_limits:
- limit_count: 1
  name: Hitpay Rate Limits
  slug: hitpay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: HitPay API Rules
  rule_count: 50
  severity_counts:
    error: 37
    hint: 0
    info: 5
    warn: 8
  slug: hitpay-rules
score:
  band: strong
  composite: 65.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 58.5
    catalog_earned_first_party: 12.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 78.9
    contract_governance: 31.8
    contract_quality: 58.3
    developer_ergonomics: 69.6
    discoverability: 75.0
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 48.0
      total: 50
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/hitpay/hitpay-2026-07-25T221304.png
security:
- kind: authentication
  name: Hitpay Authentication
  slug: hitpay-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Hitpay Domain Security
  slug: hitpay-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Hitpay Vulnerability Disclosure
  slug: hitpay-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Hitpay Trust Center
  slug: hitpay-trust-center
  summary_line: PCI DSS, MAS Major Payment Institution (MPI)
skill_count: 4
skills:
- name: Collect a payment with HitPay
  slug: hitpay-collect-payment
- name: Set up HitPay recurring billing
  slug: hitpay-recurring-billing
- name: Refund a HitPay charge
  slug: hitpay-refund-charge
- name: Verify a HitPay webhook
  slug: hitpay-verify-webhook
slug: hitpay
tags:
- Payments
- Fintech
- PayNow
- Southeast Asia
- Small Business
website: https://www.hitpayapp.com/
---
