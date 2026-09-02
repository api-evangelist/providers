---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Freepik Agentic Access
  operation_count: 22
  slug: freepik-agentic-access
  summary_line: 22 operations · 19 acting
api_count: 1
apis:
- description: Generate music and sound effects.
  name: Freepik Audio API
  slug: freepik-audio-api
- description: Upscale, relight, restyle, or edit images.
  name: Freepik Image Editing API
  slug: freepik-image-editing-api
- description: Generate images from text or reference inputs.
  name: Freepik Image Generation API
  slug: freepik-image-generation-api
- description: Search Freepik's stock library.
  name: Freepik Resources API
  slug: freepik-resources-api
- description: Poll asynchronous task status.
  name: Freepik Tasks API
  slug: freepik-tasks-api
- description: Generate video from images or text.
  name: Freepik Video Generation API
  slug: freepik-video-generation-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Freepik / Magnific Audio API
  slug: open-freepik-audio-api
- collection_type: open
  name: Freepik / Magnific Audio Image Editing API
  slug: open-freepik-image-editing-api
- collection_type: open
  name: Freepik / Magnific Audio Image Generation API
  slug: open-freepik-image-generation-api
- collection_type: open
  name: Freepik / Magnific Audio Resources API
  slug: open-freepik-resources-api
- collection_type: open
  name: Freepik / Magnific Audio Tasks API
  slug: open-freepik-tasks-api
- collection_type: open
  name: Freepik / Magnific Audio Video Generation API
  slug: open-freepik-video-generation-api
- collection_type: open
  name: Freepik / Magnific API
  slug: open-freepik
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freepik-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freepik-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freepik-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freepik-company
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freepik-company
- group: company
  title: ''
  type: Website
  url: https://www.freepik.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freepik.com/
- group: start
  title: ''
  type: Signup
  url: https://www.freepik.com/profile/signup
created: '2025-01-07'
description: Freepik is a leading platform that provides high-quality graphic resources for designers, marketers, and creative professionals. Its developer platform (operated through Magnific) offers AI image, video, audio generation, image editing, and access to the Freepik stock library.
finops:
- name: Freepik Finops
  service_category: API
  slug: freepik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freepik.png
layout: provider
modified: '2026-05-19'
name: Freepik
nav: Providers
network: true
overview: 'Freepik publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Image Editing API, Image Generation API, and 3 more. Tagged areas include Artificial Intelligence, Graphics, Illustrations, Image-Generation, and Photos.


  Freepik''s developer surface includes authentication, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Freepik Plans Pricing
  plan_count: 3
  slug: freepik-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Freepik Rate Limits
  slug: freepik-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freepik/refs/heads/main/screenshots/freepik-2026-06-20T181529.png
security:
- kind: authentication
  name: Freepik Authentication
  slug: freepik-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freepik Domain Security
  slug: freepik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freepik
tags:
- Artificial Intelligence
- Graphics
- Illustrations
- Image-Generation
- Photos
- Video Generation
website: https://www.freepik.com/
---
