---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.music.ai/v1
  baseurl_source: declared
  description: Account/application metadata.
  name: Moises Application API
  slug: moises-application-api
- baseURL: https://api.music.ai/v1
  baseurl_source: declared
  description: Create, retrieve, list, and delete processing jobs.
  name: Moises Jobs API
  slug: moises-jobs-api
- baseURL: https://api.music.ai/v1
  baseurl_source: declared
  description: Temporary file staging for input audio.
  name: Moises Upload API
  slug: moises-upload-api
- baseURL: https://api.music.ai/v1
  baseurl_source: declared
  description: List the workflows configured in your account.
  name: Moises Workflows API
  slug: moises-workflows-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Music AI Application API
  slug: open-moises-application-api
- collection_type: open
  name: Music AI Application Jobs API
  slug: open-moises-jobs-api
- collection_type: open
  name: Music AI Application Upload API
  slug: open-moises-upload-api
- collection_type: open
  name: Music AI Application Workflows API
  slug: open-moises-workflows-api
common:
- group: company
  title: ''
  type: Website
  url: https://moises.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://music.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://music.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://music.ai/docs/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://music.ai/docs/getting-started/quick-start/
- group: commercial
  title: ''
  type: Pricing
  url: https://music.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://music.ai/dash
- group: operate
  title: ''
  type: Support
  url: https://help.moises.ai/hc/
- group: company
  title: ''
  type: Blog
  url: https://moises.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moises-ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/moises-music-ai-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moises-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/moises-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moises-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/moises-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/moises-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moises-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/moises-music-ai-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/moises-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moises-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moises-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moises-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moises-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Moises is the creative suite for musicians from Music AI, Inc., serving more than 70 million musicians worldwide with AI-powered tools for practice, performance, and creation — stem separation to isolate vocals and instruments, chord and key detection, AI-generated stems, and voice synthesis across web, desktop, iOS, and Android. The same models power the Music AI developer platform (music.ai, formerly reached at developer.moises.ai), a B2B REST API that exposes those capabilities as composable Modules assembled into Workflows and executed as asynchronous Jobs. Developers upload audio to temporary storage, submit a job against a workflow, and poll for results, with official Node.js and Python SDKs and a command-line client. Moises won iPad App of the Year (2024) and was an Apple Design Awards finalist (2025), and is backed by Norwest Venture Partners.
image: https://music.ai/favicon.ico
layout: provider
modified: '2026-07-20'
name: Moises
nav: Providers
network: true
overview: 'Moises publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Application API, Jobs API, Upload API, and 1 more. Tagged areas include Company, Music, Audio, Artificial Intelligence, and Machine-Learning.


  Moises'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 56.1
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 41.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moises/refs/heads/main/screenshots/moises-2026-08-07T184046.png
security:
- kind: authentication
  name: Moises Authentication
  slug: moises-authentication
  summary_line: apiKey · 1 scheme
slug: moises
tags:
- Company
- Music
- Audio
- Artificial Intelligence
- Machine-Learning
- Stem Separation
- Audio Processing
- Media
- Developer Platform
- SDK
website: https://moises.ai
---
