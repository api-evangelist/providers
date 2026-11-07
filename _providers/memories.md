---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Memories Agentic Access
  operation_count: 34
  slug: memories-agentic-access
  summary_line: 34 operations · 20 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.memories.ai
  baseurl_source: declared
  description: The Serve API from Memories — 30 operation(s) for serve.
  name: Memories Serve API
  slug: memories-serve-api
- baseURL: https://api.memories.ai
  baseurl_source: declared
  description: The Stream Understanding API from Memories — 2 operation(s) for stream understanding.
  name: Memories Stream Understanding API
  slug: memories-stream-understanding-api
- baseURL: https://api.memories.ai
  baseurl_source: declared
  description: The Understand API from Memories — 2 operation(s) for understand.
  name: Memories Understand API
  slug: memories-understand-api
artifact_total: 17
asyncapis:
- description: ''
  name: Memories Webhooks
  slug: memories-webhooks
collections:
- collection_type: open
  name: Memories Platform API (Docs Mapping) Serve API
  slug: open-memories-serve-api
- collection_type: open
  name: Memories Platform API (Docs Mapping) Serve Stream Understanding API
  slug: open-memories-stream-understanding-api
- collection_type: open
  name: Memories Platform API (Docs Mapping) Serve Understand API
  slug: open-memories-understand-api
common:
- group: commercial
  href: https://artifacts.apis.io/memories/plans/memories-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/memories-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://memories.ai/blogs
- group: auth
  href: https://artifacts.apis.io/memories/security/memories-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/memories-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-platform.memories.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api-tools.memories.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-tools.memories.ai/visual-intelligence/getting-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://api-tools.memories.ai/visual-intelligence/getting-started/introduction
- group: start
  title: ''
  type: SignUp
  url: https://api-platform.memories.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://api-tools.memories.ai/visual-search/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Memories-ai-labs
- group: auth
  title: ''
  type: Compliance
  url: https://memories.ai/security
- group: auth
  href: https://artifacts.apis.io/memories/authentication/memories-authentication.yml
  title: ''
  type: Authentication
  url: authentication/memories-authentication.yml
- group: agent
  href: https://artifacts.apis.io/memories/agentic-access/memories-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/memories-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/memories/packages/memories-packages.yml
  title: ''
  type: Packages
  url: packages/memories-packages.yml
- group: build
  href: https://artifacts.apis.io/memories/cli/memories-cli.yml
  title: ''
  type: CLI
  url: cli/memories-cli.yml
- group: agent
  href: https://artifacts.apis.io/memories/mcp/memories-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/memories-mcp.yml
- group: agent
  href: https://artifacts.apis.io/memories/llms/memories-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memories-llms.txt
- group: agent
  href: https://artifacts.apis.io/memories/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/memories/asyncapi/memories-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/memories-webhooks.yml
- group: design
  href: https://artifacts.apis.io/memories/errors/memories-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/memories-error-codes.yml
- group: design
  href: https://artifacts.apis.io/memories/conventions/memories-conventions.yml
  title: ''
  type: Conventions
  url: conventions/memories-conventions.yml
- group: operate
  href: https://artifacts.apis.io/memories/rate-limits/memories-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/memories-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/memories/lifecycle/memories-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/memories-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/memories/conformance/memories-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memories-conformance.yml
- group: design
  href: https://artifacts.apis.io/memories/data-model/memories-data-model.yml
  title: ''
  type: DataModel
  url: data-model/memories-data-model.yml
- group: auth
  href: https://artifacts.apis.io/memories/security/memories-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memories-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/memories/well-known/memories-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/memories-well-known.yml
- group: other
  href: https://artifacts.apis.io/memories/overlays/memories-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/memories-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://memories.ai
created: '2026-07-17'
description: 'Memories.ai (MAVI) is a video-intelligence platform that turns raw video into searchable, agent-ready understanding. It ships three products on a shared video-understanding stack: Visual Intelligence (stateless REST APIs for transcription, captioning, frame description, embeddings, social-media scraping, and real-time audio/video stream moderation via VLMs such as Gemini, Nova, and Qwen), Visual Search (an auto-indexed private and public video/image library searchable by text, image, or transcript), and Visual Agents (pre-built workflows for video search, AI video editing, and screenplay extraction). The platform authenticates with sk-mavi- API keys, bills on a unified per-endpoint credit model, and is HIPAA, SOC 2 Type 2, and GDPR compliant. It is a Seedcamp portfolio company.'
finops:
- has_sources: true
  method: derived
  name: Memories Finops
  primary_unit: 1,000 queries
  service_category: ''
  slug: memories-finops
  template: false
image: https://mintcdn.com/memories/xyhRN3OJaXxxzcxh/logo/logo.png
layout: provider
modified: '2026-10-06'
name: Memories
nav: Providers
network: true
overview: 'Memories publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Serve API, Stream Understanding API, and Understand API. Tagged areas include Company, Video Intelligence, Video Understanding, Video Search, and Transcription.


  The Memories catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Memories'' developer surface includes engineering blog, documentation, API reference, getting-started guide, signup flow, pricing, authentication, and 22 more developer resources.'
plans:
- name: Memories Plans Pricing
  plan_count: 15
  slug: memories-plans-pricing
- name: Memories Price Estimates
  plan_count: 0
  slug: memories-price-estimates
random_paper: 1
rate_limits:
- limit_count: 4
  name: Memories Rate Limits
  slug: memories-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Memories API Rules
  rule_count: 48
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 5
  slug: memories-rules
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.6
  facets:
    access_clarity: 72.4
    contract_governance: 31.8
    contract_quality: 60.2
    developer_ergonomics: 61.9
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/memories/memories-2026-08-07T172506.png
security:
- kind: authentication
  name: Memories Authentication
  slug: memories-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Memories Domain Security
  slug: memories-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Memories Trust Center
  slug: memories-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 1
skills:
- name: Video Intelligence Platform
  slug: memories-video-intelligence-platform
slug: memories
tags:
- Company
- Video Intelligence
- Video Understanding
- Video Search
- Transcription
- Embeddings
- Multimodal AI
- Content Moderation
- AI Agents
- Machine Learning
website: http://memories.ai
---
