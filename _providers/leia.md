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
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Leia Agentic Access
  operation_count: 12
  slug: leia-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 4
apis:
- baseURL: https://api.immersity.ai
  baseurl_source: declared
  description: The Media Transformation API from Leia — 9 operation(s) for media transformation.
  name: Leia Media Transformation API
  slug: leia-media-transformation-api
- baseURL: https://api.immersity.ai
  baseurl_source: declared
  description: The Product Pricing API from Leia — 1 operation(s) for product pricing.
  name: Leia Product Pricing API
  slug: leia-product-pricing-api
- baseURL: https://api.immersity.ai
  baseurl_source: declared
  description: The Protocol API from Leia — 1 operation(s) for protocol.
  name: Leia Protocol API
  slug: leia-protocol-api
- baseURL: https://api.immersity.ai
  baseurl_source: declared
  description: The Storage API from Leia — 1 operation(s) for storage.
  name: Leia Storage API
  slug: leia-storage-api
artifact_total: 12
asyncapis:
- description: ''
  name: Leia Callbacks
  slug: leia-callbacks
collections:
- collection_type: open
  name: immersity-ai-authentication
  slug: open-leia-immersity-authentication
- collection_type: open
  name: Immersity Cloud API
  slug: open-leia-immersity-cloud-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/leia-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/leia-immersity-cloud-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://immersity.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://immersity.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs-api.immersity.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs-api.immersity.ai/reference/transactioncontroller_estimatemonodepth-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-api.immersity.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/immersityai
- group: company
  title: ''
  type: Blog
  url: https://immersity.ai/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LeiaInc
- group: commercial
  title: ''
  type: Pricing
  url: https://immersity.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.immersity.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://immersity.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://immersity.ai/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://immersity.ai/faqs
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leia-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/leia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leia-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leia-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/leia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leia-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leia-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leia-callbacks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/leia-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leia-plans.yml
- group: build
  title: ''
  type: Examples
  url: examples/leia-immersity-cloud-api-examples.yml
created: '2026-08-01'
description: Leia Inc. is the Silicon Valley company behind Immersity, a platform for immersive 3D experiences on everyday devices. Spun out of HP Labs in 2014 by physicist David Fattal, Leia pairs a Switchable-Display hardware stack (nano-optics, liquid-crystal switchable layer, per-pixel panel calibration, shipped in Lume Pad, Acer SpatialLabs, Samsung Odyssey 3D, ASUS, Nubia and zSpace devices) with Spatial AI software that converts flat 2D photos and video into stereo, top-bottom, LIF and Apple Vision spatial output in real time. Developers reach that Spatial AI through the Immersity Cloud API — a credit-metered REST API at api.immersity.ai with OAuth 2.0 client-credentials auth via a Keycloak realm, covering disparity-map estimation, animation generation, stereo SBS and top-bottom rendering, LIF encode/decode, 2D-to-3D video conversion and presigned Leia Storage uploads. Formerly known as LeiaPix; the company acquired Dimenco and the Philips 3D patent portfolio in 2023 and holds 2,000+
  patents.
image: https://cdn.prod.website-files.com/684b15b38863077bd3c46420/6895344cc46838641181605c_OpenGraph_V1.png
layout: provider
modified: '2026-08-01'
name: Leia
nav: Providers
network: true
overview: 'Leia publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Media Transformation API, Product Pricing API, Protocol API, and 1 more. Tagged areas include 3D, Spatial Computing, Computer-Vision, depth-estimation, and Image Processing.


  The Leia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Leia Plans
  plan_count: 6
  slug: leia-plans
random_paper: 12
scopes:
- name: Leia Scopes
  scope_count: 20
  slug: leia-scopes
  summary_line: 20 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 68.8
    developer_ergonomics: 57.7
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 53.5
  provenance:
    agentic_access: first-party
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
screenshot: https://raw.githubusercontent.com/api-evangelist/leia/refs/heads/main/screenshots/leia-2026-08-07T171526.png
security:
- kind: authentication
  name: Leia Authentication
  slug: leia-authentication
  summary_line: oauth2/http/apiKey · 2 schemes
- kind: domain-security
  name: Leia Domain Security
  slug: leia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leia
tags:
- 3D
- Spatial Computing
- Computer-Vision
- depth-estimation
- Image Processing
- Video Processing
- Generative AI
- Displays
- Media Transformation
- Immersive Experiences
website: https://immersity.ai/
---
