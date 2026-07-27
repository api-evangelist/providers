---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 8
  name: Hitpay Agentic Access
  operation_count: 12
  slug: hitpay-agentic-access
  summary_line: 12 operations · 8 acting · 8 human-in-the-loop
api_count: 24
apis:
- description: The Account Status API from HitPay — 1 operation(s) for account status.
  name: HitPay Account Status API
  slug: hitpay-account-status-api
- description: The Balances API from HitPay — 3 operation(s) for balances.
  name: HitPay Balances API
  slug: hitpay-balances-api
- description: The Beneficiaries API from HitPay — 3 operation(s) for beneficiaries.
  name: HitPay Beneficiaries API
  slug: hitpay-beneficiaries-api
- description: The Charge API from HitPay — 1 operation(s) for charge.
  name: HitPay Charge API
  slug: hitpay-charge-api
- description: The Charges API from HitPay — 4 operation(s) for charges.
  name: HitPay Charges API
  slug: hitpay-charges-api
- description: The Customers API from HitPay — 2 operation(s) for customers.
  name: HitPay Customers API
  slug: hitpay-customers-api
- description: The Invoices API from HitPay — 2 operation(s) for invoices.
  name: HitPay Invoices API
  slug: hitpay-invoices-api
- description: The Notifications API from HitPay — 1 operation(s) for notifications.
  name: HitPay Notifications API
  slug: hitpay-notifications-api
- description: The Orders API from HitPay — 2 operation(s) for orders.
  name: HitPay Orders API
  slug: hitpay-orders-api
- description: The Payment Requests API from HitPay — 4 operation(s) for payment requests.
  name: HitPay Payment Requests API
  slug: hitpay-payment-requests-api
- description: The Product Category API from HitPay — 1 operation(s) for product category.
  name: HitPay Product Category API
  slug: hitpay-product-category-api
- description: The Products API from HitPay — 2 operation(s) for products.
  name: HitPay Products API
  slug: hitpay-products-api
- description: The Readers API from HitPay — 2 operation(s) for readers.
  name: HitPay Readers API
  slug: hitpay-readers-api
- description: The Recurring Billing API from HitPay — 5 operation(s) for recurring billing.
  name: HitPay Recurring Billing API
  slug: hitpay-recurring-billing-api
- description: The Refund API from HitPay — 2 operation(s) for refund.
  name: HitPay Refund API
  slug: hitpay-refund-api
- description: Refund completed PayNow or card charges.
  name: HitPay Refunds API
  slug: hitpay-refunds-api
- description: The Remitters API from HitPay — 2 operation(s) for remitters.
  name: HitPay Remitters API
  slug: hitpay-remitters-api
- description: The Staffs API from HitPay — 2 operation(s) for staffs.
  name: HitPay Staffs API
  slug: hitpay-staffs-api
- description: The Static Qr API from HitPay — 2 operation(s) for static qr.
  name: HitPay Static Qr API
  slug: hitpay-static-qr-api
- description: The Subscription Plan API from HitPay — 2 operation(s) for subscription plan.
  name: HitPay Subscription Plan API
  slug: hitpay-subscription-plan-api
- description: Reusable recurring-billing plan templates.
  name: HitPay Subscription Plans API
  slug: hitpay-subscription-plans-api
- description: The Transfers API from HitPay — 3 operation(s) for transfers.
  name: HitPay Transfers API
  slug: hitpay-transfers-api
- description: The Virtual Accounts API from HitPay — 2 operation(s) for virtual accounts.
  name: HitPay Virtual Accounts API
  slug: hitpay-virtual-accounts-api
- description: The Webhook Events API from HitPay — 2 operation(s) for webhook events.
  name: HitPay Webhook Events API
  slug: hitpay-webhook-events-api
artifact_total: 34
asyncapis:
- description: ''
  name: Hitpay Events Webhooks
  slug: hitpay-events-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hitpay-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hitpay-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hitpay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hitpay-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/hitpay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hitpay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hitpay-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hitpayapp.com/blog
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hitpay-openapi-original.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hitpay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hitpay-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hitpay-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hitpay-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hitpay-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hitpay-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hitpay-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hitpay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hitpay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.hitpayapp.com/security
- group: design
  title: ''
  type: Components
  url: components/hitpay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hitpay-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hitpay-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hitpay-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
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
- name: Hitpay Finops
  service_category: Financial Services
  slug: hitpay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hitpay.png
layout: provider
mcp_servers:
- description: ''
  name: hitpay-mcp.yml
  slug: hitpay-mcpyml
modified: '2026-07-17'
name: HitPay
nav: Providers
network: true
overview: 'HitPay publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Account Status API, Balances API, Beneficiaries API, and 21 more. Tagged areas include Payments, Fintech, PayNow, Southeast Asia, and SMB.


  The HitPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HitPay''s developer surface includes authentication, documentation, engineering blog, CLI, sandbox, changelog, getting-started guide, and 30 more developer resources.'
plans:
- name: Hitpay Plans Pricing
  plan_count: 3
  slug: hitpay-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: Hitpay Rate Limits
  slug: hitpay-rate-limits
score:
  band: strong
  composite: 68.4
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 61.3
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 68.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hitpay/refs/heads/main/screenshots/hitpay-2026-07-25T221304.png
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
slug: hitpay
tags:
- Payments
- Fintech
- PayNow
- Southeast Asia
- SMB
website: https://www.hitpayapp.com/
---
