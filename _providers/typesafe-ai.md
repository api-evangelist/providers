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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Hosted, anonymous, read-mostly MCP server over the published TypeSafe documentation corpus. Three tools: search_type_safe_ai (knowledge-base search), query_docs_filesystem_type_safe_ai (read-only rg/t'
  name: TypeSafe AI Documentation MCP Server
  slug: docs-mcp
- baseURL: https://api.typesafe.ai
  baseurl_source: declared
  description: The Models API from TypeSafe AI — 1 operation(s) for models.
  name: TypeSafe AI Models API
  slug: typesafe-ai-models-api
- baseURL: https://api.typesafe.ai
  baseurl_source: declared
  description: The Systemone API from TypeSafe AI — 1 operation(s) for systemone.
  name: TypeSafe AI Systemone API
  slug: typesafe-ai-systemone-api
artifact_total: 16
common:
- group: other
  href: https://artifacts.apis.io/typesafe-ai/capabilities/typesafe-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/typesafe-ai-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/typesafe-ai/security/typesafe-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/typesafe-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/typesafe-ai/security/typesafe-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/typesafe-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://typesafe.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.typesafe.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.typesafe.ai/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.typesafe.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.typesafe.ai/introduction/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://console.typesafe.ai/
- group: start
  title: ''
  type: Login
  url: https://console.typesafe.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://typesafe.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://typesafe.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/typesafe-ai
- group: company
  title: ''
  type: Blog
  url: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- group: other
  title: ''
  type: Leadership
  url: https://typesafe.ai/team
- group: operate
  title: ''
  type: StatusPage
  url: https://status.typesafe.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.typesafe.ai/
- group: agent
  href: https://artifacts.apis.io/typesafe-ai/mcp/typesafe-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/typesafe-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/typesafe-ai/a2a/typesafe-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/typesafe-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/typesafe-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/typesafe-ai/llms/typesafe-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/typesafe-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/typesafe-ai/well-known/typesafe-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/typesafe-ai-well-known.yml
- group: auth
  href: https://artifacts.apis.io/typesafe-ai/well-known/typesafe-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/typesafe-ai-security.txt
- group: build
  href: https://artifacts.apis.io/typesafe-ai/packages/typesafe-ai-packages.yml
  title: ''
  type: Packages
  url: packages/typesafe-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/typesafe-ai/packages/typesafe-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/typesafe-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/typesafe-ai/authentication/typesafe-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/typesafe-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/typesafe-ai/conventions/typesafe-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/typesafe-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/typesafe-ai/conformance/typesafe-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/typesafe-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/typesafe-ai/errors/typesafe-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/typesafe-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/typesafe-ai/lifecycle/typesafe-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/typesafe-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/typesafe-ai/changelog/typesafe-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/typesafe-ai-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/typesafe-ai/plans/typesafe-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/typesafe-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/typesafe-ai/rate-limits/typesafe-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/typesafe-ai-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/typesafe-ai/sandbox/typesafe-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/typesafe-ai-sandbox.yml
- group: design
  href: https://artifacts.apis.io/typesafe-ai/data-model/typesafe-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/typesafe-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/typesafe-ai/examples/typesafe-ai-examples.yml
  title: ''
  type: Examples
  url: examples/typesafe-ai-examples.yml
- group: other
  href: https://artifacts.apis.io/typesafe-ai/overlays/typesafe-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/typesafe-ai-openapi-overlay.yaml
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/typesafe-ai
- group: auth
  href: https://artifacts.apis.io/typesafe-ai/security/typesafe-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/typesafe-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/typesafe-ai/security/typesafe-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/typesafe-ai-trust-center.yml
- group: operate
  title: ''
  type: IncidentNotification
  url: https://typesafe.ai/legal/data-processing
- group: other
  title: ''
  type: Subprocessors
  url: https://trust.typesafe.ai/subprocessors
- group: other
  title: ''
  type: DataResidency
  url: https://typesafe.ai/legal/privacy-policy
- group: other
  title: ''
  type: AITransparency
  url: https://docs.typesafe.ai/model-jaggedness/jev-1.13
created: '2026-09-19'
description: 'TypeSafe AI is a San Francisco AI lab building System One models — a class of model trained to return typed, calibrated decisions for software instead of generated text. Its flagship and first System One model, Jev, is served by a single HTTP endpoint: POST /v1/systemone takes a `state` (a string, JSON object, or array) plus a map of typed questions and returns one structured answer per question. Three question primitives are published: Noul (a yes/no question answered with the probability the answer is yes), Choice (one option from a caller-defined set, returned with the full probability distribution) and Score (a rating against ordered rubric levels, returned as a probability-weighted value plus a legend). Choice and Score answers also carry a confidence value derived from the distribution, which is the mechanism TypeSafe intends callers to threshold on to decide when code may act autonomously and when it must escalate to a human. The model is trained with Reinforcement Learning
  for Calibrated Decisions (RLCD) rather than RLHF, is not fine-tuned or LoRA-adapted per customer, and is not trained on customer requests or responses. The company publishes an OpenAPI 3.1 contract on its API host, official Python and TypeScript SDKs, an installable Agent Skill for Claude Code and other coding agents, an A2A agent card, an anonymous documentation MCP server, an llms.txt index, a Better Stack status page and a Vanta trust center.'
finops:
- has_sources: true
  method: derived
  name: Typesafe Ai Finops
  primary_unit: ''
  service_category: ''
  slug: typesafe-ai-finops
  template: true
image: https://framerusercontent.com/images/RtIGTDwO43jR4ZDilesXiR5znc.jpg
layout: provider
mcp_servers:
- description: TypeSafe runs a live, anonymous, hosted MCP server at https://docs.typesafe.ai/mcp. It answered a cold JSON-RPC tools/list with no credentials and returned three real tools with full inputSchema, plus
  name: TypeSafe AI
  slug: typesafe-ai
modified: '2026-09-19'
name: TypeSafe AI
nav: Providers
network: true
overview: 'TypeSafe AI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Models API, Systemone API, and 1 more. Tagged areas include Artificial Intelligence, Machine Learning, Classification, Content Moderation, and Decision Support.


  The TypeSafe AI catalog on APIs.io includes 1 Spectral governance ruleset.


  TypeSafe AI''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, changelog, and 37 more developer resources.'
plans:
- name: Typesafe Ai Plans Pricing
  plan_count: 0
  slug: typesafe-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Typesafe Ai Rate Limits
  slug: typesafe-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: TypeSafe AI API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 1
  slug: typesafe-ai-rules
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 35.5
    contract_governance: 31.8
    contract_quality: 53.4
    developer_ergonomics: 69.0
    discoverability: 75.8
    operational_transparency: 36.8
  previous_composite: 53.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 47.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/typesafe-ai/typesafe-ai-2026-10-11T131335.png
security:
- kind: authentication
  name: Typesafe Ai Authentication
  slug: typesafe-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Typesafe Ai Domain Security
  slug: typesafe-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Typesafe Ai Vulnerability Disclosure
  slug: typesafe-ai-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Typesafe Ai Trust Center
  slug: typesafe-ai-trust-center
  summary_line: observed, observed_note, how_to_close
skill_count: 4
skills:
- name: Discover models and pin a version
  slug: typesafe-ai-discover-models-and-pin-a-version
- name: Evaluate state with typed questions
  slug: typesafe-ai-evaluate-state-with-typed-questions
- name: TypeSafe
  slug: typesafe-ai-provider-docs-skill
- name: typesafe-ai
  slug: typesafe-ai-provider-github-skill
slug: typesafe-ai
tags:
- Artificial Intelligence
- Machine Learning
- Classification
- Content Moderation
- Decision Support
- Structured Outputs
- Inference
- LLM Alternative
- Agent Skills
- MCP
- Agent-Native
- Developer Tools
- A2A
website: https://typesafe.ai/
---
