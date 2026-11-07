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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cerebras Systems Agentic Access
  operation_count: 8
  slug: cerebras-systems-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 2
apis:
- baseURL: https://api.cerebras.ai
  baseurl_source: declared
  description: The Completions API from Cerebras Systems — 1 operation(s) for completions.
  name: Cerebras Systems Completions API
  slug: cerebras-systems-completions-api
- baseURL: https://api.cerebras.ai
  baseurl_source: declared
  description: The Models API from Cerebras Systems — 2 operation(s) for models.
  name: Cerebras Systems Models API
  slug: cerebras-systems-models-api
- baseURL: https://api.cerebras.ai
  baseurl_source: declared
  description: The Public Models API from Cerebras Systems — 2 operation(s) for public models.
  name: Cerebras Systems Public Models API
  slug: cerebras-systems-public-models-api
- baseURL: https://api.cerebras.ai
  baseurl_source: declared
  description: The Tcp Warming API from Cerebras Systems — 1 operation(s) for tcp warming.
  name: Cerebras Systems Tcp Warming API
  slug: cerebras-systems-tcp-warming-api
- baseURL: https://api.cerebras.ai
  baseurl_source: declared
  description: The Chat Completions API from Cerebras Systems — 1 operation(s) for chat completions.
  name: Cerebras Systems Chat Completions API
  slug: cerebras-systems-chat-completions-api
artifact_total: 26
collections:
- collection_type: postman
  name: Cerebras Inference Chat API
  slug: postman-cerebras-systems-chat-api
- collection_type: postman
  name: Cerebras Inference Chat Completions API
  slug: postman-cerebras-systems-completions-api
- collection_type: postman
  name: Cerebras Inference Chat Models API
  slug: postman-cerebras-systems-models-api
- collection_type: postman
  name: Cerebras Inference Chat Public Models API
  slug: postman-cerebras-systems-public-models-api
- collection_type: postman
  name: Cerebras Inference Chat Tcp Warming API
  slug: postman-cerebras-systems-tcp-warming-api
- collection_type: open
  name: Cerebras Inference Chat API
  slug: open-cerebras-systems-chat-api
- collection_type: open
  name: Cerebras Inference Chat Completions API
  slug: open-cerebras-systems-completions-api
- collection_type: open
  name: Cerebras Inference Chat Models API
  slug: open-cerebras-systems-models-api
- collection_type: open
  name: Cerebras Inference Chat Public Models API
  slug: open-cerebras-systems-public-models-api
- collection_type: open
  name: Cerebras Inference Chat Tcp Warming API
  slug: open-cerebras-systems-tcp-warming-api
common:
- group: other
  href: https://artifacts.apis.io/cerebras-systems/capabilities/cerebras-systems-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cerebras-systems-capability-edges.yml
- group: other
  title: ''
  type: ModelZoo
  url: https://github.com/Cerebras/modelzoo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerebras-systems
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/CerebrasSystems
- group: operate
  title: ''
  type: Status
  url: https://status.cerebras.ai
- group: agent
  title: ''
  type: LlmsText
  url: https://inference-docs.cerebras.ai/llms.txt
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cerebras-systems/overview
- group: auth
  href: https://artifacts.apis.io/cerebras-systems/security/cerebras-systems-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cerebras-systems-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.cerebras.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://inference-docs.cerebras.ai
- group: docs
  title: ''
  type: Documentation
  url: https://inference-docs.cerebras.ai
- group: docs
  title: ''
  type: APIReference
  url: https://inference-docs.cerebras.ai/api-reference/chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://inference-docs.cerebras.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://inference-docs.cerebras.ai/support/overview
- group: company
  title: ''
  type: Blog
  url: https://www.cerebras.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cerebras
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cerebras.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.cerebras.ai
- group: start
  title: ''
  type: Login
  url: https://cloud.cerebras.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cerebras.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerebras.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cerebras.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cerebras.ai
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cerebras.ai
- group: auth
  title: ''
  type: Security
  url: https://trust.cerebras.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://inference-docs.cerebras.ai/support/change-log
- group: operate
  title: ''
  type: Deprecation
  url: https://inference-docs.cerebras.ai/support/deprecation
- group: build
  href: https://artifacts.apis.io/cerebras-systems/packages/cerebras-systems-packages.yml
  title: ''
  type: Packages
  url: packages/cerebras-systems-packages.yml
