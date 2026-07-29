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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Automate and schedule predictive query training and batch predictions. Retrain a predictive query (re-ingesting data from the source), trigger recurring batch predictions, monitor job status and evalu
  name: Kumo REST API
  slug: kumoai-rest-api
- description: Open-source Model Context Protocol server that empowers AI assistants with KumoRFM. Builds, manages, and visualizes relational graphs directly from CSV or Parquet files, converts natural language into
  name: KumoRFM MCP Server
  slug: kumoai-rfm-mcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://kumo.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nvidia.com/sdgm/rfm/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nvidia.com/sdgm/rfm/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nvidia.com/sdgm/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nvidia.com/sdgm/quick-start/rfm
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/kumoaibuilders/shared_invite/zt-2z9uih3lf-fPM1z2ACZg~oS3ObmiQLKQ
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kumo-ai
- group: start
  title: ''
  type: SignUp
  url: https://kumorfm.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.nvidia.com/sdgm/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://docs.nvidia.com/sdgm/security-and-governance
- group: auth
  title: ''
  type: Compliance
  url: https://docs.nvidia.com/sdgm/security-and-governance
- group: auth
  title: ''
  type: TrustCenter
  url: security/kumoai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kumoai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kumoai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kumoai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kumoai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kumoai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kumoai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kumoai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kumoai-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/kumoai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kumoai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kumoai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kumoai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kumoai-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kumoai-conformance.yml
created: '2026-07-17'
description: Kumo.AI builds predictive AI for relational data. Its flagship model, KumoRFM, is a pre-trained Relational Foundation Model that generates training-free predictions over multi-table data by interpreting a data warehouse as a temporal heterogeneous graph, queried through a SQL-like Predictive Query Language (PQL). Kumo exposes this through a Python SDK (kumoai), a REST API for automating retraining and batch predictions, an open-source Model Context Protocol server (kumo-rfm-mcp) for agentic workflows, and a published Agent Skills catalog. It ships as SaaS, VPC/BYOC, a Snowflake Native Application, and a Databricks Native Application. Kumo product documentation is now hosted by NVIDIA under Structured Data and Graph Models.
image: https://avatars.githubusercontent.com/u/83320328?v=4
layout: provider
mcp_servers:
- description: ''
  name: kumoai-mcp.yml
  slug: kumoai-mcpyml
- description: ''
  name: kumoai-mcp.yml
  slug: kumoai-mcpyml-2
modified: '2026-07-19'
name: Kumo.AI
nav: Providers
network: true
overview: 'Kumo.AI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Machine Learning, Predictive Analytics, and Graph Neural Networks.


  Kumo.AI''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, changelog, and 20 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 0
  name: Kumoai Rate Limits
  slug: kumoai-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 35.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kumoai/refs/heads/main/screenshots/kumoai-2026-07-25T224329.png
security:
- kind: authentication
  name: Kumoai Authentication
  slug: kumoai-authentication
  summary_line: apiKey/snowflakeCredentials/http · 4 schemes
- kind: domain-security
  name: Kumoai Domain Security
  slug: kumoai-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Kumoai Vulnerability Disclosure
  slug: kumoai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Kumoai Trust Center
  slug: kumoai-trust-center
  summary_line: SOC 2
slug: kumoai
tags:
- Company
- Ai
- Machine Learning
- Predictive Analytics
- Graph Neural Networks
- Foundation Models
- Data Warehouse
- Model Context Protocol
- Agents
- Relational Data
website: https://kumo.ai
---
