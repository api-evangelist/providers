---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 41
  human_in_the_loop: 1
  name: Eu Sovereign Cloud Api Agentic Access
  operation_count: 89
  slug: eu-sovereign-cloud-api-agentic-access
  summary_line: 89 operations · 41 acting · 1 human-in-the-loop
api_count: 24
apis:
- baseURL: https://demo.secapi.cloud/providers/seca.object-storage
  baseurl_source: spec
  description: Account management
  name: Sovereign European Cloud API (SECA) Account API
  slug: eu-sovereign-cloud-api-account-api
- baseURL: https://demo.secapi.cloud/providers/seca.activity-log
  baseurl_source: spec
  description: Activity Log management
  name: Sovereign European Cloud API (SECA) Activity Log API
  slug: eu-sovereign-cloud-api-activity-log-api
- baseURL: https://demo.secapi.cloud/providers/seca.storage
  baseurl_source: spec
  description: Block-Storage management
  name: Sovereign European Cloud API (SECA) Block Storage API
  slug: eu-sovereign-cloud-api-block-storage-api
- baseURL: https://demo.secapi.cloud/providers/seca.kubernetes
  baseurl_source: spec
  description: Cluster management
  name: Sovereign European Cloud API (SECA) Cluster API
  slug: eu-sovereign-cloud-api-cluster-api
- baseURL: https://demo.secapi.cloud/providers/seca.storage
  baseurl_source: spec
  description: Image management
  name: Sovereign European Cloud API (SECA) Image API
  slug: eu-sovereign-cloud-api-image-api
- baseURL: https://demo.secapi.cloud/providers/seca.compute
  baseurl_source: spec
  description: Instance management
  name: Sovereign European Cloud API (SECA) Instance API
  slug: eu-sovereign-cloud-api-instance-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Internet Gateway management
  name: Sovereign European Cloud API (SECA) Internet Gateway API
  slug: eu-sovereign-cloud-api-internet-gateway-api
- baseURL: https://demo.secapi.cloud/providers/seca.nat-gateway
  baseurl_source: spec
  description: Internet Nat Gateway Instance management
  name: Sovereign European Cloud API (SECA) Internet Nat Gateway Instance API
  slug: eu-sovereign-cloud-api-internet-nat-gateway-instance-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Network management
  name: Sovereign European Cloud API (SECA) Network API
  slug: eu-sovereign-cloud-api-network-api
- baseURL: https://demo.secapi.cloud/providers/seca.load-balancer
  baseurl_source: spec
  description: Network Load Balancer management
  name: Sovereign European Cloud API (SECA) Network Load Balancer API
  slug: eu-sovereign-cloud-api-network-load-balancer-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Nic management
  name: Sovereign European Cloud API (SECA) Nic API
  slug: eu-sovereign-cloud-api-nic-api
- baseURL: https://demo.secapi.cloud/providers/seca.kubernetes
  baseurl_source: spec
  description: Node-Pool management
  name: Sovereign European Cloud API (SECA) Node Pool API
  slug: eu-sovereign-cloud-api-node-pool-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Public Ip management
  name: Sovereign European Cloud API (SECA) Public Ip API
  slug: eu-sovereign-cloud-api-public-ip-api
- baseURL: https://demo.secapi.cloud/providers/seca.region
  baseurl_source: spec
  description: Region management
  name: Sovereign European Cloud API (SECA) Region API
  slug: eu-sovereign-cloud-api-region-api
- baseURL: https://demo.secapi.cloud/providers/seca.authorization
  baseurl_source: spec
  description: Role management
  name: Sovereign European Cloud API (SECA) Role API
  slug: eu-sovereign-cloud-api-role-api
- baseURL: https://demo.secapi.cloud/providers/seca.authorization
  baseurl_source: spec
  description: Role Assignment management
  name: Sovereign European Cloud API (SECA) Role Assignment API
  slug: eu-sovereign-cloud-api-role-assignment-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Route-Table management
  name: Sovereign European Cloud API (SECA) Route Table API
  slug: eu-sovereign-cloud-api-route-table-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Security Group management
  name: Sovereign European Cloud API (SECA) Security Group API
  slug: eu-sovereign-cloud-api-security-group-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Security Group Rule management
  name: Sovereign European Cloud API (SECA) Security Group Rule API
  slug: eu-sovereign-cloud-api-security-group-rule-api
- baseURL: https://demo.secapi.cloud/providers/seca.compute
  baseurl_source: spec
  description: Sku management
  name: Sovereign European Cloud API (SECA) Sku API
  slug: eu-sovereign-cloud-api-sku-api
