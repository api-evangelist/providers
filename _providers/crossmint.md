---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Crossmint Agentic Access
  operation_count: 18
  slug: crossmint-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 1
apis:
- description: REST API to create and manage server-side custodial and non-custodial smart wallets across EVM and Solana, sign transactions, manage delegated permissions.
  name: Crossmint Wallets API
  slug: wallets-api
- description: REST API to mint and manage NFTs on multiple chains, including collection creation, batch minting, and metadata management.
  name: Crossmint Minting API
  slug: minting-api
- description: REST API for hosted and headless checkout flows allowing credit-card and crypto purchases of NFTs.
  name: Crossmint Checkout API
  slug: checkout-api
- description: REST API to issue, manage, and verify verifiable credentials anchored on chain.
  name: Crossmint Verifiable Credentials API
  slug: credentials-api
- description: REST Order API for fully headless on-chain commerce flows including fiat and crypto payment intents.
  name: Crossmint Headless Checkout (Order API)
  slug: headless-checkout
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Wallets API from Crossmint — 2 operation(s) for wallets.
  name: Crossmint Wallets API
  slug: crossmint-wallets-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The actions API from Crossmint — 1 operation(s) for actions.
  name: Crossmint Actions API
  slug: crossmint-actions-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Agent Checkout Browser Profiles API from Crossmint — 2 operation(s) for agent checkout browser profiles.
  name: Crossmint Agent Checkout Browser Profiles API
  slug: crossmint-agent-checkout-browser-profiles-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Agent Checkout Buyer Profiles API from Crossmint — 2 operation(s) for agent checkout buyer profiles.
  name: Crossmint Agent Checkout Buyer Profiles API
  slug: crossmint-agent-checkout-buyer-profiles-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Agent Checkouts API from Crossmint — 5 operation(s) for agent checkouts.
  name: Crossmint Agent Checkouts API
  slug: crossmint-agent-checkouts-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Headless Checkout Orders API from Crossmint — 4 operation(s) for headless checkout orders.
  name: Crossmint Headless Checkout Orders API
  slug: crossmint-headless-checkout-orders-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The IP Story Protocol API from Crossmint — 14 operation(s) for ip story protocol.
  name: Crossmint IP Story Protocol API
  slug: crossmint-ip-story-protocol-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Minting API Collections API from Crossmint — 2 operation(s) for minting api collections.
  name: Crossmint Minting API Collections API
  slug: crossmint-minting-api-collections-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Minting API NFTs API from Crossmint — 3 operation(s) for minting api nfts.
  name: Crossmint Minting API NFTs API
  slug: crossmint-minting-api-nfts-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Minting API NFTs V1 Alpha1 API from Crossmint — 1 operation(s) for minting api nfts v1 alpha1.
  name: Crossmint Minting API NFTs V1 Alpha1 API
  slug: crossmint-minting-api-nfts-v1-alpha1-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Minting API SFTs API from Crossmint — 1 operation(s) for minting api sfts.
  name: Crossmint Minting API SFTs API
  slug: crossmint-minting-api-sfts-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Minting API Templates API from Crossmint — 2 operation(s) for minting api templates.
  name: Crossmint Minting API Templates API
  slug: crossmint-minting-api-templates-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Minting API Unstable API from Crossmint — 3 operation(s) for minting api unstable.
  name: Crossmint Minting API Unstable API
  slug: crossmint-minting-api-unstable-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Order Intents API from Crossmint — 3 operation(s) for order intents.
  name: Crossmint Order Intents API
  slug: crossmint-order-intents-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Payment Methods API from Crossmint — 3 operation(s) for payment methods.
  name: Crossmint Payment Methods API
  slug: crossmint-payment-methods-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Tokens API from Crossmint — 2 operation(s) for tokens.
  name: Crossmint Tokens API
  slug: crossmint-tokens-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Tokens by Locator API from Crossmint — 1 operation(s) for tokens by locator.
  name: Crossmint Tokens by Locator API
  slug: crossmint-tokens-by-locator-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Unstable API from Crossmint — 5 operation(s) for unstable.
  name: Crossmint Unstable API
  slug: crossmint-unstable-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Unstable Tokens by Locator API from Crossmint — 1 operation(s) for unstable tokens by locator.
  name: Crossmint Unstable Tokens by Locator API
  slug: crossmint-unstable-tokens-by-locator-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The User Documents API from Crossmint — 2 operation(s) for user documents.
  name: Crossmint User Documents API
  slug: crossmint-user-documents-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Users API from Crossmint — 3 operation(s) for users.
  name: Crossmint Users API
  slug: crossmint-users-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Users - Linked Wallets API from Crossmint — 1 operation(s) for users - linked wallets.
  name: Crossmint Users - Linked Wallets API
  slug: crossmint-users-linked-wallets-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The V1 Alpha1 API from Crossmint — 2 operation(s) for v1 alpha1.
  name: Crossmint V1 Alpha1 API
  slug: crossmint-v1-alpha1-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The V1 Alpha2 API from Crossmint — 3 operation(s) for v1 alpha2.
  name: Crossmint V1 Alpha2 API
  slug: crossmint-v1-alpha2-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Verifiable Credentials API from Crossmint — 2 operation(s) for verifiable credentials.
  name: Crossmint Verifiable Credentials API
  slug: crossmint-verifiable-credentials-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Verifiable Credentials Types API from Crossmint — 2 operation(s) for verifiable credentials types.
  name: Crossmint Verifiable Credentials Types API
  slug: crossmint-verifiable-credentials-types-api
