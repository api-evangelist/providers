---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://arpeggi.io/api/kits/v1
  baseurl_source: declared
  description: Split an audio track into vocal and instrument stems.
  name: Arpeggi Labs Stem Splitter API
  slug: arpeggi-labs-stem-splitter-api
- baseURL: https://arpeggi.io/api/kits/v1
  baseurl_source: declared
  description: Isolate vocals from a mixed audio track.
  name: Arpeggi Labs Vocal Separation API
  slug: arpeggi-labs-vocal-separation-api
- baseURL: https://arpeggi.io/api/kits/v1
  baseurl_source: declared
  description: Blend two to four voice models into a new voice model.
  name: Arpeggi Labs Voice Blender API
  slug: arpeggi-labs-voice-blender-api
- baseURL: https://arpeggi.io/api/kits/v1
  baseurl_source: declared
  description: Convert an input performance to a target voice model.
  name: Arpeggi Labs Voice Conversion API
  slug: arpeggi-labs-voice-conversion-api
- baseURL: https://arpeggi.io/api/kits/v1
  baseurl_source: declared
  description: Browse and retrieve available voice models.
  name: Arpeggi Labs Voice Models API
  slug: arpeggi-labs-voice-models-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kits AI Stem Splitter API
  slug: open-arpeggi-labs-stem-splitter-api
- collection_type: open
  name: Kits AI Stem Splitter Vocal Separation API
  slug: open-arpeggi-labs-vocal-separation-api
- collection_type: open
  name: Kits AI Stem Splitter Voice Blender API
  slug: open-arpeggi-labs-voice-blender-api
- collection_type: open
  name: Kits AI Stem Splitter Voice Conversion API
  slug: open-arpeggi-labs-voice-conversion-api
- collection_type: open
  name: Kits AI Stem Splitter Voice Models API
  slug: open-arpeggi-labs-voice-models-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/arpeggi-labs-kits-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arpeggi-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arpeggi-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kits.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.kits.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kits.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kits.ai/api-reference/introduction/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kits.ai/api-reference/introduction/quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.kits.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.kits.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arpeggi-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://app.kits.ai/subscriptions
- group: start
  title: ''
  type: SignUp
  url: https://app.kits.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kits.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kits.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arpeggi-labs-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arpeggi-labs-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arpeggi-labs-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arpeggi-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arpeggi-labs-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arpeggi-labs-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arpeggi-labs-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/arpeggi-labs-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/arpeggi-labs-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Arpeggi Labs is the company behind Kits AI, a studio-quality AI music and audio platform for musicians, producers, and developers. Kits AI provides voice cloning and conversion, an AI singing generator with 100+ royalty-free artist voice models, vocal isolation, stem separation, AI mastering, and a voice-model blender, alongside an ethically sourced "Earn" program that pays vocalists to license digital clones of their voice. The Kits AI API exposes these capabilities as asynchronous inference jobs over a REST interface at arpeggi.io/api/kits/v1, authenticated with a bearer API key: create a voice conversion, vocal separation, stem split, or voice-blend job, then poll for the signed output file URLs. Arpeggi Labs is an a16z portfolio company; its earlier product was Arpeggi Studio, a web3 in-browser music creation platform.'
image: https://kits.ai/opengraph-image
layout: provider
modified: '2026-07-18'
name: Arpeggi Labs
nav: Providers
network: true
overview: 'Arpeggi Labs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Stem Splitter API, Vocal Separation API, Voice Blender API, and 2 more. Tagged areas include Company, Music, Audio, Artificial Intelligence, and Voice.


  Arpeggi Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 18 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 2
  name: Arpeggi Labs Rate Limits
  slug: arpeggi-labs-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 46.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arpeggi-labs/refs/heads/main/screenshots/arpeggi-labs-2026-07-25T201241.png
security:
- kind: authentication
  name: Arpeggi Labs Authentication
  slug: arpeggi-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arpeggi Labs Domain Security
  slug: arpeggi-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arpeggi-labs
tags:
- Company
- Music
- Audio
- Artificial Intelligence
- Voice
- Machine-Learning
- Generative AI
- Media
website: https://kits.ai
---
