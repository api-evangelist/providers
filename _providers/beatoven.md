---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Beatoven Agentic Access
  operation_count: 2
  slug: beatoven-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://public-api.beatoven.ai
  baseurl_source: declared
  description: Poll asynchronous composition task status and retrieve generated assets.
  name: Beatoven.ai Tasks API
  slug: beatoven-tasks-api
- baseURL: https://public-api.beatoven.ai
  baseurl_source: declared
  description: Compose new tracks from natural language prompts.
  name: Beatoven.ai Tracks API
  slug: beatoven-tracks-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Beatoven Composition API
  slug: open-beatoven-composition-api
- collection_type: open
  name: Beatoven Composition Tasks API
  slug: open-beatoven-tasks-api
- collection_type: open
  name: Beatoven Composition Tasks Tracks API
  slug: open-beatoven-tracks-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Beatoven/public-api/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beatoven-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beatoven-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beatoven-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.beatoven.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.beatoven.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Beatoven/public-api
- group: start
  title: ''
  type: GettingStarted
  url: https://sync.beatoven.ai/apiDashboard
- group: start
  title: ''
  type: Signup
  url: https://sync.beatoven.ai/
- group: start
  title: ''
  type: Signup
  url: https://sync.beatoven.ai/apiDashboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Beatoven
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Beatoven/public-api/tree/main/sdk
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Beatoven/public-api/tree/main/examples
- group: company
  title: ''
  type: Blog
  url: https://www.beatoven.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beatoven.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/beatoven-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beatoven-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/beatoven-finops.yml
- group: other
  title: ''
  type: Artists
  url: https://www.beatoven.ai/artists
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beatoven.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beatoven.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@beatoven.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beatoven-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/beatoven_ai
created: '2026-05-24'
description: Beatoven.ai is an Indian generative-music startup (Bengaluru, founded 2021) building text-to-music and text-to-sound-effects models for video creators, podcasters, game developers, and brands. Its Maestro Music and Maestro SFX models render royalty-free background tracks and foley from natural-language prompts, with downloads delivered as mp3, aac, or wav plus separately rendered stems (bass, chords, melody, percussion). Beatoven is Fairly Trained certified - musicians whose work appears in the training corpus receive equitable compensation. The company exposes a public REST Composition API (public-api.beatoven.ai) plus an open-source Python SDK (github.com/Beatoven/public-api), a Make.com integration, and a self-serve API dashboard. The company has raised an ~$1.3M pre-Series A led by Capital 2B and IvyCap Ventures, claims 2M+ creators and 15M+ tracks generated, and reports 96% of its revenue from international markets.
examples:
- key_count: 3
  name: Beatoven Compose Request Example
  slug: beatoven-compose-request-example
- key_count: 2
  name: Beatoven Compose Response Example
  slug: beatoven-compose-response-example
- key_count: 2
  name: Beatoven Task Status Response Example
  slug: beatoven-task-status-response-example
features:
- Maestro Music - text-to-music generation rendered as mp3, aac, or wav
- Maestro SFX - text-to-sound-effects generation
- Stems delivery on every track - bass, chords, melody, and percussion as separate audio files
- Asynchronous task-based REST API with status polling (composing / running / composed)
- Optional looping flag for loopable backgrounds
- Bearer-token authentication, single endpoint surface (POST /api/v1/tracks/compose, GET /api/v1/tasks/{task_id})
- Open-source Python SDK (pip install via git+ subdirectory) with async/await client
- Make.com integration - Create and Compose Track, Composition Status, Make an API Call modules
- Royalty-free, non-exclusive perpetual commercial license on downloads
- Fairly Trained certification - musicians in the training set receive compensation
- Web product tiers (Trial, Creator $10/mo, Visionary $20/mo) and Pay-as-You-Go at $3/minute
- 2M+ creators, 15M+ tracks generated, 96% revenue from international markets
finops:
- name: Beatoven Finops
  service_category: AI and Machine Learning
  slug: beatoven-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beatoven.png
json_schemas:
- name: Beatoven Compose Request
  property_count: 3
  slug: beatoven-compose-request
- name: Beatoven Track
  property_count: 3
  slug: beatoven-track
jsonld:
- class_count: 0
  name: Beatoven Context
  property_count: 4
  slug: beatoven-context
layout: provider
modified: '2026-05-24'
name: Beatoven.ai
nav: Providers
network: true
overview: 'Beatoven.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network: Tasks API and Tracks API. Tagged areas include Artificial Intelligence, Music, Music Generation, Generative Audio, and Text-to-Music.


  The Beatoven.ai catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Beatoven.ai''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, code examples, engineering blog, and 17 more developer resources.'
plans:
- name: Beatoven Plans Pricing
  plan_count: 5
  slug: beatoven-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Beatoven Rate Limits
  slug: beatoven-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Beatoven.ai API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: beatoven-composition-rules
- effective_rule_count: 5
  extends: []
  name: Beatoven.ai API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: beatoven-jsonschema-spectral-rules
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 85.0
    catalog_earned_first_party: 0.0
    catalog_gap: 30.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 54.5
    contract_quality: 70.4
    developer_ergonomics: 48.8
    discoverability: 68.5
    governance: 54.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Beatoven Authentication
  slug: beatoven-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Beatoven Domain Security
  slug: beatoven-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beatoven
tags:
- Artificial Intelligence
- Music
- Music Generation
- Generative Audio
- Text-to-Music
- Text To SFX
- Royalty-Free Music
- Background Music
- Video Creators
- Podcasts
- Stems
- Fairly Trained
- India
website: https://www.beatoven.ai
---
