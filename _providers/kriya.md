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
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://api.kriya.co/payments/
  baseurl_source: declared
  description: The Buyers API from Kriya — 6 operation(s) for buyers.
  name: Kriya Buyers API
  slug: kriya-buyers-api
- baseURL: https://api.kriya.co/payments/
  baseurl_source: declared
  description: The Onboarding API API from Kriya — 2 operation(s) for onboarding api.
  name: Kriya Onboarding API API
  slug: kriya-onboarding-api-api
- baseURL: https://api.kriya.co/payments/
  baseurl_source: declared
  description: The OnboardingJourney API from Kriya — 1 operation(s) for onboardingjourney.
  name: Kriya OnboardingJourney API
  slug: kriya-onboardingjourney-api
- baseURL: https://api.kriya.co/payments/
  baseurl_source: declared
  description: The Orders API from Kriya — 7 operation(s) for orders.
  name: Kriya Orders API
  slug: kriya-orders-api
- baseURL: https://api.kriya.co/payments/
  baseurl_source: declared
  description: The Payments API from Kriya — 3 operation(s) for payments.
  name: Kriya Payments API
  slug: kriya-payments-api
- baseURL: https://api.kriya.co/payments/
  baseurl_source: declared
  description: The Scenario API from Kriya — 1 operation(s) for scenario.
  name: Kriya Scenario API
  slug: kriya-scenario-api
artifact_total: 17
asyncapis:
- description: ''
  name: Kriya Payments Webhooks
  slug: kriya-payments-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kriya Onboarding Buyers API
  slug: open-kriya-buyers-api
- collection_type: open
  name: Kriya Onboarding Buyers Onboarding API API
  slug: open-kriya-onboarding-api-api
- collection_type: open
  name: Kriya Onboarding Buyers OnboardingJourney API
  slug: open-kriya-onboardingjourney-api
- collection_type: open
  name: Kriya Onboarding Buyers Orders API
  slug: open-kriya-orders-api
- collection_type: open
  name: Kriya Onboarding Buyers Payments API
  slug: open-kriya-payments-api
- collection_type: open
  name: Kriya Onboarding Buyers Scenario API
  slug: open-kriya-scenario-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kriya-onboarding-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Kriya
nav: Providers
network: true
overview: 'Kriya publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Buyers API, Onboarding API API, OnboardingJourney API, and 3 more. Tagged areas include Company, Fintech, Payments, Embedded Finance, and Buy Now Pay Later.


  The Kriya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kriya''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 20 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 54.5
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 37.7
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
