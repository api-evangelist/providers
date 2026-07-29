---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: WebSocket API for AI image inference powered by the RunWare / DiffusionMaster platform. Supports text-to-image and image-to-image generation, model / LoRA selection, ControlNet, inpainting, outpaintin
  name: PicFinder Image Inference API
  slug: picfinder-image-inference-api
artifact_total: 4
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: picfinder-mcp.yml
  slug: picfinder-mcpyml
modified: '2026-07-20'
name: PicFinder
nav: Providers
network: true
overview: 'PicFinder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Image Generation, and Generative AI.


  PicFinder''s developer surface includes documentation, API reference, signup flow, support, authentication, and 11 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 25.1
  delta: -1.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.0
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Machine Learning
- Image Generation
- Generative AI
- Text to Image
- Image to Image
- Developer Tools
- SDK
- WebSocket
website: https://picfinder.ai/support
---
