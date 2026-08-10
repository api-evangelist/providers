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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: The Buyers API from Kriya — 6 operation(s) for buyers.
  name: Kriya Buyers API
  slug: kriya-buyers-api
- description: The Onboarding API API from Kriya — 2 operation(s) for onboarding api.
  name: Kriya Onboarding API API
  slug: kriya-onboarding-api-api
- description: The OnboardingJourney API from Kriya — 1 operation(s) for onboardingjourney.
  name: Kriya OnboardingJourney API
  slug: kriya-onboardingjourney-api
- description: The Orders API from Kriya — 7 operation(s) for orders.
  name: Kriya Orders API
  slug: kriya-orders-api
- description: The Payments API from Kriya — 3 operation(s) for payments.
  name: Kriya Payments API
  slug: kriya-payments-api
- description: The Scenario API from Kriya — 1 operation(s) for scenario.
  name: Kriya Scenario API
  slug: kriya-scenario-api
artifact_total: 11
asyncapis:
- description: ''
  name: Kriya Payments Webhooks
  slug: kriya-payments-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kriya.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kriya.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kriya.co/payments
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kriya.co/payments#section/API-Endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kriya.co/payments#section/Integration-Scenarios
- group: operate
  title: ''
  type: Support
  url: https://www.kriya.co/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.kriya.co/blog
- group: start
  title: ''
  type: Login
  url: https://merchant.kriya.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kriya.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kriya.co/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.kriya.co/responsible-disclosure
- group: auth
  title: ''
  type: Authentication
  url: authentication/kriya-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kriya-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kriya-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/kriya-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kriya-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kriya-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kriya-payments-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kriya-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kriya-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/kriya-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kriya-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kriya-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kriya-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kriya-domain-security.yml
created: '2026-07-17'
description: Kriya (Kriya Finance Limited, London) is a UK B2B embedded-finance and working-capital provider that lets merchants offer trade credit to their business buyers. Its products span Embedded PayLater (B2B buy-now-pay-later terms at checkout), Invoice Finance, working capital loans, buyer authentication, offline payments and a Kriya-on-Stripe integration. Kriya publishes two partner-facing REST APIs — the Payments API for buyer registration, risk decisioning, order lifecycle and payment deductions, and the Onboarding API for automating company and KYC checks — alongside a hosted Payments Journey and Onboarding Journey web flow, HMAC-signed webhooks, a dedicated test environment with scenario simulators, and e-commerce plugins for BigCommerce, Magento, nopCommerce, PrestaShop and Salesforce. Kriya was acquired by Allica Bank in October 2025.
image: https://cdn.kriya.co/images/KriyaPaymentsAPI-API-Integration-Sequence-Flow.png
layout: provider
mcp_servers:
- description: ''
  name: kriya-mcp.yml
  slug: kriya-mcpyml
modified: '2026-07-19'
name: Kriya
nav: Providers
network: true
overview: 'Kriya publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Buyers API, Onboarding API API, OnboardingJourney API, and 3 more. Tagged areas include Company, Fintech, Payments, Embedded Finance, and Buy Now Pay Later.


  The Kriya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kriya''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 19 more developer resources.'
random_paper: 80
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.6
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 18.4
  previous_composite: 48.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kriya/refs/heads/main/screenshots/kriya-2026-07-25T224301.png
security:
- kind: authentication
  name: Kriya Authentication
  slug: kriya-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kriya Domain Security
  slug: kriya-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kriya Vulnerability Disclosure
  slug: kriya-vulnerability-disclosure
  summary_line: contact published
slug: kriya
tags:
- Company
- Fintech
- Payments
- Embedded Finance
- Buy Now Pay Later
- B2B Payments
- Invoice Finance
- Lending
- Working Capital
- Onboarding
- KYC
- United Kingdom
website: https://www.kriya.co
---
