---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'All-in-one REST API for digital investing: onboarding, accounts (GIA/ISA/JISA/SIPP), funding, custody, trading, portfolio management, transfers, cash savings, valuations, performance and reporting. OA'
  name: WealthKernel API
  slug: wealthkernel-api
artifact_total: 4
asyncapis:
- description: ''
  name: Wealthkernel Webhooks
  slug: wealthkernel-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wealthkernel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wealthkernel.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wealthkernel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wealthkernel.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wealthkernel.com/docs/api/2021-05-17
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wealthkernel.com/docs/api/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.wealthkernel.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wealthkernel
- group: start
  title: ''
  type: SignUp
  url: https://www.wealthkernel.com/enquiries
- group: operate
  title: ''
  type: Support
  url: https://www.wealthkernel.com/enquiries
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wealthkernel.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wealthkernel.com/policies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wealthkernel.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.wealthkernel.com/regulatory
- group: auth
  title: ''
  type: Authentication
  url: authentication/wealthkernel-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wealthkernel-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/wealthkernel-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wealthkernel-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wealthkernel-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wealthkernel-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wealthkernel-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wealthkernel-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/wealthkernel-openid-configuration.json
- group: design
  title: ''
  type: DataModel
  url: data-model/wealthkernel-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wealthkernel-llms.txt
created: '2026-07-17'
description: 'WealthKernel is a UK- and EU-regulated digital investing infrastructure provider that offers "investing as a service" through a single REST API. It supplies the building blocks fintechs, wealth managers and established businesses need to launch digital investing propositions: client onboarding with KYC/AML, tax-wrapper accounts (GIA, ISA, JISA, SIPP), account funding (BACS, CHAPS, open banking, direct debits), custody as a licensed UK custodian, fractional and multi-currency trading, portfolio management and rebalancing, cash savings, transfers, valuations, performance reporting and FCA transaction reporting. WealthKernel is authorised and regulated by the Financial Conduct Authority (FRN 723719), registered with Spain''s CNMV, and ISO 27001:2022 certified. The API is documented on Stoplight and secured with OAuth2 client-credentials via an OpenID Connect authorization server, with sandbox and production environments, webhooks and documented idempotency, pagination and eventual-consistency
  conventions.'
image: https://cdn.prod.website-files.com/60dee70f5b4eb4b1921e29e2/69e72e3dbb1f3b0c28b179ca_WK_Logo_2026_Light.svg
layout: provider
modified: '2026-07-21'
name: WealthKernel
nav: Providers
network: true
overview: 'WealthKernel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Investing, Wealth Management, Brokerage, and Custody.


  The WealthKernel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WealthKernel''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 47.5
  delta: 4.7
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 42.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wealthkernel Authentication
  slug: wealthkernel-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Wealthkernel Domain Security
  slug: wealthkernel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wealthkernel
tags:
- Company
- Investing
- Wealth Management
- Brokerage
- Custody
- Fintech
- Investment API
- Embedded Finance
- ISA
- SIPP
- Banking as a Service
- United Kingdom
- Europe
website: https://www.wealthkernel.com
---
