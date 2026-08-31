---
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Dataloop (Dell Data Orchestration Engine) platform REST API. Every part of the platform — projects, datasets, items, annotations, recipes and ontologies, tasks and assignments, packages, services,
  name: Dataloop Platform API
  slug: platform-api
artifact_total: 7
asyncapis:
- description: ''
  name: Dataloop Platform Events
  slug: dataloop-platform-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dataloop-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://dataloop.ai/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dataloop-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://dataloop.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dataloop.ai/resources
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dataloop.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sdk-docs.dataloop.ai/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dataloop.ai/onboarding/onboarding
- group: operate
  title: ''
  type: Support
  url: https://dataloop.ai/contact/
- group: company
  title: ''
  type: Blog
  url: https://dataloop.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dataloop-ai
- group: start
  title: ''
  type: SignUp
  url: https://console.dataloop.ai/welcome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataloop.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataloop.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.dataloop.ai/docs/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/dataloop-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dataloop.ai/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.dataloop.ai/docs/deprecations
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dataloop-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dataloop-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dataloop-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dataloop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dataloop-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dataloop-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/dataloop-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dataloop-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dataloop-cli.yml
- group: design
  title: ''
  type: Components
  url: components/dataloop-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dataloop-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dataloop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dataloop-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dataloop-platform-events.yml
created: '2026-08-04'
description: 'Dataloop is an enterprise AI data platform for the full unstructured-data lifecycle — ingesting images, video, audio, text and LiDAR from cloud or on-premises storage, labeling and reviewing it through managed annotation tasks and recipes, orchestrating it with pipelines and serverless functions (FaaS), and turning it into governed, model-ready datasets. The platform is programmable end to end: a JWT-authenticated REST API at gate.dataloop.ai/api/v1, a first-party Python SDK and `dlp` CLI (dtlpy), a JavaScript SDK, and a Vue component library for building in-platform applications. Founded in Israel in 2017, Dataloop was acquired by Dell Technologies in December 2025 and the platform is now marketed as the Dell Data Orchestration Engine (DDOE).'
image: https://dataloop.ai/wp-content/uploads/2024/02/dataloop-logo-main.svg
layout: provider
mcp_servers:
- description: ''
  name: Dataloop MCP Server
  slug: dataloop-mcp-server
modified: '2026-08-04'
name: DataLoop
nav: Providers
network: true
overview: 'DataLoop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine-Learning, Data Management, Data Annotation, and MLOps.


  The DataLoop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DataLoop''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 25 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 50.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dataloop/refs/heads/main/screenshots/dataloop-2026-08-07T164125.png
security:
- kind: authentication
  name: Dataloop Authentication
  slug: dataloop-authentication
  summary_line: http/oauth2/apiKey · 5 schemes
- kind: domain-security
  name: Dataloop Domain Security
  slug: dataloop-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dataloop Vulnerability Disclosure
  slug: dataloop-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Dataloop Trust Center
  slug: dataloop-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 27017:2015, ISO/IEC 27018:2019, GDPR, AWS Qualified Software
slug: dataloop
tags:
- Artificial Intelligence
- Machine-Learning
- Data Management
- Data Annotation
- MLOps
- Computer-Vision
- Generative AI
- Data Labeling
- Pipelines
- Serverless
- Enterprise Software
- Company
website: https://dataloop.ai/
---
