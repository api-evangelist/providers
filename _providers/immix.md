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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 51
  human_in_the_loop: 5
  name: Immix Agentic Access
  operation_count: 87
  slug: immix-agentic-access
  summary_line: 87 operations · 51 acting · 5 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: Deposit and withdrawal addresses declared on an account and verified by a second user.
  name: IMMIX Account addresses API
  slug: immix-account-addresses-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: 'What each account holds at its venue, as the venue last stated it: the latest reading per account and asset, published by the platform''s account connectors — never the platform''s own books.'
  name: IMMIX Account balances API
  slug: immix-account-balances-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: 'Venue accounts discovered through a credential: classified into a portfolio, approved, frozen, retired.'
  name: IMMIX Accounts API
  slug: immix-accounts-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: 'The organisation''s algo instances: created with a config document, started and stopped, re-configured while they run, halted all at once; the documents'' history, the orders an instance placed, and the'
  name: IMMIX Algos API
  slug: immix-algos-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: 'Per-asset limits: ticket size, approval threshold, reconciliation tolerance.'
  name: IMMIX Asset policies API
  slug: immix-asset-policies-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: The assets API from IMMIX — 2 operation(s) for assets.
  name: IMMIX Assets API
  slug: immix-assets-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: Per-chain transfer limits.
  name: IMMIX Chain policies API
  slug: immix-chain-policies-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: 'Venue API keys: created as proposals, approved under maker-checker, rotated and revoked. The key material is taken once and never served.'
  name: IMMIX Credentials API
  slug: immix-credentials-api
- baseURL: https://immix.xyz
  baseurl_source: declared
  description: The Enquiry API from IMMIX — 1 operation(s) for enquiry.
  name: IMMIX Enquiry API
  slug: immix-enquiry-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: Fills, joined to their order by `orderId`.
  name: IMMIX Executions API
  slug: immix-executions-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: The instruments API from IMMIX — 2 operation(s) for instruments.
  name: IMMIX Instruments API
  slug: immix-instruments-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: The outcome of a write that answered `202`.
  name: IMMIX Operations API
  slug: immix-operations-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: Submit, read and cancel orders.
  name: IMMIX Orders API
  slug: immix-orders-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: How the organisation groups its accounts.
  name: IMMIX Portfolios API
  slug: immix-portfolios-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: Per-instrument and organisation-wide order limits, and the trading halt.
  name: IMMIX Trading policies API
  slug: immix-trading-policies-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: Members of the organisation, and your own row.
  name: IMMIX Users API
  slug: immix-users-api
- baseURL: https://api.immix.xyz/v1
  baseurl_source: declared
  description: The venues API from IMMIX — 2 operation(s) for venues.
  name: IMMIX Venues API
  slug: immix-venues-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/immix/agentic-access/immix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/immix-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/immix/rules/immix-rules.yml
  title: ''
  type: Spectral
  url: rules/immix-rules.yml
- group: design
  href: https://artifacts.apis.io/immix/json-ld/immix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/immix-context.jsonld
- group: design
  href: https://artifacts.apis.io/immix/vocabulary/immix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/immix-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/immix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/immix/data-model/immix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/immix-data-model.yml
- group: operate
  href: https://artifacts.apis.io/immix/changelog/immix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/immix-changelog.yml
- group: design
  href: https://artifacts.apis.io/immix/conventions/immix-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/immix-conventions.yml
- group: design
  href: https://artifacts.apis.io/immix/conventions/immix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/immix-conventions.yml
- group: auth
  href: https://artifacts.apis.io/immix/security/immix-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/immix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/immix/authentication/immix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/immix-authentication.yml
- group: design
  href: https://artifacts.apis.io/immix/lifecycle/immix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/immix-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/immix/errors/immix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/immix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/immix/conformance/immix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/immix-conformance.yml
- group: other
  href: https://artifacts.apis.io/immix/overlays/immix-enquiry-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/immix-enquiry-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/immix/llms/immix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/immix-llms.txt
- group: auth
  href: https://artifacts.apis.io/immix/well-known/immix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/immix-security.txt
- group: auth
  href: https://artifacts.apis.io/immix/well-known/immix-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/immix-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/immix/well-known/immix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/immix-well-known.yml
- group: other
  href: https://artifacts.apis.io/immix/hosts/immix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/immix-hosts.yml
- group: other
  href: https://artifacts.apis.io/immix/vendors/immix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/immix-vendors.yml
- group: build
  href: https://artifacts.apis.io/immix/packages/immix-packages.yml
  title: ''
  type: SDKs
  url: packages/immix-packages.yml
- group: build
  href: https://artifacts.apis.io/immix/packages/immix-packages.yml
  title: ''
  type: Packages
  url: packages/immix-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://immix.xyz/press/immix-raises-3-5-million
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.immix.xyz/trading/changelog/overview
- group: auth
  href: https://artifacts.apis.io/immix/security/immix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/immix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/immix/security/immix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/immix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://immix.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.immix.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.immix.xyz/trading/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.immix.xyz/trading/api-reference/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.immix.xyz/trading/docs/quickstart.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinstrats
created: '2026-10-29'
description: IMMIX is an AI-native trading firm that makes markets in non-USD stablecoin FX, providing direct executable liquidity for payment firms, stablecoin issuers, venues and platforms. Leveraging deep‑learning models, IMMIX forecasts market states across thousands of instruments, pricing and trading them as principal. The platform offers a REST API and WebSocket market‑data streams, enabling clients to integrate stablecoin FX liquidity into their services with high throughput and low latency. IMMIX aims to decentralize stablecoin liquidity beyond the dollar, reducing conversion costs and improving market efficiency.
image: https://immix.xyz/og/immix.png
json_schemas:
- name: Accepted
  property_count: 1
  slug: immix-accepted
- name: CredentialRow
  property_count: 34
  slug: immix-credential-row
- name: Instrument
  property_count: 34
  slug: immix-data-instrument
- name: LeadSubmission
  property_count: 4
  slug: immix-lead-submission
- name: CancelOrdersResponse
  property_count: 40
  slug: immix-orders-cancel-orders-response
- name: GetOrdersResponse
  property_count: 40
  slug: immix-orders-get-orders-response
- name: SubmitOrdersResponse
  property_count: 40
  slug: immix-orders-submit-orders-response
- name: TradingPolicyRow
  property_count: 18
  slug: immix-trading-policy-row
jsonld:
- class_count: 120
  name: Immix Context
  property_count: 117
  slug: immix-context
layout: provider
modified: '2026-10-29'
name: IMMIX
nav: Providers
network: true
overview: 'IMMIX publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account addresses API, Account balances API, Accounts API, and 14 more. Tagged areas include Company, Fintech, Stablecoins, Foreign Exchange, and Artificial Intelligence.


  The IMMIX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IMMIX''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, and 28 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 0
  name: Immix Rate Limits
  slug: immix-rate-limits
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: IMMIX API Rules
  rule_count: 20
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 4
  slug: immix-rules
scopes:
- name: Immix Scopes
  scope_count: 0
  slug: immix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 64.3
    developer_ergonomics: 44.5
    discoverability: 74.1
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/immix/immix-2026-11-03T133712.png
security:
- kind: authentication
  name: Immix Authentication
  slug: immix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Immix Domain Security
  slug: immix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Immix Vulnerability Disclosure
  slug: immix-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: create-user
  slug: immix-create-user
slug: immix
tags:
- Company
- Fintech
- Stablecoins
- Foreign Exchange
- Artificial Intelligence
website: https://immix.xyz/
---
