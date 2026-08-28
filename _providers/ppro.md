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
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: PPRO's current-generation REST payments platform. Payment charges, payment instruments, payment agreements and payment sessions are the four core objects; captures, refunds and voids are sub-resources
  name: PPRO Global API
  slug: ppro-global-api
- description: Merchant boarding and enrollment for PPRO platforms and PSPs — create and amend merchants, people, platforms and PSP records, and enroll merchants onto payment methods. The boarding contract publishes
  name: PPRO Onboarding API
  slug: ppro-onboarding-api
artifact_total: 10
asyncapis:
- description: ''
  name: Ppro Webhooks
  slug: ppro-webhooks
common:
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
overview: 'PPRO publishes 2 APIs on the [APIs.io](https://apis.io/) network: Global API and Onboarding API. Tagged areas include Payments, Local Payment Methods, Financial Services, Fintech, and Acquiring.


  The PPRO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PPRO''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 26 more developer resources.'
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
  band: strong
  composite: 56.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 61.3
    developer_ergonomics: 54.2
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 73.7
  provenance:
    conformance: first-party
    contracts:
      callable: 90.9
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- Financial Services
- Fintech
- Acquiring
- Checkout
- E-commerce
- Digital Wallets
- Recurring Payments
- Disputes
- Chargebacks
- Company
website: https://www.ppro.com/
---
