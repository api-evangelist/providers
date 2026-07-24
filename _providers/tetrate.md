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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Tetrate Agentic Access
  operation_count: 39
  slug: tetrate-agentic-access
  summary_line: 39 operations · 22 acting
api_count: 15
apis:
- description: 'The Tetrate Service Bridge (TSB) Platform API provides programmatic management of the TSB control plane, including organizations, tenants, workspaces, and cluster onboarding. It exposes REST and gRPC '
  name: Tetrate Service Bridge Platform API
  slug: tsb-platform-api
- description: The TSB Gateway API manages ingress and egress gateway configuration for services in a Tetrate Service Bridge environment. It provides resources for defining gateway groups, IngressGateway, EgressGate
  name: Tetrate Service Bridge Gateway API
  slug: tsb-gateway-api
- description: The TSB Traffic API provides configuration resources for managing service-to-service traffic within a Tetrate Service Bridge workspace. It supports traffic groups, TrafficSetting, and ServiceRoute obj
  name: Tetrate Service Bridge Traffic API
  slug: tsb-traffic-api
- description: 'The TSB Security API provides configuration resources for enforcing security policies in a Tetrate Service Bridge environment. It includes security groups, SecuritySetting, and ServiceSecuritySetting '
  name: Tetrate Service Bridge Security API
  slug: tsb-security-api
- description: The TSB Observability API exposes metrics, topology, and service observability data for workloads managed by Tetrate Service Bridge. It provides access to service-level metrics, traffic telemetry, and
  name: Tetrate Service Bridge Observability API
  slug: tsb-observability-api
- description: Manage API objects within applications
  name: Tetrate APIs API
  slug: tetrate-apis-api
- description: Manage application objects
  name: Tetrate Applications API
  slug: tetrate-applications-api
- description: Manage onboarded Kubernetes clusters
  name: Tetrate Clusters API
  slug: tetrate-clusters-api
- description: Manage gateway groups and ingress/egress gateways
  name: Tetrate Gateway Groups API
  slug: tetrate-gateway-groups-api
- description: Manage TSB organizations
  name: Tetrate Organizations API
  slug: tetrate-organizations-api
- description: Manage roles, bindings, and access policies
  name: Tetrate RBAC API
  slug: tetrate-rbac-api
- description: Manage security settings and policies
  name: Tetrate Security Groups API
  slug: tetrate-security-groups-api
- description: Manage tenants within organizations
  name: Tetrate Tenants API
  slug: tetrate-tenants-api
- description: Manage traffic settings and service routes
  name: Tetrate Traffic Groups API
  slug: tetrate-traffic-groups-api
- description: Manage workspaces within tenants
  name: Tetrate Workspaces API
  slug: tetrate-workspaces-api
artifact_total: 56
collections:
- collection_type: open
  name: Tetrate Service Bridge REST API
  slug: open-tetrate-service-bridge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tetrate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tetrate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tetrate-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tetrate
- group: company
  title: ''
  type: Website
  url: https://tetrate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tetrate.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tetrate.io/service-bridge/latest/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://tetrate.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tetrateio
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tetrateio/tetrate
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tetrate.io/service-bridge/latest/release-notes/
- group: operate
  title: ''
  type: Support
  url: https://tetrate.io/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://tetrate.io/tetrate-service-bridge/
- group: operate
  title: ''
  type: Community
  url: https://tetrate.io/community/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/tetrate-service-bridge-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tsb-resource-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tsb-resource-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tetrate-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tetrate-vocabulary.yml
created: '2026-03-16'
description: Tetrate is an enterprise service mesh company that provides Tetrate Service Bridge (TSB), a multi-cluster, multi-cloud service mesh management platform built on Istio and Envoy Proxy. Tetrate offers management APIs for traffic, security, and observability across distributed microservice environments, as well as Tetrate Istio Distro (TID), a vetted upstream Istio distribution with FIPS-verified builds. TSB exposes a REST management plane API for programmatic control of organizations, tenants, workspaces, clusters, applications, gateways, traffic routing, and security policies.
examples:
- key_count: 2
  name: Tetrate Service Bridge Create Api Example
  slug: tetrate-service-bridge-create-api-example
