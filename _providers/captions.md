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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 11
  human_in_the_loop: 5
  name: Captions Agentic Access
  operation_count: 23
  slug: captions-agentic-access
  summary_line: 23 operations · 11 acting · 5 human-in-the-loop
api_count: 7
apis:
- description: The Audio API from Captions — 1 operation(s) for audio.
  name: Captions Audio API
  slug: captions-audio-api
- description: The health API from Captions — 1 operation(s) for health.
  name: Captions health API
  slug: captions-health-api
- description: The internal API from Captions — 8 operation(s) for internal.
  name: Captions internal API
  slug: captions-internal-api
- description: The Meta Text Overlays API from Captions — 2 operation(s) for meta text overlays.
  name: Captions Meta Text Overlays API
  slug: captions-meta-text-overlays-api
- description: The root API from Captions — 1 operation(s) for root.
  name: Captions root API
  slug: captions-root-api
- description: The Video Captions API from Captions — 3 operation(s) for video captions.
  name: Captions Video Captions API
  slug: captions-video-captions-api
- description: The Videos API from Captions — 3 operation(s) for videos.
  name: Captions Videos API
  slug: captions-videos-api
artifact_total: 23
common:
- group: start
  title: ''
  type: Portal
  url: https://platform.mirage.app/
- group: docs
  title: ''
  type: Documentation
  url: https://captions.ai/help/docs/api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://captions.ai/help/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://captions.ai/help
- group: operate
  title: ''
  type: Support
  url: https://captions.ai/help
- group: company
  title: ''
  type: Blog
  url: https://captions.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://captions.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://captions.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mirage.app/legal/captions-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mirage.app/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/captions-ai
- group: company
  title: ''
  type: Website
  url: https://captions.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://mirage.statuspage.io
- group: auth
  title: ''
  type: Compliance
  url: https://captions.ai/solutions/enterprise
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/captions-mirage-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/captions-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/captions-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/captions-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/captions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/captions-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/captions-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/captions-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/captions-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/captions-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/captions-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/captions-plans.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/captionsapp
- group: other
  title: ''
  type: X
  url: https://x.com/getcaptionsapp
- group: operate
  title: ''
  type: ChangeLog
  url: https://captions.ai/help/whats-new
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/captions-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/captions-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/captions-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/captions-context.jsonld
created: '2026-07-17'
description: 'Captions is an AI video editor and generator built by Mirage, an AI research company headquartered in New York City. The consumer and enterprise apps automate the most time-consuming parts of video production — cutting scenes, adding B-roll, inserting music and sound effects, generating and styling captions, dubbing into 30+ languages, correcting eye contact, and generating entirely new videos from a text prompt or a selfie via AI Avatars, AI Actors, and AI Twins. The Mirage Video API (api.mirage.app) exposes this pipeline to developers: asynchronous AI video generation, adding stylized captions to videos, caption-template discovery, text-to-speech audio, and meta text overlays. Authentication is a simple x-api-key header, keys are minted in the Mirage platform dashboard, and long-running jobs are polled for status.'
examples:
- key_count: 5
  name: Captions Add Captions Example
  slug: captions-add-captions-example
- key_count: 6
  name: Captions Creator Submit Example
  slug: captions-creator-submit-example
- key_count: 6
  name: Captions Generate Video Example
  slug: captions-generate-video-example
finops:
- name: Captions Finops
  service_category: ''
  slug: captions-finops
image: https://captions.ai/logo256.png
json_schemas:
- name: MACaptionTemplate
  property_count: 5
  slug: captions-caption-template
- name: CreatorJobPollResponse
  property_count: 4
  slug: captions-creator-job
- name: MAVideo
  property_count: 12
  slug: captions-video
jsonld:
- class_count: 3
  name: Captions Context
  property_count: 31
  slug: captions-context
layout: provider
mcp_servers:
- description: ''
  name: captions-mcp.yml
  slug: captions-mcpyml
modified: '2026-08-08'
name: Captions
nav: Providers
network: true
overview: 'Captions publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audio API, health API, internal API, and 4 more. Tagged areas include Company, Video, Artificial Intelligence, Video Editing, and Video Generation.


  The Captions catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Captions'' developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Captions Plans Pricing
  plan_count: 6
  slug: captions-plans-pricing
- name: Captions Plans
  plan_count: 5
  slug: captions-plans
random_paper: 53
rate_limits:
- limit_count: 6
  name: Captions Rate Limits
  slug: captions-rate-limits
rules:
- name: Captions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: captions-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 70.5
  delta: 17.5
  facets:
    commercial_clarity: 92.1
    contract_quality: 52.4
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 89.6
    operational_transparency: 68.4
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/captions/refs/heads/main/screenshots/captions-2026-07-25T204454.png
security:
- kind: authentication
  name: Captions Authentication
  slug: captions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Captions Domain Security
  slug: captions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: captions
tags:
- Company
- Video
- Artificial Intelligence
- Video Editing
- Video Generation
- Captions
- Subtitles
- Text to Speech
- AI Avatars
- Content Creation
- Media
website: https://captions.ai
---
