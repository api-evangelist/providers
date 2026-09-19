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
    agent_skills: derived
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
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-09-18'
api_count: 1
apis:
- description: Legacy marketplace/collections API — obtain a JWT with your API key and secret, then manage NFT collections and in-platform tokens for token checkout.
  name: Tweed API (V1)
  slug: tweed-api-v1
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The assets API from Tweed — 5 operation(s) for assets.
  name: Tweed assets API
  slug: tweed-assets-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The audit-event-mappings API from Tweed — 1 operation(s) for audit-event-mappings.
  name: Tweed audit-event-mappings API
  slug: tweed-audit-event-mappings-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The auth API from Tweed — 3 operation(s) for auth.
  name: Tweed auth API
  slug: tweed-auth-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The blockchains API from Tweed — 4 operation(s) for blockchains.
  name: Tweed blockchains API
  slug: tweed-blockchains-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The checkout API from Tweed — 4 operation(s) for checkout.
  name: Tweed checkout API
  slug: tweed-checkout-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The contracts API from Tweed — 5 operation(s) for contracts.
  name: Tweed contracts API
  slug: tweed-contracts-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The items API from Tweed — 5 operation(s) for items.
  name: Tweed items API
  slug: tweed-items-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The payouts API from Tweed — 4 operation(s) for payouts.
  name: Tweed payouts API
  slug: tweed-payouts-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The platform-webhooks API from Tweed — 3 operation(s) for platform-webhooks.
  name: Tweed platform-webhooks API
  slug: tweed-platform-webhooks-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The Rate API from Tweed — 1 operation(s) for rate.
  name: Tweed Rate API
  slug: tweed-rate-api
- baseURL: https://api-v2.prod.paytweed.com
  baseurl_source: declared
  description: The tickets API from Tweed — 1 operation(s) for tickets.
  name: Tweed tickets API
  slug: tweed-tickets-api
artifact_total: 27
asyncapis:
- description: ''
  name: Tweed Webhooks
  slug: tweed-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tweed assets API
  slug: open-tweed-assets-api
- collection_type: open
  name: Tweed assets audit-event-mappings API
  slug: open-tweed-audit-event-mappings-api
- collection_type: open
  name: Tweed assets auth API
  slug: open-tweed-auth-api
- collection_type: open
  name: Tweed assets blockchains API
  slug: open-tweed-blockchains-api
- collection_type: open
  name: Tweed assets checkout API
  slug: open-tweed-checkout-api
- collection_type: open
  name: Tweed assets contracts API
  slug: open-tweed-contracts-api
- collection_type: open
  name: Tweed assets items API
  slug: open-tweed-items-api
- collection_type: open
  name: Tweed assets payouts API
  slug: open-tweed-payouts-api
- collection_type: open
  name: Tweed assets platform-webhooks API
  slug: open-tweed-platform-webhooks-api
- collection_type: open
  name: Tweed assets Rate API
  slug: open-tweed-rate-api
- collection_type: open
  name: Tweed assets tickets API
  slug: open-tweed-tickets-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/overlays/tweed-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tweed-api-v2-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.paytweed.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paytweed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paytweed.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paytweed.com/developer-tools/api/api-v2/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paytweed.com/getting-started/embedded-wallets-or-waas
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.paytweed.com/developer-tools/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/authentication/tweed-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tweed-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/security/tweed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tweed-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/packages/tweed-packages.yml
  title: ''
  type: Packages
  url: packages/tweed-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/packages/tweed-packages.yml
  title: ''
  type: SDKs
  url: packages/tweed-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/mcp/tweed-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tweed-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/llms/tweed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tweed-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/conformance/tweed-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tweed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.paytweed.com/getting-started/token-checkout-or-payments/legacy-token-checkout/features/aml-and-kyc-policy-overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/lifecycle/tweed-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tweed-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/asyncapi/tweed-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tweed-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/sandbox/tweed-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tweed-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/conventions/tweed-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tweed-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/components/tweed-components.yml
  title: ''
  type: Components
  url: components/tweed-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/data-model/tweed-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tweed-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tweed is an Accel-backed embedded-crypto platform offering Wallet-as-a-Service and NFT/token checkout APIs. Platforms embed self-custodial wallets (social login recovery, EIP-1193 EVM provider) and sell fungible and non-fungible tokens to buyers paying by card, Apple Pay, or Google Pay, with fiat, native, or stablecoin settlement across 12+ chains including Ethereum, Polygon, Base, Solana, and Tezos. A REST API (V2) manages contracts, items, payouts, checkouts, and HMAC-signed webhooks; note the marketing site and dashboard host were unreachable as of July 2026 while the docs, API, and npm SDKs remain live.
image: https://2034179314-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgQyCg5IN7Cv6AnUUpGl2%2Ficon%2F7r4C3KWx4NfmxABWz0oa%2FIcon-Square_Black-4x.jpeg?alt=media&token=55a8df5f-9429-454e-b864-52cb0bea5e25
layout: provider
modified: '2026-07-21'
name: Tweed
nav: Providers
network: true
overview: 'Tweed publishes 11 APIs on the [APIs.io](https://apis.io/) network, including assets API, audit-event-mappings API, auth API, and 8 more. Tagged areas include Company, Payments, Crypto, Wallets, and NFT.


  The Tweed catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tweed''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, sandbox, and 16 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 4.5
    contract_quality: 50.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 7.9
  previous_composite: 38.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tweed/refs/heads/main/screenshots/tweed-2026-09-02T164612.png
security:
- kind: authentication
  name: Tweed Authentication
  slug: tweed-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Tweed Domain Security
  slug: tweed-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tweed
tags:
- Company
- Payments
- Crypto
- Wallets
- NFT
- Blockchain
- Web3
- Checkout
website: https://www.paytweed.com/
---
