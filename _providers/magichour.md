---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.magichour.ai
  baseurl_source: declared
  description: API related to audio projects
  name: Magic Hour Audio Projects API
  slug: magichour-audio-projects-api
- baseURL: https://api.magichour.ai
  baseurl_source: declared
  description: API related to uploading assets used for video generation
  name: Magic Hour Files API
  slug: magichour-files-api
- baseURL: https://api.magichour.ai
  baseurl_source: declared
  description: API related to image projects
  name: Magic Hour Image Projects API
  slug: magichour-image-projects-api
- baseURL: https://api.magichour.ai
  baseurl_source: declared
  description: API related to video projects
  name: Magic Hour Video Projects API
  slug: magichour-video-projects-api
artifact_total: 10
asyncapis:
- description: ''
  name: Magichour Webhooks
  slug: magichour-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magichour-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magichour-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/magichour-llms.txt
- group: company
  title: ''
  type: Website
  url: https://magichour.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.magichour.ai
- group: build
  title: ''
  type: Packages
  url: packages/magichour-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/magichour-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/magichour-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/magichour-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/magichour-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/magichour-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/magichour-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/magichour-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/magichour-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/magichour-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/magichour-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/magichour-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/magichour-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/magichour-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magichour-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/magichour-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/magichour-webhooks.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://magichour.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magichourhq
- group: company
  title: ''
  type: Blog
  url: https://magichour.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://magichour.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://magichour.ai/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://magichour.ai/developer
created: '2026-08-22'
description: Magic Hour is an AI media generation platform for video, image and audio, exposed as a public REST API. The contract is an OpenAPI 3.0 document of 33 paths and 36 operations served from api.magichour.ai with bearer authentication, covering generators for headshots, clothes changing, face editing, GIFs, image editing and upscaling, plus video and audio synthesis. Operations are priced in credits and the documentation states the credit cost per call. Magic Hour publishes two llms.txt files — one on the marketing site and a different one on the docs host — plus a 653KB llms-full.txt, and documents an HMAC-SHA256 signed webhook surface with a full event-type reference.
image: https://magichour.ai/logo-social.png
layout: provider
mcp_servers:
- description: ''
  name: Magic Hour MCP servers
  slug: magic-hour-mcp-servers
modified: '2026-09-03'
name: Magic Hour
nav: Providers
network: true
overview: 'Magic Hour publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Audio Projects API, Files API, Image Projects API, and 1 more. Tagged areas include AI Video, Image-Generation, Audio, Generative AI, and Voice Cloning.


  The Magic Hour catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Magic Hour''s developer surface includes authentication, changelog, sandbox, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Magichour Plans Pricing
  plan_count: 7
  slug: magichour-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Magichour Rate Limits
  slug: magichour-rate-limits
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 63.1
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 63.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magichour/refs/heads/main/screenshots/magichour-2026-09-02T150355.png
security:
- kind: authentication
  name: Magichour Authentication
  slug: magichour-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Magichour Domain Security
  slug: magichour-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: magichour
tags:
- AI Video
- Image-Generation
- Audio
- Generative AI
- Voice Cloning
- Text-To-Video
website: https://magichour.ai
---
