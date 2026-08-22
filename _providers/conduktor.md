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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Conduktor Agentic Access
  operation_count: 22
  slug: conduktor-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 7
apis:
- description: Manage cluster certificates in Console
  name: Conduktor Certificates API
  slug: conduktor-certificates-api
- description: Manage Kafka cluster registrations in Console
  name: Conduktor Clusters API
  slug: conduktor-clusters-api
- description: Manage groups and RBAC permissions in Console
  name: Conduktor Groups API
  slug: conduktor-groups-api
- description: Gateway interceptors for data security, quality, and governance
  name: Conduktor Interceptors API
  slug: conduktor-interceptors-api
- description: Declarative Application, ApplicationInstance, and TopicPolicy resources
  name: Conduktor Self-Service API
  slug: conduktor-self-service-api
- description: Manage organization users in Console
  name: Conduktor Users API
  slug: conduktor-users-api
- description: Gateway virtual clusters, service accounts, and tokens
  name: Conduktor Virtual Clusters API
  slug: conduktor-virtual-clusters-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Conduktor Certificates API
  slug: open-conduktor-certificates-api
- collection_type: open
  name: Conduktor Certificates Clusters API
  slug: open-conduktor-clusters-api
- collection_type: open
  name: Conduktor Certificates Groups API
  slug: open-conduktor-groups-api
- collection_type: open
  name: Conduktor Certificates Interceptors API
  slug: open-conduktor-interceptors-api
- collection_type: open
  name: Conduktor Certificates Self-Service API
  slug: open-conduktor-self-service-api
- collection_type: open
  name: Conduktor Certificates Users API
  slug: open-conduktor-users-api
- collection_type: open
  name: Conduktor Certificates Virtual Clusters API
  slug: open-conduktor-virtual-clusters-api
- collection_type: open
  name: Conduktor API
  slug: open-conduktor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/conduktor-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/conduktor-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/conduktor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conduktor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/conduktor-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conduktor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conduktor
- group: company
  title: ''
  type: Website
  url: https://www.conduktor.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conduktor.io
- group: commercial
  title: ''
  type: Plans
  url: plans/conduktor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conduktor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/conduktor-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.conduktor.io/blog/feed.xml
created: '2026-06-21'
description: Conduktor is an Apache Kafka management and data-governance platform. Conduktor Console provides a REST API and CLI to manage clusters, topics, consumer groups, certificates, users, groups, and granular RBAC, plus declarative Self-Service resources (Application, ApplicationInstance, TopicPolicy). Conduktor Gateway is a Kafka proxy with a REST API for interceptors (data security, quality, governance) and virtual clusters.
finops:
- name: Conduktor Finops
  service_category: Analytics and Data Management
  slug: conduktor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conduktor.png
layout: provider
modified: '2026-06-21'
name: Conduktor
nav: Providers
network: true
overview: 'Conduktor publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Clusters API, Groups API, and 4 more. Tagged areas include Apache Kafka, Streaming, Data Governance, Kafka Management, and Gateway.


  Conduktor''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Conduktor Plans Pricing
  plan_count: 5
  slug: conduktor-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Conduktor Rate Limits
  slug: conduktor-rate-limits
score:
  band: thin
  composite: 37.8
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 47.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conduktor/refs/heads/main/screenshots/conduktor-2026-07-25T210238.png
security:
- kind: authentication
  name: Conduktor Authentication
  slug: conduktor-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Conduktor Domain Security
  slug: conduktor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Conduktor Vulnerability Disclosure
  slug: conduktor-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Conduktor Trust Center
  slug: conduktor-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: conduktor
tags:
- Apache Kafka
- Streaming
- Data Governance
- Kafka Management
- Gateway
website: https://www.conduktor.io
---
