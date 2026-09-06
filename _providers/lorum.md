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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Accounts API from Lorum — 5 operation(s) for accounts.
  name: Lorum Accounts API
  slug: lorum-accounts-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Customers API from Lorum — 10 operation(s) for customers.
  name: Lorum Customers API
  slug: lorum-customers-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Customers V2 API from Lorum — 1 operation(s) for customers v2.
  name: Lorum Customers V2 API
  slug: lorum-customers-v2-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Documents API from Lorum — 2 operation(s) for documents.
  name: Lorum Documents API
  slug: lorum-documents-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Exchange API from Lorum — 2 operation(s) for exchange.
  name: Lorum Exchange API
  slug: lorum-exchange-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Internal Transfers API from Lorum — 1 operation(s) for internal transfers.
  name: Lorum Internal Transfers API
  slug: lorum-internal-transfers-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Oauth API from Lorum — 1 operation(s) for oauth.
  name: Lorum Oauth API
  slug: lorum-oauth-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Payments API from Lorum — 2 operation(s) for payments.
  name: Lorum Payments API
  slug: lorum-payments-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Simulation API from Lorum — 4 operation(s) for simulation.
  name: Lorum Simulation API
  slug: lorum-simulation-api
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Transactions API from Lorum — 8 operation(s) for transactions.
  name: Lorum Transactions API
  slug: lorum-transactions-api
artifact_total: 24
asyncapis:
- description: Real-time webhook events emitted by Lorum for payments, transfers, currency exchanges, account changes, and customer onboarding. Generated from the provider's published webhook catalogue (docs.lorum.c
  name: Lorum (Fuse) Webhooks
  slug: lorum-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fuse Accounts API
  slug: open-lorum-accounts-api
- collection_type: open
  name: Fuse Accounts Customers API
  slug: open-lorum-customers-api
- collection_type: open
  name: Fuse Accounts Customers V2 API
  slug: open-lorum-customers-v2-api
- collection_type: open
  name: Fuse Accounts Documents API
  slug: open-lorum-documents-api
- collection_type: open
  name: Fuse Accounts Exchange API
  slug: open-lorum-exchange-api
- collection_type: open
  name: Fuse Accounts Internal Transfers API
  slug: open-lorum-internal-transfers-api
- collection_type: open
  name: Fuse Accounts Oauth API
  slug: open-lorum-oauth-api
- collection_type: open
  name: Fuse Accounts Payments API
  slug: open-lorum-payments-api
- collection_type: open
  name: Fuse Accounts Simulation API
  slug: open-lorum-simulation-api
- collection_type: open
  name: Fuse Accounts Transactions API
  slug: open-lorum-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lorum-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lorum-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lorum.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lorum.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lorum.com/reference/getting-a-bearer-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lorum.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/lorum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lorum-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lorum-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lorum-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lorum-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lorum.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/lorum-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lorum-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lorum-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lorum-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lorum-well-known.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/lorum-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lorum-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lorum-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lorum-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lorum.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lorum.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.lorum.com/
- group: operate
  title: ''
  type: Support
  url: https://www.lorum.com/contact-us
- group: company
  title: ''
  type: Website
  url: https://www.lorum.com
created: '2026-07-17'
description: Lorum (developer brand "Fuse") is a fintech providing banking-grade clearing, settlement, and treasury infrastructure - "built for clearing, not lending." Through one API it offers multi-currency clearing across 30+ markets, programmable segregated account infrastructure (including virtual IBANs), and cash management with FX and liquidity sweeps. It targets payroll/EOR platforms, fintechs and PSPs, trading and investment platforms, and marketplaces that need to move and settle funds across global payment rails without standing up local banking entities. The API (OAuth2 client-credentials auth, idempotency-keyed money movement, and webhook event notifications) covers customers/KYC, accounts, payments, internal transfers, currency exchange, documents, batch payments, and full sandbox scheme simulation. Lorum is backed by Northzone.
image: https://cdn.prod.website-files.com/691dc048eb27bd1d29e459b1/692b0683e9466303595474d6_1ddad7f49147abb7075cab3048b9487b_Opengraph.png
layout: provider
modified: '2026-07-20'
name: Lorum
nav: Providers
network: true
overview: 'Lorum publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Customers API, Customers V2 API, and 7 more. Tagged areas include Company, Fintech, Payments, Banking, and Clearing.


  The Lorum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lorum''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 20 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 18
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
    contract_quality: 65.1
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 39.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lorum/refs/heads/main/screenshots/lorum-2026-07-25T225554.png
security:
- kind: authentication
  name: Lorum Authentication
  slug: lorum-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Lorum Domain Security
  slug: lorum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lorum
tags:
- Company
- Fintech
- Payments
- Banking
- Clearing
- Settlement
- Treasury
- Multi-Currency
- Account
- Foreign Exchange
- Webhook
website: https://www.lorum.com
---
