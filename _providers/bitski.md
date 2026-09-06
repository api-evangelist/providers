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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Bitski Agentic Access
  operation_count: 35
  slug: bitski-agentic-access
  summary_line: 35 operations · 14 acting
api_count: 2
apis:
- baseURL: https://api.bitski.com
  baseurl_source: declared
  description: The activity API from Bitski — 1 operation(s) for activity.
  name: Bitski activity API
  slug: bitski-activity-api
- baseURL: https://api.bitski.com
  baseurl_source: declared
  description: The Commerce API from Bitski — 10 operation(s) for commerce.
  name: Bitski Commerce API
  slug: bitski-commerce-api
- baseURL: https://api.bitski.com
  baseurl_source: declared
  description: The Droplinks API from Bitski — 3 operation(s) for droplinks.
  name: Bitski Droplinks API
  slug: bitski-droplinks-api
- baseURL: https://api.bitski.com
  baseurl_source: declared
  description: The Minting API from Bitski — 8 operation(s) for minting.
  name: Bitski Minting API
  slug: bitski-minting-api
- baseURL: https://api.bitski.com
  baseurl_source: declared
  description: The Token Gating API from Bitski — 3 operation(s) for token gating.
  name: Bitski Token Gating API
  slug: bitski-token-gating-api
artifact_total: 16
asyncapis:
- description: ''
  name: Bitski Activity Webhooks
  slug: bitski-activity-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NFT Service APIs activity API
  slug: open-bitski-activity-api
- collection_type: open
  name: NFT Service APIs activity Commerce API
  slug: open-bitski-commerce-api
- collection_type: open
  name: NFT Service APIs activity Droplinks API
  slug: open-bitski-droplinks-api
- collection_type: open
  name: NFT Service APIs activity Minting API
  slug: open-bitski-minting-api
- collection_type: open
  name: NFT Service APIs activity Token Gating API
  slug: open-bitski-token-gating-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bitski-nft-service-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bitski.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bitski.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitski.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bitski.com/wallet-as-a-service/nft-apis/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitski.com/wallet-as-a-service/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.bitski.com/integrations/faq
- group: company
  title: ''
  type: Blog
  url: https://blog.bitski.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BitskiCo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitski.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitski.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitski.com/privacy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/bitski
- group: build
  title: ''
  type: Packages
  url: packages/bitski-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitski-packages.yml
- group: design
  title: ''
  type: Components
  url: components/bitski-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitski-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bitski-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitski-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitski-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitski-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bitski-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitski-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitski-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bitski-activity-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bitski-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitski-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitski-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitski-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitski-llms.txt
created: '2026-07-17'
description: Bitski is a Web3 wallet-as-a-service (WaaS) and NFT infrastructure provider that lets developers embed secure, hardware-backed crypto wallets and onboarding into web and mobile applications without users installing an extension. Its platform spans OAuth2/OIDC authentication, wallet creation (account-abstraction, hardware-backed, on-chain multi-sig, and seed-phrase import), and a suite of NFT Service APIs for minting, commerce (credit card, ACH, and crypto checkout), token gating, droplinks, auctions, and wallet experience data (balances, activity, portfolio, floor prices). Bitski publishes REST OpenAPI specs served from api.bitski.com, JavaScript/React and iOS SDKs, activity webhooks, and node infrastructure for EVM chains. Backed by a16z and Kindred Ventures.
image: https://cdn.bitskistatic.com/images/favicons/favicon-2f714ec5ebed6f2ec47661e04dd1322b.png
layout: provider
modified: '2026-07-18'
name: Bitski
nav: Providers
network: true
overview: 'Bitski publishes 5 APIs on the [APIs.io](https://apis.io/) network, including activity API, Commerce API, Droplinks API, and 2 more. Tagged areas include Web3, Crypto Wallet, Wallet as a Service, NFT, and Blockchain.


  The Bitski catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bitski''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 24 more developer resources.'
random_paper: 16
scopes:
- name: Bitski Scopes
  scope_count: 2
  slug: bitski-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 55.3
    developer_ergonomics: 60.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitski/refs/heads/main/screenshots/bitski-2026-08-17T122909.png
security:
- kind: authentication
  name: Bitski Authentication
  slug: bitski-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Bitski Domain Security
  slug: bitski-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitski
tags:
- Web3
- Crypto Wallet
- Wallet as a Service
- NFT
- Blockchain
- Authentication
- Payments
- Developer Tools
- Company
website: https://bitski.com/
---
