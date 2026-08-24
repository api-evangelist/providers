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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Low-latency online feature serving for model inference — read single or batched feature vectors, wildcard queries, and feature-service metadata. Authenticated with an Authorization Tecton-key header b
  name: Tecton FeatureService HTTP API
  slug: tecton-featureservice-http-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.tecton.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tecton.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tecton.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tecton.ai/docs/reading-feature-data/reading-online-features-for-inference-using-the-http-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tecton.ai/docs/tutorials/tecton-quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tecton-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://tecton.statuspage.io
- group: auth
  title: ''
  type: Compliance
  url: https://docs.tecton.ai/docs/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/tecton-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tecton-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tecton-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/tecton-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tecton-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tecton-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tecton-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tecton-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tecton-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tecton-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tecton-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tecton-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tecton-llms.txt
created: '2026-07-17'
description: Tecton is the enterprise feature platform (feature store) for real-time machine learning and AI at scale. It transforms raw batch, streaming, and real-time data into ML-ready features and embeddings, orchestrates the pipelines that materialize them, and serves them to models online with low latency and ~100ms freshness while guaranteeing training/serving consistency. Developers define features as code with the Python SDK and `tecton` CLI, then read them for inference through the FeatureService HTTP API and open-source Python and Java client libraries. Backed by Andreessen Horowitz, Lux Capital, and SV Angel.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tecton.png
layout: provider
mcp_servers:
- description: ''
  name: Tecton MCP Server
  slug: tecton-mcp-server
modified: '2026-07-21'
name: Tecton
nav: Providers
network: true
overview: 'Tecton publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Machine-Learning, Feature Store, Feature Platform, and MLOps.


  Tecton''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, and 16 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 26.1
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 26.1
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Tecton Authentication
  slug: tecton-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Tecton Domain Security
  slug: tecton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tecton Trust Center
  slug: tecton-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tecton
tags:
- Company
- Machine-Learning
- Feature Store
- Feature Platform
- MLOps
- Artificial Intelligence
- Real-Time Data
- SDK
website: https://www.tecton.ai
---
