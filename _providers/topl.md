---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The gRPC interface to the Apparatus (Topl) blockchain: NodeRpc on the Bifrost full node for submitting transactions, reading blocks and following the chain tip, and the Genus indexer''s BlockService, T'
  name: Apparatus (Topl) Node and Genus gRPC API
  slug: apparatus-node
artifact_total: 4
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Topl
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Topl/Knowledge-Base
- group: other
  title: ''
  type: Protobuf
  url: grpc/topl-protobuf.yml
- group: build
  title: ''
  type: Packages
  url: packages/topl-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/topl-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/topl-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/topl-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/topl-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/topl-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/topl-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/topl-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/topl-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/topl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/topl-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/topl-llms.txt
created: '2026-08-30'
description: 'Topl was an impact-technology company founded in 2017 out of Rice University and based in Houston, Texas, building a proof-of-stake blockchain that let organizations prove ethical and sustainable practices on-ledger. It raised a $3M seed in 2020 and a $15M Series A in 2022, and shipped a real developer platform: the Bifrost node, the Genus indexer, the Brambl SDK family for Scala, TypeScript, JavaScript and Dart, and the brambl-cli client. In late 2023 the company rebranded to Apparatus and repositioned around Thunder, a Bitcoin Layer 2. It appears to have wound down after that — the last first-party artifact of any kind shipped on 2024-09-26, all ten remaining public repositories are archived, every documentation and API host now fails to resolve, and the topl.co domain lapsed and was re-registered by an unrelated owner on 2024-12-30. What survives, and what this profile is built from, is the contract itself: a 38-file proto3 module defining 6 gRPC services, 30 RPCs and 138
  messages, still downloadable from the Buf Schema Registry, plus the published SDKs and container images.'
image: https://raw.githubusercontent.com/Topl/Knowledge-Base/main/static/img/apparatus-logo.svg
layout: provider
modified: '2026-08-30'
name: Topl
nav: Providers
network: true
overview: 'Topl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Distributed Ledger, gRPC, and Protobuf.


  Topl''s developer surface includes documentation, CLI, authentication, changelog, and 11 more developer resources.'
plans:
- name: Topl Plans Pricing
  plan_count: 0
  slug: topl-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Topl Rate Limits
  slug: topl-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 16.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/topl/refs/heads/main/screenshots/topl-2026-09-02T163927.png
security:
- kind: authentication
  name: Topl Authentication
  slug: topl-authentication
  summary_line: 0 schemes
slug: topl
tags:
- Company
- Blockchain
- Distributed Ledger
- gRPC
- Protobuf
- Web3
- Proof of Stake
- Sustainability
- Impact
- Tokenization
- Wound Down
---
