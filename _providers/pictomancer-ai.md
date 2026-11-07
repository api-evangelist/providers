---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: half
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Official hosted Model Context Protocol server at https://api.pictomancer.ai/mcp (Streamable HTTP, protocol revision 2025-06-18, no authentication required, 120 requests/minute). Anonymous tools/list r
  name: Pictomancer.ai MCP Server
  slug: pictomancer-ai-mcp-server
- description: Agent-to-Agent endpoint at https://api.pictomancer.ai/a2a (JSON-RPC) described by a published agent card — canonical /.well-known/agent-card.json on api.pictomancer.ai (protocolVersion 0.3, graded con
  name: Pictomancer.ai A2A Agent
  slug: pictomancer-ai-a2a-agent
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Analyze API from Pictomancer.ai — 1 operation(s) for analyze.
  name: Pictomancer.ai Analyze API
  slug: pictomancer-ai-analyze-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Compress API from Pictomancer.ai — 1 operation(s) for compress.
  name: Pictomancer.ai Compress API
  slug: pictomancer-ai-compress-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Convert API from Pictomancer.ai — 1 operation(s) for convert.
  name: Pictomancer.ai Convert API
  slug: pictomancer-ai-convert-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Crop API from Pictomancer.ai — 1 operation(s) for crop.
  name: Pictomancer.ai Crop API
  slug: pictomancer-ai-crop-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Estimate API from Pictomancer.ai — 1 operation(s) for estimate.
  name: Pictomancer.ai Estimate API
  slug: pictomancer-ai-estimate-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Info API from Pictomancer.ai — 1 operation(s) for info.
  name: Pictomancer.ai Info API
  slug: pictomancer-ai-info-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Optimize For Vision API from Pictomancer.ai — 1 operation(s) for optimize for vision.
  name: Pictomancer.ai Optimize For Vision API
  slug: pictomancer-ai-optimize-for-vision-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Optimize Generated API from Pictomancer.ai — 1 operation(s) for optimize generated.
  name: Pictomancer.ai Optimize Generated API
  slug: pictomancer-ai-optimize-generated-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Pipeline API from Pictomancer.ai — 1 operation(s) for pipeline.
  name: Pictomancer.ai Pipeline API
  slug: pictomancer-ai-pipeline-api
- baseURL: https://api.pictomancer.ai
  baseurl_source: declared
  description: The Resize API from Pictomancer.ai — 1 operation(s) for resize.
  name: Pictomancer.ai Resize API
  slug: pictomancer-ai-resize-api
artifact_total: 24
asyncapis:
- description: ''
  name: Pictomancer Ai Webhooks
  slug: pictomancer-ai-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/pictomancer-ai/rate-limits/pictomancer-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pictomancer-ai-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/pictomancer-ai/overlays/pictomancer-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pictomancer-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/pictomancer-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/pictomancer-ai/skills/pictomancer-ai-optimize-generated-image.md
  title: ''
  type: AgentSkill
  url: skills/pictomancer-ai-optimize-generated-image.md
- group: agent
  href: https://artifacts.apis.io/pictomancer-ai/skills/pictomancer-ai-resize-and-deliver-to-bucket.md
  title: ''
  type: AgentSkill
  url: skills/pictomancer-ai-resize-and-deliver-to-bucket.md
- group: agent
  href: https://artifacts.apis.io/pictomancer-ai/skills/pictomancer-ai-pipeline-with-cost-cap.md
  title: ''
  type: AgentSkill
  url: skills/pictomancer-ai-pipeline-with-cost-cap.md
- group: company
  title: ''
  type: Website
  url: https://pictomancer.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.pictomancer.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.pictomancer.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.pictomancer.ai/
- group: start
  title: ''
  type: Login
  url: https://app.pictomancer.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.pictomancer.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://pictomancer.ai/#pricing
- group: commercial
  href: https://artifacts.apis.io/pictomancer-ai/plans/pictomancer-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pictomancer-ai-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://pictomancer.ai/changelog
- group: operate
  href: https://artifacts.apis.io/pictomancer-ai/changelog/pictomancer-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pictomancer-ai-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://pictomancer.ai/status
