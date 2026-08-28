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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Temporal Io Agentic Access
  operation_count: 17
  slug: temporal-io-agentic-access
  summary_line: 17 operations · 7 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: The gRPC OperatorService for cluster-level administration - managing custom search attributes (add/remove/list), Nexus endpoints (create/get/update/ delete/list), remote clusters, and namespace deleti
  name: Temporal Operator Service API
  slug: temporal-io-operator-service-api
- description: 'The Temporal Cloud control-plane API (CloudService) for programmatically managing Temporal Cloud resources - namespaces, users, service accounts, API keys, regions, account settings, Nexus endpoints, '
  name: Temporal Cloud Operations API
  slug: temporal-io-cloud-operations-api
- description: Temporal Nexus connects Temporal applications across namespaces and teams via named Nexus endpoints backed by synchronous and asynchronous Nexus operations. Endpoints are registered through the Operat
  name: Temporal Nexus API
  slug: temporal-io-nexus-api
- description: Cluster and system information.
  name: Temporal Cluster API
  slug: temporal-io-cluster-api
- description: Read namespace metadata (read-only subset over HTTP).
  name: Temporal Namespaces API
  slug: temporal-io-namespaces-api
- description: Cancel, terminate, and reset workflow executions.
  name: Temporal Workflow Lifecycle API
  slug: temporal-io-workflow-lifecycle-api
- description: Signal, query, and update running workflow executions.
  name: Temporal Workflow Messaging API
  slug: temporal-io-workflow-messaging-api
- description: Start, describe, list, count, and read the history of workflow executions.
  name: Temporal Workflows API
  slug: temporal-io-workflows-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Temporal HTTP Cluster API
  slug: open-temporal-io-cluster-api
- collection_type: open
  name: Temporal HTTP Cluster Namespaces API
  slug: open-temporal-io-namespaces-api
- collection_type: open
  name: Temporal HTTP Cluster Workflow Lifecycle API
  slug: open-temporal-io-workflow-lifecycle-api
- collection_type: open
  name: Temporal HTTP Cluster Workflow Messaging API
  slug: open-temporal-io-workflow-messaging-api
- collection_type: open
  name: Temporal HTTP Cluster Workflows API
  slug: open-temporal-io-workflows-api
- collection_type: open
  name: Temporal HTTP API
  slug: open-temporal-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/temporal-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/temporal-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/temporal-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/temporal-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/temporal-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/temporalio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/temporal-technologies
- group: company
  title: ''
  type: Website
  url: https://temporal.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.temporal.io
- group: commercial
  title: ''
  type: Plans
  url: plans/temporal-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/temporal-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/temporal-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://temporal.io/blog/feed.xml
created: '2026-07-02'
description: 'Temporal is a durable execution platform for orchestrating long-running, fault-tolerant workflows. Its primary API surface is gRPC - the WorkflowService, OperatorService, and (on Temporal Cloud) the Cloud Operations API are defined as protobuf in github.com/temporalio/api and github.com/temporalio/cloud-api. Temporal also ships a first-party HTTP API: a grpc-gateway that maps a REST/JSON subset of the WorkflowService onto paths under /api/v1, for automation and environments where gRPC is impractical. Temporal is open source (MIT) and self-hostable, and is also available as the managed Temporal Cloud.'
finops:
- name: Temporal Io Finops
  service_category: Compute and Workflow Orchestration
  slug: temporal-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/temporal-io.png
layout: provider
modified: '2026-07-02'
name: Temporal
nav: Providers
network: true
overview: 'Temporal publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Namespaces API, Workflow Lifecycle API, and 2 more. Tagged areas include Durable Execution, Workflow Orchestration, gRPC, Workflows, and Open-Source.


  Temporal''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Temporal Io Plans Pricing
  plan_count: 5
  slug: temporal-io-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Temporal Io Rate Limits
  slug: temporal-io-rate-limits
score:
  band: developing
  composite: 40.7
  delta: 1.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 54.6
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Temporal Io Authentication
  slug: temporal-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Temporal Io Domain Security
  slug: temporal-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Temporal Io Vulnerability Disclosure
  slug: temporal-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Temporal Io Trust Center
  slug: temporal-io-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: temporal-io
tags:
- Durable Execution
- Workflow Orchestration
- gRPC
- Workflows
- Open-Source
- Temporal Cloud
website: https://temporal.io/
---
