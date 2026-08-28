---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oumi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oumi.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.oumi.ai
- group: start
  title: ''
  type: Portal
  url: https://platform.oumi.ai
- group: docs
  title: ''
  type: Documentation
  url: https://oumi.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://oumi.ai/docs/en/latest/api/oumi.html
- group: start
  title: ''
  type: GettingStarted
  url: https://oumi.ai/docs/en/latest/get_started/quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/oumi
- group: company
  title: ''
  type: Blog
  url: https://oumiai.substack.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oumi-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://oumi.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.oumi.ai/signin
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oumi-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/oumi-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/oumi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oumi-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oumi-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oumi-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oumi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oumi-well-known.yml
created: '2026-07-17'
description: Oumi (Open Universal Machine Intelligence) is an open-source, Apache-2.0 platform for ML engineers and researchers to train, fine-tune, evaluate, and deploy foundation models (LLMs and VLMs) through a single unified interface. It ships as a Python library and a first-party command-line tool (train, evaluate, infer, launch, deploy, analyze, synth, tune) covering the full model development lifecycle — data synthesis, supervised fine-tuning, DPO/preference learning, evaluation judges, quantization, hyperparameter tuning, and inference across local, cloud, and HPC targets. A hosted managed platform (platform.oumi.ai) adds a Free/Pro/Enterprise product layer, and an oumi-mcp Model Context Protocol server exposes Oumi to MCP-capable assistants such as Claude and Cursor. Backed by Obvious Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oumi.png
layout: provider
mcp_servers:
- description: Oumi ships a first-party Model Context Protocol (MCP) server, `oumi-mcp`, introduced in the v0.8 release (May 2026) for integration with MCP-capable assistants such as Claude and Cursor. It exposes Ou
  name: Oumi MCP Server
  slug: oumi-mcp-server
modified: '2026-07-20'
name: Oumi
nav: Providers
network: true
overview: 'Oumi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Economic Health, Artificial Intelligence, Machine-Learning, and LLM.


  Oumi''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 17.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oumi/refs/heads/main/screenshots/oumi-2026-08-07T191044.png
security:
- kind: domain-security
  name: Oumi Domain Security
  slug: oumi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oumi
tags:
- Company
- Economic Health
- Artificial Intelligence
- Machine-Learning
- LLM
- Foundation Models
- Fine-Tuning
- Model Training
- Open-Source
- MLOps
- Developer Tools
- Inference
website: https://oumi.ai
---
