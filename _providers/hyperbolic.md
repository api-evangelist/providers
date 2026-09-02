---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hyperbolic Agentic Access
  operation_count: 5
  slug: hyperbolic-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: OpenAI-compatible inference API for 25+ open-source models. Surfaces include text chat, vision, image generation (FLUX, Stable Diffusion, LoRA adapters), and audio (Melo TTS). Pay-as-you-go from $0.00
  name: Hyperbolic Serverless Inference API
  slug: inference
- description: Bare-metal GPU rental with SSH access for full control. Hourly rates from $1.39-$1.99 with no long-term commitments. Reserved clusters available monthly/annually with up to 40% discount.
  name: Hyperbolic On-Demand GPU API
  slug: gpu
- description: The Audio API from Hyperbolic — 1 operation(s) for audio.
  name: Hyperbolic Audio API
  slug: hyperbolic-audio-api
- description: The Chat API from Hyperbolic — 1 operation(s) for chat.
  name: Hyperbolic Chat API
  slug: hyperbolic-chat-api
- description: The Completions API from Hyperbolic — 1 operation(s) for completions.
  name: Hyperbolic Completions API
  slug: hyperbolic-completions-api
- description: The Image API from Hyperbolic — 1 operation(s) for image.
  name: Hyperbolic Image API
  slug: hyperbolic-image-api
- description: The Models API from Hyperbolic — 1 operation(s) for models.
  name: Hyperbolic Models API
  slug: hyperbolic-models-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hyperbolic Inference Audio API
  slug: open-hyperbolic-audio-api
- collection_type: open
  name: Hyperbolic Inference Audio Chat API
  slug: open-hyperbolic-chat-api
- collection_type: open
  name: Hyperbolic Inference Audio Completions API
  slug: open-hyperbolic-completions-api
- collection_type: open
  name: Hyperbolic Inference Audio Image API
  slug: open-hyperbolic-image-api
- collection_type: open
  name: Hyperbolic Inference Audio Models API
  slug: open-hyperbolic-models-api
- collection_type: open
  name: Hyperbolic Inference API
  slug: open-hyperbolic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperbolic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperbolic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperbolic-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HyperbolicLabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperbolic-labs
- group: company
  title: ''
  type: Website
  url: https://hyperbolic.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbolic.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperbolic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperbolic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperbolic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://hyperbolic.ai/blog
created: '2026-05-08'
description: Hyperbolic Labs is an open-access AI cloud offering on-demand GPU rentals and serverless LLM inference. Hosts 25+ open-source models with OpenAI-compatible chat, vision, image generation (FLUX, Stable Diffusion, LoRA), and audio (Melo TTS) APIs. Reserved-cluster pricing available with 3-12 month commitments and up to 40% discount.
finops:
- name: Hyperbolic Finops
  service_category: AI
  slug: hyperbolic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperbolic.png
layout: provider
modified: '2026-05-08'
name: Hyperbolic
nav: Providers
network: true
overview: 'Hyperbolic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Completions API, and 2 more. Tagged areas include Artificial Intelligence, LLM, Inference, GPU, and Open-Source.


  Hyperbolic''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hyperbolic Plans Pricing
  plan_count: 1
  slug: hyperbolic-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Hyperbolic Rate Limits
  slug: hyperbolic-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperbolic/refs/heads/main/screenshots/hyperbolic-2026-06-20T183118.png
security:
- kind: authentication
  name: Hyperbolic Authentication
  slug: hyperbolic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hyperbolic Domain Security
  slug: hyperbolic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperbolic
tags:
- Artificial Intelligence
- LLM
- Inference
- GPU
- Open-Source
- Serverless
- Image-Generation
- Audio
website: https://hyperbolic.xyz/
---
