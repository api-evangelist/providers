---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Mubert Agentic Access
  operation_count: 37
  slug: mubert-agentic-access
  summary_line: 37 operations · 18 acting
api_count: 1
apis:
- description: Price
  name: Mubert Price API
  slug: mubert-price-api
- description: Public
  name: Mubert Public API
  slug: mubert-public-api
- description: Public Service
  name: Mubert Public Service API
  slug: mubert-public-service-api
- description: Service
  name: Mubert Service API
  slug: mubert-service-api
- description: Stripe
  name: Mubert Stripe API
  slug: mubert-stripe-api
- description: Subscription
  name: Mubert Subscription API
  slug: mubert-subscription-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mubert AI Music API v3
  slug: open-mubert-music-api
- collection_type: open
  name: Mubert AI Music API v3 Price API
  slug: open-mubert-price-api
- collection_type: open
  name: Mubert AI Music API v3 Price Public API
  slug: open-mubert-public-api
- collection_type: open
  name: Mubert AI Music API v3 Price Public Service API
  slug: open-mubert-public-service-api
- collection_type: open
  name: Mubert AI Music API v3 Price Service API
  slug: open-mubert-service-api
- collection_type: open
  name: Mubert AI Music API v3 Price Stripe API
  slug: open-mubert-stripe-api
- collection_type: open
  name: Mubert AI Music API v3 Price Subscription API
  slug: open-mubert-subscription-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mubert-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mubert-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mubert-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mubert.com/
- group: other
  title: ''
  type: ProductPage
  url: https://mubert.com/api
- group: other
  title: ''
  type: ProductPage
  url: https://mubert.com/render
- group: other
  title: ''
  type: ProductPage
  url: https://mubert.com/play
- group: other
  title: ''
  type: ProductPage
  url: https://mubert.com/business
- group: other
  title: ''
  type: ProductPage
  url: https://mubert.com/studio
- group: docs
  title: ''
  type: Documentation
  url: https://mubert.com/api
- group: docs
  title: ''
  type: SwaggerUI
  url: https://music-api.mubert.com/api/v3/swagger
- group: docs
  title: ''
  type: AIDocumentation
  url: https://music-api.mubert.com/swagger-doc/llms.txt
- group: docs
  title: ''
  type: AIDocumentation
  url: https://music-api.mubert.com/swagger-doc/llms-full.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MubertAI
- group: build
  title: ''
  type: Examples
  url: https://github.com/MubertAI/Mubert-Text-to-Music
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/MubertAI/skills
- group: company
  title: ''
  type: Blog
  url: https://mubert.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mubert.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mubert.com/legal/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://mubert.com/contact
- group: commercial
  title: ''
  type: Plans
  url: plans/mubert-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mubert-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mubert-finops.yml
created: '2026-05-23'
description: Mubert is a generative AI music platform that composes royalty-free, DMCA-free music in real time from millions of artist-contributed loops, samples, and stems. The B2B Mubert AI Music API (v3) powers track generation, continuous HTTP / WebRTC streaming, browse access to a pre-generated music library, and service-tier customer + license + Stripe subscription administration. Mubert is used by apps, games, video tools, health and fitness products, and AI-content pipelines (including integrations with Picsart, Canva, and Restream) to embed adaptive generative music inside their experiences.
examples:
- key_count: 2
  name: Mubert Create Customer Example
  slug: mubert-create-customer-example
- key_count: 2
  name: Mubert Create Track Example
  slug: mubert-create-track-example
- key_count: 2
  name: Mubert Edit Track Example
  slug: mubert-edit-track-example
- key_count: 2
  name: Mubert Get Streaming Link Example
  slug: mubert-get-streaming-link-example
features:
- Generative track creation from text prompts, image prompts, or playlist taxonomy
- Live streaming over HTTP and WebRTC with sub-second latency
- Continuous stream control — restart, set-intensity, set-loop-state
- 150+ genres, 50+ moods, 200+ million unique tracks per the provider
- Stem-level editing (drums, bass, leads, vocals) and 12+ part replacement (drums, percs, hats, claps, bass, mids, leads, fx, vocals, pads, riser, impact)
- Track durations 15-1500 seconds, modes track or loop, intensities low/medium/high
- Pre-generated music library browsable by genre, mood, BPM range, key, activity
- Track-store cache for re-issuing previously generated tracks
- Generate-similar endpoint to create variations of an existing track
- Record a live stream session into a fixed track asset
- Service-tier customer CRUD with custom_id for mapping back to your users
- Service-tier license management exposing features, bitrates, intensities, formats, modes, and per-customer quotas
- Stripe-backed subscription buy / cancel / billing portal flows
- License-level webhooks for billing and generation lifecycle events
- All output is royalty-free, DMCA-free, and cleared for commercial use and monetization
- AI-optimized documentation: llms.txt and llms-full.txt published alongside Swagger UI
- Official MubertAI/skills repo of Agent Skills (setup, generate, streaming, library, manage)
finops:
- name: Mubert Finops
  service_category: AI and Machine Learning
  slug: mubert-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mubert.png
integrations:
- Picsart — generative music in UGC content tooling
- Canva — music inside the design surface
- Restream — live-stream background music
- Stripe — subscription billing
json_schemas:
- name: Mubert Customer
  property_count: 6
  slug: mubert-customer
- name: Mubert License
  property_count: 13
  slug: mubert-license
- name: Mubert Playlist
  property_count: 5
  slug: mubert-playlist
- name: Mubert Streaming Link
  property_count: 7
  slug: mubert-streaming-link
- name: Mubert Track
  property_count: 12
  slug: mubert-track
json_structures:
- name: Mubert License Structure
  property_count: 13
  slug: mubert-license-structure
- name: Mubert Track Structure
  property_count: 12
  slug: mubert-track-structure
jsonld:
- class_count: 6
  name: Mubert Context
  property_count: 30
  slug: mubert-context
layout: provider
modified: '2026-05-25'
name: Mubert
nav: Providers
network: true
overview: 'Mubert publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Price API, Public API, Public Service API, and 3 more. Tagged areas include AI Music, Generative, Royalty-Free, Streaming, and Text-to-Music.


  The Mubert catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mubert''s developer surface includes authentication, documentation, code examples, engineering blog, and 19 more developer resources.'
plans:
- name: Mubert Plans Pricing
  plan_count: 4
  slug: mubert-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Mubert Rate Limits
  slug: mubert-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Mubert API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mubert-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Mubert API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 2
  slug: mubert-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 75.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 2.6
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mubert/refs/heads/main/screenshots/mubert-2026-06-20T185853.png
security:
- kind: authentication
  name: Mubert Authentication
  slug: mubert-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Mubert Domain Security
  slug: mubert-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mubert
tags:
- AI Music
- Generative
- Royalty-Free
- Streaming
- Text-to-Music
- Image-to-Music
- Stems
- B2B
use_cases:
- Apps embedding adaptive background music
- Games with dynamic, progression-aware soundscapes
- Health, fitness, and wellness apps with BPM/heart-rate mapped music
- Video editors and podcast tools needing royalty-free score generation
- AI content pipelines pairing image / text generation with matching music
- User-generated content platforms offering safe-to-publish music
- Marketing, advertising, and brand audio for retail and OOH
website: https://mubert.com/
---
