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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Cloudera Agentic Access
  operation_count: 11
  slug: cloudera-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 12
apis:
- description: The Cloudera CDP Public Cloud Control Plane REST API manages CDP environments, datalakes, data hubs, machine learning workspaces, data warehouses and data engineering services. Access requires a Cloud
  name: Cloudera CDP Public Cloud Control Plane API
  slug: cdp-control-plane
- description: Cloudera Manager exposes a JSON REST API at /api/v{N} for managing clusters, services, roles, configurations, hosts, parcels, tags and audits. Authentication uses HTTP basic auth with the same credent
  name: Cloudera Manager API
  slug: manager
- description: Cruise Control on CDP exposes REST endpoints for rebalancing Kafka clusters, monitoring partition load, and triggering anomaly checks.
  name: Cloudera Cruise Control REST API
  slug: cruise-control
- description: Streams Replication Manager (SRM) exposes a REST API for inspecting cross-cluster Kafka replication topology, lag, and metrics.
  name: Streams Replication Manager Service REST API
  slug: srm
- description: The HBase REST Server provides a REST front-end to HBase tables for get/put/scan/delete, namespace and table management - installable via Cloudera Manager.
  name: HBase REST Server
  slug: hbase-rest
- description: YARN Queue Manager exposes a REST API for managing capacity scheduler queues, ACLs, and resource allocations on a CDP cluster.
  name: YARN Queue Manager API
  slug: yarn-queue-manager
- description: The DataEngineering API from Cloudera — 1 operation(s) for dataengineering.
  name: Cloudera DataEngineering API
  slug: cloudera-dataengineering-api
- description: The Datahub API from Cloudera — 2 operation(s) for datahub.
  name: Cloudera Datahub API
  slug: cloudera-datahub-api
- description: The Datalake API from Cloudera — 2 operation(s) for datalake.
  name: Cloudera Datalake API
  slug: cloudera-datalake-api
- description: The Environments API from Cloudera — 3 operation(s) for environments.
  name: Cloudera Environments API
  slug: cloudera-environments-api
- description: The IAM API from Cloudera — 2 operation(s) for iam.
  name: Cloudera IAM API
  slug: cloudera-iam-api
- description: The ML API from Cloudera — 1 operation(s) for ml.
  name: Cloudera ML API
  slug: cloudera-ml-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloudera CDP Public Cloud Control Plane DataEngineering API
  slug: open-cloudera-dataengineering-api
- collection_type: open
  name: Cloudera CDP Public Cloud Control Plane DataEngineering Datahub API
  slug: open-cloudera-datahub-api
- collection_type: open
  name: Cloudera CDP Public Cloud Control Plane DataEngineering Datalake API
  slug: open-cloudera-datalake-api
- collection_type: open
  name: Cloudera CDP Public Cloud Control Plane DataEngineering Environments API
  slug: open-cloudera-environments-api
- collection_type: open
  name: Cloudera CDP Public Cloud Control Plane DataEngineering IAM API
  slug: open-cloudera-iam-api
- collection_type: open
  name: Cloudera CDP Public Cloud Control Plane DataEngineering ML API
  slug: open-cloudera-ml-api
- collection_type: open
  name: Cloudera CDP Public Cloud Control Plane API
  slug: open-cloudera
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudera-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudera-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudera-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudera-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudera
- group: company
  title: ''
  type: Website
  url: https://www.cloudera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudera.com/
- group: operate
  title: ''
  type: Support
  url: https://my.cloudera.com/knowledge.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudera.com/legal/privacy.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudera
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudera-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudera-rules.yml
created: '2024-01-01'
description: Cloudera is a hybrid data platform company offering the Cloudera Data Platform (CDP) for data engineering, data warehousing, machine learning, streaming, and operational data. The platform exposes multiple REST APIs including the CDP Public Cloud Control Plane API for managing environments, datalakes, data hubs and workloads, the Cloudera Manager API for cluster lifecycle and configuration management, and per-service REST APIs across the runtime (Cruise Control, Streams Replication Manager, HBase REST, YARN Queue Manager, etc.). APIs are JSON, support standard CRUD, and are typically authenticated via API access keys, basic auth, or session cookies.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudera.png
jsonld:
- class_count: 0
  name: Cloudera Context
  property_count: 7
  slug: cloudera-context
layout: provider
modified: '2026-04-25'
name: Cloudera
nav: Providers
network: true
overview: 'Cloudera publishes 6 APIs on the [APIs.io](https://apis.io/) network, including DataEngineering API, Datahub API, Datalake API, and 3 more. Tagged areas include Big Data, Data Engineering, Data Lakehouse, Data Platform, and Data Warehouse.


  The Cloudera catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudera''s developer surface includes authentication, documentation, support, GitHub presence, and 8 more developer resources.'
random_paper: 7
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Cloudera API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: cloudera-rules
score:
  band: thin
  composite: 35.3
  delta: 2.9
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 45.5
    contract_quality: 53.7
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 45.5
    operational_transparency: 5.3
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudera/refs/heads/main/screenshots/cloudera-2026-06-20T174548.png
security:
- kind: authentication
  name: Cloudera Authentication
  slug: cloudera-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudera Domain Security
  slug: cloudera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloudera Trust Center
  slug: cloudera-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cloudera
tags:
- Big Data
- Data Engineering
- Data Lakehouse
- Data Platform
- Data Warehouse
- Hadoop
- Hybrid Cloud
- Machine-Learning
- Streaming
website: https://www.cloudera.com/
---
