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
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'OAuth2 client-credentials REST API for B2B BNPL: checkout sessions, hosted payment page, backend order creation, order management, captures (invoices), payment confirmation, refunds/credit notes, and '
  name: Billie Payment API
  slug: billie-payment-api
artifact_total: 5
asyncapis:
- description: ''
  name: Billie Webhooks
  slug: billie-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/billie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://billie.io/coordinated-vulnerability-disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/billie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billie.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.billie.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billie.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.billie.io/reference/integration-checklist
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.billie.io/docs/get-started-with-billies-api-integration
- group: auth
  title: ''
  type: Authentication
  url: authentication/billie-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/billie-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/billie-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/billie-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/billie-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/billie-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/billie-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/billie-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/billie-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/billie-conventions.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/billie-decline-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/billie-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/billie-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.billie.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/billie-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/billie-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/billie-components.yml
- group: operate
  title: ''
  type: Support
  url: https://help.billie.io/merchant/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.billie.io/merchant/s/
- group: company
  title: ''
  type: Blog
  url: https://www.billie.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ozean12
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.billie.io/public/registration
- group: start
  title: ''
  type: Login
  url: https://dashboard.billie.io/public/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.billie.io/datenschutz
- group: other
  title: ''
  type: Imprint
  url: https://www.billie.io/impressum
created: '2026-07-17'
description: Billie is a Berlin-based B2B "buy now, pay later" (BNPL) payment provider that lets merchants offer business buyers invoice purchase, pay-after-delivery, and installment terms at checkout while Billie assumes the credit and fraud risk and pays the merchant out. Its Payment API v2 (paella.billie.io) uses OAuth 2.0 client-credentials and covers checkout sessions, a hosted payment page, direct backend order creation, order management, captures (invoicing), payment confirmation, refunds/credit notes, and a webhook event surface. Billie also ships an embeddable checkout widget, a PHP SDK, e-commerce plugins (Shopware, Magento, WooCommerce, JTL), and partner routes via Klarna, Mollie, Adyen, Stripe, and Kustom. Backed by Creandum and Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/billie.png
layout: provider
modified: '2026-07-18'
name: Billie
nav: Providers
network: true
overview: 'Billie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, BNPL, and Buy Now Pay Later.


  The Billie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Billie''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 27 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 38.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/screenshots/billie-2026-07-25T202942.png
security:
- kind: authentication
  name: Billie Authentication
  slug: billie-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Billie Domain Security
  slug: billie-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Billie Vulnerability Disclosure
  slug: billie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: billie
tags:
- Company
- Fintech
- Payments
- BNPL
- Buy Now Pay Later
- B2B
- Invoicing
- Checkout
- Germany
website: https://www.billie.io/
---
