---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
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
artifact_total: 15
collections:
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
- group: commercial
  href: https://artifacts.apis.io/moises/plans/moises-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moises-plans-pricing.yml
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
  href: https://artifacts.apis.io/moises/openapi/_original/moises-music-ai-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/moises-music-ai-openapi.yml
- group: auth
  href: https://artifacts.apis.io/moises/authentication/moises-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moises-authentication.yml
- group: build
  href: https://artifacts.apis.io/moises/packages/moises-packages.yml
  title: ''
  type: Packages
  url: packages/moises-packages.yml
- group: build
  href: https://artifacts.apis.io/moises/packages/moises-packages.yml
  title: ''
  type: SDKs
  url: packages/moises-packages.yml
- group: build
  href: https://artifacts.apis.io/moises/cli/moises-cli.yml
  title: ''
  type: CLI
  url: cli/moises-cli.yml
- group: agent
  href: https://artifacts.apis.io/moises/mcp/moises-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/moises-mcp.yml
- group: agent
  href: https://artifacts.apis.io/moises/llms/moises-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moises-llms.txt
- group: other
  href: https://artifacts.apis.io/moises/overlays/moises-music-ai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moises-music-ai-overlay.yaml
- group: design
  href: https://artifacts.apis.io/moises/conformance/moises-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moises-conformance.yml
- group: design
  href: https://artifacts.apis.io/moises/errors/moises-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/moises-error-codes.yml
- group: design
  href: https://artifacts.apis.io/moises/lifecycle/moises-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moises-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/moises/conventions/moises-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moises-conventions.yml
- group: design
  href: https://artifacts.apis.io/moises/data-model/moises-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moises-data-model.yml
- group: agent
  href: https://artifacts.apis.io/moises/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Moises is the creative suite for musicians from Music AI, Inc., serving more than 70 million musicians worldwide with AI-powered tools for practice, performance, and creation — stem separation to isolate vocals and instruments, chord and key detection, AI-generated stems, and voice synthesis across web, desktop, iOS, and Android. The same models power the Music AI developer platform (music.ai, formerly reached at developer.moises.ai), a B2B REST API that exposes those capabilities as composable Modules assembled into Workflows and executed as asynchronous Jobs. Developers upload audio to temporary storage, submit a job against a workflow, and poll for results, with official Node.js and Python SDKs and a command-line client. Moises won iPad App of the Year (2024) and was an Apple Design Awards finalist (2025), and is backed by Norwest Venture Partners.
finops:
- has_sources: true
  method: derived
  name: Moises Finops
  primary_unit: subscription
  service_category: ''
  slug: moises-finops
  template: false
image: https://music.ai/favicon.ico
layout: provider
modified: '2026-07-20'
name: Moises
nav: Providers
network: true
overview: 'Moises publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Application API, Jobs API, Upload API, and 1 more. Tagged areas include Company, Music, Audio, Artificial Intelligence, and Machine Learning.


  The Moises catalog on APIs.io includes 1 Spectral governance ruleset.


  Moises'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 18 more developer resources.'
plans:
- name: Moises Plans Pricing
  plan_count: 3
  slug: moises-plans-pricing
- name: Moises Price Estimates
  plan_count: 0
  slug: moises-price-estimates
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Moises API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: moises-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 50.5
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 48.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moises/moises-2026-08-07T184046.png
security:
- kind: authentication
  name: Moises Authentication
  slug: moises-authentication
  summary_line: apiKey · 1 scheme
skill_count: 2
skills:
- name: Discover workflows and manage jobs
  slug: moises-manage-jobs
- name: Separate stems with Music AI
  slug: moises-separate-stems
slug: moises
tags:
- Company
- Music
- Audio
- Artificial Intelligence
- Machine Learning
- Stem Separation
- Audio Processing
- Media
- Developer Platform
- SDK
website: https://moises.ai
---
