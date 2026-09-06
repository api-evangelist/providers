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
  - '{''url'': ''https://www.soundtrackyourbrand.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.soundtrack.io/ — a different registrable domain (soundtrackyourbrand.com -> soundtrack.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Single-endpoint GraphQL API (queries, mutations and websocket subscriptions) for building display, control and monitoring apps on top of Soundtrack — now-playing, playback control, device pairing, sch
  name: Soundtrack API
  slug: soundtrack-api
artifact_total: 4
asyncapis:
- description: 'Event/streaming surface of the Soundtrack API, derived from the GraphQL Subscriptions root type via introspection. Clients subscribe over websocket to the single GraphQL endpoint (token supplied as a '
  name: Soundtrack API — GraphQL Subscriptions
  slug: soundtrack-your-brand-subscriptions-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundtrack-your-brand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soundtrackyourbrand.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.soundtrackyourbrand.com/v2/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.soundtrackyourbrand.com/v2/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.soundtrackyourbrand.com/v2/explore
- group: start
  title: ''
  type: GettingStarted
  url: https://api.soundtrackyourbrand.com/v2/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.soundtrackyourbrand.com/v2/docs/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soundtrack.io/
- group: company
  title: ''
  type: Blog
  url: https://www.soundtrackyourbrand.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.soundtrackyourbrand.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soundtrackyourbrand
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soundtrackyourbrand.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.soundtrackyourbrand.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.soundtrackyourbrand.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soundtrackyourbrand.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soundtrackyourbrand.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundtrack-your-brand-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soundtrack-your-brand-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/soundtrack-your-brand-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soundtrack-your-brand-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soundtrack-your-brand-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/soundtrack-your-brand-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/soundtrack-your-brand-subscriptions-asyncapi.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/soundtrack-your-brand-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soundtrack-your-brand-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/soundtrack-your-brand-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Soundtrack Your Brand (Soundtrack) is a Stockholm-based business music streaming company that provides licensed background music for physical spaces such as retail stores, restaurants, cafes, hotels and gyms. Its Soundtrack API is a single-endpoint GraphQL API that lets partners and customers build display, control and monitoring applications on top of Soundtrack: read what is currently playing in a sound zone, control playback, pair playback devices, and manage schedules, playlists and music libraries across accounts and locations. The API is free for paying Soundtrack customers and is complemented by a partner-gated native Player SDK for embedding Soundtrack playback in hardware.'
image: https://api.soundtrackyourbrand.com/v2/docs/img/favicon.ico
layout: provider
modified: '2026-07-21'
name: Soundtrack Your Brand
nav: Providers
network: true
overview: 'Soundtrack Your Brand publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Music Streaming, Background Music, and GraphQL.


  The Soundtrack Your Brand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Soundtrack Your Brand''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, pricing, and 20 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 16
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
    contract_quality: 53.1
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 41.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soundtrack-your-brand/refs/heads/main/screenshots/soundtrack-your-brand-2026-08-17T082005.png
security:
- kind: authentication
  name: Soundtrack Your Brand Authentication
  slug: soundtrack-your-brand-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Soundtrack Your Brand Domain Security
  slug: soundtrack-your-brand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundtrack-your-brand
tags:
- Company
- Music
- Music Streaming
- Background Music
- GraphQL
- Retail
- Hospitality
- Audio
website: https://www.soundtrackyourbrand.com
---