- baseURL: https://demo.secapi.cloud/providers/seca.network
  baseurl_source: spec
  description: Subnet management
  name: Sovereign European Cloud API (SECA) Subnet API
  slug: eu-sovereign-cloud-api-subnet-api
- baseURL: https://demo.secapi.cloud
  baseurl_source: spec
  description: Wellknown management
  name: Sovereign European Cloud API (SECA) Wellknown API
  slug: eu-sovereign-cloud-api-wellknown-api
- baseURL: https://demo.secapi.cloud/providers/seca.workspace
  baseurl_source: spec
  description: Workspace management
  name: Sovereign European Cloud API (SECA) Workspace API
  slug: eu-sovereign-cloud-api-workspace-api
artifact_total: 66
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/agentic-access/eu-sovereign-cloud-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eu-sovereign-cloud-api-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/rules/eu-sovereign-cloud-api-spec-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/eu-sovereign-cloud-api-spec-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/rules/eu-sovereign-cloud-api-rules.yml
  title: ''
  type: Spectral
  url: rules/eu-sovereign-cloud-api-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/json-ld/eu-sovereign-cloud-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eu-sovereign-cloud-api-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/vocabulary/eu-sovereign-cloud-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eu-sovereign-cloud-api-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/data-model/eu-sovereign-cloud-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eu-sovereign-cloud-api-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/cli/eu-sovereign-cloud-api-cli.yml
  title: ''
  type: CLI
  url: cli/eu-sovereign-cloud-api-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/changelog/eu-sovereign-cloud-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/eu-sovereign-cloud-api-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/conventions/eu-sovereign-cloud-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/eu-sovereign-cloud-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/conventions/eu-sovereign-cloud-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eu-sovereign-cloud-api-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/lifecycle/eu-sovereign-cloud-api-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/eu-sovereign-cloud-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/lifecycle/eu-sovereign-cloud-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/eu-sovereign-cloud-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/errors/eu-sovereign-cloud-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eu-sovereign-cloud-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/conformance/eu-sovereign-cloud-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eu-sovereign-cloud-api-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/overlays/eu-sovereign-cloud-api-extensions-activitylog-v1beta1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eu-sovereign-cloud-api-extensions-activitylog-v1beta1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/hosts/eu-sovereign-cloud-api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eu-sovereign-cloud-api-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/vendors/eu-sovereign-cloud-api-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eu-sovereign-cloud-api-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/packages/eu-sovereign-cloud-api-packages.yml
  title: ''
  type: SDKs
  url: packages/eu-sovereign-cloud-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/packages/eu-sovereign-cloud-api-packages.yml
  title: ''
  type: Packages
  url: packages/eu-sovereign-cloud-api-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/security/eu-sovereign-cloud-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eu-sovereign-cloud-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/authentication/eu-sovereign-cloud-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eu-sovereign-cloud-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.secapi.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://spec.secapi.cloud/docs/content/intro
- group: docs
  title: ''
  type: APIReference
  url: https://spec.secapi.cloud/docs/api/Foundation/Authorization-v1/authorization
- group: start
  title: ''
  type: GettingStarted
  url: https://spec.secapi.cloud/docs/content/Examples/usage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eu-sovereign-cloud
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/eu-sovereign-cloud/spec
- group: operate
  title: ''
  type: Support
  url: https://github.com/eu-sovereign-cloud/spec/blob/main/CHAT.md
- group: other
  title: ''
  type: Contributing
  url: https://github.com/eu-sovereign-cloud/spec/blob/main/CONTRIBUTING.md
- group: other
  title: ''
  type: Email
  url: mailto:info@secapi.cloud
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/eu-sovereign-cloud/spec/blob/223b40530a7dc57def8ce373a0e14de577fc3d40/config/vacuum/ruleset.yaml
created: '2026-10-09'
description: SECA (Sovereign European Cloud API) is an open industry standard API specification for cloud infrastructure management, introduced as a collaboration by the European cloud service providers Aruba, IONOS and Dynamo. Built on OpenAPI, it aims to enable sovereign multi-cloud deployment of workloads across European public Infrastructure-as-a-Service providers, ensuring interoperability, data sovereignty and freedom from vendor lock-in as a building block for the EuroStack. The specification and its tooling are developed openly in the eu-sovereign-cloud GitHub organization and documented at spec.secapi.cloud.
image: https://www.secapi.cloud/wp-content/uploads/2025/03/Seca-share.png
json_schemas:
- name: AccountIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-account-iterator
- name: ActivityLogIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-activity-log-iterator
- name: Block-StorageIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-block-storage-iterator
- name: BlockStorage
  property_count: 0
  slug: eu-sovereign-cloud-api-block-storage
- name: ClusterIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-cluster-iterator
- name: ImageIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-image-iterator
- name: Image
  property_count: 0
  slug: eu-sovereign-cloud-api-image
