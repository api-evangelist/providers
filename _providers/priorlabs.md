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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Priorlabs Agentic Access
  operation_count: 7
  slug: priorlabs-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 2
apis:
- description: The Prediction API from Prior Labs — 3 operation(s) for prediction.
  name: Prior Labs Prediction API
  slug: priorlabs-prediction-api
- description: The Training API from Prior Labs — 4 operation(s) for training.
  name: Prior Labs Training API
  slug: priorlabs-training-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TabPFN Prediction API
  slug: open-priorlabs-prediction-api
- collection_type: open
  name: TabPFN Prediction Training API
  slug: open-priorlabs-training-api
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.priorlabs.ai/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.priorlabs.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.priorlabs.ai/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.priorlabs.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://priorlabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PriorLabs
- group: start
  title: ''
  type: SignUp
  url: https://ux.priorlabs.ai/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://priorlabs.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://priorlabs.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@priorlabs.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.priorlabs.ai/changelog
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/priorlabs-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/priorlabs-tabpfn-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/priorlabs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/priorlabs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/priorlabs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/priorlabs-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/priorlabs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/priorlabs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/priorlabs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/priorlabs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/priorlabs-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/priorlabs-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/priorlabs-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/priorlabs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/priorlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://priorlabs.ai/
created: '2026-07-17'
description: Prior Labs builds TabPFN, a tabular foundation model that delivers strong predictions on structured/tabular data in seconds — no dataset-specific training, tuning, or ML pipelines required. TabPFN-3 handles classification, regression, time-series forecasting, anomaly detection, synthetic data generation, embeddings, and uncertainty quantification via in-context learning, scaling to 1M rows, 2,000 columns, and 160 classes. Prior Labs exposes TabPFN through a cloud REST API (api.priorlabs.ai), Python and R client SDKs, a Model Context Protocol server for AI agents, and private deployments on AWS SageMaker, Databricks, and Azure AI Foundry. The company was published in Nature and is now part of SAP.
image: https://priorlabs.ai/pl.svg
layout: provider
mcp_servers:
- description: ''
  name: Prior Labs MCP Server
  slug: prior-labs-mcp-server
modified: '2026-07-20'
name: Prior Labs
nav: Providers
network: true
overview: 'Prior Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: Prediction API and Training API. Tagged areas include Company, Machine-Learning, Artificial Intelligence, Tabular Data, and Foundation Models.


  Prior Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, changelog, and 21 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 61.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/priorlabs/refs/heads/main/screenshots/priorlabs-2026-08-17T081338.png
security:
- kind: authentication
  name: Priorlabs Authentication
  slug: priorlabs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Priorlabs Domain Security
  slug: priorlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: priorlabs
tags:
- Company
- Machine-Learning
- Artificial Intelligence
- Tabular Data
- Foundation Models
- Predictions
- Data Science
- MCP
- SDK
website: https://priorlabs.ai/
---
