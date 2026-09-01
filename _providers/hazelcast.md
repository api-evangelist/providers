---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Hazelcast Agentic Access
  operation_count: 19
  slug: hazelcast-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- description: Cluster information and management endpoints.
  name: Hazelcast Cluster API
  slug: hazelcast-cluster-api
- description: Runtime configuration management.
  name: Hazelcast Configuration API
  slug: hazelcast-configuration-api
- description: Liveness and readiness checks.
  name: Hazelcast Health API
  slug: hazelcast-health-api
- description: Distributed map operations under /hazelcast/rest/maps.
  name: Hazelcast Maps API
  slug: hazelcast-maps-api
- description: Distributed queue operations under /hazelcast/rest/queues.
  name: Hazelcast Queues API
  slug: hazelcast-queues-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hazelcast REST Cluster API
  slug: open-hazelcast-cluster-api
- collection_type: open
  name: Hazelcast REST Cluster Configuration API
  slug: open-hazelcast-configuration-api
- collection_type: open
  name: Hazelcast REST Cluster Health API
  slug: open-hazelcast-health-api
- collection_type: open
  name: Hazelcast REST Cluster Maps API
  slug: open-hazelcast-maps-api
- collection_type: open
  name: Hazelcast REST Cluster Queues API
  slug: open-hazelcast-queues-api
- collection_type: open
  name: Hazelcast REST API
  slug: open-hazelcast
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hazelcast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hazelcast-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hazelcast
- group: company
  title: ''
  type: Website
  url: https://hazelcast.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hazelcast.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hazelcast.com/hazelcast/latest/getting-started/get-started-docker
- group: operate
  title: ''
  type: Support
  url: https://hazelcast.com/support/
- group: company
  title: ''
  type: Blog
  url: https://hazelcast.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hazelcast
- group: operate
  title: ''
  type: Community
  url: https://slack.hazelcast.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.hazelcast.com/llms.txt
created: '2025-08-19'
description: Hazelcast is a real-time data platform that helps businesses accelerate their applications with data caching, data integration, and distributed computing. Hazelcast provides in-memory computing capabilities for high-performance, low-latency applications, exposing a REST API for managing maps, queues, cluster state, configuration, and health.
finops:
- name: Hazelcast Finops
  service_category: API
  slug: hazelcast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hazelcast.png
layout: provider
modified: '2026-05-19'
name: Hazelcast
nav: Providers
network: true
overview: 'Hazelcast publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Configuration API, Health API, and 2 more. Tagged areas include Data Caching, Distributed Computing, In-Memory Computing, Real-Time, and REST.


  Hazelcast''s developer surface includes documentation, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Hazelcast Plans Pricing
  plan_count: 3
  slug: hazelcast-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Hazelcast Rate Limits
  slug: hazelcast-rate-limits
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 40.8
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hazelcast/refs/heads/main/screenshots/hazelcast-2026-06-20T182545.png
security:
- kind: domain-security
  name: Hazelcast Domain Security
  slug: hazelcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hazelcast
tags:
- Data Caching
- Distributed Computing
- In-Memory Computing
- Real-Time
- REST
website: https://hazelcast.com/
---
