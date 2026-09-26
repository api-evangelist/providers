---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-09-25'
api_count: 2
apis:
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Accounts API from Interchecks — 16 operation(s) for accounts.
  name: Interchecks Accounts API
  slug: interchecks-accounts-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: OAuth 2.0 is used for authentication and authorization to the API. Client ID and Secret Key can be generated in the Developer Portal.
  name: Interchecks Authentication API
  slug: interchecks-authentication-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: Endpoints to retrieve a payer's connected accounts (aka good funds accounts) and payout method configuration for the `payer_id` designated in the URL.
  name: Interchecks Payers API
  slug: interchecks-payers-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Payload API from Interchecks — 5 operation(s) for payload.
  name: Interchecks Payload API
  slug: interchecks-payload-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Payment Accounts - Bank API from Interchecks — 2 operation(s) for payment accounts - bank.
  name: Interchecks Payment Accounts - Bank API
  slug: interchecks-payment-accounts-bank-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Payment Accounts - Card API from Interchecks — 3 operation(s) for payment accounts - card.
  name: Interchecks Payment Accounts - Card API
  slug: interchecks-payment-accounts-card-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Payment Accounts - PayPal API from Interchecks — 3 operation(s) for payment accounts - paypal.
  name: Interchecks Payment Accounts - PayPal API
  slug: interchecks-payment-accounts-paypal-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Payments API from Interchecks — 7 operation(s) for payments.
  name: Interchecks Payments API
  slug: interchecks-payments-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Recipient Emails API from Interchecks — 1 operation(s) for recipient emails.
  name: Interchecks Recipient Emails API
  slug: interchecks-recipient-emails-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Recipient Verification API from Interchecks — 1 operation(s) for recipient verification.
  name: Interchecks Recipient Verification API
  slug: interchecks-recipient-verification-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Recipients API from Interchecks — 9 operation(s) for recipients.
  name: Interchecks Recipients API
  slug: interchecks-recipients-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Reports API from Interchecks — 5 operation(s) for reports.
  name: Interchecks Reports API
  slug: interchecks-reports-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Test Harness API from Interchecks — 4 operation(s) for test harness.
  name: Interchecks Test Harness API
  slug: interchecks-test-harness-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Transactions API from Interchecks — 4 operation(s) for transactions.
  name: Interchecks Transactions API
  slug: interchecks-transactions-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Widgets API from Interchecks — 4 operation(s) for widgets.
  name: Interchecks Widgets API
  slug: interchecks-widgets-api
- baseURL: https://prod.api.interchecks.io
  baseurl_source: declared
  description: The Oauth2 API from Interchecks — 1 operation(s) for oauth2.
  name: Interchecks Oauth2 API
  slug: interchecks-oauth2-api
artifact_total: 21
asyncapis:
- description: ''
  name: Interchecks Webhooks
  slug: interchecks-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/capabilities/interchecks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/interchecks-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/overlays/interchecks-payments-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/interchecks-payments-api-v2-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/security/interchecks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/interchecks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.interchecks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://home.interchecks.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs-v2.interchecks.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs-v2.interchecks.com/reference/about-recipients
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-v2.interchecks.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/interchecks
- group: start
  title: ''
  type: SignUp
  url: https://interchecks.com/login
- group: operate
  title: ''
  type: Support
  url: mailto:tech@interchecks.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gointerchecks/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/authentication/interchecks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/interchecks-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/conventions/interchecks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/interchecks-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/conventions/interchecks-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/interchecks-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/errors/interchecks-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/interchecks-error-codes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/errors/interchecks-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/interchecks-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/lifecycle/interchecks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/interchecks-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/changelog/interchecks-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/interchecks-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/sandbox/interchecks-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/interchecks-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/components/interchecks-components.yml
  title: ''
  type: Components
  url: components/interchecks-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/data-model/interchecks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/interchecks-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/conformance/interchecks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/interchecks-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/conformance/interchecks-conformance.yml
  title: ''
  type: Compliance
  url: conformance/interchecks-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/asyncapi/interchecks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/interchecks-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/llms/interchecks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/interchecks-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/plans/interchecks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/interchecks-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/rate-limits/interchecks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/interchecks-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/packages/interchecks-packages.yml
  title: ''
  type: Packages
  url: packages/interchecks-packages.yml
created: '2026-08-23'
description: Interchecks Technologies, Inc. is a US instant-payments platform that moves money in both directions for payers who need to fund accounts and pay out to consumers at scale. Its Payments API v2 is a REST contract covering recipient onboarding and TIN verification, destination account management across bank (Plaid-linked), debit card, PayPal, Venmo and prepaid rails, immediate disbursement transactions across ACH standard/same-day, ACH Funding Plus, RTP, Instant Deposit (Visa/Mastercard OCT), Instant Funding (AFT), paper check, eCheck and prepaid, plus embeddable widgets, settlement and activity reporting, envelope-encrypted payloads and signed webhooks. The company reports more than $50 billion processed over ten years for online gaming and prediction markets, on-demand payroll, lending and digital banking clients, and publishes PCI DSS Level 1 Service Provider and SOC 2 Type 2 attestations.
image: https://home.interchecks.com/images/interchecks-logo-white.svg
layout: provider
modified: '2026-08-23'
name: Interchecks
nav: Providers
network: true
overview: 'Interchecks publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Payers API, and 13 more. Tagged areas include Payments, Payouts, ACH, Real-Time Payments, and Instant Payments.


  The Interchecks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Interchecks'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 23 more developer resources.'
plans:
- name: Interchecks Plans Pricing
  plan_count: 0
  slug: interchecks-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Interchecks Rate Limits
  slug: interchecks-rate-limits
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 53.4
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 45.7
  provenance:
    conformance: first-party
    contracts:
      callable: 62.5
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/interchecks/refs/heads/main/screenshots/interchecks-2026-09-02T145907.png
security:
- kind: authentication
  name: Interchecks Authentication
  slug: interchecks-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Interchecks Domain Security
  slug: interchecks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: interchecks
tags:
- Payments
- Payouts
- ACH
- Real-Time Payments
- Instant Payments
- Disbursements
- Cards
- Financial Services
- Fintech
- Webhook
website: https://home.interchecks.com/
---
