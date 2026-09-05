---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Luma Labs Agentic Access
  operation_count: 13
  slug: luma-labs-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
apis:
- description: The Dream Machine API exposes Luma's Ray and Photon model families for programmatic image and video generation. It provides endpoints for creating, listing, retrieving, and deleting generations, gener
  name: Luma Dream Machine API
  slug: dream-machine-api
- baseURL: https://api.lumalabs.ai/dream-machine/v1
  baseurl_source: declared
  description: The Concepts API from Luma AI — 1 operation(s) for concepts.
  name: Luma AI Concepts API
  slug: luma-labs-concepts-api
- baseURL: https://api.lumalabs.ai/dream-machine/v1
  baseurl_source: declared
  description: The Credits API from Luma AI — 1 operation(s) for credits.
  name: Luma AI Credits API
  slug: luma-labs-credits-api
- baseURL: https://api.lumalabs.ai/dream-machine/v1
  baseurl_source: declared
  description: The Generations API from Luma AI — 4 operation(s) for generations.
  name: Luma AI Generations API
  slug: luma-labs-generations-api
- baseURL: https://api.lumalabs.ai/dream-machine/v1
  baseurl_source: declared
  description: The Image API from Luma AI — 2 operation(s) for image.
  name: Luma AI Image API
  slug: luma-labs-image-api
- baseURL: https://api.lumalabs.ai/dream-machine/v1
  baseurl_source: declared
  description: The System API from Luma AI — 1 operation(s) for system.
  name: Luma AI System API
  slug: luma-labs-system-api
- baseURL: https://api.lumalabs.ai/dream-machine/v1
  baseurl_source: declared
  description: The Video API from Luma AI — 3 operation(s) for video.
  name: Luma AI Video API
  slug: luma-labs-video-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Luma Dream Machine Concepts API
  slug: open-luma-labs-concepts-api
- collection_type: open
  name: Luma Dream Machine Concepts Credits API
  slug: open-luma-labs-credits-api
- collection_type: open
  name: Luma Dream Machine Concepts Generations API
  slug: open-luma-labs-generations-api
- collection_type: open
  name: Luma Dream Machine Concepts Image API
  slug: open-luma-labs-image-api
- collection_type: open
  name: Luma Dream Machine Concepts System API
  slug: open-luma-labs-system-api
- collection_type: open
  name: Luma Dream Machine Concepts Video API
  slug: open-luma-labs-video-api
- collection_type: open
  name: Luma Dream Machine API
  slug: open-luma-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/luma-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luma-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/luma-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lumalabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lumalabs.ai
- group: company
  title: ''
  type: Blog
  url: https://lumalabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumalabs
- group: commercial
  title: ''
  type: Pricing
  url: https://lumalabs.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lumalabs.ai/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumalabs.ai/legal/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/LumaLabsAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/luma-ai
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/lumalabs
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lumalabs.ai/llms.txt
created: '2026-05-23'
description: Luma AI is a generative media company best known for Dream Machine, a family of image and video models including Ray (video), Photon and Photon Flash (image). The Dream Machine API gives developers access to text-to-video, image-to-video, image generation, upscaling, video modification with style transfer, reframing, audio attachment, and concept controls. Luma serves creators, agencies, and product teams building generative media features, and monetizes through consumer subscription tiers (Plus, Pro, Ultra), team and enterprise plans, and a credit-based developer API.
finops:
- name: Luma Labs Finops
  service_category: API
  slug: luma-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luma-labs.png
layout: provider
modified: '2026-05-23'
name: Luma AI
nav: Providers
network: true
overview: 'Luma AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Concepts API, Credits API, Generations API, and 3 more. Tagged areas include Artificial Intelligence, Generative AI, Video, Image, and Text-to-Video.


  Luma AI''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Luma Labs Plans Pricing
  plan_count: 1
  slug: luma-labs-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Luma Labs Rate Limits
  slug: luma-labs-rate-limits
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 36.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luma-labs/refs/heads/main/screenshots/luma-labs-2026-06-20T184752.png
security:
- kind: authentication
  name: Luma Labs Authentication
  slug: luma-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Luma Labs Domain Security
  slug: luma-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: luma-labs
tags:
- Artificial Intelligence
- Generative AI
- Video
- Image
- Text-to-Video
- Image-to-Video
- Upscaling
- Reframing
- Dream Machine
- Ray
- Photon
- Creative Tools
website: https://lumalabs.ai
---
