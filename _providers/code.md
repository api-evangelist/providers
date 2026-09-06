---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Code payments gRPC/Protobuf API — account, currency, messaging, and transaction (intent/swap) services that power the Code wallet and SDK.
  name: Code Protobuf API
  slug: code-protobuf-api
artifact_total: 4
asyncapis:
- description: ''
  name: Code Webhooks
  slug: code-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://getcode.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://code-payments.github.io/code-sdk/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://code-payments.github.io/code-sdk/docs/guide/introduction.html
- group: docs
  title: ''
  type: APIReference
  url: https://code-payments.github.io/code-sdk/docs/reference/app.html
- group: start
  title: ''
  type: GettingStarted
  url: https://code-payments.github.io/code-sdk/docs/guide/quick-start.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/code-payments
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/T8Tpj8DBFp
- group: build
  title: ''
  type: Packages
  url: packages/code-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/code-packages.yml
- group: design
  title: ''
  type: Components
  url: components/code-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/code-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/code-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/code-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/code-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/code-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/code-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/code-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/code-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/code-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/code-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/code-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/code-domain-security.yml
created: '2026-07-17'
description: 'Code is an open, self-custodial payments protocol and mobile wallet built on the Solana blockchain. Its SDK lets any web developer embed a "Pay with Code" button and accept permissionless micropayments — as little as 5 cents per transaction plus a flat 1-cent blockchain fee — with no sign-up required and just a few lines of code. The API is defined as gRPC/Protobuf services (code-protobuf-api): clients sign transaction intents with a self-custodial Ed25519 keypair, payments are created as idempotent payment intents, and completion is confirmed server-side or via JWT-signed webhooks. The entire stack — SDKs (JavaScript, Go, Python, PHP), the Code VM, and the on-chain Solana programs — is open source under the code-payments GitHub org. Code was seeded by Union Square Ventures.'
image: https://avatars.githubusercontent.com/u/151064663?v=4
layout: provider
modified: '2026-07-18'
name: Code
nav: Providers
network: true
overview: 'Code publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Micropayments, Wallets, and Solana.


  The Code catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Code''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 17 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 33.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/code/refs/heads/main/screenshots/code-2026-07-25T205901.png
security:
- kind: authentication
  name: Code Authentication
  slug: code-authentication
  summary_line: self-custodial-keypair/jwt · 2 schemes
- kind: domain-security
  name: Code Domain Security
  slug: code-domain-security
  summary_line: DMARC
slug: code
tags:
- Company
- Payments
- Micropayments
- Wallets
- Solana
- Blockchain
- Cryptocurrency
- gRPC
- Self-Custodial
website: https://getcode.com
---
