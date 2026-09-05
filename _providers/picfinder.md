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
  band: human-only
  dimensions:
    agent_card: false
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: WebSocket API for AI image inference powered by the RunWare / DiffusionMaster platform. Supports text-to-image and image-to-image generation, model / LoRA selection, ControlNet, inpainting, outpaintin
  name: PicFinder Image Inference API
  slug: picfinder-image-inference-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://picfinder.ai/support
- group: docs
  title: ''
  type: Documentation
  url: https://picfinder.ai/support
- group: docs
  title: ''
  type: APIReference
  url: https://www.npmjs.com/package/picfinder-sdk
- group: start
  title: ''
  type: SignUp
  url: https://picfinder.ai/sign-up-account-details
- group: start
  title: ''
  type: Login
  url: https://picfinder.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://picfinder.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://picfinder.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://picfinder.ai/support
- group: build
  title: ''
  type: Packages
  url: packages/picfinder-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/picfinder-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/picfinder-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/picfinder-conventions.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/picfinder-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/picfinder-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/picfinder-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/picfinder-llms.txt
created: '2026-07-17'
description: PicFinder (PicFinder.ai) is an AI-powered image generation platform that turns text prompts into unlimited realistic, artistic, and abstract images in near real time. Beyond the consumer web app and Figma plugin, PicFinder exposes a developer API for programmatic image inference powered by the RunWare / DiffusionMaster inference platform. The API is delivered over a WebSocket connection and authenticated with an API key, and supports text-to-image and image-to-image generation, model and LoRA selection (including CivitAI models), ControlNet guidance, inpainting and outpainting, background removal, GAN upscaling, image-to-text interrogation, prompt enhancement, and similar-image retrieval. A first-party JavaScript / TypeScript SDK (picfinder-sdk) wraps the WebSocket protocol for both browser and Node.js environments. PicFinder was surfaced as an a16z portfolio company and profiled into the API Evangelist network.
image: https://picfinder.ai/favicon.ico
layout: provider
modified: '2026-07-20'
name: PicFinder
nav: Providers
network: true
overview: 'PicFinder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Image-Generation, and Generative AI.


  PicFinder''s developer surface includes documentation, API reference, signup flow, support, authentication, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.7
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/picfinder/refs/heads/main/screenshots/picfinder-2026-09-02T151219.png
security:
- kind: authentication
  name: Picfinder Authentication
  slug: picfinder-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Picfinder Domain Security
  slug: picfinder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: picfinder
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Image-Generation
- Generative AI
- Text-to-Image
- Image to Image
- Developer Tools
- SDK
- WebSocket
website: https://picfinder.ai/support
---
