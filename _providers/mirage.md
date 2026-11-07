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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 5
  name: Mirage Agentic Access
  operation_count: 23
  slug: mirage-agentic-access
  summary_line: 23 operations · 11 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.mirage.app
  baseurl_source: declared
  description: The Audio API from Mirage — 1 operation(s) for audio.
  name: Mirage Audio API
  slug: mirage-audio-api
- baseURL: https://api.mirage.app
  baseurl_source: declared
  description: The health API from Mirage — 1 operation(s) for health.
  name: Mirage Health API
  slug: mirage-health-api
- baseURL: https://api.mirage.app
  baseurl_source: declared
  description: The internal API from Mirage — 8 operation(s) for internal.
  name: Mirage Internal API
  slug: mirage-internal-api
- baseURL: https://api.mirage.app
  baseurl_source: declared
  description: The Meta Text Overlays API from Mirage — 2 operation(s) for meta text overlays.
  name: Mirage Meta Text Overlays API
  slug: mirage-meta-text-overlays-api
- baseURL: https://api.mirage.app
  baseurl_source: declared
  description: The root API from Mirage — 1 operation(s) for root.
  name: Mirage Root API
  slug: mirage-root-api
- baseURL: https://api.mirage.app
  baseurl_source: declared
  description: The Video Captions API from Mirage — 3 operation(s) for video captions.
  name: Mirage Video Captions API
  slug: mirage-video-captions-api
- baseURL: https://api.mirage.app
  baseurl_source: declared
  description: The Videos API from Mirage — 3 operation(s) for videos.
  name: Mirage Videos API
  slug: mirage-videos-api
artifact_total: 24
asyncapis:
- description: ''
  name: Mirage Webhooks
  slug: mirage-webhooks
collections:
- collection_type: open
  name: Mirage Video Audio API
  slug: open-mirage-audio-api
- collection_type: open
  name: Mirage Video Audio health API
  slug: open-mirage-health-api
- collection_type: open
  name: Mirage Video Audio internal API
  slug: open-mirage-internal-api
- collection_type: open
  name: Mirage Video Audio Meta Text Overlays API
  slug: open-mirage-meta-text-overlays-api
- collection_type: open
  name: Mirage Video Audio root API
  slug: open-mirage-root-api
- collection_type: open
  name: Mirage Video Audio Video Captions API
  slug: open-mirage-video-captions-api
- collection_type: open
  name: Mirage Video Audio Videos API
  slug: open-mirage-videos-api
common:
- group: other
  href: https://artifacts.apis.io/mirage/capabilities/mirage-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mirage-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/mirage/plans/mirage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mirage-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.captions.ai/
- group: other
  href: https://artifacts.apis.io/mirage/overlays/mirage-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirage-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/mirage/security/mirage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mirage-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/mirage/agentic-access/mirage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mirage-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://captions.ai/help/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://captions.ai/help/docs/api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://captions.ai/help/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://captions.ai/help/docs/api/overview
- group: auth
  href: https://artifacts.apis.io/mirage/authentication/mirage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mirage-authentication.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://captions.ai/help/docs/api/pricing
- group: start
  title: ''
  type: SignUp
  url: https://captions.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mirage.app/legal/captions-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mirage.app/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://captions.ai/help
- group: company
  title: ''
  type: Blog
  url: https://captions.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://captions.ai/help/whats-new
- group: operate
  href: https://artifacts.apis.io/mirage/changelog/mirage-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mirage-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://captions.ai/solutions/enterprise
- group: design
  href: https://artifacts.apis.io/mirage/errors/mirage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mirage-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mirage/conventions/mirage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mirage-conventions.yml
- group: design
  href: https://artifacts.apis.io/mirage/lifecycle/mirage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mirage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mirage/data-model/mirage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mirage-data-model.yml
- group: design
  href: https://artifacts.apis.io/mirage/conformance/mirage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mirage-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mirage/mcp/mirage-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mirage-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mirage/llms/mirage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mirage-llms.txt
- group: agent
  href: https://artifacts.apis.io/mirage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mirage/asyncapi/mirage-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mirage-webhooks.yml
created: '2026-07-17'
description: 'Mirage is an AI research company headquartered in New York City that builds Captions, an AI video editor and generator used by more than 20 million creators, small businesses, and enterprises worldwide. The Mirage Video API exposes the company''s state-of-the-art video models over a simple HTTP interface: generate expressive human video from an image and audio (Mirage Video 1), apply styled captions to an existing video, synthesize speech with text-to-speech voices, and render meta text overlays. It is an asynchronous submit-and-poll REST API authenticated with an x-api-key header and priced by usage (per minute of captioning, per second of generated video).'
finops:
- has_sources: true
  method: derived
  name: Mirage Finops
  primary_unit: minute of input video (rounded up to nearest minute)
  service_category: ''
  slug: mirage-finops
  template: false
image: https://captions.ai/mrkt-static/captions-og-image.png
layout: provider
modified: '2026-07-20'
name: Mirage
nav: Providers
network: true
overview: 'Mirage publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Health API, Internal API, and 4 more. Tagged areas include Company, Artificial Intelligence, Video, Video Generation, and Captions.


  The Mirage catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mirage''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, support, and 22 more developer resources.'
plans:
- name: Mirage Plans Pricing
  plan_count: 2
  slug: mirage-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Mirage API Rules
  rule_count: 44
  severity_counts:
    error: 34
    hint: 0
    info: 3
    warn: 7
  slug: mirage-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mirage/mirage-2026-08-07T183717.png
security:
- kind: authentication
  name: Mirage Authentication
  slug: mirage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mirage Domain Security
  slug: mirage-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: Add styled captions to a video with Mirage
  slug: mirage-caption-video
- name: Generate an expressive human video with Mirage
  slug: mirage-generate-video
- name: Synthesize speech with Mirage text-to-speech
  slug: mirage-text-to-speech
slug: mirage
tags:
- Company
- Artificial Intelligence
- Video
- Video Generation
- Captions
- Media
- Content Creation
- Text-to-Speech
- Machine Learning
website: https://www.captions.ai/
---
