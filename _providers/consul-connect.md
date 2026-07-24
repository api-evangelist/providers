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
artifact_total: 15
collections:
- collection_type: open
  name: HashiCorp Consul Connect API
  slug: open-consul-connect
common:
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
- group: other
  title: ''
  type: Capability
  url: capabilities/manage-service-intentions.yml
- group: other
  title: ''
  type: Capability
  url: capabilities/rotate-mesh-ca.yml
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
random_paper: 23
rate_limits:
- limit_count: 4
  name: Consul Connect Rate Limits
  slug: consul-connect-rate-limits
rules:
- name: Consul Connect API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: consul-connect-jsonschema-spectral-rules
- name: Consul Connect API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: consul-connect-rules
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.1
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 49.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
