---
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
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The Accounts API from Interchecks — 16 operation(s) for accounts.
  name: Interchecks Accounts API
  slug: interchecks-accounts-api
- description: OAuth 2.0 is used for authentication and authorization to the API. Client ID and Secret Key can be generated in the Developer Portal.
  name: Interchecks Authentication API
  slug: interchecks-authentication-api
- description: The Oauth2 API from Interchecks — 1 operation(s) for oauth2.
  name: Interchecks Oauth2 API
  slug: interchecks-oauth2-api
- description: Endpoints to retrieve a payer's connected accounts (aka good funds accounts) and payout method configuration for the `payer_id` designated in the URL.
  name: Interchecks Payers API
  slug: interchecks-payers-api
- description: The Payload API from Interchecks — 5 operation(s) for payload.
  name: Interchecks Payload API
  slug: interchecks-payload-api
- description: The Payment Accounts - Bank API from Interchecks — 2 operation(s) for payment accounts - bank.
  name: Interchecks Payment Accounts - Bank API
  slug: interchecks-payment-accounts-bank-api
- description: The Payment Accounts - Card API from Interchecks — 3 operation(s) for payment accounts - card.
  name: Interchecks Payment Accounts - Card API
  slug: interchecks-payment-accounts-card-api
- description: The Payment Accounts - PayPal API from Interchecks — 3 operation(s) for payment accounts - paypal.
  name: Interchecks Payment Accounts - PayPal API
  slug: interchecks-payment-accounts-paypal-api
- description: The Payments API from Interchecks — 7 operation(s) for payments.
  name: Interchecks Payments API
  slug: interchecks-payments-api
- description: The Recipient Emails API from Interchecks — 1 operation(s) for recipient emails.
  name: Interchecks Recipient Emails API
  slug: interchecks-recipient-emails-api
- description: The Recipient Verification API from Interchecks — 1 operation(s) for recipient verification.
  name: Interchecks Recipient Verification API
  slug: interchecks-recipient-verification-api
- description: The Recipients API from Interchecks — 9 operation(s) for recipients.
  name: Interchecks Recipients API
  slug: interchecks-recipients-api
- description: The Reports API from Interchecks — 5 operation(s) for reports.
  name: Interchecks Reports API
  slug: interchecks-reports-api
- description: The Test Harness API from Interchecks — 4 operation(s) for test harness.
  name: Interchecks Test Harness API
  slug: interchecks-test-harness-api
- description: The Transactions API from Interchecks — 4 operation(s) for transactions.
  name: Interchecks Transactions API
  slug: interchecks-transactions-api
- description: The Widgets API from Interchecks — 4 operation(s) for widgets.
  name: Interchecks Widgets API
  slug: interchecks-widgets-api
artifact_total: 21
asyncapis:
- description: ''
  name: Interchecks Webhooks
  slug: interchecks-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/interchecks-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/interchecks-payments-api-v2-overlay.yaml
- group: auth
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
  title: ''
  type: Authentication
  url: authentication/interchecks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/interchecks-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/interchecks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/interchecks-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/interchecks-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/interchecks-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/interchecks-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/interchecks-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/interchecks-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/interchecks-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/interchecks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/interchecks-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/interchecks-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/interchecks-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/interchecks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/interchecks-rate-limits.yml
- group: build
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
overview: 'Interchecks publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Oauth2 API, and 13 more. Tagged areas include Payments, Payouts, ACH, Real-Time Payments, and Instant Payments.


  The Interchecks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Interchecks'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 23 more developer resources.'
plans:
- name: Interchecks Plans Pricing
  plan_count: 0
  slug: interchecks-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Interchecks Rate Limits
  slug: interchecks-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 47.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Financial-Services
- Fintech
- Webhook
website: https://home.interchecks.com/
---
