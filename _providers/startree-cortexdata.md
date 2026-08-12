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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Query API API from StarTree (Cortexdata) — 1 operation(s) for query api.
  name: StarTree (Cortexdata) Query API API
  slug: startree-cortexdata-query-api-api
artifact_total: 5
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/startree-cortexdata-query-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/startree-cortexdata-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/startree-cortexdata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://startree.ai/responsible-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/startree-cortexdata-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/startree-cortexdata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/startree-cortexdata-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/startree-cortexdata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/startree-cortexdata-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/startree-cortexdata-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.startree.ai/products/startree-cloud/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/startree-cortexdata-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/startree-cortexdata-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/startree-cortexdata-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.startree.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.startree.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.startree.ai/api-reference/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/startreedata
- group: operate
  title: ''
  type: Support
  url: https://support.startree.ai/
- group: company
  title: ''
  type: Blog
  url: https://startree.ai/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://startree.ai/pricing/
- group: start
  title: ''
  type: Login
  url: https://startree.cloud/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://startree.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://startree.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.startree.ai/
created: '2026-07-17'
description: StarTree is a real-time analytics company founded by the creators of Apache Pinot. Its managed StarTree Cloud platform ingests streaming and batch data (Kafka, Confluent, S3, GCS, Iceberg and more), models it, and serves sub-second, high-concurrency SQL analytics for customer-facing, agent-facing, and operational use cases via a console, client libraries, and REST APIs. StarTree Cloud runs as SaaS, BYOC, or BYOK, adds indexing, tiered storage, RBAC/SSO, and SOC 2 + ISO 27001 security, and includes the ThirdEye anomaly detection product. Authenticated with a console-issued Bearer JWT.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/startree-cortexdata.png
layout: provider
mcp_servers:
- description: ''
  name: startree-cortexdata-mcp.yml
  slug: startree-cortexdata-mcpyml
modified: '2026-07-21'
name: StarTree (Cortexdata)
nav: Providers
network: true
overview: 'StarTree (Cortexdata) publishes 1 API on the [APIs.io](https://apis.io/) network: Query API API. Tagged areas include Company, Ai Infrastructure, Real-Time Analytics, Apache Pinot, and OLAP.


  StarTree (Cortexdata)''s developer surface includes authentication, changelog, documentation, API reference, support, engineering blog, pricing, and 19 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 50.9
  delta: -1.7
  facets:
    commercial_clarity: 52.6
    contract_quality: 58.2
    developer_ergonomics: 58.2
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 52.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Startree Cortexdata Authentication
  slug: startree-cortexdata-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Startree Cortexdata Domain Security
  slug: startree-cortexdata-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Startree Cortexdata Vulnerability Disclosure
  slug: startree-cortexdata-vulnerability-disclosure
  summary_line: disclosure policy published
slug: startree-cortexdata
tags:
- Company
- Ai Infrastructure
- Real-Time Analytics
- Apache Pinot
- OLAP
- Analytics
- Streaming Data
- Database
website: https://www.startree.ai/
---