- name: InstanceIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-instance-iterator
- name: Instance
  property_count: 0
  slug: eu-sovereign-cloud-api-instance
- name: InstanceSku
  property_count: 0
  slug: eu-sovereign-cloud-api-instance-sku
- name: InternetGateway
  property_count: 0
  slug: eu-sovereign-cloud-api-internet-gateway
- name: InternetNatGatewayInstanceIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-internet-nat-gateway-instance-iterator
- name: InternetNatGatewayInstance
  property_count: 0
  slug: eu-sovereign-cloud-api-internet-nat-gateway-instance
- name: KubernetesCluster
  property_count: 0
  slug: eu-sovereign-cloud-api-kubernetes-cluster
- name: KubernetesNodePool
  property_count: 0
  slug: eu-sovereign-cloud-api-kubernetes-node-pool
- name: NetworkLoadBalancerIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-network-load-balancer-iterator
- name: NetworkLoadBalancer
  property_count: 0
  slug: eu-sovereign-cloud-api-network-load-balancer
- name: Network
  property_count: 0
  slug: eu-sovereign-cloud-api-network
- name: Nic
  property_count: 0
  slug: eu-sovereign-cloud-api-nic
- name: Node-PoolIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-node-pool-iterator
- name: ObjectStorageAccount
  property_count: 0
  slug: eu-sovereign-cloud-api-object-storage-account
- name: RegionIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-region-iterator
- name: Region
  property_count: 2
  slug: eu-sovereign-cloud-api-region
- name: RoleAssignmentIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-role-assignment-iterator
- name: RoleAssignment
  property_count: 0
  slug: eu-sovereign-cloud-api-role-assignment
- name: RoleIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-role-iterator
- name: Role
  property_count: 0
  slug: eu-sovereign-cloud-api-role
- name: SecurityGroupRule
  property_count: 0
  slug: eu-sovereign-cloud-api-security-group-rule
- name: SecurityGroup
  property_count: 0
  slug: eu-sovereign-cloud-api-security-group
- name: SkuIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-sku-iterator
- name: StorageSku
  property_count: 0
  slug: eu-sovereign-cloud-api-storage-sku
- name: Subnet
  property_count: 0
  slug: eu-sovereign-cloud-api-subnet
- name: Wellknown
  property_count: 2
  slug: eu-sovereign-cloud-api-wellknown
- name: WorkspaceIterator
  property_count: 2
  slug: eu-sovereign-cloud-api-workspace-iterator
- name: Workspace
  property_count: 0
  slug: eu-sovereign-cloud-api-workspace
jsonld:
- class_count: 82
  name: Eu Sovereign Cloud Api Context
  property_count: 127
  slug: eu-sovereign-cloud-api-context
layout: provider
modified: '2026-10-09'
name: Sovereign European Cloud API (SECA)
nav: Providers
network: true
overview: 'Sovereign European Cloud API (SECA) publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Activity Log API, Block Storage API, and 20 more. Tagged areas include Company, Cloud, Cloud Infrastructure, Sovereignty, and Europe.


  The Sovereign European Cloud API (SECA) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sovereign European Cloud API (SECA)''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 25 more developer resources.'
plans:
- name: Eu Sovereign Cloud Api Plans Pricing
  plan_count: 0
  slug: eu-sovereign-cloud-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Eu Sovereign Cloud Api Rate Limits
  slug: eu-sovereign-cloud-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Sovereign European Cloud API (SECA) API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 2
  slug: eu-sovereign-cloud-api-rules
- authorship: provider
  effective_rule_count: 45
  extends: []
  name: Sovereign European Cloud API (SECA) — spec rules
  rule_count: 45
  severity_counts:
    error: 23
    hint: 0
    info: 2
    warn: 20
  slug: eu-sovereign-cloud-api-spec-spectral-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 74.3
    catalog_earned_first_party: 18.0
    catalog_gap: 40.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.5
  facets:
    access_clarity: 0.0
    contract_governance: 76.5
    contract_quality: 63.1
    developer_ergonomics: 61.3
    discoverability: 62.5
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/eu-sovereign-cloud-api/refs/heads/main/screenshots/eu-sovereign-cloud-api-2026-10-11T104313.png
security:
- kind: authentication
  name: Eu Sovereign Cloud Api Authentication
  slug: eu-sovereign-cloud-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eu Sovereign Cloud Api Domain Security
  slug: eu-sovereign-cloud-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eu-sovereign-cloud-api
tags:
- Company
- Cloud
- Cloud Infrastructure
- Sovereignty
- Europe
- Open Standard
- Multi-Cloud
- Interoperability
- OpenAPI
website: https://www.secapi.cloud/
---
