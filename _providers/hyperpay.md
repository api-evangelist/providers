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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 5
  name: Hyperpay Agentic Access
  operation_count: 9
  slug: hyperpay-agentic-access
  summary_line: 9 operations · 6 acting · 5 human-in-the-loop
api_count: 1
apis:
- description: HyperSplit distributes a single collected payment across multiple sub-merchants or beneficiaries for marketplace and platform payout scenarios. Onboarding and API access are arranged with a HyperPay a
  name: HyperPay HyperSplit
  slug: hyperpay-hypersplit
- description: HyperBill issues invoices and shareable payment links that collect payment through the HyperPay platform without a custom checkout integration.
  name: HyperPay HyperBill
  slug: hyperpay-hyperbill
- baseURL: https://eu-prod.oppwa.com/v1
  baseurl_source: declared
  description: Hosted widget checkout preparation and result.
  name: HyperPay COPYandPAY API
  slug: hyperpay-copyandpay-api
- baseURL: https://eu-prod.oppwa.com/v1
  baseurl_source: declared
  description: Server-to-Server payments and back-office operations.
  name: HyperPay Payments API
  slug: hyperpay-payments-api
- baseURL: https://eu-prod.oppwa.com/v1
  baseurl_source: declared
  description: Query the status of a prior payment.
  name: HyperPay Query API
  slug: hyperpay-query-api
- baseURL: https://eu-prod.oppwa.com/v1
  baseurl_source: declared
  description: Tokenization of payment instruments for one-click and recurring.
  name: HyperPay Registrations API
  slug: hyperpay-registrations-api
artifact_total: 24
asyncapis:
- description: ''
  name: Hyperpay Webhooks
  slug: hyperpay-webhooks
collections:
- collection_type: postman
  name: HyperPay Payment COPYandPAY API
  slug: postman-hyperpay-copyandpay-api
- collection_type: postman
  name: HyperPay Payment COPYandPAY Payments API
  slug: postman-hyperpay-payments-api
- collection_type: postman
  name: HyperPay Payment COPYandPAY Query API
  slug: postman-hyperpay-query-api
- collection_type: postman
  name: HyperPay Payment COPYandPAY Registrations API
  slug: postman-hyperpay-registrations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HyperPay Payment COPYandPAY API
  slug: open-hyperpay-copyandpay-api
- collection_type: open
  name: HyperPay Payment COPYandPAY Payments API
  slug: open-hyperpay-payments-api
- collection_type: open
  name: HyperPay Payment COPYandPAY Query API
  slug: open-hyperpay-query-api
- collection_type: open
  name: HyperPay Payment COPYandPAY Registrations API
  slug: open-hyperpay-registrations-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hyperpay/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperpay-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hyperpay-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hyperpay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperpay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperpay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hyperpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hyperpay.docs.oppwa.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperpay
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperpay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperpay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperpay-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hyperpay.com/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hyperpay.docs.oppwa.com/
- group: docs
  title: ''
  type: APIReference
  url: https://hyperpay.docs.oppwa.com/reference/parameters
- group: start
  title: ''
  type: GettingStarted
  url: https://hyperpay.docs.oppwa.com/tutorials/integration-guide
- group: operate
  title: ''
  type: Support
  url: https://www.hyperpay.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyperpay.com/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/hyperpay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hyperpay-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hyperpay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hyperpay-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hyperpay-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/hyperpay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/hyperpay-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hyperpay-result-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/hyperpay-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hyperpay-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/hyperpay-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hyperpay-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hyperpay-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/hyperpay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hyperpay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hyperpay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: HyperPay is a MENA / Saudi Arabia online payment gateway built on the ACI / OPPWA Open Payment Platform. Its REST API powers the COPYandPAY hosted widget and a Server-to-Server integration, accepting cards (VISA, MASTER, AMEX), the Saudi domestic mada scheme, STC Pay, and Apple Pay, priced and settled in SAR. Additional products include HyperSplit (marketplace payouts) and HyperBill (invoicing).
finops:
- name: Hyperpay Finops
  service_category: Payment Processing
  slug: hyperpay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperpay.png
layout: provider
modified: '2026-07-18'
name: HyperPay
nav: Providers
network: true
overview: 'HyperPay publishes 4 APIs on the [APIs.io](https://apis.io/) network, including COPYandPAY API, Payments API, Query API, and 1 more. Tagged areas include Payments, Payment Gateway, Fintech, MENA, and Saudi Arabia.


  The HyperPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HyperPay''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, sandbox, and 28 more developer resources.'
plans:
- name: Hyperpay Plans Pricing
  plan_count: 2
  slug: hyperpay-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Hyperpay Rate Limits
  slug: hyperpay-rate-limits
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 59.4
    developer_ergonomics: 74.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 62.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperpay/refs/heads/main/screenshots/hyperpay-2026-07-25T221905.png
security:
- kind: authentication
  name: Hyperpay Authentication
  slug: hyperpay-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Hyperpay Domain Security
  slug: hyperpay-domain-security
  summary_line: HSTS
- kind: vulnerability-disclosure
  name: Hyperpay Vulnerability Disclosure
  slug: hyperpay-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Hyperpay Trust Center
  slug: hyperpay-trust-center
  summary_line: PCI-DSS Level 1, SAMA (Saudi Central Bank) licensed payment service provider
slug: hyperpay
tags:
- Payments
- Payment Gateway
- Fintech
- MENA
- Saudi Arabia
- mada
- Apple Pay
- Cards
website: https://www.hyperpay.com/
---
