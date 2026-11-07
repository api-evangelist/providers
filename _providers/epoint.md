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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST payment gateway for accepting online card payments in Azerbaijan. Covers payment creation and hosted checkout, card registration/tokenization and saved-card charges, refunds and reversals, pre-au
  name: Epoint Payment API
  slug: epoint-payment-api
artifact_total: 4
asyncapis:
- description: ''
  name: Epoint Callbacks Webhooks
  slug: epoint-callbacks-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://epoint.az
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.epoint.az/en
- group: docs
  title: ''
  type: Documentation
  url: https://developer.epoint.az/en
- group: docs
  title: ''
  type: APIReference
  url: https://developer.epoint.az/en
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.epoint.az/en
- group: company
  title: ''
  type: Blog
  url: https://epoint.az/en/news
- group: operate
  title: ''
  type: Support
  url: https://epoint.az/en/contact
- group: start
  title: ''
  type: Login
  url: https://epoint.az/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://epoint.az/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://epoint.az/en/privacy
- group: auth
  href: https://artifacts.apis.io/epoint/authentication/epoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/epoint-authentication.yml
- group: build
  href: https://artifacts.apis.io/epoint/errors/epoint-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/epoint-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/epoint/errors/epoint-decline-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/epoint-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/epoint/conventions/epoint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/epoint-conventions.yml
- group: design
  href: https://artifacts.apis.io/epoint/asyncapi/epoint-callbacks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/epoint-callbacks-webhooks.yml
- group: design
  href: https://artifacts.apis.io/epoint/lifecycle/epoint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/epoint-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/epoint/packages/epoint-packages.yml
  title: ''
  type: Packages
  url: packages/epoint-packages.yml
- group: build
  href: https://artifacts.apis.io/epoint/packages/epoint-packages.yml
  title: ''
  type: SDKs
  url: packages/epoint-packages.yml
- group: design
  href: https://artifacts.apis.io/epoint/components/epoint-components.yml
  title: ''
  type: Components
  url: components/epoint-components.yml
- group: design
  href: https://artifacts.apis.io/epoint/conformance/epoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/epoint-conformance.yml
- group: agent
  href: https://artifacts.apis.io/epoint/mcp/epoint-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/epoint-mcp.yml
- group: agent
  href: https://artifacts.apis.io/epoint/well-known/epoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/epoint-well-known.yml
- group: auth
  href: https://artifacts.apis.io/epoint/security/epoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/epoint-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/epoint/llms/epoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/epoint-llms.txt
created: '2026-07-17'
description: Epoint (epoint.az) is an Azerbaijani digital payment aggregator and e-commerce platform for small and medium enterprises, backed by 500 Global. It lets merchants accept online card payments on their website, mobile app, or social page and layers on card tokenization (saved cards), split payments, pre-authorization, installment payments, payouts to any Azerbaijani business card 24/7, wallets, invoicing, QR/link payments, recurring payments, and Apple Pay / Google Pay. Its REST payment API (base https://epoint.az/api/1) authenticates every request with a merchant public_key plus a SHA1 data+signature scheme and returns results both synchronously and via signed callbacks to the merchant's result_url.
image: https://epoint.az/images/logo.png
layout: provider
modified: '2026-07-19'
name: Epoint
nav: Providers
network: true
overview: 'Epoint is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Gateway, Fintech, and E-Commerce.


  The Epoint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Epoint''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - azerbaijan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 38.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/epoint/epoint-2026-07-25T213527.png
security:
- kind: authentication
  name: Epoint Authentication
  slug: epoint-authentication
  summary_line: custom-signature · 1 scheme
- kind: domain-security
  name: Epoint Domain Security
  slug: epoint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: epoint
tags:
- Company
- Payments
- Payment Gateway
- Fintech
- E-Commerce
- Card Payments
- Azerbaijan
- Apple Pay
- Google Pay
- Digital Wallet
website: https://epoint.az
---
