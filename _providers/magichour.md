---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.2
  scored_at: '2026-11-06'
api_count: 1
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
artifact_total: 16
asyncapis:
- description: ''
  name: Magichour Webhooks
  slug: magichour-webhooks
common:
- group: other
  href: https://artifacts.apis.io/magichour/capabilities/magichour-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/magichour-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/magichour/security/magichour-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/magichour-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/magichour/authentication/magichour-authentication.yml
  title: ''
  type: Authentication
  url: authentication/magichour-authentication.yml
- group: agent
  href: https://artifacts.apis.io/magichour/llms/magichour-llms.txt
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
  href: https://artifacts.apis.io/magichour/packages/magichour-packages.yml
  title: ''
  type: Packages
  url: packages/magichour-packages.yml
- group: build
  href: https://artifacts.apis.io/magichour/packages/magichour-packages.yml
  title: ''
  type: SDKs
  url: packages/magichour-packages.yml
- group: agent
  href: https://artifacts.apis.io/magichour/well-known/magichour-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/magichour-well-known.yml
- group: agent
  href: https://artifacts.apis.io/magichour/mcp/magichour-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/magichour-mcp.yml
- group: build
  href: https://artifacts.apis.io/magichour/mcp/magichour-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/magichour-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/magichour/a2a/magichour-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/magichour-a2a.yml
- group: agent
  href: https://artifacts.apis.io/magichour/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/magichour/conformance/magichour-conformance.yml
  title: ''
  type: Conformance
  url: conformance/magichour-conformance.yml
- group: design
  href: https://artifacts.apis.io/magichour/errors/magichour-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/magichour-problem-types.yml
- group: design
  href: https://artifacts.apis.io/magichour/lifecycle/magichour-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/magichour-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/magichour/lifecycle/magichour-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/magichour-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/magichour/conventions/magichour-conventions.yml
  title: ''
  type: Conventions
  url: conventions/magichour-conventions.yml
- group: operate
  href: https://artifacts.apis.io/magichour/changelog/magichour-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/magichour-changelog.yml
- group: start
  href: https://artifacts.apis.io/magichour/sandbox/magichour-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/magichour-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/magichour/plans/magichour-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/magichour-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/magichour/rate-limits/magichour-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/magichour-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/magichour/data-model/magichour-data-model.yml
  title: ''
  type: DataModel
  url: data-model/magichour-data-model.yml
- group: design
  href: https://artifacts.apis.io/magichour/asyncapi/magichour-webhooks.yml
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
- group: operate
  title: ''
  type: Support
  url: mailto:support@magichour.ai
created: '2026-08-22'
description: Magic Hour is an AI media generation platform for video, image and audio, exposed as a public REST API. The contract is an OpenAPI 3.0 document of 33 paths and 36 operations served from api.magichour.ai with bearer authentication, covering generators for headshots, clothes changing, face editing, GIFs, image editing and upscaling, plus video and audio synthesis. Operations are priced in credits and the documentation states the credit cost per call. Magic Hour publishes two llms.txt files — one on the marketing site and a different one on the docs host — plus a 653KB llms-full.txt, and documents an HMAC-SHA256 signed webhook surface with a full event-type reference.
finops:
- has_sources: true
  method: derived
  name: Magichour Finops
  primary_unit: ''
  service_category: ''
  slug: magichour-finops
  template: true
image: https://magichour.ai/logo-social.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.magichour.ai requiring an API key.
  name: Magic Hour MCP servers
  slug: magic-hour-mcp-servers
modified: '2026-09-03'
name: Magic Hour
nav: Providers
network: true
overview: 'Magic Hour publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio Projects API, Files API, Image Projects API, and 1 more. Tagged areas include AI Video, Image Generation, Audio, Generative AI, and Voice Cloning.


  The Magic Hour catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Magic Hour''s developer surface includes authentication, changelog, sandbox, pricing, engineering blog, support, and 25 more developer resources.'
plans:
- name: Magichour Plans Pricing
  plan_count: 7
  slug: magichour-plans-pricing
- name: Magichour Price Estimates
  plan_count: 0
  slug: magichour-price-estimates
random_paper: 23
rate_limits:
- limit_count: 3
  name: Magichour Rate Limits
  slug: magichour-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Magic Hour API Rules
  rule_count: 54
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 4
  slug: magichour-rules
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 57.6
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 73.7
  previous_composite: 63.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/magichour/magichour-2026-09-02T150355.png
security:
- kind: authentication
  name: Magichour Authentication
  slug: magichour-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Magichour Domain Security
  slug: magichour-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Magichour
  slug: magichour-agent-skill
- name: magichour-generate-image
  slug: magichour-generate-image
- name: magichour-generate-video
  slug: magichour-generate-video
slug: magichour
tags:
- AI Video
- Image Generation
- Audio
- Generative AI
- Voice Cloning
- Video Generation
- A2A
website: https://magichour.ai
---
