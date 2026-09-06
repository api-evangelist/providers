---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: HTTP endpoint for invoking a single published glif (AI workflow) by ID and passing a list of named or positional string inputs. POST a JSON body with `id` and `inputs` to https://simple-api.glif.app u
  name: Glif Simple API
  slug: glif-simple-api
- description: Read-and-write REST API for the Glif platform — list and fetch glifs (`/glifs`), look up runs (`/runs`), fetch the authenticated user (`/me`), look up users (`/user`), and browse curated collections (
  name: Glif REST API
  slug: glif-rest-api
artifact_total: 4
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/glif-app-a2a.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/glif-app-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glif-app-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://glif.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glif.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glif.app/getting-started/intro-to-glif
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glif.app/getting-started/faqs
- group: operate
  title: ''
  type: ChangeLog
  url: https://glif.app/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://glif.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glif.app/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glif.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://glif.app/contact
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/nuR9zZ2nsh
- group: build
  title: ''
  type: GitHub
  url: https://github.com/glifxyz
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/heyglif
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heyglif
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@heyglif
- group: build
  title: ''
  type: Tools
  url: https://github.com/glifxyz/glif-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/glifxyz/ComfyUI-GlifNodes
- group: build
  title: ''
  type: Tools
  url: https://github.com/glifxyz/ComfyUI-GlifVision
- group: build
  title: ''
  type: SDKs
  url: https://github.com/glifxyz/glif-client-python
- group: build
  title: ''
  type: SampleApps
  url: https://github.com/glifxyz/glif-api-demo
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/glifxyz/api-docs
- group: other
  title: ''
  type: Application
  url: https://chromewebstore.google.com/detail/glif-remix-the-web-with-a/abfbooehhdjcgmbmcpkcebcmpfnlingo
- group: other
  title: ''
  type: CompanyProfile
  url: https://pitchbook.com/profiles/company/535615-03
created: '2026-05-25'
description: Glif is a creative AI platform from Spellcasters, Inc. — originally launched in 2023 as a no-code visual workflow builder for chaining text, image, audio, and video models into shareable "glifs", and re-launched in March 2026 as Glif 2.0, a single chat-based AI agent with access to 100+ native tools (Claude Sonnet 4.5, Claude Opus 4.1, GPT-4o, Nano Banana Pro, Flux 2 Turbo, Seedream V4, Kling 2.5 Turbo Pro, VEO 3.1, Hailuo 2.3, ElevenLabs, MiniMax v2, FFmpeg, web search and more). Glif raised a $17.5M seed round led by a16z and USV in April 2026. The platform is used by creators, e-commerce sellers, performance marketers, and agencies to produce short-form video, product shoots, ad campaigns, character/comic art, memes, logos, and SVG vector graphics. Glif's public REST and Simple APIs were deprecated on 2026-05-20 in favor of the chat agent surface; the open Glif MCP server, ComfyUI custom nodes, Chrome extension, and Python client remain the canonical programmatic entry points
  to the platform. Profiled in the API Evangelist network as a reference case for the "no-code AI workflow builder → AI agent" platform pivot, alongside peers such as Anthropic, OpenAI, and other foundation-model orchestration providers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-25'
name: Glif
nav: Providers
network: true
overview: 'Glif publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, No-Code, Workflows, Creative AI, and Generative AI.


  Glif''s developer surface includes developer portal, documentation, changelog, pricing, support, GitHub presence, YouTube channel, and 18 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glif-app/refs/heads/main/screenshots/glif-app-2026-06-20T181913.png
security:
- kind: domain-security
  name: Glif App Domain Security
  slug: glif-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Glif App Vulnerability Disclosure
  slug: glif-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: glif-app
tags:
- Artificial Intelligence
- No-Code
- Workflows
- Creative AI
- Generative AI
- Video Generation
- Image-Generation
- ComfyUI
- MCP
- LLM Apps
website: https://glif.app
---
