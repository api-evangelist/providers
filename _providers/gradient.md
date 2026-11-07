---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Gradient Agentic Access
  operation_count: 3
  slug: gradient-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://apis.gradient.network/api/v1
  baseurl_source: declared
  description: Text completion
  name: Gradient Completions API
  slug: gradient-completions-api
- baseURL: https://apis.gradient.network/api/v1
  baseurl_source: declared
  description: Model listing and management
  name: Gradient Models API
  slug: gradient-models-api
- baseURL: https://apis.gradient.network/api/v1
  baseurl_source: declared
  description: Chat completion
  name: Gradient Chat Completions API
  slug: gradient-chat-completions-api
artifact_total: 12
collections:
- collection_type: open
  name: Gradient Cloud AI Chat API
  slug: open-gradient-chat-api
- collection_type: open
  name: Gradient Cloud AI Chat Completions API
  slug: open-gradient-completions-api
- collection_type: open
  name: Gradient Cloud AI Chat Models API
  slug: open-gradient-models-api
common:
- group: company
  title: ''
  type: Website
  url: https://gradient.network
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gradient.network
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gradient.network
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gradient.network/enterprise-solutions/gradient-cloud/api-reference-documentation
- group: company
  title: ''
  type: Blog
  url: https://gradient.network/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/gradientnetwork
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GradientHQ
- group: agent
  href: https://artifacts.apis.io/gradient/llms/gradient-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gradient-llms.txt
- group: auth
  href: https://artifacts.apis.io/gradient/authentication/gradient-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gradient-authentication.yml
- group: agent
  href: https://artifacts.apis.io/gradient/agentic-access/gradient-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gradient-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gradient/security/gradient-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gradient-domain-security.yml
- group: build
  href: https://artifacts.apis.io/gradient/packages/gradient-packages.yml
  title: ''
  type: Packages
  url: packages/gradient-packages.yml
- group: agent
  href: https://artifacts.apis.io/gradient/mcp/gradient-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gradient-mcp.yml
- group: other
  href: https://artifacts.apis.io/gradient/overlays/gradient-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gradient-cloud-overlay.yaml
- group: design
  href: https://artifacts.apis.io/gradient/conformance/gradient-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gradient-conformance.yml
- group: design
  href: https://artifacts.apis.io/gradient/errors/gradient-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gradient-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gradient/lifecycle/gradient-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gradient-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gradient/conventions/gradient-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gradient-conventions.yml
- group: operate
  href: https://artifacts.apis.io/gradient/changelog/gradient-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gradient-changelog.yml
- group: build
  href: https://artifacts.apis.io/gradient/cli/gradient-cli.yml
  title: ''
  type: CLI
  url: cli/gradient-cli.yml
- group: design
  href: https://artifacts.apis.io/gradient/data-model/gradient-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gradient-data-model.yml
- group: agent
  href: https://artifacts.apis.io/gradient/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Gradient is a decentralized AI infrastructure company building the Open Intelligence Stack — a peer-powered, sovereign alternative to centralized AI clouds. Its stack pairs Parallax (a distributed model-serving / world inference engine that turns heterogeneous machines into one AI cluster), Lattica (a universal peer-to-peer data-motion engine that moves model weights and inference tokens across a global machine mesh), Echo (distributed reinforcement learning) and Symphony (a decentralized multi-agent framework). Gradient Cloud is the enterprise inference offering, exposing an OpenAI-compatible REST API (model listing, chat completion, and text completion, streaming or non-streaming) at apis.gradient.network. The projects run atop a Solana-based network whose Sentry Node browser extension let contributors share edge compute. Gradient is backed by Multicoin Capital and Wing Venture Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gradient.png
layout: provider
modified: '2026-07-19'
name: Gradient
nav: Providers
network: true
overview: 'Gradient publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Completions API, Models API, and Chat Completions API. Tagged areas include Company, Web3, Artificial Intelligence, Machine Learning, and Inference.


  The Gradient catalog on APIs.io includes 1 Spectral governance ruleset.


  Gradient''s developer surface includes documentation, API reference, engineering blog, support, authentication, changelog, CLI, and 15 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Gradient API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: gradient-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 14.6
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gradient/gradient-2026-07-25T220159.png
security:
- kind: authentication
  name: Gradient Authentication
  slug: gradient-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gradient Domain Security
  slug: gradient-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Run a chat completion on Gradient Cloud
  slug: gradient-chat-completion
- name: Run a text completion on Gradient Cloud
  slug: gradient-text-completion
slug: gradient
tags:
- Company
- Web3
- Artificial Intelligence
- Machine Learning
- Inference
- Decentralized Infrastructure
- Distributed Computing
- Edge Computing
- Developer Tools
website: https://gradient.network
---
