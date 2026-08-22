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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Service Fabric Agentic Access
  operation_count: 9
  slug: service-fabric-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 6
apis:
- description: Service Fabric SDK provides client libraries for .NET, Java, and Go for building Service Fabric services and interacting with the cluster. The SDK includes Reliable Collections, Reliable Actors, and t
  name: Service Fabric SDK
  slug: service-fabric-sdk
- description: Application deployment and lifecycle
  name: Service Fabric Applications API
  slug: service-fabric-applications-api
- description: Cluster-level operations and configuration
  name: Service Fabric Cluster API
  slug: service-fabric-cluster-api
- description: Health state queries and reporting
  name: Service Fabric Health API
  slug: service-fabric-health-api
- description: Cluster node management
  name: Service Fabric Nodes API
  slug: service-fabric-nodes-api
- description: Service management within applications
  name: Service Fabric Services API
  slug: service-fabric-services-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Service Fabric Cluster Management Applications API
  slug: open-service-fabric-applications-api
- collection_type: open
  name: Service Fabric Management Applications Cluster API
  slug: open-service-fabric-cluster-api
- collection_type: open
  name: Service Fabric Cluster Management API
  slug: open-service-fabric-cluster
- collection_type: open
  name: Service Fabric Cluster Management Applications Health API
  slug: open-service-fabric-health-api
- collection_type: open
  name: Service Fabric Cluster Management Applications Nodes API
  slug: open-service-fabric-nodes-api
- collection_type: open
  name: Service Fabric Cluster Management Applications Services API
  slug: open-service-fabric-services-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/service-fabric-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/service-fabric-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/service-fabric-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.microsoft.com/en-us/azure/service-fabric/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/microsoft/service-fabric
- group: docs
  title: ''
  type: Documentation
  url: https://docs.microsoft.com/en-us/azure/service-fabric/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started
- group: docs
  title: ''
  type: Reference
  url: https://docs.microsoft.com/en-us/rest/api/servicefabric/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/microsoft/service-fabric/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/service-fabric/blob/master/LICENSE
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/service-fabric-application-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/service-fabric-application-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/service-fabric-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/service-fabric-create-application-example.json
- group: build
  title: ''
  type: Examples
  url: examples/service-fabric-get-cluster-health-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/service-fabric-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/service-fabric-rules.yml
created: '2026-05-02'
description: Azure Service Fabric is an open-source distributed systems platform for packaging, deploying, and managing scalable and reliable microservices and containers. Service Fabric powers many Microsoft Azure core services, and thousands of services at scale including Azure SQL Database, Azure Cosmos DB, Skype for Business, and Cortana. Service Fabric provides a programming model for building stateful and stateless microservices, reliable collections, and actor-based services. The Service Fabric REST API enables cluster management, application lifecycle, and service configuration.
examples:
- key_count: 3
  name: Service Fabric Create Application Example
  slug: service-fabric-create-application-example
- key_count: 2
  name: Service Fabric Get Cluster Health Example
  slug: service-fabric-get-cluster-health-example
finops:
- name: Service Fabric Finops
  service_category: API
  slug: service-fabric-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/service-fabric.png
json_schemas:
- name: Service Fabric Application
  property_count: 8
  slug: service-fabric-application
json_structures:
- name: Service Fabric Application Structure
  property_count: 0
  slug: service-fabric-application-structure
jsonld:
- class_count: 21
  name: Service Fabric Context
  property_count: 3
  slug: service-fabric-context
layout: provider
modified: '2026-05-19'
name: Service Fabric
nav: Providers
network: true
overview: 'Service Fabric publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Cluster API, Health API, and 2 more. Tagged areas include Distributed Systems, Microservices, Containers, Cloud Native, and Kubernetes.


  The Service Fabric catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Service Fabric''s developer surface includes GitHub presence, documentation, getting-started guide, changelog, code examples, and 12 more developer resources.'
plans:
- name: Service Fabric Plans Pricing
  plan_count: 3
  slug: service-fabric-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Service Fabric Rate Limits
  slug: service-fabric-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Service Fabric API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: service-fabric-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Service Fabric API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: service-fabric-rules
score:
  band: thin
  composite: 37.6
  delta: -5.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 62.1
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 28.9
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/service-fabric/refs/heads/main/screenshots/service-fabric-2026-06-20T193724.png
security:
- kind: domain-security
  name: Service Fabric Domain Security
  slug: service-fabric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Service Fabric Vulnerability Disclosure
  slug: service-fabric-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: service-fabric
tags:
- Distributed Systems
- Microservices
- Containers
- Cloud Native
- Kubernetes
- Azure
- Open Source
website: https://docs.microsoft.com/en-us/azure/service-fabric/
---
