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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for the Tecton feature platform - the Feature Service (low-latency online feature retrieval, e.g. POST /api/v1/feature-service/get-features), the Ingest API, the Metadata API, and SCIM 2.0 pr
  name: Tecton HTTP API
  slug: tecton-http-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.tecton.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tecton.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tecton.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tecton.ai/http-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tecton.ai/docs/tutorials/tecton-quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.tecton.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tecton-ai
- group: operate
  title: ''
  type: Support
  url: https://support.tecton.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tecton.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tecton.ai/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tecton.ai/whats-new/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.tecton.ai/docs/security
- group: build
  title: ''
  type: Packages
  url: packages/tecton-databricks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tecton-databricks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tecton-databricks-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tecton-databricks-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tecton-databricks-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tecton-databricks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tecton-databricks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tecton-databricks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tecton-databricks-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tecton-databricks-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tecton-databricks-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tecton-databricks-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tecton-databricks-domain-security.yml
created: '2026-07-17'
description: 'Tecton is a feature platform (feature store) for machine learning and AI. It lets data and ML teams define feature transformations once and run them across batch, streaming, and real-time data sources, then materialize and serve those features from a low-latency online store. Features are authored in Python and managed GitOps-style via the tecton CLI and SDK, and consumed at inference time over the Feature Service HTTP API (Authorization: Tecton-key, or Service-Account OAuth). Tecton also ships an Ingest API, a Metadata API, an official MCP server, and Java/Python clients. The company was acquired by Databricks in August 2025 and its platform now powers real-time features and context serving for AI agents.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tecton-databricks.png
layout: provider
mcp_servers:
- description: ''
  name: Tecton (Databricks) MCP Server
  slug: tecton-databricks-mcp-server
modified: '2026-07-21'
name: Tecton (Databricks)
nav: Providers
network: true
overview: 'Tecton (Databricks) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Infrastructure, Feature Store, Feature Platform, and Machine-Learning.


  Tecton (Databricks)''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, CLI, and 18 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 33.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Tecton Databricks Authentication
  slug: tecton-databricks-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tecton Databricks Domain Security
  slug: tecton-databricks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tecton Databricks Trust Center
  slug: tecton-databricks-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tecton-databricks
tags:
- Company
- AI Infrastructure
- Feature Store
- Feature Platform
- Machine-Learning
- MLOps
- Real-Time
- Databricks
website: https://www.tecton.ai/
---
