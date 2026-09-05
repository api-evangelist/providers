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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-09-04'
api_count: 21
apis:
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: 'Session and token issuance for the TVU public HTTP API — obtain a SID (session ID) used as an HTTP request header, alongside the Authorization: Bearer AppSecret and AccessKey signature schemes documen'
  name: TVU Networks Authentication
  slug: authentication
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU Channel FAST playout — channel definition, scheduling and playout control for 24/7 linear and FAST channel distribution. Contract assembled from the 14 per-endpoint OpenAPI 3.0.1 exports TVU publi
  name: TVU Networks Channel API
  slug: channel-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: 'TVU Remote Commentator — event, session and audio-mix control for remote commentary contribution into a live production. Contract assembled from the 8 per-endpoint OpenAPI 3.0.1 exports TVU publishes '
  name: TVU Networks Commentator API
  slug: commentator-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: Media export and thumbnail job submission — submit an export or thumbnail job with an optional idempotency uuid and callbackUrl webhook, then poll or receive the completed asset. Contract assembled fr
  name: TVU Networks Export
  slug: export
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU Grid device and transmission control — device listing and status, pairing tokens, grid metadata, geolocation of paired transmitters, live start/stop and real-time live parameters. Contract assembl
  name: TVU Networks Grid API
  slug: grid-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: Input and output module management — encoder profiles, input modules, output modules and preview decoders for TVU transmission endpoints. Contract assembled from the 23 per-endpoint OpenAPI 3.0.1 expo
  name: TVU Networks Input & Output Module API
  slug: input-output-module-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: Media information lookup — metadata and technical detail for a media asset held in the TVU platform. Contract assembled from the 2 per-endpoint OpenAPI 3.0.1 exports TVU publishes on its own API docum
  name: TVU Networks Media Info
  slug: media-info
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: Media service endpoints backing TVU Producer — tvucc-media and tvucc-share output settings, share video start/stop, go-live and account information. Contract assembled from the 11 per-endpoint OpenAPI
  name: TVU Networks Media Service For Producer
  slug: media-service-for-producer
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU MediaHub cloud routing — create and manage source objects, outputs, encoding profiles, destinations, projects and routes, and connect or disconnect live signal paths between any input and any outp
  name: TVU Networks MediaHub API
  slug: mediahub-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU MediaMind story creation — create and manage stories that assemble media, transcripts and metadata for newsroom production. Contract assembled from the 1 per-endpoint OpenAPI 3.0.1 exports TVU pub
  name: TVU Networks MediaMind Story Creation
  slug: mediamind-story-creation
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: MOS (Media Object Server) gateway — newsroom computer system integration for TVU Channel and playout. Contract assembled from the 3 per-endpoint OpenAPI 3.0.1 exports TVU publishes on its own API docu
  name: TVU Networks MOS Gateway API
  slug: mos-gateway-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU object and tangible model — the REST and GraphQL surface over TVU objects, tangibles, relationships and tags that gives every TVU resource (pack, receiver, grid, SDI port, shared memory) an addres
  name: TVU Networks Object API
  slug: object-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU Partyline remote collaboration and cloud conferencing — party creation and membership, participant state, audio mixing and picture-in-picture control for live guest workflows. Contract assembled f
  name: TVU Networks Partyline API
  slug: partyline-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU Producer cloud production switcher — programs, input sources, overlays, clip player and playlists, collaborators, followers and Producer AI, exposed through the graphql2rest operation set. Contrac
  name: TVU Networks Producer API
  slug: producer-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: Publicly reachable TVU endpoints that require no session — health, version and no-login status lookups. Contract assembled from the 4 per-endpoint OpenAPI 3.0.1 exports TVU publishes on its own API do
  name: TVU Networks Public Endpoints
  slug: public
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: SCTE-35 ad-marker insertion — enable SCTE on a channel and inject manual SCTE cues into a live playout stream. Contract assembled from the 2 per-endpoint OpenAPI 3.0.1 exports TVU publishes on its own
  name: TVU Networks ScteService API
  slug: scteservice-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU Search / MediaMind media search and metadata — cross-type media content search, slug and recording management, speech transcription and face-recognition metadata, export and thumbnail jobs, and we
  name: TVU Networks Search API
  slug: search-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU shortcut operations — saved one-touch actions that trigger a composed TVU workflow. Contract assembled from the 5 per-endpoint OpenAPI 3.0.1 exports TVU publishes on its own API documentation site
  name: TVU Networks Shortcut API
  slug: shortcut-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: Ungrouped TVU public API endpoints — object service CRUD, resource estimation and metadata, dashboards proxy, and slug recording operations that TVU publishes outside a named folder in its API documen
  name: TVU Networks Ungrouped Endpoints
  slug: uncategorized
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU usage reporting — device usage information for billing and utilisation reporting. Contract assembled from the 1 per-endpoint OpenAPI 3.0.1 exports TVU publishes on its own API documentation site.
  name: TVU Networks UsageService API
  slug: usageservice-api
