---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: Checkout Session management
  name: Super Payments Checkout Sessions API
  slug: super-payments-checkout-sessions-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: The Customer API from Super Payments — 2 operation(s) for customer.
  name: Super Payments Customer API
  slug: super-payments-customer-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: Manage payment links for one-time payments
  name: Super Payments Payment Links API
  slug: super-payments-payment-links-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: The Payment Methods API from Super Payments — 4 operation(s) for payment methods.
  name: Super Payments Payment Methods API
  slug: super-payments-payment-methods-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: Payment processing and management
  name: Super Payments Payments API
  slug: super-payments-payments-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: Refund management
  name: Super Payments Refunds API
  slug: super-payments-refunds-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: Rewards configuration and calculation and management
  name: Super Payments Rewards API
  slug: super-payments-rewards-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: Settlement batches, details, and reconciliation
  name: Super Payments Settlements API
  slug: super-payments-settlements-api
- baseURL: https://api.superpayments.com/2026-04-01
  baseurl_source: declared
  description: The Webhooks API from Super Payments — 0 operation(s) for webhooks.
  name: Super Payments Webhooks API
  slug: super-payments-webhooks-api
artifact_total: 30
asyncapis:
- description: Super Payments delivers real-time event notifications to merchant-configured endpoints. Webhooks are configured per Integration in the Business Portal. Every request carries a super-signature header (
  name: Super Payments Webhooks
  slug: super-payments-webhooks-asyncapi
collections:
- collection_type: postman
  name: Super Payments Checkout Sessions API
  slug: postman-super-payments-checkout-sessions-api
- collection_type: postman
  name: Super Payments Checkout Sessions Customer API
  slug: postman-super-payments-customer-api
- collection_type: postman
  name: Super Payments Checkout Sessions Payment Links API
  slug: postman-super-payments-payment-links-api
- collection_type: postman
  name: Super Payments Checkout Sessions Payment Methods API
  slug: postman-super-payments-payment-methods-api
- collection_type: postman
  name: Super Checkout Sessions Payments API
  slug: postman-super-payments-payments-api
- collection_type: postman
  name: Super Payments Checkout Sessions Refunds API
  slug: postman-super-payments-refunds-api
- collection_type: postman
  name: Super Payments Checkout Sessions Rewards API
  slug: postman-super-payments-rewards-api
- collection_type: postman
  name: Super Payments Checkout Sessions Settlements API
  slug: postman-super-payments-settlements-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Super Payments Checkout Sessions API
  slug: open-super-payments-checkout-sessions-api
- collection_type: open
  name: Super Payments Checkout Sessions Customer API
  slug: open-super-payments-customer-api
- collection_type: open
  name: Super Payments Checkout Sessions Payment Links API
  slug: open-super-payments-payment-links-api
- collection_type: open
  name: Super Payments Checkout Sessions Payment Methods API
  slug: open-super-payments-payment-methods-api
- collection_type: open
  name: Super Checkout Sessions Payments API
  slug: open-super-payments-payments-api
- collection_type: open
  name: Super Payments Checkout Sessions Refunds API
  slug: open-super-payments-refunds-api
- collection_type: open
  name: Super Payments Checkout Sessions Rewards API
  slug: open-super-payments-rewards-api
- collection_type: open
  name: Super Payments Checkout Sessions Settlements API
  slug: open-super-payments-settlements-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/super-payments-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/super-payments-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/super-payments/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/super-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.superpayments.com/for-business
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superpayments.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superpayments.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.superpayments.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superpayments.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.superpayments.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.superpayments.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superpayments
- group: commercial
  title: ''
  type: Pricing
  url: https://www.superpayments.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://business.superpayments.com
- group: start
  title: ''
  type: Login
  url: https://business.superpayments.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.superpayments.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.superpayments.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superpayments.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.superpayments.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/super-payments-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.superpayments.com/reference/upgrading
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/super-payments-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/super-payments-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/super-payments-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/super-payments-webhooks-asyncapi.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/super-payments-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/super-payments-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/super-payments-decline-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/super-payments-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/super-payments-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/super-payments-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/super-payments-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/super-payments-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/super-payments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/super-payments-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/super-payments-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/super-payments-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Super Payments is a UK payments provider offering free card and open-banking (pay-by-bank) payment processing for businesses, funded by a customer-acquisition and cash-rewards model rather than per-transaction fees. Its REST API lets merchants create payments and checkout sessions, issue refunds, manage customers and reusable payment methods, run settlements and reconciliation, create no-code payment links, and configure cash rewards. The API uses date-based URL versioning, static API-key authentication, RFC 9457 problem+json errors, cursor pagination, HMAC-signed webhooks, an embedded super-card web component and hosted payment page, and a React Native SDK. Backed by Accel and Union Square Ventures.
image: https://framerusercontent.com/images/eAdDRGD6sLo1NlXEu8bPS71k.png
layout: provider
modified: '2026-07-21'
name: Super Payments
nav: Providers
network: true
overview: 'Super Payments publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Checkout Sessions API, Customer API, Payment Links API, and 6 more. Tagged areas include Company, Payments, Open Banking, Cash Rewards, and Checkout.


  The Super Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Super Payments'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 2
  name: Super Payments Rate Limits
  slug: super-payments-rate-limits
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 66.1
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 59.2
  previous_composite: 57.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/super-payments/refs/heads/main/screenshots/super-payments-2026-08-17T082158.png
security:
- kind: authentication
  name: Super Payments Authentication
  slug: super-payments-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Super Payments Domain Security
  slug: super-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: super-payments
tags:
- Company
- Payments
- Open Banking
- Cash Rewards
- Checkout
- Fintech
- United Kingdom
- Pay by Bank
website: https://www.superpayments.com/for-business
---
