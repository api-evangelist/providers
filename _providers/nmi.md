---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 8
apis:
- description: The core NMI Payment API (Direct Post) enables transaction processing across card-present, ecommerce, mobile, and alternative payment methods including Apple Pay and Google Pay. Supports authorization
  name: NMI Payment API
  slug: nmi-payment-api
- description: The NMI Customer Vault API enables secure storage and management of customer payment credentials at Level 1 PCI compliance. Supports creating, updating, and retrieving tokenized customer payment profi
  name: NMI Customer Vault API
  slug: nmi-customer-vault-api
- description: The NMI Recurring Billing API provides subscription and recurring payment management including plan creation, subscription enrollment, billing cycle configuration, and automated payment scheduling. Su
  name: NMI Recurring Billing API
  slug: nmi-recurring-billing-api
- description: The NMI Query API provides transaction data retrieval and reporting capabilities including detailed transaction records, customer data, invoice information, and account reporting with customizable que
  name: NMI Query API
  slug: nmi-query-api
- description: The NMI Merchant Onboarding API enables payment facilitators and ISOs to programmatically onboard merchants through a complete application workflow. Supports application creation and submission, autom
  name: NMI Merchant Onboarding API
  slug: nmi-merchant-onboarding-api
- description: The NMI Webhooks API provides event-driven integration for real-time notifications on transaction events, recurring billing updates, settlements, and chargebacks. Includes webhook registration managem
  name: NMI Webhooks API
  slug: nmi-webhooks-api
- description: The NMI Three Step Redirect API keeps merchants outside the scope of transmitting sensitive payment data by routing cardholder information directly to NMI servers. Supports transaction, recurring bill
  name: NMI Three Step Redirect API
  slug: nmi-three-step-redirect-api
- description: The NMI Customer-Present Cloud API enables browser-based point-of-sale payment processing without software installation. Supports cloud device registration and control, payment requests on connected d
  name: NMI Customer-Present Cloud API
  slug: nmi-customer-present-cloud-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nmi-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.nmi.com
- group: other
  title: ''
  type: Developer Experience
  url: https://www.nmi.com/dev-experience/
- group: build
  title: ''
  type: SDKs
  url: https://www.nmi.com/payment-gateway-sdks-apis/
- group: start
  title: ''
  type: Integration Portal
  url: https://secure.networkmerchants.com/gw/merchants/resources/integration/integration_portal.php
- group: start
  title: ''
  type: Sandbox
  url: https://docs.nmi.com/docs/sandbox-testing
- group: operate
  title: ''
  type: Support
  url: https://support.nmi.com
- group: company
  title: ''
  type: Blog
  url: https://www.nmi.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.nmi.com/about-us/contact-us/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: NMI is a global embedded payments enablement platform providing full-stack payment technology with REST APIs for payment processing, tokenization, recurring billing, customer vault management, and payment facilitation across ecommerce, in-person, mobile, and unattended acquisition channels. With over 20 years of operation, NMI connects 1.2 million active merchants, 6,000 channel partners, and 150+ processor connections, processing over $502 billion in annual payments volume.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nmi.png
layout: provider
modified: '2026-06-13'
name: NMI
nav: Providers
network: true
overview: 'NMI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Payment API, Customer Vault API, Recurring Billing API, and 3 more. Tagged areas include Payments, Payment Gateway, Payment Processing, Tokenization, and Recurring Billing.


  NMI''s developer surface includes developer portal, sandbox, support, engineering blog, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 36.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nmi/refs/heads/main/screenshots/nmi-2026-06-20T190340.png
security:
- kind: domain-security
  name: Nmi Domain Security
  slug: nmi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nmi
tags:
- Payments
- Payment Gateway
- Payment Processing
- Tokenization
- Recurring Billing
- Customer Vault
- Fintech
- Embedded Payments
- Payment Facilitation
website: https://docs.nmi.com
---