artifact_total: 48
collections:
- collection_type: open
  name: Crossmint Wallets Balances API
  slug: open-crossmint-balances-api
- collection_type: open
  name: Crossmint Wallets Balances NFTs API
  slug: open-crossmint-nfts-api
- collection_type: open
  name: Crossmint Wallets Balances Signatures API
  slug: open-crossmint-signatures-api
- collection_type: open
  name: Crossmint Wallets Balances Signers API
  slug: open-crossmint-signers-api
- collection_type: open
  name: Crossmint Wallets Balances Transactions API
  slug: open-crossmint-transactions-api
- collection_type: open
  name: Crossmint Wallets Balances Transfers API
  slug: open-crossmint-transfers-api
- collection_type: open
  name: Crossmint Balances Wallets API
  slug: open-crossmint-wallets-api
- collection_type: open
  name: Crossmint Wallets API
  slug: open-crossmint
common:
- group: other
  href: https://artifacts.apis.io/crossmint/capabilities/crossmint-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/crossmint-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/crossmint/agentic-access/crossmint-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crossmint-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/crossmint/security/crossmint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossmint-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crossmint/security/crossmint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossmint-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/crossmint/authentication/crossmint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crossmint-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crossmint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crossmint-io
- group: company
  title: ''
  type: Website
  url: https://www.crossmint.com/
- group: commercial
  href: https://artifacts.apis.io/crossmint/plans/crossmint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crossmint-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/crossmint/rate-limits/crossmint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crossmint-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crossmint/finops/crossmint-finops.yml
  title: ''
  type: FinOps
  url: finops/crossmint-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.crossmint.com/llms.txt
created: '2026-05-08'
description: Crossmint is a Web3 platform offering APIs for wallets, NFT minting, checkout, payments, embedded checkout, and verifiable credentials. Supports server-managed wallets across EVM and Solana, fiat-on-ramp checkout, and credit-card-funded NFT purchases.
finops:
- has_sources: true
  method: generated
  name: Crossmint Finops
  primary_unit: ''
  service_category: Web3
  slug: crossmint-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crossmint.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.crossmint.com over HTTP; 3 tools listed.
  name: Crossmint MCP Server
  slug: crossmint
modified: '2026-05-08'
name: Crossmint
nav: Providers
network: true
overview: 'Crossmint publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Wallets API, Actions API, Agent Checkout Browser Profiles API, and 28 more. Tagged areas include Web3, Wallets, NFT, Payments, and Checkout.


  The Crossmint catalog on APIs.io includes 1 Spectral governance ruleset.


  Crossmint''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Crossmint Plans Pricing
  plan_count: 3
  slug: crossmint-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Crossmint Rate Limits
  slug: crossmint-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Crossmint API Rules
  rule_count: 62
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 9
  slug: crossmint-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 57.3
    developer_ergonomics: 21.4
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 76.5
      total: 34
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 16.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/crossmint/crossmint-2026-06-20T175244.png
security:
- kind: authentication
  name: Crossmint Authentication
  slug: crossmint-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crossmint Domain Security
  slug: crossmint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crossmint Vulnerability Disclosure
  slug: crossmint-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crossmint
tags:
- Web3
- Wallets
- NFT
- Payments
- Checkout
website: https://www.crossmint.com/
---
