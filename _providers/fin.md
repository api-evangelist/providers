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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Fin Agentic Access
  operation_count: 62
  slug: fin-agentic-access
  summary_line: 62 operations · 31 acting
api_count: 2
apis:
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: A modified OAuth 2.0 Client Credential Flow
  name: Fin Authentication API
  slug: fin-authentication-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: Retrieve wallet balance information
  name: Fin Balances API
  slug: fin-balances-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: Manage beneficiary accounts for payments and transfers
  name: Fin Beneficiaries API
  slug: fin-beneficiaries-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: A set of endpoints to retrieve contextual data to assemble requests to fin.com's API
  name: Fin Catalogue API
  slug: fin-catalogue-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: The Crypto Orchestration API from Fin — 3 operation(s) for crypto orchestration.
  name: Fin Crypto Orchestration API
  slug: fin-crypto-orchestration-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: Customer management and document upload operations
  name: Fin Customers API
  slug: fin-customers-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: Retrieve fees and foreign exchange rates
  name: Fin Fees & FX Rates API
  slug: fin-fees-fx-rates-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: Transaction history and management for beneficiaries
  name: Fin Transactions API
  slug: fin-transactions-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: Create and manage virtual accounts for USD to USDC conversions
  name: Fin Virtual Accounts API
  slug: fin-virtual-accounts-api
- baseURL: https://api.fin.com
  baseurl_source: declared
  description: The Webhooks API from Fin — 0 operation(s) for webhooks.
  name: Fin Webhooks API
  slug: fin-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: Fin Webhooks
  slug: fin-webhooks
collections:
- collection_type: open
  name: Fin.com Authentication API
  slug: open-fin-authentication-api
- collection_type: open
  name: Fin.com Authentication Balances API
  slug: open-fin-balances-api
- collection_type: open
  name: Fin.com Authentication Beneficiaries API
  slug: open-fin-beneficiaries-api
- collection_type: open
  name: Fin.com Authentication Catalogue API
  slug: open-fin-catalogue-api
- collection_type: open
  name: Fin.com Authentication Crypto Orchestration API
  slug: open-fin-crypto-orchestration-api
- collection_type: open
  name: Fin.com Authentication Customers API
  slug: open-fin-customers-api
- collection_type: open
  name: Fin.com Authentication Fees & FX Rates API
  slug: open-fin-fees-fx-rates-api
- collection_type: open
  name: Fin.com Authentication Transactions API
  slug: open-fin-transactions-api
- collection_type: open
  name: Fin.com Authentication Virtual Accounts API
  slug: open-fin-virtual-accounts-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fin.com/rss.xml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fin.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fin.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fin.com/index
- group: docs
  href: https://artifacts.apis.io/fin/openapi/_original/fin-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/fin-openapi-original.yml
- group: other
  href: https://artifacts.apis.io/fin/overlays/fin-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fin-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/fin/authentication/fin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fin-authentication.yml
- group: design
  href: https://artifacts.apis.io/fin/conventions/fin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fin-conventions.yml
- group: design
  href: https://artifacts.apis.io/fin/errors/fin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fin-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fin/asyncapi/fin-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fin-webhooks.yml
- group: design
  href: https://artifacts.apis.io/fin/conformance/fin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fin-conformance.yml
- group: design
  href: https://artifacts.apis.io/fin/lifecycle/fin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fin-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://fin.instatus.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.fin.com/changelogs/2026-04-20
- group: operate
  href: https://artifacts.apis.io/fin/changelog/fin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fin-changelog.yml
- group: start
  href: https://artifacts.apis.io/fin/sandbox/fin-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fin-sandbox.yml
- group: design
  href: https://artifacts.apis.io/fin/data-model/fin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fin-data-model.yml
- group: agent
  href: https://artifacts.apis.io/fin/mcp/fin-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fin-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fin/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fin/agentic-access/fin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fin-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fin/security/fin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fin-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/fin/llms/fin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fin-llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:support@fin.com
- group: company
  title: ''
  type: Blog
  url: https://www.fin.com/stories
- group: company
  title: ''
  type: Website
  url: https://www.fin.com
created: '2026-07-17'
description: Fin (fin.com) is a global cross-border payments infrastructure company that moves money internationally over stablecoin rails and direct liquidity networks instead of traditional correspondent banking, settling in minutes rather than days. Its Orchestration API lets businesses onboard individual and business customers (KYC/KYB), create beneficiaries, quote FX and fees, send transfer and batch payouts, provision multi-currency virtual accounts that convert fiat deposits to crypto (e.g. USD to USDC), and run crypto orchestration across exchanges. Founded by ex-Citadel engineers, Fin raised a $17M Series A to bring its stablecoin-powered high-value payments product to market. This profile was enriched from the public developer surface at developer.fin.com.
image: https://cdn.sanity.io/images/xemwqsar/production/0e65aec0795ced77ed5301b8627cbb88059d11d2-1200x630.webp?w=1200&h=630&q=80&fit=crop
layout: provider
modified: '2026-10-06'
name: Fin
nav: Providers
network: true
overview: 'Fin publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Balances API, Beneficiaries API, and 7 more. Tagged areas include Company, Payments, Cross-Border Payments, Stablecoins, and Fintech.


  The Fin catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fin''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 19 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Fin API Rules
  rule_count: 63
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 8
  slug: fin-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 58.5
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fin/fin-2026-07-25T214454.png
security:
- kind: authentication
  name: Fin Authentication
  slug: fin-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Fin Domain Security
  slug: fin-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Onboard a customer and send a cross-border payout
  slug: fin-onboard-and-payout
- name: Provision a virtual account to collect and convert funds
  slug: fin-virtual-account-collect
slug: fin
tags:
- Company
- Payments
- Cross-Border Payments
- Stablecoins
- Fintech
- Money Movement
- Foreign Exchange
- Virtual Accounts
- Cryptocurrency
website: https://www.fin.com
---
