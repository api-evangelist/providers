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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Card-linking REST API — programs, cards, transactions, brands, locations, offers and webhooks. Enroll Visa/Mastercard/Amex cards via PCI-compliant SDKs and receive enriched real-time transactions over
  name: Fidel API
  slug: fidel-api
artifact_total: 4
asyncapis:
- description: ''
  name: Fidel Webhooks
  slug: fidel-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://fidelapi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.fidel.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fidelapi.com/docs/select
- group: docs
  title: ''
  type: APIReference
  url: https://reference.fidel.uk/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fidelapi.com/docs/select/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://fidellimited.zendesk.com/
- group: company
  title: ''
  type: Blog
  url: https://fidelapi.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Enigmatic-Smile
- group: commercial
  title: ''
  type: Pricing
  url: https://fidelapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.fidel.uk/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fidelapi.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fidelapi.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fidel.uk
- group: build
  title: ''
  type: Packages
  url: packages/fidel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fidel-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fidel-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fidel-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fidel-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fidel-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fidel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://fidelapi.com/legal/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fidel-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/fidel-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fidel-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fidel-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fidel-llms.txt
created: '2026-07-17'
description: Fidel (Enigmatic Smile Ltd, trading as Fidel API) is a card-linking and payments-data platform that lets developers connect Visa, Mastercard and Amex cards to web and mobile applications through a single API. PCI-compliant card-capture SDKs (Web, iOS, Android, React Native) securely tokenize card details, and Fidel then delivers enriched, real-time transaction records to the integrator's servers over webhooks whenever a linked card is used at a participating merchant. Products include the Select Transactions API, an Offers / card-linked-rewards API, card enrollment SDKs, and attribution & insights. Founded in 2015 and headquartered in the UK, Fidel operates in the United States, United Kingdom, Ireland, Canada, Sweden and the UAE, and absorbs PCI scope on behalf of its integrators.
image: https://fidelapi.com/fidel_social.png
layout: provider
modified: '2026-07-19'
name: Fidel
nav: Providers
network: true
overview: 'Fidel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Card Linking, Transaction, and Fintech.


  The Fidel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fidel''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 44.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 42.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fidel/refs/heads/main/screenshots/fidel-2026-07-25T214420.png
security:
- kind: authentication
  name: Fidel Authentication
  slug: fidel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fidel Domain Security
  slug: fidel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fidel
tags:
- Company
- Payments
- Card Linking
- Transaction
- Fintech
- Embedded Finance
- Loyalty
- Rewards
- Webhook
- SDK
website: https://fidelapi.com
---