- baseURL: https://api.tvunetworks.com
  baseurl_source: declared
  description: TVU workflow orchestration — define and run automated media workflows across the TVU ecosystem. Contract assembled from the 5 per-endpoint OpenAPI 3.0.1 exports TVU publishes on its own API documentat
  name: TVU Networks Workflow API
  slug: workflow-api
artifact_total: 26
asyncapis:
- description: ''
  name: Tvu Networks Webhooks
  slug: tvu-networks-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tvu-networks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tvu-networks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tvunetworks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tvunetworks.com/tvu-developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tvunetworks.cn/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tvunetworks.cn/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tvunetworks.cn/doc-8184935
- group: operate
  title: ''
  type: Support
  url: https://www.tvunetworks.com/faqs-support/
- group: company
  title: ''
  type: Blog
  url: https://www.tvunetworks.com/stories/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tvunetworks
- group: start
  title: ''
  type: SignUp
  url: https://www.tvunetworks.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tvunetworks.com/company-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tvunetworks.com/company-privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tvunetworks.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tvu-networks-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/tvu-networks-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tvu-networks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tvu-networks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tvu-networks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tvu-networks-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tvu-networks-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tvu-networks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tvu-networks-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tvu-networks-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-01'
description: TVU Networks is a live video transmission and cloud production company founded in 2005 and headquartered in Mountain View, California. Its IP-based ecosystem covers acquisition (TVU One and TVU Anywhere bonded-cellular transmitters), cloud routing and distribution (TVU MediaHub), cloud production (TVU Producer, TVU Partyline, TVU Remote Commentator), FAST and linear playout (TVU Channel), and AI-assisted media management and search (TVU MediaMind, TVU Search). TVU publishes a public HTTP API across those products — 352 operations spanning MediaHub routing, Search and metadata, Producer control, Grid device transmission, Partyline, Channel playout, SCTE-35 ad insertion and a MOS newsroom gateway — documented on its own Apifox-hosted API documentation site, with Bearer AppSecret, SID session and AccessKey-signature authentication.
image: https://www.tvunetworks.com/wp-content/themes/tvunetworks/images/emblem-green.png
layout: provider
modified: '2026-09-01'
name: TVU Networks
nav: Providers
network: true
overview: 'TVU Networks publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Authentication, Channel API, Commentator API, and 18 more. Tagged areas include Company, Media, Video, Broadcast, and Live Streaming.


  The TVU Networks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TVU Networks'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Tvu Networks Plans Pricing
  plan_count: 0
  slug: tvu-networks-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Tvu Networks Rate Limits
  slug: tvu-networks-rate-limits
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 60.5
    developer_ergonomics: 58.9
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tvu-networks/refs/heads/main/screenshots/tvu-networks-2026-09-02T164606.png
security:
- kind: authentication
  name: Tvu Networks Authentication
  slug: tvu-networks-authentication
  summary_line: apikey/bearer/signature · 3 schemes
- kind: domain-security
  name: Tvu Networks Domain Security
  slug: tvu-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tvu-networks
tags:
- Company
- Media
- Video
- Broadcast
- Live Streaming
- Video Transmission
- Cloud Production
- Media Supply Chain
- Playout
- FAST Channels
- Remote Production
- Metadata
- Search
- SCTE-35
- MOS
website: https://www.tvunetworks.com/
---
