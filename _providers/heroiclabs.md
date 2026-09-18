---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 249
  human_in_the_loop: 5
  name: Heroiclabs Agentic Access
  operation_count: 310
  slug: heroiclabs-agentic-access
  summary_line: 310 operations · 249 acting · 5 human-in-the-loop
api_count: 4
apis:
- baseURL: https://127.0.0.1:7350
  baseurl_source: declared
  description: The Nakama API is the core REST and WebSocket API for Heroic Labs' open-source game backend server. It provides endpoints for user authentication (social, device, email, and custom), account managemen
  name: Nakama API
  slug: nakama-api
- description: The Satori API is Heroic Labs' LiveOps platform API enabling game developers to manage live operations including feature flags, A/B experiments, audiences, and scheduled events without redeploying gam
  name: Satori API
  slug: satori-api
- baseURL: https://127.0.0.1:7350
  baseurl_source: declared
  description: The Console API from Heroic Labs — 73 operation(s) for console.
  name: Heroic Labs Console API
  slug: heroiclabs-console-api
- baseURL: https://127.0.0.1:7350
  baseurl_source: declared
  description: The Rpc API from Heroic Labs — 131 operation(s) for rpc.
  name: Heroic Labs Rpc API
  slug: heroiclabs-rpc-api
artifact_total: 33
asyncapis:
- description: ''
  name: Heroiclabs Nakama Realtime Events
  slug: heroiclabs-nakama-realtime-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hiro RPC Console API
  slug: open-heroiclabs-console-api
- collection_type: open
  name: Hiro RPC Console Nakama API
  slug: open-heroiclabs-nakama-api
- collection_type: open
  name: Hiro Console Rpc API
  slug: open-heroiclabs-rpc-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/overlays/heroiclabs-nakama-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/heroiclabs-nakama-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/heroiclabs/nakama/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/heroiclabs/nakama/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/heroiclabs/nakama/blob/master/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/agentic-access/heroiclabs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/heroiclabs-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/security/heroiclabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heroiclabs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/authentication/heroiclabs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/heroiclabs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://heroiclabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://heroiclabs.com/docs/nakama/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/heroiclabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heroic-labs
- group: company
  title: ''
  type: Blog
  url: https://heroiclabs.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://heroiclabs.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://heroiclabs.com/docs/nakama/getting-started/console/status/
- group: other
  title: ''
  type: X
  url: https://twitter.com/heroicdev
- group: operate
  title: ''
  type: Forums
  url: https://forum.heroiclabs.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/plans/heroiclabs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/heroiclabs-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/rate-limits/heroiclabs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/heroiclabs-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/finops/heroiclabs-finops.yml
  title: ''
  type: FinOps
  url: finops/heroiclabs-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/vocabulary/heroiclabs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/heroiclabs-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/json-ld/heroiclabs-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/heroiclabs-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://heroiclabs.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://heroiclabs.com/docs/nakama/
- group: start
  title: ''
  type: GettingStarted
  url: https://heroiclabs.com/docs/nakama/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://forum.heroiclabs.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heroiclabs
- group: start
  title: ''
  type: SignUp
  url: https://cloud.heroiclabs.com/register
- group: start
  title: ''
  type: Login
  url: https://cloud.heroiclabs.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heroiclabs.com/tos.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heroiclabs.com/privacypolicy.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/packages/heroiclabs-packages.yml
  title: ''
  type: Packages
  url: packages/heroiclabs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/packages/heroiclabs-packages.yml
  title: ''
  type: SDKs
  url: packages/heroiclabs-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/mcp/heroiclabs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/heroiclabs-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/llms/heroiclabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heroiclabs-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/grpc/heroiclabs-nakama-realtime.proto
  title: ''
  type: Protobuf
  url: grpc/heroiclabs-nakama-realtime.proto
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/conformance/heroiclabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/heroiclabs-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://heroiclabs.com/docs/heroic-cloud/enterprise/privacy-compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/errors/heroiclabs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/heroiclabs-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/lifecycle/heroiclabs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/heroiclabs-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/changelog/heroiclabs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/heroiclabs-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/cli/heroiclabs-cli.yml
  title: ''
  type: CLI
  url: cli/heroiclabs-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/sandbox/heroiclabs-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/heroiclabs-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/conventions/heroiclabs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/heroiclabs-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/data-model/heroiclabs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/heroiclabs-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/asyncapi/heroiclabs-nakama-realtime-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/heroiclabs-nakama-realtime-events.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-12'
