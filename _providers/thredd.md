---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
api_count: 10
apis:
- description: Create, retrieve, update, renew, replace, and convert physical and virtual cards; manage card status, cardholder details, card images, encrypted card data, and bulk card creation. The core issuing sur
  name: Thredd Cards API
  slug: thredd-cards-api
- description: Retrieve card transactions and transaction history, including load / unload operations and balances, for cards managed on the Thredd platform.
  name: Thredd Card Transactions API
  slug: thredd-transactions-api
- description: List and update card control groups, manage merchant allow / disallow lists and card acceptors, and configure card spend limits at the product level.
  name: Thredd Card Controls & Limits API
  slug: thredd-card-controls-limits-api
- description: Create, list, update, and delete 3-D Secure credentials and configuration for strong customer authentication (SCA) on issued cards.
  name: Thredd 3-D Secure (SCA) API
  slug: thredd-3ds-api
- description: Set, retrieve, and unblock cardholder PINs, and retrieve and unblock CVV2 values and their status, over the Thredd API Hub.
  name: Thredd PIN & CVV Management API
  slug: thredd-pin-cvv-api
- description: Enroll and provision cards into Apple Pay and Google Pay, generate wallet web-provisioning tokens, and manage payment-instrument tokenization for digital wallets.
  name: Thredd Digital Wallets API
  slug: thredd-digital-wallets-api
- description: Create and manage webhooks and event subscriptions to receive asynchronous notifications of card, transaction, and account events from the Thredd platform.
  name: Thredd Webhooks & Event Subscriptions API
  slug: thredd-webhooks-api
- description: Credit account and credit-program endpoints for managing credit overviews and related credit issuing capabilities on the Thredd platform.
  name: Thredd Credit API
  slug: thredd-credit-api
- description: Create customisable card numbers (custom PAN) so programs can define specific primary account number patterns for their issued cards.
  name: Thredd Custom PAN API
  slug: thredd-custom-pan-api
- description: Account-level endpoints supporting account records and money-movement flows (including ACH / micro-deposit verification) on the Thredd platform.
  name: Thredd Accounts API
  slug: thredd-accounts-api
artifact_total: 14
asyncapis:
- description: ''
  name: Thredd Webhooks
  slug: thredd-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thredd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thredd-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thredd-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thredd-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/thredd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thredd-problem-types.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thredd-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thredd-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thredd-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thredd-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://thredd.statuspage.io/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/thredd-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thredd-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thredd-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.thredd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devportal.thredd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thredd.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cardsapidocs.thredd.com/v2.0/
- group: start
  title: ''
  type: GettingStarted
  url: https://cardsapidocs.thredd.com/v2.0/docs/getting-started-1
- group: auth
  title: ''
  type: Authentication
  url: https://cardsapidocs.thredd.com/v2.0/docs/get-an-authentication-token
- group: start
  title: ''
  type: SignUp
  url: https://cardsapidocs.thredd.com/v2.0/docs/gaining-access-to-the-developer-portal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thredd/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thredd.com/privacy-policy
created: '2026-07-24'
description: 'Thredd (formerly Global Processing Services / GPS) is a London-headquartered issuer-processor and next-generation payments technology company, founded in 2007, rebranded to Thredd in 2023, and backed by Advent International. It provides card issuing and issuer processing for fintechs, neobanks, banking-as-a-service platforms, and program managers across Mastercard, Visa, and Discover, spanning 40+ countries, with real-time transaction authorization (External Host Interface / EHI), digital-wallet tokenization (Apple Pay, Google Pay), 3-D Secure / strong customer authentication, card controls, and fraud / scam detection. Its home market is the United Kingdom. Thredd ships a genuine public developer surface: a self-serve Developer Portal (devportal.thredd.com) that grants a sandbox client id and secret, an API Hub REST API at api.thredd.com, and a ReadMe-hosted API reference (cardsapidocs.thredd.com) documenting roughly 129 endpoints across more than a dozen product OpenAPI definitions
  (core cards, transactions, credit, custom PAN, card limits, card controls, digital wallets, 3DS, ACH, open banking, alias directory, and web services). Authentication is FAPI-grade OAuth2 client-credentials using private_key_jwt client assertions over mutual TLS, brokered by Cloudentity with Raidiam Connect acting as the certificate authority; webhooks and event subscriptions are supported. The underlying OpenAPI files render only through the hub and are not anonymously downloadable.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Thredd
nav: Providers
network: true
overview: 'Thredd publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Issuer Processor, Card Issuing, and Payment Processing.


  The Thredd catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Thredd''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, signup flow, and 16 more developer resources.'
random_paper: 5
scopes:
- name: Thredd Scopes
  scope_count: 6
  slug: thredd-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 32.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 41.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 70.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thredd/refs/heads/main/screenshots/thredd-2026-08-17T082352.png
security:
- kind: authentication
  name: Thredd Authentication
  slug: thredd-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Thredd Domain Security
  slug: thredd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thredd
tags:
- Payments
- United Kingdom
- Issuer Processor
- Card Issuing
- Payment Processing
- Banking as a Service
- Digital Wallet
- Cross-Border
- Fraud
- Open Banking
- FAPI
website: https://www.thredd.com/
---
