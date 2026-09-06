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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nala Agentic Access
  operation_count: 8
  slug: nala-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- baseURL: https://rest.prod.rafiki-api.com/v1
  baseurl_source: declared
  description: The Bank API from NALA — 1 operation(s) for bank.
  name: NALA Bank API
  slug: nala-bank-api
- baseURL: https://rest.prod.rafiki-api.com/v1
  baseurl_source: declared
  description: The Lookup API from NALA — 1 operation(s) for lookup.
  name: NALA Lookup API
  slug: nala-lookup-api
- baseURL: https://rest.prod.rafiki-api.com/v1
  baseurl_source: declared
  description: The Payment Account API from NALA — 1 operation(s) for payment account.
  name: NALA Payment Account API
  slug: nala-payment-account-api
- baseURL: https://rest.prod.rafiki-api.com/v1
  baseurl_source: declared
  description: The Payout API from NALA — 2 operation(s) for payout.
  name: NALA Payout API
  slug: nala-payout-api
- baseURL: https://rest.prod.rafiki-api.com/v1
  baseurl_source: declared
  description: The Wallet API from NALA — 1 operation(s) for wallet.
  name: NALA Wallet API
  slug: nala-wallet-api
artifact_total: 17
asyncapis:
- description: ''
  name: Nala Rafiki Webhooks
  slug: nala-rafiki-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Resources Bank API
  slug: open-nala-bank-api
- collection_type: open
  name: Resources Bank Lookup API
  slug: open-nala-lookup-api
- collection_type: open
  name: Resources Bank Payment Account API
  slug: open-nala-payment-account-api
- collection_type: open
  name: Resources Bank Payout API
  slug: open-nala-payout-api
- collection_type: open
  name: Resources Bank Wallet API
  slug: open-nala-wallet-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nala-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nala.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rafiki.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rafiki.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rafiki.com/reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rafiki.com/recipes/create-account-and-send-money
- group: operate
  title: ''
  type: Support
  url: https://help.nala.money/en/
- group: company
  title: ''
  type: Blog
  url: https://www.nala.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NalaMoney
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rafiki.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nala.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nala.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nala-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nala-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nala-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nala-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nala-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nala-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nala-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/nala-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nala-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nala-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nala-rafiki-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nala-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nala-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/nala-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nala-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nala-rafiki-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nala-create-account-and-send-payout.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nala-lookup-recipient-account.md
- group: start
  title: ''
  type: SignUp
  url: https://rafiki.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.rafiki.com
created: '2026-07-17'
description: 'NALA is a fintech building cross-border payments infrastructure for emerging markets. Its consumer app is an international money-transfer and multi-currency account used to send money from the UK, US and EU to 35+ countries across Africa and Asia, with 98% of transfers arriving within minutes. NALA''s B2B product, Rafiki, is a single API for global payouts and collections: move, collect and settle funds in local currency or stablecoins (USDC/USDT) across the US, UK, Europe, Asia and Africa, reaching 300+ banks and 40+ mobile-money operators with real-time FX, lookups, wallet statements, webhooks and built-in compliance and sanctions screening. Backed by Bessemer Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nala.png
layout: provider
mcp_servers:
- description: Rafiki's remote MCP server. Gives AI editors (Cursor, Windsurf) and general tools (Claude Desktop) access to Rafiki documentation search and code generation for Rafiki API integrations.
  name: NALA MCP Server
  slug: nala-mcp-server
modified: '2026-07-20'
name: NALA
nav: Providers
network: true
overview: 'NALA publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bank API, Lookup API, Payment Account API, and 2 more. Tagged areas include Company, Fintech, Payments, Remittances, and Money Transfer.


  The NALA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NALA''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 26 more developer resources.'
random_paper: 13
scopes:
- name: Nala Scopes
  scope_count: 9
  slug: nala-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 57.9
    developer_ergonomics: 57.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
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
screenshot: https://raw.githubusercontent.com/api-evangelist/nala/refs/heads/main/screenshots/nala-2026-08-07T184612.png
security:
- kind: authentication
  name: Nala Authentication
  slug: nala-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nala Domain Security
  slug: nala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nala
tags:
- Company
- Fintech
- Payments
- Remittances
- Money Transfer
- Payouts
- Cross-Border Payments
- Mobile Money
- Stablecoins
- Africa
website: https://www.nala.com/
---
