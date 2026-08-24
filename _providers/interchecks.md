---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for creating and managing recipients, destination payment accounts (bank, card, PayPal, Venmo, prepaid), payments accepted in the Recipient Portal or a hosted widget, and transactions for imm
  name: Interchecks Payments API v2
  slug: interchecks-payments-api-v2
artifact_total: 6
asyncapis:
- description: ''
  name: Interchecks Webhooks
  slug: interchecks-webhooks
common:
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
overview: 'Interchecks publishes 1 API on the [APIs.io](https://apis.io/) network: Payments API v2. Tagged areas include Payments, Payouts, ACH, Real-Time Payments, and Instant Payments.


  The Interchecks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Interchecks'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 21 more developer resources.'
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
  composite: 48.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 58.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
- Webhooks
website: https://home.interchecks.com/
---
