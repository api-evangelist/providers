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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Horizon Robotics'' hosted Model Context Protocol server for the OpenExplorer toolchain. Probed anonymously on 2026-08-22: MCP protocol version 2025-06-18, serverInfo "Open Explorer MCP Server" v3.9.0, '
  name: Open Explorer MCP Server
  slug: open-explorer-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.horizon.auto/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.horizon.auto/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.horizon.auto/docs
- group: company
  title: ''
  type: Blog
  url: https://developer.horizon.auto/blog
- group: operate
  title: ''
  type: Support
  url: https://developer.horizon.auto/forum
- group: start
  title: ''
  type: SignUp
  url: https://developer.horizon.auto/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HorizonRobotics
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.horizon.auto/en/legal/privacy
- group: other
  title: ''
  type: IntellectualProperty
  url: https://www.horizon.auto/en/legal/intellectual-property-rights
- group: auth
  title: ''
  type: Security
  url: security/horizon-robotics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/horizon-robotics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/horizon-robotics-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/horizon-robotics-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/horizon-robotics-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/horizon-robotics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/horizon-robotics-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/horizon-robotics-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/horizon-robotics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/horizon-robotics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/horizon-robotics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/horizon-robotics-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/horizon-robotics-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/horizon-robotics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/horizon-robotics-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/horizon-robotics-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/horizon-robotics-llms.txt
created: '2026-08-22'
description: 'Horizon Robotics (Hong Kong Stock Exchange: 9660.HK) is a Chinese provider of smart-driving computing solutions, founded in 2015, that designs the Journey (征程) family of automotive AI processors around its proprietary BPU (Brain Processing Unit) architecture and pairs them with a full software stack — Horizon Mono ADAS, Horizon SuperDrive assisted driving, TogetheROS, Matrix, QoHo and AIDI. Its developer-facing surface is not a hosted web API but a toolchain: OpenExplorer (OE), the model compilation, quantization and deployment kit built around HBDK, HMCT, the Horizon PyTorch Plugin, horizon_tc_ui and the UCP on-board runtime, documented at developer.horizon.auto and doc.oe.horizon.auto. Horizon publishes two genuine agent surfaces on top of that toolchain: a live, unauthenticated remote Model Context Protocol server at mcp.oe.horizon.auto that exposes semantic code and documentation retrieval, and OE-Skills, an Apache-2.0 pack of 37 structured Agent Skills for Claude Code,
  Codex and Cursor that drive HBDK compilation, PTQ/QAT quantization, UCP on-board inference and LLM compression.'
image: https://www.horizon.auto/favicon.ico
layout: provider
mcp_servers:
- description: 'Horizon Robotics'' hosted Model Context Protocol server for the OpenExplorer (OE) toolchain. It gives a coding agent semantic retrieval over Horizon''s indexed codebases (Milvus-backed) and the Horizon '
  name: Open Explorer MCP Server
  slug: open-explorer-mcp-server
modified: '2026-08-22'
name: Horizon Robotics
nav: Providers
network: true
overview: 'Horizon Robotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automotive, Autonomous Driving, and Semiconductors.


  Horizon Robotics'' developer surface includes documentation, engineering blog, support, signup flow, CLI, authentication, changelog, and 20 more developer resources.'
plans:
- name: Horizon Robotics Plans Pricing
  plan_count: 0
  slug: horizon-robotics-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Horizon Robotics Rate Limits
  slug: horizon-robotics-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 27.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/horizon-robotics/refs/heads/main/screenshots/horizon-robotics-2026-09-02T145749.png
security:
- kind: authentication
  name: Horizon Robotics Authentication
  slug: horizon-robotics-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Horizon Robotics Domain Security
  slug: horizon-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Horizon Robotics Vulnerability Disclosure
  slug: horizon-robotics-vulnerability-disclosure
  summary_line: contact published
slug: horizon-robotics
tags:
- Company
- Artificial Intelligence
- Automotive
- Autonomous Driving
- Semiconductors
- Robotics
- Edge AI
- Machine-Learning
- MCP
- Agent Skills
- Developer Tools
- China
website: https://www.horizon.auto/en
---
