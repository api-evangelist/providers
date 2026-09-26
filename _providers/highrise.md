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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: wss://highrise.game/web/botapi
  baseurl_source: declared
  description: WebSocket API for building and running programmable bots inside Highrise rooms. Bots receive a stream of room events (chat, emotes, reactions, joins/leaves, movement, tips, voice, DMs, moderation) and
  name: Highrise Bot API
  slug: highrise-bot-api
- description: Highrise Studio is the world-building toolset. Its Engine API and Cloud API let creators script custom worlds, games and experiences in Lua with deep customization of the Highrise runtime.
  name: Highrise Studio (Engine + Cloud API)
  slug: highrise-studio-engine-cloud-api
- baseURL: wss://highrise.game/web/botapi
  baseurl_source: declared
  description: The grabs API from Highrise — 2 operation(s) for grabs.
  name: Highrise Grabs API
  slug: highrise-grabs-api
- baseURL: wss://highrise.game/web/botapi
  baseurl_source: declared
  description: The items API from Highrise — 2 operation(s) for items.
  name: Highrise Items API
  slug: highrise-items-api
- baseURL: wss://highrise.game/web/botapi
  baseurl_source: declared
  description: The posts API from Highrise — 2 operation(s) for posts.
  name: Highrise Posts API
  slug: highrise-posts-api
- baseURL: wss://highrise.game/web/botapi
  baseurl_source: declared
  description: The rooms API from Highrise — 2 operation(s) for rooms.
  name: Highrise Rooms API
  slug: highrise-rooms-api
- baseURL: wss://highrise.game/web/botapi
  baseurl_source: declared
  description: The users API from Highrise — 2 operation(s) for users.
  name: Highrise Users API
  slug: highrise-users-api
artifact_total: 16
asyncapis:
- description: Event surface of the Highrise Bot API, generated faithfully from the official highrise-bot-sdk event model (github.com/pocketzworld/python-bot-sdk, src/highrise/models.py). Bots open a single WebSocke
  name: Highrise Bot API — Event Surface
  slug: highrise-bot-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Highrise Web grabs API
  slug: open-highrise-grabs-api
- collection_type: open
  name: Highrise Web grabs items API
  slug: open-highrise-items-api
- collection_type: open
  name: Highrise Web grabs posts API
  slug: open-highrise-posts-api
- collection_type: open
  name: Highrise Web grabs rooms API
  slug: open-highrise-rooms-api
- collection_type: open
  name: Highrise Web grabs users API
  slug: open-highrise-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://highrise.game
- group: start
  title: ''
  type: DeveloperPortal
  url: https://create.highrise.game
- group: docs
  title: ''
  type: Documentation
  url: https://create.highrise.game/learn
- group: docs
  title: ''
  type: APIReference
  url: https://create.highrise.game/learn
- group: start
  title: ''
  type: GettingStarted
  url: https://create.highrise.game/learn/guides/bots/creating-a-bot
- group: operate
  title: ''
  type: Support
  url: https://support.highrise.game
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pocketzworld
- group: commercial
  title: ''
  type: TermsOfService
  url: https://highrise.game/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://highrise.game/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://highrise.game/account/settings
- group: company
  title: ''
  type: Partnerships
  url: https://create.highrise.game/partnerships
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/packages/highrise-packages.yml
  title: ''
  type: Packages
  url: packages/highrise-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/packages/highrise-packages.yml
  title: ''
  type: SDKs
  url: packages/highrise-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/cli/highrise-cli.yml
  title: ''
  type: CLI
  url: cli/highrise-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/authentication/highrise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/highrise-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/conventions/highrise-conventions.yml
  title: ''
  type: Conventions
  url: conventions/highrise-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/errors/highrise-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/highrise-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/data-model/highrise-data-model.yml
  title: ''
  type: DataModel
  url: data-model/highrise-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/conformance/highrise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/highrise-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/lifecycle/highrise-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/highrise-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/changelog/highrise-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/highrise-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/mcp/highrise-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/highrise-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/llms/highrise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/highrise-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/well-known/highrise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/highrise-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/security/highrise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/highrise-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/overlays/highrise-web-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/highrise-web-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/asyncapi/highrise-bot-api-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/highrise-bot-api-asyncapi.yml
created: '2026-07-17'
description: 'Highrise is a mobile-first virtual world by Pocket Worlds Inc where users create avatars, hang out in social rooms, design and trade fashion items, and build custom worlds. Alongside the consumer app, Highrise operates a developer platform for creators: a WebSocket Bot API for running programmable bots inside rooms (official Python and .NET SDKs), a read-only REST Web API exposing public users, rooms, posts, items and grabs data, and Highrise Studio with an Engine API and Cloud API for scripting worlds and games in Lua. Bots authenticate with an API token minted from the Highrise account settings and are bound to a room ID.'
image: https://highrise.game/assets/images/highrise-meta.png
layout: provider
modified: '2026-07-19'
name: Highrise
nav: Providers
network: true
overview: 'Highrise publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bot API, Grabs API, Items API, and 4 more. Tagged areas include Company, Virtual World, Metaverse, Social, and Gaming.


  The Highrise catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Highrise''s developer surface includes documentation, API reference, getting-started guide, support, CLI, authentication, changelog, and 21 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 21.9
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 39.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/screenshots/highrise-2026-07-25T221206.png
security:
- kind: authentication
  name: Highrise Authentication
  slug: highrise-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Highrise Domain Security
  slug: highrise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: highrise
tags:
- Company
- Virtual World
- Metaverse
- Social
- Gaming
- Avatars
- Bots
- Developer Platform
- Chat
- Real-Time
website: https://highrise.game
---
