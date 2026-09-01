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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Pliant''s Pro API (Customer) is the REST API that powers hi.health by Pliant. It lets a customer programmatically access Pliant credit-card data and features: issue and manage virtual and physical card'
  name: Pliant Pro API (Customer)
  slug: pliant-pro-api-customer
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getpliant.com/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://customer-api.getpliant.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://customer-api.getpliant.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://customer-api.getpliant.com/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.getpliant.com/en/
- group: company
  title: ''
  type: Blog
  url: https://getpliant.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://getpliant.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getpliant.com/?language=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getpliant.com/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getpliant.com/en/imprint
- group: operate
  title: ''
  type: StatusPage
  url: https://customer-api.getpliant.com/page/status
- group: operate
  title: ''
  type: Deprecation
  url: https://customer-api.getpliant.com/docs/versioning
- group: design
  title: ''
  type: Webhooks
  url: https://customer-api.getpliant.com/docs/authenticated-callback-usage
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getpliant
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hi-health-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hi-health-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hi-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hi-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hi-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hi-health-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hi-health-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hi-health-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hi-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hi-health-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hi-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getpliant.com/.well-known/security.txt
created: '2026-07-17'
description: 'Hi Health (hi.health) is a European digital-health payments company, originally a Speedinvest portfolio company, now operating as "hi.health by Pliant". The hi.health domain redirects to Pliant, and the product replaces legacy insurance reimbursement with a cashless, real-time claims-and-payments platform for health & care, home & property, travel, corporate/group, and auto/mobility insurance. It is built on Pliant''s card-issuing infrastructure and exposed through Pliant''s Pro API (Customer): a REST API for issuing and managing virtual and physical credit cards, cardholders, card accounts, transactions, receipts, accounting integration, and payments, with OAuth 2.0 (Auth0) client-credentials authentication, asynchronous callback webhooks, a sandbox environment, PCI-DSS certified sensitive-card-data endpoints, and a hosted developer portal, changelog, and status page.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hi-health.png
layout: provider
modified: '2026-07-19'
name: Hi Health
nav: Providers
network: true
overview: 'Hi Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Insurance, Payments, and Fintech.


  Hi Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 32.9
  previous_composite: 31.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hi-health/refs/heads/main/screenshots/hi-health-2026-07-25T221130.png
security:
- kind: authentication
  name: Hi Health Authentication
  slug: hi-health-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hi Health Domain Security
  slug: hi-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hi Health Vulnerability Disclosure
  slug: hi-health-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hi-health
tags:
- Company
- Health
- Insurance
- Payments
- Fintech
- Card Issuing
- Reimbursement
- Insurtech
- Digital Health
- Speedinvest
website: https://getpliant.com/en/developers
---
