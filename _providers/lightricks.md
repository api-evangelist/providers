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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Lightricks Agentic Access
  operation_count: 28
  slug: lightricks-agentic-access
  summary_line: 28 operations · 26 acting
api_count: 3
apis:
- description: The asyncVideoGeneration API from Lightricks — 8 operation(s) for asyncvideogeneration.
  name: Lightricks asyncVideoGeneration API
  slug: lightricks-asyncvideogeneration-api
- description: The upload API from Lightricks — 1 operation(s) for upload.
  name: Lightricks upload API
  slug: lightricks-upload-api
- description: The videoGeneration API from Lightricks — 5 operation(s) for videogeneration.
  name: Lightricks videoGeneration API
  slug: lightricks-videogeneration-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightricks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lightricks-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.lightricks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ltx.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ltx.io/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ltx.io/api-documentation/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ltx.io/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://console.ltx.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.ltx.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.ltx.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://ltx.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lightricks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://static.lightricks.com/legal/terms-of-use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.lightricks.com/legal/privacy-policy.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ltx.video/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ltx.io/ltx-2-deprecation
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lightricks.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightricks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightricks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightricks-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/lightricks-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightricks-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightricks-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/lightricks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightricks-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightricks-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightricks-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightricks-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/lightricks-api-catalog.json
- group: design
  title: ''
  type: Conformance
  url: conformance/lightricks-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightricks-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightricks-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lightricks-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://ltx.io/changelog
- group: other
  title: ''
  type: Overlay
  url: overlays/lightricks-ltx-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lightricks-generate-video-from-text.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lightricks-animate-an-image.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lightricks-edit-an-existing-video.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lightricks-upscale-and-reframe.md
created: '2026-07-17'
description: Lightricks is a Jerusalem-based creative-technology company behind the Facetune, Photoleap and Videoleap consumer apps and the LTX generative video platform. Its developer-facing product is the LTX API at api.ltx.video, a video-generation API covering text-to-video, image-to-video, audio-to-video, retake, extend, HDR upscale and reframe, offered in synchronous (v1) and asynchronous job-based (v2) forms and billed per second of output. Lightricks also publishes the LTX-2 and LTX-Video open-weight models, a ComfyUI node set and a LoRA trainer on GitHub under Apache-2.0.
image: https://avatars.githubusercontent.com/u/3170348?v=4
layout: provider
mcp_servers:
- description: ''
  name: lightricks-mcp.yml
  slug: lightricks-mcpyml
modified: '2026-07-19'
name: Lightricks
nav: Providers
network: true
overview: 'Lightricks publishes 3 APIs on the [APIs.io](https://apis.io/) network: asyncVideoGeneration API, upload API, and videoGeneration API. Tagged areas include Company, Consumer, Artificial Intelligence, Generative AI, and Video.


  Lightricks'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 33 more developer resources.'
random_paper: 49
rate_limits:
- limit_count: 0
  name: Lightricks Rate Limits
  slug: lightricks-rate-limits
score:
  band: strong
  composite: 56.3
  delta: 0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 55.9
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightricks/refs/heads/main/screenshots/lightricks-2026-07-25T225127.png
security:
- kind: authentication
  name: Lightricks Authentication
  slug: lightricks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lightricks Domain Security
  slug: lightricks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lightricks Trust Center
  slug: lightricks-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: lightricks
tags:
- Company
- Consumer
- Artificial Intelligence
- Generative AI
- Video
- Video Generation
- Media
- Machine Learning
- Creative Tools
website: https://www.lightricks.com/
---
