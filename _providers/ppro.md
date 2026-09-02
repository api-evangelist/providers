---
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-09-01'
api_count: 21
apis:
- description: The Authorization Endpoints API from PPRO — 5 operation(s) for authorization endpoints.
  name: PPRO Authorization Endpoints API
  slug: ppro-authorization-endpoints-api
- description: The Capture Endpoints API from PPRO — 2 operation(s) for capture endpoints.
  name: PPRO Capture Endpoints API
  slug: ppro-capture-endpoints-api
- description: Endpoints for generating and retrieving dispute reports
  name: PPRO Dispute Reports API
  slug: ppro-dispute-reports-api
- description: The Disputes API from PPRO — 6 operation(s) for disputes.
  name: PPRO Disputes API
  slug: ppro-disputes-api
- description: The Enrollment Endpoints API from PPRO — 2 operation(s) for enrollment endpoints.
  name: PPRO Enrollment Endpoints API
  slug: ppro-enrollment-endpoints-api
- description: The Internal API from PPRO — 4 operation(s) for internal.
  name: PPRO Internal API
  slug: ppro-internal-api
- description: Merchant management
  name: PPRO Merchants API
  slug: ppro-merchants-api
- description: The Payment Agreement Revocations API from PPRO — 1 operation(s) for payment agreement revocations.
  name: PPRO Payment Agreement Revocations API
  slug: ppro-payment-agreement-revocations-api
- description: The Payment Agreements API from PPRO — 2 operation(s) for payment agreements.
  name: PPRO Payment Agreements API
  slug: ppro-payment-agreements-api
- description: The payment-charge-controller API from PPRO — 1 operation(s) for payment-charge-controller.
  name: PPRO Payment Charge Controller API
  slug: ppro-payment-charge-controller-api
- description: The Payment Charges API from PPRO — 1 operation(s) for payment charges.
  name: PPRO Payment Charges API
  slug: ppro-payment-charges-api
- description: The Payment Instruments API from PPRO — 2 operation(s) for payment instruments.
  name: PPRO Payment Instruments API
  slug: ppro-payment-instruments-api
- description: The Payment Sessions API from PPRO — 3 operation(s) for payment sessions.
  name: PPRO Payment Sessions API
  slug: ppro-payment-sessions-api
- description: Person management
  name: PPRO People API
  slug: ppro-people-api
- description: Platform management
  name: PPRO Platforms API
  slug: ppro-platforms-api
- description: PSP management
  name: PPRO PS Ps API
  slug: ppro-psps-api
- description: The Refund Endpoints API from PPRO — 2 operation(s) for refund endpoints.
  name: PPRO Refund Endpoints API
  slug: ppro-refund-endpoints-api
- description: The Void Endpoints API from PPRO — 2 operation(s) for void endpoints.
  name: PPRO Void Endpoints API
  slug: ppro-void-endpoints-api
artifact_total: 26
asyncapis:
- description: ''
  name: Ppro Webhooks
  slug: ppro-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ppro-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ppro-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.ppro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developerhub.ppro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developerhub.ppro.com/global-api/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developerhub.ppro.com/global-api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developerhub.ppro.com/global-api/docs/get-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/ppro-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ppro-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ppro-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ppro-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ppro-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/ppro-failure-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ppro-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ppro.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ppro-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ppro-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/ppro-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ppro-packages.yml
- group: design
  title: ''
  type: Components
  url: components/ppro-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ppro-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ppro-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ppro-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ppro.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ppro-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ppro-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/pprodev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PPRO
- group: company
  title: ''
  type: Blog
  url: https://www.ppro.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.ppro.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.ppro.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ppro.com/legal/payment-services-agreement-general-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ppro.com/legal/privacy-notice/
- group: commercial
  title: ''
  type: Plans
  url: plans/ppro-plans-pricing.yml
created: '2026-08-26'
description: PPRO is a local payments infrastructure company that lets payment service providers, acquirers, platforms and enterprise merchants accept the payment methods consumers actually use in their own market — bank redirects such as iDEAL, BLIK, Przelewy24 and Pay By Bank, wallets such as Alipay, WeChat Pay, Amazon Pay, Cash App Pay, TWINT and Swish, cash and voucher rails such as Boleto, OXXO, Multibanco and Indomaret, SEPA Direct Debit, Pix, UPI, BNPL and stablecoins — through a single REST integration. The PPRO Global API is an OpenAPI 3.1 platform built around four core objects (payment charges, payment instruments, payment agreements and payment sessions) plus captures, refunds, voids, fund statuses, disputes and chargebacks, with CloudEvents 1.0.2 webhooks, an idempotency-key contract, a documented token-bucket rate limit, a Drop-in Checkout component library and a hosted Model Context Protocol server so coding agents can call the platform directly.
image: https://files.readme.io/920bf80-ppro_logo_black.svg
layout: provider
mcp_servers:
- description: PPRO publishes a first-party, hosted Model Context Protocol server that fronts the Global API. It is a streamable-HTTP MCP server (serverInfo global-api-mcp 1.0.0, protocolVersion 2025-06-18) exposing
  name: PPRO Global API MCP Server
  slug: ppro-global-api-mcp-server
modified: '2026-08-26'
name: PPRO
nav: Providers
network: true
overview: 'PPRO publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Authorization Endpoints API, Capture Endpoints API, Dispute Reports API, and 15 more. Tagged areas include Payments, Local Payment Methods, Financial-Services, Fintech, and Acquiring.


  The PPRO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PPRO''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 28 more developer resources.'
plans:
- name: Ppro Plans Pricing
  plan_count: 0
  slug: ppro-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Ppro Rate Limits
  slug: ppro-rate-limits
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 53.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ppro Authentication
  slug: ppro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ppro Domain Security
  slug: ppro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ppro Vulnerability Disclosure
  slug: ppro-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Ppro Trust Center
  slug: ppro-trust-center
  summary_line: trust center published
slug: ppro
tags:
- Payments
- Local Payment Methods
- Financial-Services
- Fintech
- Acquiring
- Checkout
- E-Commerce
- Digital Wallet
- Recurring Payments
- Disputes
- Chargebacks
- Company
website: https://www.ppro.com/
---
