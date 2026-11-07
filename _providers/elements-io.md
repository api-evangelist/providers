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
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Elements Io Webhooks
  slug: elements-io-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/elements-io/well-known/elements-io-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elements-io-status-security.txt
- group: design
  href: https://artifacts.apis.io/elements-io/asyncapi/elements-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/elements-io-webhooks.yml
- group: build
  href: https://artifacts.apis.io/elements-io/cli/elements-io-cli.yml
  title: ''
  type: CLI
  url: cli/elements-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/elements-io/changelog/elements-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elements-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/elements-io/conventions/elements-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elements-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/elements-io/authentication/elements-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elements-io-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.circle.com/cctp/migration-from-v1-to-v2.md
- group: design
  href: https://artifacts.apis.io/elements-io/lifecycle/elements-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elements-io-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/elements-io/llms/elements-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elements-io-llms.txt
- group: other
  href: https://artifacts.apis.io/elements-io/a2a/elements-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/elements-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/elements-io/well-known/elements-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elements-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/elements-io/hosts/elements-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elements-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/elements-io/vendors/elements-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elements-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agents.circle.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.circle.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.circle.com/
- group: start
  title: ''
  type: SignUp
  url: https://console.circle.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.circle.com/legal/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.circle.com/developer
- group: company
  title: ''
  type: Blog
  url: https://www.circle.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.circle.com/stablecoins/quickstarts/transfer-usdc-evm
- group: docs
  title: ''
  type: Documentation
  url: https://developers.circle.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.circle.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/elements-io/security/elements-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elements-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.elements.io
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://developers.circle.com/mcp
  - status: 403
    url: https://www.elements.io/mcp
  - status: 200
    url: http://www.elements.io
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Circle provides a full‑stack platform that offers regulated stablecoins such as USDC and EURC, tokenized money‑market funds, and wrapped BTC, along with APIs and services for digital‑asset accounts, payments, treasury management, on‑chain FX, and developer tools for building AI‑native and blockchain applications. It serves businesses, banks, developers, and institutional users that need to mint, hold, move, and trade digital currencies globally.
image: https://cdn.prod.website-files.com/67116d0daddc92483c812e88/6a1ee203d94902c2fd7260bb_share-q2-2026-home.jpg
layout: provider
modified: '2026-10-25'
name: Elements
nav: Providers
network: true
overview: 'Elements is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Stablecoins, Digital Assets, Payments, Treasury Management, and Trading Services.


  The Elements catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Elements'' developer surface includes CLI, changelog, authentication, support, signup flow, engineering blog, getting-started guide, and 18 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 47.6
    discoverability: 55.4
    operational_transparency: 53.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 16.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/elements-io/elements-io-2026-11-03T131419.png
security:
- kind: authentication
  name: Elements Io Authentication
  slug: elements-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Elements Io Domain Security
  slug: elements-io-domain-security
  summary_line: TLSv1.3
slug: elements-io
tags:
- Stablecoins
- Digital Assets
- Payments
- Treasury Management
- Trading Services
website: http://www.elements.io
---
