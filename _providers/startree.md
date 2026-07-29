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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Startree Agentic Access
  operation_count: 1
  slug: startree-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Query API API from StarTree — 1 operation(s) for query api.
  name: StarTree Query API API
  slug: startree-query-api-api
artifact_total: 6
common:
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
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.startree.ai/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.startree.ai/
- group: company
  title: ''
  type: Blog
  url: https://startree.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/startreedata
- group: commercial
  title: ''
  type: Pricing
  url: https://startree.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://startree.ai/trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://startree.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://startree.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://startree.statuspage.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/startree-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/startree-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/startree-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/startree-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/startree-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/startree-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/startree-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/startree-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://startree.ai/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/startree-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/startree-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://startree.ai/responsible-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/startree-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/startree-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://startree.ai/
created: '2026-07-17'
description: StarTree is a real-time analytics platform built on Apache Pinot, the open-source OLAP database for user-facing and agent-facing analytics. StarTree Cloud is the fully managed, enterprise-grade service — sub-second queries at high concurrency, streaming and batch ingestion up to millions of events per second, scalable upserts, in-place queries on Apache Iceberg tables, and ThirdEye anomaly detection. It ships enterprise security (RBAC, SSO, encryption, SOC 2 / ISO 27001 / HIPAA) with SaaS, BYOC, and BYOK deployment options, and exposes Controller, Broker, and Query REST APIs plus an official MCP server for agents.
image: https://startree.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: startree-mcp.yml
  slug: startree-mcpyml
modified: '2026-07-21'
name: StarTree
nav: Providers
network: true
overview: 'StarTree publishes 1 API on the [APIs.io](https://apis.io/) network: Query API API. Tagged areas include Company, Data, Analytics, Real-Time Analytics, and OLAP.


  StarTree''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 54.8
  delta: 0.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 56.8
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Startree Authentication
  slug: startree-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Startree Domain Security
  slug: startree-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Startree Vulnerability Disclosure
  slug: startree-vulnerability-disclosure
  summary_line: disclosure policy published
slug: startree
tags:
- Company
- Data
- Analytics
- Real-Time Analytics
- OLAP
- Apache Pinot
- Streaming
- Database
website: https://startree.ai/
---
