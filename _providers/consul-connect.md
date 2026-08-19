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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Consul Connect Agentic Access
  operation_count: 9
  slug: consul-connect-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 4
apis:
- description: Consul Connect configuration entries (service-defaults, service-resolver, service-router, service-splitter, service-intentions, mesh, proxy-defaults) that declaratively configure mesh behavior. Config
  name: Consul Connect Configuration Entries
  slug: consul-connect-config-entries
- description: 'Consul Connect supports four gateway types for traffic flowing into and out of the mesh: mesh gateways for cross-datacenter and cross-partition traffic, ingress gateways for North-South entry, termina'
  name: Consul Connect Gateways
  slug: consul-connect-gateways
- description: Certificate authority management
  name: Consul Connect CA API
  slug: consul-connect-ca-api
- description: Service-to-service traffic authorization
  name: Consul Connect Intentions API
  slug: consul-connect-intentions-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Consul Connect CA API
  slug: open-consul-connect-ca-api
- collection_type: open
  name: HashiCorp Consul Connect CA Intentions API
  slug: open-consul-connect-intentions-api
- collection_type: open
  name: HashiCorp Consul Connect API
  slug: open-consul-connect
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/hashicorp/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/hashicorp/consul/blob/main/.github/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/consul-connect-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consul-connect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/consul-connect-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.consul.io/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/consul-connect-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/consul-connect-intention-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/consul-connect-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/consul-connect-rules.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/consul/docs/connect
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/consul/api-docs/connect
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hashicorp/consul
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/hashicorp/consul/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/hashicorp/consul/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/hashicorp/consul/blob/main/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog/feed.xml
created: '2025-01-01'
description: Consul Connect is the service mesh subsystem of HashiCorp Consul. Connect provides service identity, mTLS, traffic authorization via intentions, and L7 traffic management through Envoy sidecar proxies. Consul Connect ships with a built-in certificate authority that can also be backed by Vault or external PKI, supports mesh, terminating, ingress, and API gateways, and spans virtual machines, Kubernetes, AWS ECS, AWS Lambda, and Nomad runtimes. Operators interact with Connect through the consul CLI, the HTTP API, configuration entries, and Kubernetes Custom Resource Definitions.
finops:
- name: Consul Connect Finops
  service_category: Service Mesh / Networking
  slug: consul-connect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consul-connect.png
json_schemas:
- name: Consul Connect Intention
  property_count: 9
  slug: consul-connect-intention
jsonld:
- class_count: 0
  name: Consul Connect Context
  property_count: 4
  slug: consul-connect-context
layout: provider
modified: '2026-05-19'
name: Consul Connect
nav: Providers
network: true
overview: 'Consul Connect publishes 2 APIs on the [APIs.io](https://apis.io/) network: CA API and Intentions API. Tagged areas include Consul, Envoy, HashiCorp, Intentions, and Kubernetes.


  The Consul Connect catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Consul Connect''s developer surface includes authentication, documentation, changelog, engineering blog, and 14 more developer resources.'
plans:
- name: Consul Connect Plans Pricing
  plan_count: 3
  slug: consul-connect-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 4
  name: Consul Connect Rate Limits
  slug: consul-connect-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Consul Connect API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: consul-connect-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Consul Connect API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: consul-connect-rules
score:
  band: thin
  composite: 33.9
  delta: -6.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 52.4
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/consul-connect/refs/heads/main/screenshots/consul-connect-2026-06-20T174917.png
security:
- kind: authentication
  name: Consul Connect Authentication
  slug: consul-connect-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Consul Connect Domain Security
  slug: consul-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: consul-connect
tags:
- Consul
- Envoy
- HashiCorp
- Intentions
- Kubernetes
- mTLS
- Service Mesh
- Sidecar
- Zero Trust
website: https://www.consul.io/
---
