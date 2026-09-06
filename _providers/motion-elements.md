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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Motion Elements Agentic Access
  operation_count: 21
  slug: motion-elements-agentic-access
  summary_line: 21 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.motionelements.com/v2
  baseurl_source: declared
  description: Authenticated account details.
  name: Motion Elements Account API
  slug: motion-elements-account-api
- baseURL: https://api.motionelements.com/v2
  baseurl_source: declared
  description: Retrieve individual marketplace elements.
  name: Motion Elements Elements API
  slug: motion-elements-elements-api
- baseURL: https://api.motionelements.com/v2
  baseurl_source: declared
  description: 'Reference metadata: media types, categories, software versions, and music facets.'
  name: Motion Elements Media types API
  slug: motion-elements-media-types-api
- baseURL: https://api.motionelements.com/v2
  baseurl_source: declared
  description: Search the marketplace across media types.
  name: Motion Elements Search API
  slug: motion-elements-search-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MotionElements Marketplace Account API
  slug: open-motion-elements-account-api
- collection_type: open
  name: MotionElements Marketplace Account Elements API
  slug: open-motion-elements-elements-api
- collection_type: open
  name: MotionElements Marketplace Account Media types API
  slug: open-motion-elements-media-types-api
- collection_type: open
  name: MotionElements Marketplace Account Search API
  slug: open-motion-elements-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/motion-elements-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motion-elements-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/motion-elements-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/motion-elements-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://motionelements.com
- group: design
  title: ''
  type: Conventions
  url: conventions/motion-elements-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/motion-elements-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/motion-elements-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/motion-elements-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/motion-elements-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/motion-elements-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.motionelements.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.motionelements.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.motionelements.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.motionelements.com/developer
- group: operate
  title: ''
  type: Support
  url: https://help.motionelements.com/
- group: company
  title: ''
  type: Blog
  url: https://www.motionelements.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/motionelements
- group: commercial
  title: ''
  type: Pricing
  url: https://www.motionelements.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.motionelements.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.motionelements.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.motionelements.com/legal/privacy
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://api-docs.motionelements.com/
created: '2026-07-17'
description: 'MotionElements is a global creative-asset marketplace and AI production platform offering an unlimited-download subscription catalog of 26M+ royalty-free assets: stock video, music, sound effects, motion and editing templates (After Effects, Premiere Pro, Final Cut / Apple Motion, DaVinci Resolve, .mogrt), photos, vectors, GIFs and Lottie animations, plus Studio AI generative tools. Its Marketplace API v2 lets platforms search, retrieve, license and download from the catalog using HTTP Basic authentication (API secret key as username) over HTTPS.'
image: https://static.moele.me/img/motionelements-og-en.220830.jpg
layout: provider
modified: '2026-07-20'
name: Motion Elements
nav: Providers
network: true
overview: 'Motion Elements publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Elements API, Media types API, and 1 more. Tagged areas include Media, Stock Media, Video, Music, and Sound Effects.


  Motion Elements'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 56.5
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 42.6
  provenance:
    agentic_access: derived
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
screenshot: https://raw.githubusercontent.com/api-evangelist/motion-elements/refs/heads/main/screenshots/motion-elements-2026-08-07T184326.png
security:
- kind: authentication
  name: Motion Elements Authentication
  slug: motion-elements-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Motion Elements Domain Security
  slug: motion-elements-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: motion-elements
tags:
- Media
- Stock Media
- Video
- Music
- Sound Effects
- Templates
- Marketplace
- Creative Assets
- Generative AI
- Search
- Company
website: https://motionelements.com
---