- group: build
  href: https://artifacts.apis.io/cerebras-systems/packages/cerebras-systems-packages.yml
  title: ''
  type: SDKs
  url: packages/cerebras-systems-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/Cerebras/cerebras-cloud-sdk-python
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/Cerebras/cerebras-cloud-sdk-node
- group: agent
  href: https://artifacts.apis.io/cerebras-systems/llms/cerebras-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cerebras-systems-llms.txt
- group: agent
  href: https://artifacts.apis.io/cerebras-systems/mcp/cerebras-systems-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cerebras-systems-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cerebras-systems/authentication/cerebras-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cerebras-systems-authentication.yml
- group: design
  href: https://artifacts.apis.io/cerebras-systems/conventions/cerebras-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cerebras-systems-conventions.yml
- group: design
  href: https://artifacts.apis.io/cerebras-systems/errors/cerebras-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cerebras-systems-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cerebras-systems/conformance/cerebras-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cerebras-systems-conformance.yml
- group: design
  href: https://artifacts.apis.io/cerebras-systems/lifecycle/cerebras-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cerebras-systems-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cerebras-systems/rate-limits/cerebras-systems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cerebras-systems-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cerebras-systems/plans/cerebras-systems-plans.yml
  title: ''
  type: Plans
  url: plans/cerebras-systems-plans.yml
- group: other
  href: https://artifacts.apis.io/cerebras-systems/overlays/cerebras-systems-inference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cerebras-systems-inference-overlay.yaml
- group: design
  href: https://artifacts.apis.io/cerebras-systems/data-model/cerebras-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cerebras-systems-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cerebras-systems/security/cerebras-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cerebras-systems-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cerebras-systems/agentic-access/cerebras-systems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cerebras-systems-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/cerebras-systems/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/cerebras-systems/changelog/cerebras-systems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cerebras-systems-changelog.yml
created: '2026-07-17'
description: 'Cerebras Systems builds the Wafer-Scale Engine (WSE) — the largest computer chip ever made — and the CS-3 systems built around it, delivering AI training and inference at speeds far beyond conventional GPUs. Cerebras Inference is the company''s cloud API: an OpenAI-compatible REST interface at api.cerebras.ai that serves open-weight frontier models (OpenAI GPT-OSS, Gemma 4, Z.ai GLM 4.7) at industry-leading tokens-per-second. Developers authenticate with a bearer API key and call chat/completions, completions, and models endpoints, with streaming, tool calling, structured outputs, vision, prompt caching, and batch inference. Custom model weights can be deployed on dedicated endpoints. Official Python and Node.js SDKs, a Cloud Console with a playground, and coding-tool integrations (VS Code, Cline, Kilo Code, OpenCode) round out the developer surface.'
finops:
- has_sources: true
  method: derived
  name: Cerebras Systems Finops
  primary_unit: starting-at
  service_category: ''
  slug: cerebras-systems-finops
  template: false
image: https://github.com/Cerebras.png
layout: provider
modified: '2026-07-18'
name: Cerebras Systems
nav: Providers
network: true
overview: 'Cerebras Systems publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Completions API, Models API, Public Models API, and 2 more. Tagged areas include Company, AI Infrastructure, Artificial Intelligence, Machine Learning, and Inference.


  The Cerebras Systems catalog on APIs.io includes 1 Spectral governance ruleset.


  Cerebras Systems'' developer surface includes status page, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 39 more developer resources.'
plans:
- name: Cerebras Systems Plans
  plan_count: 3
  slug: cerebras-systems-plans
random_paper: 20
rate_limits:
- limit_count: 0
  name: Cerebras Systems Rate Limits
  slug: cerebras-systems-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Cerebras Systems API Rules
  rule_count: 44
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 3
  slug: cerebras-systems-rules
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 42.1
    developer_ergonomics: 72.0
    discoverability: 73.2
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cerebras-systems/cerebras-systems-2026-07-25T204949.png
security:
- kind: authentication
  name: Cerebras Systems Authentication
  slug: cerebras-systems-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cerebras Systems Domain Security
  slug: cerebras-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cerebras Systems Trust Center
  slug: cerebras-systems-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: Run a fast chat completion
  slug: cerebras-systems-fast-chat-completion
- name: Chat completion with structured JSON output
  slug: cerebras-systems-structured-outputs
- name: Chat completion with tool calling
  slug: cerebras-systems-tool-calling
slug: cerebras-systems
tags:
- Company
- AI Infrastructure
- Artificial Intelligence
- Machine Learning
- Inference
- LLM
- Developer Tools
- Cloud Computing
- Semiconductors
website: https://www.cerebras.ai
---
