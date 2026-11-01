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
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Service Fabric Agentic Access
  operation_count: 9
  slug: service-fabric-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- description: Service Fabric SDK provides client libraries for .NET, Java, and Go for building Service Fabric services and interacting with the cluster. The SDK includes Reliable Collections, Reliable Actors, and t
  name: Service Fabric SDK
  slug: service-fabric-sdk
- baseURL: http://{cluster-endpoint}:19080
  baseurl_source: declared
  description: Application deployment and lifecycle
  name: Service Fabric Applications API
  slug: service-fabric-applications-api
- baseURL: http://{cluster-endpoint}:19080
  baseurl_source: declared
  description: Cluster-level operations and configuration
  name: Service Fabric Cluster API
  slug: service-fabric-cluster-api
- baseURL: http://{cluster-endpoint}:19080
  baseurl_source: declared
  description: Health state queries and reporting
  name: Service Fabric Health API
  slug: service-fabric-health-api
- baseURL: http://{cluster-endpoint}:19080
  baseurl_source: declared
  description: Cluster node management
  name: Service Fabric Nodes API
  slug: service-fabric-nodes-api
- baseURL: http://{cluster-endpoint}:19080
  baseurl_source: declared
  description: Service management within applications
  name: Service Fabric Services API
  slug: service-fabric-services-api
artifact_total: 25
collections:
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
- group: commercial
  href: https://artifacts.apis.io/service-fabric/plans/service-fabric-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/service-fabric-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/service-fabric/rate-limits/service-fabric-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/service-fabric-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/service-fabric/finops/service-fabric-finops.yml
  title: ''
  type: FinOps
  url: finops/service-fabric-finops.yml
- group: other
  href: https://artifacts.apis.io/service-fabric/capabilities/service-fabric-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/service-fabric-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/service-fabric/agentic-access/service-fabric-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/service-fabric-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/service-fabric/security/service-fabric-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/service-fabric-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/service-fabric/security/service-fabric-domain-security.yml
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
  href: https://artifacts.apis.io/service-fabric/json-schema/service-fabric-application-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/service-fabric-application-schema.json
- group: design
  href: https://artifacts.apis.io/service-fabric/json-structure/service-fabric-application-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/service-fabric-application-structure.json
- group: design
  href: https://artifacts.apis.io/service-fabric/json-ld/service-fabric-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/service-fabric-context.jsonld
- group: build
  href: https://artifacts.apis.io/service-fabric/examples/service-fabric-create-application-example.json
  title: ''
  type: Examples
  url: examples/service-fabric-create-application-example.json
- group: build
  href: https://artifacts.apis.io/service-fabric/examples/service-fabric-get-cluster-health-example.json
  title: ''
  type: Examples
  url: examples/service-fabric-get-cluster-health-example.json
- group: design
  href: https://artifacts.apis.io/service-fabric/vocabulary/service-fabric-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/service-fabric-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/service-fabric/rules/service-fabric-rules.yml
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
- has_sources: false
  method: generated
  name: Service Fabric Finops
  primary_unit: request
  service_category: API
  slug: service-fabric-finops
  template: true
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
overview: 'Service Fabric publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Cluster API, Health API, and 3 more. Tagged areas include Distributed Systems, Microservices, Containers, Cloud-Native, and Kubernetes.


  The Service Fabric catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Service Fabric''s developer surface includes GitHub presence, documentation, getting-started guide, changelog, code examples, and 16 more developer resources.'
plans:
- name: Service Fabric Plans Pricing
  plan_count: 3
  slug: service-fabric-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Service Fabric Rate Limits
  slug: service-fabric-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Service Fabric — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: service-fabric-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 49
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
  composite: 36.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.4
    catalog_earned_first_party: 0.0
    catalog_gap: 54.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 27.3
    contract_quality: 57.6
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 39.5
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/service-fabric/service-fabric-2026-06-20T193724.png
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
- Cloud-Native
- Kubernetes
- Microsoft Azure
- Open Source
website: https://docs.microsoft.com/en-us/azure/service-fabric/
---
