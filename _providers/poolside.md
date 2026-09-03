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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: OpenAI-compatible inference API for poolside's Laguna agentic-coding models. Send chat-completion and model-listing requests from your own tools, scripts, and applications using the OpenAI SDK by swit
  name: Poolside API
  slug: poolside-api
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.poolside.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.poolside.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.poolside.ai/api/openai-api-examples
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.poolside.ai/get-started/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.poolside.ai/get-started/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://platform.poolside.ai
- group: start
  title: ''
  type: Login
  url: https://docs.poolside.ai/get-started/log-in
- group: operate
  title: ''
  type: Support
  url: https://docs.poolside.ai/support/overview
- group: company
  title: ''
  type: Blog
  url: https://poolside.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.poolside.ai/legal/end-user-license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.poolside.ai/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.poolside.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.poolside.ai/release-notes/overview
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poolside-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/poolside-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/poolside-security.txt
- group: auth
  title: ''
  type: Security
  url: https://poolside.ai/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/poolside-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poolside-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/poolside-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/poolside-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/poolside-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/poolside-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/poolside-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/poolside-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/poolside-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/poolside-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/poolside-problem-types.yml
created: '2026-07-17'
description: poolside builds open-weight foundation models and the systems that refine them for agentic software engineering. Its Laguna model family (Laguna XS 2.1, a 33B on-device model, and Laguna M.1, a 225B model with a 256K context window) is served through an OpenAI-compatible inference API at inference.poolside.ai, the hosted Poolside Platform, OpenRouter, and self-managed on-premises / cloud Kubernetes deployments (Amazon EKS, OpenShift, upstream Kubernetes). Developers work with the models through the `pool` Agent CLI, editor and coding-agent integrations (VS Code, JetBrains, Neovim, Zed, Cline, Goose, GitHub Copilot), the Agent Client Protocol, MCP servers, and reusable Skills / AGENTS.md instructions. poolside targets secure, self-hosted enterprise and government software engineering and is backed by SoftBank Vision Fund.
image: https://poolside.ai/og/og-home.png
layout: provider
modified: '2026-07-20'
name: poolside
nav: Providers
network: true
overview: 'poolside publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Artificial Intelligence, Machine-Learning, and Foundation Models.


  poolside''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, support, engineering blog, and 22 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 32.6
  provenance:
    conformance: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poolside/refs/heads/main/screenshots/poolside-2026-09-02T151727.png
security:
- kind: authentication
  name: Poolside Authentication
  slug: poolside-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Poolside Domain Security
  slug: poolside-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Poolside Vulnerability Disclosure
  slug: poolside-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Poolside Trust Center
  slug: poolside-trust-center
  summary_line: trust center published
slug: poolside
tags:
- Company
- Enterprise
- Artificial Intelligence
- Machine-Learning
- Foundation Models
- Coding Assistant
- Developer Tools
- LLM
- Agents
- Code Generation
- Inference
- OpenAI-Compatible
website: https://platform.poolside.ai
---
