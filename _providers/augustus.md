---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 12
  name: Augustus Agentic Access
  operation_count: 37
  slug: augustus-agentic-access
  summary_line: 37 operations · 12 acting · 12 human-in-the-loop
api_count: 1
apis:
- description: The 2023-01-01 Ivy API for Open Banking pay-ins and Manual Bank Transfer. Checkout sessions, orders, customers, refunds, banks, capabilities, and beneficiary payouts. Existing Ivy customers keep using
  name: Ivy API (Open Banking)
  slug: ivy-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Account Programs API from Augustus — 3 operation(s) for account programs.
  name: Augustus Account Programs API
  slug: augustus-account-programs-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Accounts API from Augustus — 6 operation(s) for accounts.
  name: Augustus Accounts API
  slug: augustus-accounts-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The API Key API from Augustus — 1 operation(s) for api key.
  name: Augustus API Key API
  slug: augustus-api-key-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The API Versions API from Augustus — 1 operation(s) for api versions.
  name: Augustus API Versions API
  slug: augustus-api-versions-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Conversions API from Augustus — 2 operation(s) for conversions.
  name: Augustus Conversions API
  slug: augustus-conversions-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Deposits API from Augustus — 2 operation(s) for deposits.
  name: Augustus Deposits API
  slug: augustus-deposits-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Events API from Augustus — 2 operation(s) for events.
  name: Augustus Events API
  slug: augustus-events-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Payouts API from Augustus — 2 operation(s) for payouts.
  name: Augustus Payouts API
  slug: augustus-payouts-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Quotes API from Augustus — 2 operation(s) for quotes.
  name: Augustus Quotes API
  slug: augustus-quotes-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Returns API from Augustus — 2 operation(s) for returns.
  name: Augustus Returns API
  slug: augustus-returns-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Scopes API from Augustus — 1 operation(s) for scopes.
  name: Augustus Scopes API
  slug: augustus-scopes-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Webhook Deliveries API from Augustus — 3 operation(s) for webhook deliveries.
  name: Augustus Webhook Deliveries API
  slug: augustus-webhook-deliveries-api
- baseURL: https://api.augustus.com
  baseurl_source: declared
  description: The Webhook Subscriptions API from Augustus — 3 operation(s) for webhook subscriptions.
  name: Augustus Webhook Subscriptions API
  slug: augustus-webhook-subscriptions-api
- baseURL: https://api.getivy.de
  baseurl_source: declared
  description: The Webhook Events API from Augustus — 0 operation(s) for webhook events.
  name: Augustus Webhook Events API
  slug: augustus-webhook-events-api
artifact_total: 34
asyncapis:
- description: ''
  name: Augustus Webhooks
  slug: augustus-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Augustus Banking Account Programs API
  slug: open-augustus-account-programs-api
- collection_type: open
  name: Augustus Banking Account Programs Accounts API
  slug: open-augustus-accounts-api
- collection_type: open
  name: Augustus Banking Account Programs API Key API
  slug: open-augustus-api-key-api
- collection_type: open
  name: Augustus Banking Account Programs API Versions API
  slug: open-augustus-api-versions-api
- collection_type: open
  name: Augustus Banking Account Programs Conversions API
  slug: open-augustus-conversions-api
- collection_type: open
  name: Augustus Banking Account Programs Deposits API
  slug: open-augustus-deposits-api
- collection_type: open
  name: Augustus Banking Account Programs Events API
  slug: open-augustus-events-api
- collection_type: open
  name: Augustus Banking Account Programs Payouts API
  slug: open-augustus-payouts-api
- collection_type: open
  name: Augustus Banking Account Programs Quotes API
  slug: open-augustus-quotes-api
- collection_type: open
  name: Augustus Banking Account Programs Returns API
  slug: open-augustus-returns-api
- collection_type: open
  name: Augustus Banking Account Programs Scopes API
  slug: open-augustus-scopes-api
- collection_type: open
  name: Augustus Banking Account Programs Webhook Deliveries API
  slug: open-augustus-webhook-deliveries-api
- collection_type: open
  name: Augustus Banking Account Programs Webhook Subscriptions API
  slug: open-augustus-webhook-subscriptions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/augustus-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/augustus-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/augustus-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/augustus-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://augustus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.augustus.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.augustus.com/docs/basics/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.augustus.com/v1/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.augustus.com/docs/basics/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://docs.augustus.com/v1/authentication
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.augustus.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.augustus.com
- group: operate
  title: ''
  type: Support
  url: https://augustus.com/company/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://augustus.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://augustus.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getivy.io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/augustus-openapi-original.yml
- group: build
  title: ''
  type: Packages
  url: packages/augustus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/augustus-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/augustus-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/augustus-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/augustus-banking-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/augustus-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/augustus-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/augustus-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/augustus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.augustus.com/v1/versioning
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/augustus-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/augustus-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/augustus-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/augustus-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/augustus-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/augustus-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Augustus (formerly Ivy, getivy.io) is a global payments and banking platform that lets developers move money between fiat and stablecoins, accept Open Banking bank payments, send payouts, run FX conversions, and hold balances through a single REST API. Building blocks include accounts and virtual accounts, account programs, checkout sessions and orders, deposits, payouts, refunds and returns, conversions and quotes, plus webhooks for real-time events. Augustus runs the Ivy Open Banking API (version 2023-01-01) alongside the newer Augustus Banking API (version 2026-05-01), authenticates with scoped bearer API keys, supports idempotent POSTs and cursor pagination, and is building an AI-native, stablecoin-based clearing bank. Backed by Creandum and Valar Ventures.
image: https://a.storyblok.com/f/292219090989234/1920x1080/ea9e21e94c/website-header.png
layout: provider
modified: '2026-07-18'
name: Augustus
nav: Providers
network: true
overview: 'Augustus publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account Programs API, Accounts API, API Key API, and 11 more. Tagged areas include Company, Fintech, Payments, Banking, and Open Banking.


  The Augustus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Augustus'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, sandbox, and 27 more developer resources.'
random_paper: 15
scopes:
- name: Augustus Scopes
  scope_count: 16
  slug: augustus-scopes
  summary_line: 16 scopes
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 60.4
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/augustus/refs/heads/main/screenshots/augustus-2026-07-25T201725.png
security:
- kind: authentication
  name: Augustus Authentication
  slug: augustus-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Augustus Domain Security
  slug: augustus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: augustus
tags:
- Company
- Fintech
- Payments
- Banking
- Open Banking
- Stablecoins
- Payouts
- Foreign Exchange
- Webhook
website: https://augustus.com/
---
