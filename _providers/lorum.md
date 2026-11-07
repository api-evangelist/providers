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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
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
- baseURL: https://api.fuse.me
  baseurl_source: declared
  description: The Oauth API from Lorum — 1 operation(s) for oauth.
  name: Lorum OAUTH API
  slug: lorum-oauth-api
artifact_total: 28
asyncapis:
- description: Real-time webhook events emitted by Lorum for payments, transfers, currency exchanges, account changes, and customer onboarding. Generated from the provider's published webhook catalogue (docs.lorum.c
  name: Lorum (Fuse) Webhooks
  slug: lorum-webhooks-asyncapi
collections:
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
  href: https://artifacts.apis.io/lorum/capabilities/lorum-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lorum-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/lorum/overlays/lorum-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/lorum/authentication/lorum-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lorum-authentication.yml
- group: design
  href: https://artifacts.apis.io/lorum/conventions/lorum-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lorum-conventions.yml
- group: design
  href: https://artifacts.apis.io/lorum/conventions/lorum-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lorum-conventions.yml
- group: design
  href: https://artifacts.apis.io/lorum/errors/lorum-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lorum-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lorum/lifecycle/lorum-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lorum-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lorum.com/
- group: design
  href: https://artifacts.apis.io/lorum/conformance/lorum-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lorum-conformance.yml
- group: start
  href: https://artifacts.apis.io/lorum/sandbox/lorum-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lorum-sandbox.yml
- group: design
  href: https://artifacts.apis.io/lorum/data-model/lorum-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lorum-data-model.yml
- group: agent
  href: https://artifacts.apis.io/lorum/mcp/lorum-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lorum-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lorum/well-known/lorum-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lorum-well-known.yml
- group: docs
  href: https://artifacts.apis.io/lorum/asyncapi/lorum-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/lorum-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/lorum/asyncapi/lorum-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/lorum-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/lorum/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lorum/llms/lorum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lorum-llms.txt
- group: auth
  href: https://artifacts.apis.io/lorum/security/lorum-domain-security.yml
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
overview: 'Lorum publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Customers API, Customers V2 API, and 7 more. Tagged areas include Company, Fintech, Payments, Banking, and Clearing.


  The Lorum catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Lorum''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 20 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Lorum API Rules
  rule_count: 64
  severity_counts:
    error: 53
    hint: 0
    info: 3
    warn: 8
  slug: lorum-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 56.1
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 23.7
  previous_composite: 40.9
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
    score: 16.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/lorum/lorum-2026-07-25T225554.png
security:
- kind: authentication
  name: Lorum Authentication
  slug: lorum-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Lorum Domain Security
  slug: lorum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: Estimate and create an outbound payment
  slug: lorum-create-outbound-payment
- name: Quote and execute a currency exchange or internal transfer
  slug: lorum-currency-exchange-and-transfer
- name: Onboard a customer and open an account
  slug: lorum-onboard-customer-and-open-account
- name: Simulate payment scheme actions in the sandbox
  slug: lorum-simulate-payments-in-sandbox
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
