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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Decodable Agentic Access
  operation_count: 26
  slug: decodable-agentic-access
  summary_line: 26 operations · 17 acting
api_count: 1
apis:
- description: Source and sink connectors between Decodable and external systems.
  name: Decodable Connections API
  slug: decodable-connections-api
- description: SQL or custom Apache Flink transformations over streams.
  name: Decodable Pipelines API
  slug: decodable-pipelines-api
- description: Account-level and control-plane resource endpoints.
  name: Decodable Resources API
  slug: decodable-resources-api
- description: Securely stored credentials referenced by connections.
  name: Decodable Secrets API
  slug: decodable-secrets-api
- description: Typed, schema-bearing channels that carry records.
  name: Decodable Streams API
  slug: decodable-streams-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Decodable Control Plane Connections API
  slug: open-decodable-connections-api
- collection_type: open
  name: Decodable Control Plane Connections Pipelines API
  slug: open-decodable-pipelines-api
- collection_type: open
  name: Decodable Control Plane Connections Resources API
  slug: open-decodable-resources-api
- collection_type: open
  name: Decodable Control Plane Connections Secrets API
  slug: open-decodable-secrets-api
- collection_type: open
  name: Decodable Control Plane Connections Streams API
  slug: open-decodable-streams-api
- collection_type: open
  name: Decodable Control Plane API
  slug: open-decodable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/decodable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/decodable-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/decodable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decodable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/decodable-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.decodable.co/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/decodableco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/decodable
- group: company
  title: ''
  type: Website
  url: https://www.decodable.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.decodable.co
- group: commercial
  title: ''
  type: Plans
  url: plans/decodable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/decodable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/decodable-finops.yml
created: '2026-06-21'
description: Decodable is a fully managed stream-processing platform built on Apache Flink and Debezium. It lets teams build real-time data pipelines by connecting sources and sinks, transforming data with SQL or custom Flink jobs, and managing connections, streams, pipelines, and secrets through a REST API, a CLI, and declarative YAML.
finops:
- name: Decodable Finops
  service_category: Analytics
  slug: decodable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decodable.png
layout: provider
modified: '2026-06-21'
name: Decodable
nav: Providers
network: true
overview: 'Decodable publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Pipelines API, Resources API, and 2 more. Tagged areas include Stream Processing, Apache Flink, Debezium, Real-Time Data, and Data Pipeline.


  Decodable''s developer surface includes authentication, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Decodable Plans Pricing
  plan_count: 3
  slug: decodable-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Decodable Rate Limits
  slug: decodable-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.2
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decodable/refs/heads/main/screenshots/decodable-2026-07-25T211523.png
security:
- kind: authentication
  name: Decodable Authentication
  slug: decodable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Decodable Domain Security
  slug: decodable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Decodable Vulnerability Disclosure
  slug: decodable-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Decodable Trust Center
  slug: decodable-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: decodable
tags:
- Stream Processing
- Apache Flink
- Debezium
- Real-Time Data
- Data Pipeline
- CDC
website: https://www.decodable.co
---
