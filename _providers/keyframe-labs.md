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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Keyframe Labs Agentic Access
  operation_count: 8
  slug: keyframe-labs-agentic-access
  summary_line: 8 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.keyframelabs.com/v1
  baseurl_source: declared
  description: The LLM models API from Keyframe Labs — 2 operation(s) for llm models.
  name: Keyframe Labs LLM models API
  slug: keyframe-labs-llm-models-api
- baseURL: https://api.keyframelabs.com/v1
  baseurl_source: declared
  description: The Meet bots API from Keyframe Labs — 3 operation(s) for meet bots.
  name: Keyframe Labs Meet bots API
  slug: keyframe-labs-meet-bots-api
- baseURL: https://api.keyframelabs.com/v1
  baseurl_source: declared
  description: The Sessions API from Keyframe Labs — 1 operation(s) for sessions.
  name: Keyframe Labs Sessions API
  slug: keyframe-labs-sessions-api
- baseURL: https://api.keyframelabs.com/v1
  baseurl_source: declared
  description: The Voices API from Keyframe Labs — 2 operation(s) for voices.
  name: Keyframe Labs Voices API
  slug: keyframe-labs-voices-api
- baseURL: https://api.keyframelabs.com/v1
  baseurl_source: declared
  description: The Avatars API from Keyframe Labs — 1 operation(s) for avatars.
  name: Keyframe Labs Avatars API
  slug: keyframe-labs-avatars-api
- baseURL: https://api.keyframelabs.com/v1
  baseurl_source: declared
  description: The Generations API from Keyframe Labs — 3 operation(s) for generations.
  name: Keyframe Labs Generations API
  slug: keyframe-labs-generations-api
artifact_total: 18
collections:
- collection_type: open
  name: Sessions LLM models API
  slug: open-keyframe-labs-llm-models-api
- collection_type: open
  name: Sessions LLM models Meet bots API
  slug: open-keyframe-labs-meet-bots-api
- collection_type: open
  name: LLM models Sessions API
  slug: open-keyframe-labs-sessions-api
- collection_type: open
  name: Sessions LLM models Voices API
  slug: open-keyframe-labs-voices-api
common:
- group: commercial
  href: https://artifacts.apis.io/keyframe-labs/plans/keyframe-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keyframe-labs-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/keyframe-labs/agentic-access/keyframe-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/keyframe-labs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/keyframe-labs/security/keyframe-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keyframe-labs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/keyframe-labs/authentication/keyframe-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keyframe-labs-authentication.yml
- group: agent
  href: https://artifacts.apis.io/keyframe-labs/llms/keyframe-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keyframe-labs-llms.txt
- group: build
  href: https://artifacts.apis.io/keyframe-labs/packages/keyframe-labs-packages.yml
  title: ''
  type: Packages
  url: packages/keyframe-labs-packages.yml
- group: build
  href: https://artifacts.apis.io/keyframe-labs/packages/keyframe-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/keyframe-labs-packages.yml
- group: design
  href: https://artifacts.apis.io/keyframe-labs/components/keyframe-labs-components.yml
  title: ''
  type: Components
  url: components/keyframe-labs-components.yml
- group: agent
  href: https://artifacts.apis.io/keyframe-labs/mcp/keyframe-labs-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/keyframe-labs-mcp.yml
- group: other
  href: https://artifacts.apis.io/keyframe-labs/overlays/keyframe-labs-sessions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keyframe-labs-sessions-overlay.yaml
- group: design
  href: https://artifacts.apis.io/keyframe-labs/conformance/keyframe-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keyframe-labs-conformance.yml
- group: design
  href: https://artifacts.apis.io/keyframe-labs/errors/keyframe-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/keyframe-labs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/keyframe-labs/lifecycle/keyframe-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/keyframe-labs-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/keyframe-labs/conventions/keyframe-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/keyframe-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/keyframe-labs/data-model/keyframe-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/keyframe-labs-data-model.yml
- group: agent
  href: https://artifacts.apis.io/keyframe-labs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.keyframelabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.keyframelabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keyframelabs.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.keyframelabs.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.keyframelabs.com/guides/getting-started/quickstart-hosted
- group: start
  title: ''
  type: SignUp
  url: https://platform.keyframelabs.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keyframelabs.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.keyframelabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keyframelabs
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/Wfce5xHNd5
- group: start
  title: ''
  type: Demo
  url: https://demo.keyframelabs.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keyframe-labs-inc
- group: company
  title: ''
  type: Twitter
  url: https://x.com/KeyframeLabs
created: '2026-07-17'
description: Keyframe Labs builds real-time foundation models that turn AI voice and text agents into lifelike, emotionally expressive video calls. Its Persona-1.5-Live product lets developers add photoreal AI avatars ("personas") to their agents and applications with a few lines of embed code, at roughly 500ms latency and from $0.06 per minute. The platform exposes a REST Sessions API (create a live session, manage meeting bots for Zoom/Meet/Teams, and list voices and LLM models), JavaScript/TypeScript SDKs, and embeddable UI elements, with hosted and self-managed integration paths that plug into agent frameworks such as LiveKit Agents, ElevenLabs Agents, and OpenAI Realtime. Founded in 2025 and backed by Y Combinator (Spring 2026), Keyframe Labs is based in San Francisco.
finops:
- has_sources: true
  method: derived
  name: Keyframe Labs Finops
  primary_unit: subscription
  service_category: ''
  slug: keyframe-labs-finops
  template: false
image: https://platform.keyframelabs.com/og.png
layout: provider
modified: '2026-07-19'
name: Keyframe Labs
nav: Providers
network: true
overview: 'Keyframe Labs publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including LLM models API, Meet bots API, Sessions API, and 3 more. Tagged areas include Company, Artificial Intelligence, Avatars, Video, and Conversational AI.


  Keyframe Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Keyframe Labs Plans Pricing
  plan_count: 5
  slug: keyframe-labs-plans-pricing
- name: Keyframe Labs Price Estimates
  plan_count: 0
  slug: keyframe-labs-price-estimates
random_paper: 19
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 47.9
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/keyframe-labs/keyframe-labs-2026-07-25T223654.png
security:
- kind: authentication
  name: Keyframe Labs Authentication
  slug: keyframe-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Keyframe Labs Domain Security
  slug: keyframe-labs-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: Send a Keyframe persona into a meeting
  slug: keyframe-labs-meeting-persona-bot
- name: Start a Keyframe persona session
  slug: keyframe-labs-start-persona-session
slug: keyframe-labs
tags:
- Company
- Artificial Intelligence
- Avatars
- Video
- Conversational AI
- Agents
- Real-Time
- Personas
- Voice
- Y Combinator
website: https://www.keyframelabs.com
---