- key_count: 2
  name: Tetrate Service Bridge Create Workspace Example
  slug: tetrate-service-bridge-create-workspace-example
- key_count: 2
  name: Tetrate Service Bridge List Tenants Example
  slug: tetrate-service-bridge-list-tenants-example
finops:
- name: Tetrate Finops
  service_category: AI Gateway / Governance
  slug: tetrate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tetrate.png
json_schemas:
- name: API
  property_count: 1
  slug: tetrate-api
- name: APIList
  property_count: 1
  slug: tetrate-apilist
- name: Application
  property_count: 1
  slug: tetrate-application
- name: ApplicationList
  property_count: 1
  slug: tetrate-applicationlist
- name: Cluster
  property_count: 1
  slug: tetrate-cluster
- name: ClusterList
  property_count: 1
  slug: tetrate-clusterlist
- name: Error
  property_count: 3
  slug: tetrate-error
- name: GatewayGroup
  property_count: 1
  slug: tetrate-gatewaygroup
- name: GatewayGroupList
  property_count: 1
  slug: tetrate-gatewaygrouplist
- name: HTTPEndpoint
  property_count: 3
  slug: tetrate-httpendpoint
- name: Organization
  property_count: 1
  slug: tetrate-organization
- name: OrganizationList
  property_count: 1
  slug: tetrate-organizationlist
- name: ResourceMeta
  property_count: 7
  slug: tetrate-resourcemeta
- name: Role
  property_count: 5
  slug: tetrate-role
- name: RoleList
  property_count: 1
  slug: tetrate-rolelist
- name: SecurityGroup
  property_count: 1
  slug: tetrate-securitygroup
- name: SecurityGroupList
  property_count: 1
  slug: tetrate-securitygrouplist
- name: Tenant
  property_count: 1
  slug: tetrate-tenant
- name: TenantList
  property_count: 1
  slug: tetrate-tenantlist
- name: TrafficGroup
  property_count: 1
  slug: tetrate-trafficgroup
- name: TrafficGroupList
  property_count: 1
  slug: tetrate-trafficgrouplist
- name: User
  property_count: 4
  slug: tetrate-user
- name: UserList
  property_count: 1
  slug: tetrate-userlist
- name: Workspace
  property_count: 1
  slug: tetrate-workspace
- name: WorkspaceList
  property_count: 1
  slug: tetrate-workspacelist
- name: TSB Resource
  property_count: 7
  slug: tsb-resource
json_structures:
- name: Tetrate Structure
  property_count: 0
  slug: tetrate-structure
- name: Tsb Resource Structure
  property_count: 0
  slug: tsb-resource-structure
jsonld:
- class_count: 10
  name: Tetrate Context
  property_count: 12
  slug: tetrate-context
layout: provider
modified: '2026-05-19'
name: Tetrate
nav: Providers
network: true
overview: 'Tetrate publishes 10 APIs on the [APIs.io](https://apis.io/) network, including APIs API, Applications API, Clusters API, and 7 more. Tagged areas include Enterprise, Envoy, Istio, Kubernetes, and Service Mesh.


  The Tetrate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tetrate''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, support, pricing, and 12 more developer resources.'
plans:
- name: Tetrate Plans Pricing
  plan_count: 2
  slug: tetrate-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 2
  name: Tetrate Rate Limits
  slug: tetrate-rate-limits
rules:
- name: Tetrate API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tetrate-jsonschema-spectral-rules
- name: Tetrate API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: tetrate-service-bridge-rules
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.0
    developer_ergonomics: 37.0
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 42.1
  previous_composite: 54.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tetrate/refs/heads/main/screenshots/tetrate-2026-06-20T195201.png
security:
- kind: authentication
  name: Tetrate Authentication
  slug: tetrate-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tetrate Domain Security
  slug: tetrate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tetrate
tags:
- Enterprise
- Envoy
- Istio
- Kubernetes
- Service Mesh
website: https://tetrate.io/
---
