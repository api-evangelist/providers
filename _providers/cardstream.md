---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: Hosted Payment Pages (HPP) integration. The merchant's browser POSTs a URL-encoded request to the Gateway, which collects and processes the cardholder's payment details on a Cardstream-hosted page (li
  name: Cardstream Gateway - Hosted Integration
  slug: cardstream-gateway-hosted
- description: Server-to-server integration. The merchant collects payment details on its own secure server and sends a URL-encoded HTTP POST directly to the Gateway for processing, supporting sales, refunds, cancel
  name: Cardstream Gateway - Direct Integration
  slug: cardstream-gateway-direct
- description: An enhancement to the Direct Integration that submits multiple transactions in a single multipart/mixed HTTP POST. The Gateway queues the transactions and returns a batch reference number used to down
  name: Cardstream Gateway - Batch Integration
  slug: cardstream-gateway-batch
- description: A client-side library where only the individual input fields that collect sensitive cardholder data are hosted by the Gateway while the rest of the payment form is served by the merchant. On submissio
  name: Cardstream Hosted Payment Fields
  slug: cardstream-hosted-payment-fields
artifact_total: 7
asyncapis:
- description: ''
  name: Cardstream Webhooks
  slug: cardstream-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardstream-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardstream.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cardstream.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://guides.gitbook.io/integrationguide/
- group: docs
  title: ''
  type: APIReference
  url: https://guides.gitbook.io/integrationguide/gateway-functionality/features/new-transactions/request-fields
- group: start
  title: ''
  type: GettingStarted
  url: https://guides.gitbook.io/integrationguide/getting-started/setting-up-your-integration
- group: auth
  title: ''
  type: Authentication
  url: https://guides.gitbook.io/integrationguide/getting-started/setting-up-your-integration/authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cardstream
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cardstream.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.cardstream.com/hc/
- group: start
  title: ''
  type: Login
  url: https://mms.cardstream.com/
- group: company
  title: ''
  type: Blog
  url: https://cardstream.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardstream.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cardstream
- group: build
  title: ''
  type: Packages
  url: packages/cardstream-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cardstream-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cardstream-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cardstream-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cardstream-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cardstream-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/cardstream-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cardstream-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://guides.gitbook.io/integrationguide/getting-started/introduction-to-our-gateway/security-and-compliance
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cardstream-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cardstream-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cardstream-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/cardstream-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cardstream-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cardstream-llms.txt
created: '2026-07-24'
description: Cardstream is an independent United Kingdom payment gateway providing a white-label payment platform that banks, PSPs, ISOs, acquirers and software companies resell under their own brand. It connects merchants to card schemes (Visa, Mastercard), digital wallets and 150+ Alternative Payment Methods from a single integration, with PCI DSS Level 1 processing, tokenisation, recurring billing, 3-D Secure 2 authentication, risk and fraud checking, and dynamic currency conversion. Its developer surface is a mature form-post gateway API exposed through three integration methods — Hosted (Hosted Payment Pages and Hosted Payment Fields), Direct (server-to-server), and Batch — documented in a public GitBook integration guide and supported by SDKs for PHP, Java, Node.js, Go, Ruby, C#, iOS and Android plus e-commerce modules. Requests are HTTP POST with application/x-www-form-urlencoded fields authenticated by merchantID plus optional password, HMAC message signing and IP allow-listing;
  the gateway does not publish a downloadable OpenAPI/Swagger definition or a JSON/REST surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Cardstream
nav: Providers
network: true
overview: 'Cardstream publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and White Label.


  The Cardstream catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cardstream''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, changelog, sandbox, and 22 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 50.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardstream/refs/heads/main/screenshots/cardstream-2026-07-25T204520.png
security:
- kind: authentication
  name: Cardstream Authentication
  slug: cardstream-authentication
  summary_line: merchantID/password/message-signing/ip-allowlist · 4 schemes
- kind: domain-security
  name: Cardstream Domain Security
  slug: cardstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cardstream
tags:
- Payments
- United Kingdom
- Payment Gateway
- Payment Processing
- White Label
- Card Payments
- Acquiring
- Hosted Payment Pages
- Tokenization
- 3D Secure
- Alternative Payment Methods
- Subscription
website: https://cardstream.com/
---