- group: design
  href: https://artifacts.apis.io/pictomancer-ai/lifecycle/pictomancer-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pictomancer-ai-lifecycle.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pictomancer.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pictomancer.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pictomancer
- group: agent
  title: ''
  type: LLMsTxt
  url: https://pictomancer.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/pictomancer-ai/llms/pictomancer-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pictomancer-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/pictomancer-ai/packages/pictomancer-ai-packages.yml
  title: ''
  type: Packages
  url: packages/pictomancer-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/pictomancer-ai/packages/pictomancer-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/pictomancer-ai-packages.yml
- group: agent
  href: https://artifacts.apis.io/pictomancer-ai/well-known/pictomancer-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pictomancer-ai-well-known.yml
- group: design
  href: https://artifacts.apis.io/pictomancer-ai/conformance/pictomancer-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pictomancer-ai-conformance.yml
- group: auth
  href: https://artifacts.apis.io/pictomancer-ai/security/pictomancer-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pictomancer-ai-domain-security.yml
- group: other
  href: https://artifacts.apis.io/pictomancer-ai/regulatory/pictomancer-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/pictomancer-ai-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://pictomancer.ai/privacy
created: '2026-09-19'
description: 'Pictomancer.ai is a Spain-registered image-optimization API built for agents: resize, compress, convert, crop, optimize-for-vision and one-call optimization of AI-generated images, processed in under 50 ms and priced per request ($0.001-$0.03, analyze free). The same ten operations are published three ways — an OpenAPI 3.1 REST API, a hosted MCP server (Streamable HTTP, listed in the official MCP Registry) and an A2A agent card — and are paid for anonymously with USDC on Base via x402 (HTTP 402 -> pay -> retry), with an API key, or free for the first 50 requests per identity. Results return inline, PUT to the caller''s own bucket, or POST to a callback endpoint. First-party SDKs ship for Python, Node, PHP and Go plus an n8n node and a WordPress plugin.'
finops:
- has_sources: true
  method: derived
  name: Pictomancer Ai Finops
  primary_unit: operation
  service_category: ''
  slug: pictomancer-ai-finops
  template: false
image: https://pictomancer.ai/apple-icon.png
layout: provider
mcp_servers:
- description: Pictomancer.ai operates one official remote MCP server at https://api.pictomancer.ai/mcp (Streamable HTTP, MCP protocol revision 2025-06-18, tools capability only, no auth required). It is discoverabl
  name: Pictomancer.ai
  slug: pictomancer-ai
modified: '2026-09-19'
name: Pictomancer.ai
nav: Providers
network: true
overview: 'Pictomancer.ai publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analyze API, Compress API, Convert API, and 9 more. Tagged areas include Company, Image, Image Optimization, Image Processing, and Media.


  The Pictomancer.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Pictomancer.ai''s developer surface includes documentation, API reference, signup flow, pricing, changelog, and 25 more developer resources.'
plans:
- name: Pictomancer Ai Plans Pricing
  plan_count: 13
  slug: pictomancer-ai-plans-pricing
- name: Pictomancer Ai Price Estimates
  plan_count: 0
  slug: pictomancer-ai-price-estimates
random_paper: 4
rate_limits:
- limit_count: 1
  name: Pictomancer Ai Rate Limits
  slug: pictomancer-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Pictomancer.ai API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 2
  slug: pictomancer-ai-rules
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 53.2
    developer_ergonomics: 33.9
    discoverability: 75.0
    operational_transparency: 63.2
  previous_composite: 52.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pictomancer-ai/pictomancer-ai-2026-10-11T112542.png
security:
- kind: authentication
  name: Pictomancer Ai Authentication
  slug: pictomancer-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Pictomancer Ai Domain Security
  slug: pictomancer-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 3
skills:
- name: Ship an AI-generated image web-ready
  slug: pictomancer-ai-optimize-generated-image
- name: Run a multi-step pipeline under a cost cap
  slug: pictomancer-ai-pipeline-with-cost-cap
- name: Resize and deliver straight to your bucket
  slug: pictomancer-ai-resize-and-deliver-to-bucket
slug: pictomancer-ai
tags:
- Company
- Image
- Image Optimization
- Image Processing
- Media
- Agents
- MCP
- A2A
- x402
- Micropayments
- Developer Tools
website: https://pictomancer.ai/
---
