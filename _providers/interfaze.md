---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Interfaze Agentic Access
  operation_count: 1
  slug: interfaze-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.interfaze.ai/v1
  baseurl_source: declared
  description: The Chat Completions API from Interfaze — 1 operation(s) for chat completions.
  name: Interfaze Chat Completions API
  slug: interfaze-chat-completions-api
artifact_total: 14
collections:
- collection_type: open
  name: Interfaze Chat API
  slug: open-interfaze-chat-api
common:
- group: other
  href: https://artifacts.apis.io/interfaze/capabilities/interfaze-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/interfaze-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/interfaze/plans/interfaze-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/interfaze-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.interfaze.ai/
- group: other
  href: https://artifacts.apis.io/interfaze/a2a/interfaze-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/interfaze-a2a.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://interfaze.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://interfaze.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://interfaze.ai/docs/api/chat-completion
- group: start
  title: ''
  type: GettingStarted
  url: https://interfaze.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://interfaze.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://interfaze.ai/dashboard
- group: operate
  title: ''
  type: Support
  url: https://interfaze.ai/help
- group: company
  title: ''
  type: Blog
  url: https://interfaze.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.interfaze.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://interfaze.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://interfaze.ai/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InterfazeAI
- group: agent
  href: https://artifacts.apis.io/interfaze/llms/interfaze-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/interfaze-llms.txt
- group: agent
  href: https://artifacts.apis.io/interfaze/well-known/interfaze-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/interfaze-well-known.yml
- group: agent
  href: https://artifacts.apis.io/interfaze/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/interfaze/mcp/interfaze-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/interfaze-mcp.yml
- group: other
  href: https://artifacts.apis.io/interfaze/overlays/interfaze-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/interfaze-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/interfaze/conformance/interfaze-conformance.yml
  title: ''
  type: Conformance
  url: conformance/interfaze-conformance.yml
- group: design
  href: https://artifacts.apis.io/interfaze/errors/interfaze-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/interfaze-problem-types.yml
- group: design
  href: https://artifacts.apis.io/interfaze/lifecycle/interfaze-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/interfaze-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/interfaze/conventions/interfaze-conventions.yml
  title: ''
  type: Conventions
  url: conventions/interfaze-conventions.yml
- group: operate
  href: https://artifacts.apis.io/interfaze/conventions/interfaze-conventions.yml
  title: ''
  type: RateLimits
  url: conventions/interfaze-conventions.yml
- group: operate
  href: https://artifacts.apis.io/interfaze/changelog/interfaze-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/interfaze-changelog.yml
- group: design
  href: https://artifacts.apis.io/interfaze/data-model/interfaze-data-model.yml
  title: ''
  type: DataModel
  url: data-model/interfaze-data-model.yml
- group: agent
  href: https://artifacts.apis.io/interfaze/agentic-access/interfaze-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/interfaze-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/interfaze/authentication/interfaze-authentication.yml
  title: ''
  type: Authentication
  url: authentication/interfaze-authentication.yml
- group: auth
  href: https://artifacts.apis.io/interfaze/security/interfaze-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/interfaze-domain-security.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@interfaze.ai
created: '2026-07-17'
description: Interfaze is a Y Combinator (P26) startup building a new model architecture for deterministic developer tasks. Interfaze-beta is a multimodal, OpenAI-compatible Chat Completion API (a hybrid Mixture-of-Architecture combining specialized DNN/CNN vision and audio models with a transformer layer) tuned for high accuracy, precision, and consistency on jobs like OCR, speech-to-text, strict structured/JSON output, object detection with bounding boxes, web search, and web scraping through a single endpoint. It exposes a 1M-token context window, 32k max output, verifiable outputs with confidence scores, built-in sandboxed compute and headless browser tools, and works with the OpenAI, Vercel AI, and LangChain SDKs by swapping the base URL. Founded in 2025 by Yoeven D Khemlani and Harsha Vardhan Khurdula (evolved from JigsawStack) and based in San Francisco.
finops:
- has_sources: true
  method: derived
  name: Interfaze Finops
  primary_unit: mtok input
  service_category: ''
  slug: interfaze-finops
  template: false
image: https://interfaze.ai/banner.png
layout: provider
modified: '2026-07-19'
name: Interfaze
nav: Providers
network: true
overview: 'Interfaze publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Chat Completions API. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM, and OCR.


  The Interfaze catalog on APIs.io includes 1 Spectral governance ruleset.


  Interfaze''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 25 more developer resources.'
plans:
- name: Interfaze Plans Pricing
  plan_count: 5
  slug: interfaze-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Interfaze API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: interfaze-rules
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 56.5
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/interfaze/interfaze-2026-07-25T222700.png
security:
- kind: authentication
  name: Interfaze Authentication
  slug: interfaze-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Interfaze Domain Security
  slug: interfaze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: object-detection
  slug: interfaze-object-detection
- name: ocr
  slug: interfaze-ocr
- name: speech-to-text
  slug: interfaze-speech-to-text
- name: structured-output
  slug: interfaze-structured-output
- name: web-scraping
  slug: interfaze-web-scraping
- name: web-search
  slug: interfaze-web-search
slug: interfaze
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM
- OCR
- Speech-to-Text
- Structured Output
- Object Detection
- Web Scraping
- Web Search
- Multi-Modal
- Developer Tools
- A2A
website: https://www.interfaze.ai/
---
