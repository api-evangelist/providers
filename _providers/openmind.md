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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Unified chat-completions endpoint that proxies multiple LLM providers (OpenAI, Anthropic via OpenRouter, Google Gemini, X.AI, DeepSeek, NEAR.AI) through a single OpenAI-compatible interface authentica
  name: OpenMind LLM API
  slug: openmind-llm-api
- description: Account and API-key management API (create/delete/list keys, account OMCU balance) at api.openmind.com/api/core, authenticated with a Clerk-issued JWT bearer token.
  name: OpenMind Core API
  slug: openmind-core-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://openmind.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.openmind.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openmind.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openmind.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openmind.com/developing/1_get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.openmind.com/api-reference/api_pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.openmind.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@openmind.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenMind
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openmind-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/openmind-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openmind-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/openmind-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openmind-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openmind-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openmind-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openmind-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openmind-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openmind-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openmind-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openmind-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/openmind-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openmind-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/openmind-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openmind-domain-security.yml
created: '2026-07-17'
description: OpenMind builds open-source software that makes robots useful. Its flagship product, OM1, is a modular AI Hardware Abstraction Layer (HAL) and agent runtime for robots that unifies perception, LLM reasoning, and action across hardware platforms such as the Unitree Go2 quadruped, Unitree G1 humanoid, TurtleBot4, Raspberry Pi, and Tesla. OpenMind operates a cloud API at api.openmind.com that provides a unified multi-provider LLM endpoint (OpenAI, Anthropic via OpenRouter, Google Gemini, X.AI, DeepSeek, NEAR.AI), speech services (Google/ElevenLabs ASR, ElevenLabs/Riva TTS), a ViLA vision-language model, and account/API-key management. Usage is metered in OMCU (OpenMind Computational Units) across free, standard, builder, pro, and enterprise plans. Premium REST APIs (Orchestrator and Nav2) provide remote SLAM, navigation, patrol, docking, and map management for the OM1 ROS2 SDK. OpenMind is backed by Pantera Capital and also develops the FABRIC decentralized robot coordination layer
  and Asimov blockchain-based governance for robots.
image: https://openmind.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: OpenMind MCP Server
  slug: openmind-mcp-server
modified: '2026-07-20'
name: OpenMind
nav: Providers
network: true
overview: 'OpenMind publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Robotics, Robots, and Artificial Intelligence.


  OpenMind''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, CLI, and 19 more developer resources.'
plans:
- name: Openmind Plans
  plan_count: 6
  slug: openmind-plans
random_paper: 18
rate_limits:
- limit_count: 5
  name: Openmind Rate Limits
  slug: openmind-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 36.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openmind/refs/heads/main/screenshots/openmind-2026-08-07T190620.png
security:
- kind: authentication
  name: Openmind Authentication
  slug: openmind-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Openmind Domain Security
  slug: openmind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openmind
tags:
- Company
- Crypto
- Robotics
- Robots
- Artificial Intelligence
- Agents
- LLM
- ROS 2
- Machine-Learning
- Autonomy
website: https://openmind.com/
---
