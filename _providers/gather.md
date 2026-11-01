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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.gather.town
  baseurl_source: declared
  description: Manage the email guestlist (members/guests) of a space
  name: Gather Guestlist API
  slug: gather-guestlist-api
- baseURL: https://api.gather.town
  baseurl_source: declared
  description: Read and write the map/room data of a space
  name: Gather Maps API
  slug: gather-maps-api
- baseURL: https://api.gather.town
  baseurl_source: declared
  description: Create and manage Gather spaces
  name: Gather Spaces API
  slug: gather-spaces-api
artifact_total: 10
collections:
- collection_type: open
  name: Gather HTTP Guestlist API
  slug: open-gather-guestlist-api
- collection_type: open
  name: Gather HTTP Guestlist Maps API
  slug: open-gather-maps-api
- collection_type: open
  name: Gather HTTP Guestlist Spaces API
  slug: open-gather-spaces-api
common:
- group: docs
  href: https://artifacts.apis.io/gather/openapi/_original/gather-http-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/gather-http-api-openapi.yml
- group: auth
  href: https://artifacts.apis.io/gather/authentication/gather-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gather-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gather/security/gather-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gather-domain-security.yml
- group: build
  href: https://artifacts.apis.io/gather/packages/gather-packages.yml
  title: ''
  type: Packages
  url: packages/gather-packages.yml
- group: build
  href: https://artifacts.apis.io/gather/packages/gather-packages.yml
  title: ''
  type: SDKs
  url: packages/gather-packages.yml
- group: agent
  href: https://artifacts.apis.io/gather/well-known/gather-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gather-well-known.yml
- group: agent
  href: https://artifacts.apis.io/gather/mcp/gather-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gather-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gather/llms/gather-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gather-llms.txt
- group: other
  href: https://artifacts.apis.io/gather/overlays/gather-http-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gather-http-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/gather/conformance/gather-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gather-conformance.yml
- group: design
  href: https://artifacts.apis.io/gather/errors/gather-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gather-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gather/lifecycle/gather-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gather-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gather.town/
- group: design
  href: https://artifacts.apis.io/gather/conventions/gather-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gather-conventions.yml
- group: design
  href: https://artifacts.apis.io/gather/data-model/gather-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gather-data-model.yml
- group: agent
  href: https://artifacts.apis.io/gather/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.gather.town/hc/en-us/categories/api-integration
- group: docs
  title: ''
  type: Documentation
  url: https://gathertown.notion.site/Gather-HTTP-API-3bbf6c59325f40aca7ef5ce14c677444
- group: docs
  title: ''
  type: APIReference
  url: https://gathertown.notion.site/Gather-HTTP-API-3bbf6c59325f40aca7ef5ce14c677444
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/gathertown/api-examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gathertown
- group: operate
  title: ''
  type: Support
  url: https://support.gather.town/
- group: company
  title: ''
  type: Blog
  url: https://gather.town/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gather.town/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gather.town/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gather.town/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gather.town/privacy
- group: company
  title: ''
  type: Website
  url: https://gather.town/
created: '2026-07-17'
description: Gather (gather.town) is a video-calling platform that places people in a navigable 2D virtual space, letting multiple groups hold separate conversations in parallel and walk in and out of them as easily as they would in real life. It is used for remote and hybrid offices, conferences, and events. Gather exposes a public HTTP API for programmatically creating spaces and reading/writing the map (room) data of a space, plus managing a space's email guestlist, and a realtime WebSocket "game" API (via the official @gathertown/gather-game-client SDK) for subscribing to player/movement/chat events and driving avatars or bots. API keys are generated at gather.town/apiKeys and require Admin or Builder permission on the target space. Gather was surfaced as a portfolio company of Index Ventures and True Ventures and enriched into the API Evangelist network.
image: https://app.gather.town/images/site/site_preview.png
layout: provider
modified: '2026-07-19'
name: Gather
nav: Providers
network: true
overview: 'Gather publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Guestlist API, Maps API, and Spaces API. Tagged areas include Company, Future Of Work, Virtual Office, Video Conferencing, and Collaboration.


  Gather''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 13.9
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 36.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gather/gather-2026-07-25T215458.png
security:
- kind: authentication
  name: Gather Authentication
  slug: gather-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gather Domain Security
  slug: gather-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Manage Gather email guestlist
  slug: gather-manage-guestlist
- name: Manage Gather space maps
  slug: gather-manage-space-maps
slug: gather
tags:
- Company
- Future Of Work
- Virtual Office
- Video Conferencing
- Collaboration
- Metaverse
- Remote Work
- Event
website: https://gather.town/
---