description: Heroic Labs is the company behind Nakama, a leading open-source game backend server providing a comprehensive REST, WebSocket, and gRPC API for building scalable multiplayer and social games. The platform delivers essential backend services including real-time matchmaking, leaderboards, tournaments, chat, friend systems, and presence tracking. Nakama exposes its functionality via RESTful HTTP endpoints, real-time WebSocket connections, and gRPC, with server runtime support for custom logic in Go, TypeScript, and Lua. Heroic Labs also offers Heroic Cloud as a fully managed deployment platform and Satori as a LiveOps product for feature flags, A/B experiments, and live events.
examples:
- key_count: 3
  name: Heroiclabs Authenticate Email Example
  slug: heroiclabs-authenticate-email-example
- key_count: 3
  name: Heroiclabs Create Match Example
  slug: heroiclabs-create-match-example
- key_count: 3
  name: Heroiclabs List Leaderboard Records Example
  slug: heroiclabs-list-leaderboard-records-example
- key_count: 3
  name: Heroiclabs Send Event Example
  slug: heroiclabs-send-event-example
- key_count: 3
  name: Heroiclabs Write Storage Object Example
  slug: heroiclabs-write-storage-object-example
finops:
- name: Heroiclabs Finops
  service_category: ''
  slug: heroiclabs-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Heroic Labs Nakama game backend platform. Nakama exposes its functionality natively through REST, WebSocket, and gRPC interfaces. This Graph
  name: Heroic Labs (Nakama) GraphQL Schema
  slug: heroiclabs-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heroiclabs.png
json_schemas:
- name: apiAccount
  property_count: 7
  slug: apiAccount
- name: apiChannelMessage
  property_count: 13
  slug: apiChannelMessage
- name: apiFriend
  property_count: 4
  slug: apiFriend
- name: apiGroup
  property_count: 12
  slug: apiGroup
- name: apiLeaderboardRecord
  property_count: 12
  slug: apiLeaderboardRecord
- name: apiMatch
  property_count: 6
  slug: apiMatch
- name: apiNotification
  property_count: 7
  slug: apiNotification
- name: apiSession
  property_count: 3
  slug: apiSession
- name: apiStorageObject
  property_count: 9
  slug: apiStorageObject
- name: apiTournament
  property_count: 21
  slug: apiTournament
jsonld:
- class_count: 0
  name: Heroiclabs Context
  property_count: 54
  slug: heroiclabs-context
layout: provider
modified: '2026-08-08'
name: Heroic Labs
nav: Providers
network: true
overview: 'Heroic Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Nakama API, Console API, and Rpc API. Tagged areas include Game Backend, Multiplayer, Real-Time, WebSocket, and Matchmaking.


  The Heroic Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Heroic Labs'' developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 39 more developer resources.'
plans:
- name: Heroiclabs Plans Pricing
  plan_count: 5
  slug: heroiclabs-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Heroiclabs Rate Limits
  slug: heroiclabs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Heroic Labs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: heroiclabs-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 83.3
    catalog_earned_first_party: 0.0
    catalog_gap: 31.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 81.6
    contract_governance: 43.2
    contract_quality: 61.5
    developer_ergonomics: 80.4
    discoverability: 81.5
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 67.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/heroiclabs/refs/heads/main/screenshots/heroiclabs-2026-07-25T221028.png
security:
- kind: authentication
  name: Heroiclabs Authentication
  slug: heroiclabs-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Heroiclabs Domain Security
  slug: heroiclabs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: heroiclabs
tags:
- Game Backend
- Multiplayer
- Real-Time
- WebSocket
- Matchmaking
- Leaderboards
- Social Gaming
- Open-Source
- LiveOps
- gRPC
website: https://heroiclabs.com/
---
