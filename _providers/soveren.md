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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Soveren Agentic Access
  operation_count: 18
  slug: soveren-agentic-access
  summary_line: 18 operations
api_count: 6
apis:
- description: The Assets API from Soveren — 4 operation(s) for assets.
  name: Soveren Assets API
  slug: soveren-assets-api
- description: The Data Types API from Soveren — 1 operation(s) for data types.
  name: Soveren Data Types API
  slug: soveren-data-types-api
- description: The Endpoints API from Soveren — 2 operation(s) for endpoints.
  name: Soveren Endpoints API
  slug: soveren-endpoints-api
- description: The Kafka API from Soveren — 4 operation(s) for kafka.
  name: Soveren Kafka API
  slug: soveren-kafka-api
- description: The S3 API from Soveren — 2 operation(s) for s3.
  name: Soveren S3 API
  slug: soveren-s3-api
- description: The SQL DB API from Soveren — 5 operation(s) for sql db.
  name: Soveren SQL DB API
  slug: soveren-sql-db-api
artifact_total: 12
asyncapis:
- description: Soveren delivers data-security events to a subscriber endpoint via outbound webhooks. Soveren POSTs an event object to a URL configured in the app under Integrations - Webhook. When a signing token is
  name: Soveren Events (Webhooks)
  slug: soveren-events-asyncapi
- description: ''
  name: Soveren Webhooks
  slug: soveren-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://soveren.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.soveren.io/en/stable/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soveren.io/en/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.soveren.io/en/stable/integration/api/ref/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.soveren.io/en/stable/
- group: company
  title: ''
  type: Blog
  url: https://soveren.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.soveren.io/sign-up
- group: operate
  title: ''
  type: Support
  url: https://soveren.io/get-a-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soveren.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.website-files.com/60ebf6ae3b0fe3c5e739324f/60ebf6ae3b0fe306a53933ce_Soveren_Website_Terms_of_Use_20102020.pdf
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/soveren-object-api-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/soveren-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/soveren-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soveren-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soveren-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/soveren-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/soveren-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soveren-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soveren-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/soveren-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soveren-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soveren-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/soveren-object-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soveren-domain-security.yml
created: '2026-07-17'
description: Soveren is a unified Data Security Posture Management (DSPM) and Data Detection and Response (DDR) platform that delivers real-time data observability for Kubernetes and cloud environments. It combines at-rest data detection with eBPF-based network traffic analysis to discover sensitive assets, map the data flows between services, detect misconfigurations (public or unencrypted S3 buckets, unencrypted RDS/network), and audit compliance posture against PCI DSS, GDPR, and CPRA. Soveren exposes a read-only Object API over the discovered inventory and an outbound webhook event surface for automation. A portfolio company of Northzone.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soveren.png
layout: provider
mcp_servers:
- description: ''
  name: soveren-mcp.yml
  slug: soveren-mcpyml
modified: '2026-07-21'
name: Soveren
nav: Providers
network: true
overview: 'Soveren publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Data Types API, Endpoints API, and 3 more. Tagged areas include Company, Infra Devtools, Data Security, DSPM, and DDR.


  The Soveren catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Soveren''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 50
score:
  band: developing
  composite: 44.7
  delta: -2.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 64.4
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Soveren Authentication
  slug: soveren-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Soveren Domain Security
  slug: soveren-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soveren
tags:
- Company
- Infra Devtools
- Data Security
- DSPM
- DDR
- Data Privacy
- Kubernetes
- Compliance
- Security
website: https://soveren.io
---
