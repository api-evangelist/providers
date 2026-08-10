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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: The wasmCloud control interface provides a NATS-based API for managing the wasmCloud lattice. It supports operations for starting and stopping actors and providers, establishing links between componen
  name: wasmCloud Control Interface API
  slug: wasmcloud-control-api
- description: 'wadm provides a declarative application deployment API for wasmCloud. Applications are defined as YAML manifests specifying components, capability providers, and their links. wadm manages the desired '
  name: wasmCloud Application Deployment Manager (wadm) API
  slug: wasmcloud-wadm-api
- description: wash (WAsmcloud SHell) is the comprehensive command-line tool for developing, building, deploying, and managing wasmCloud applications and WebAssembly components. It bundles a wasmCloud host, NATS ser
  name: wasmCloud wash CLI
  slug: wasmcloud-wash-cli
- description: 'wasmCloud interfaces are defined using WebAssembly Interface Type (WIT), the open standard interface description language maintained as part of the W3C WebAssembly Component Model. wasmCloud supports '
  name: wasmCloud WIT Interfaces
  slug: wasmcloud-interfaces
- description: 'The wasmCloud Kubernetes Operator enables running wasmCloud infrastructure natively on Kubernetes clusters. It deploys wasmCloud hosts as Kubernetes workloads and bridges the Kubernetes control plane '
  name: wasmCloud Kubernetes Operator
  slug: wasmcloud-kubernetes-operator
artifact_total: 21
asyncapis:
- description: AsyncAPI specification for the wasmCloud Control Interface, a NATS-based API for managing the wasmCloud lattice. Operators and tooling (wash CLI, wasmCloud dashboard, wadm) interact with wasmCloud hos
  name: wasmCloud Control Interface API
  slug: wasmcloud-control-asyncapi
- description: The wasmCloud lattice event system publishes CloudEvents-format messages to NATS subjects describing the lifecycle of components, capability providers, links, and hosts within a wasmCloud lattice. All
  name: wasmCloud Lattice Events
  slug: wasmcloud-lattice-events-asyncapi
- description: The wasmCloud Application Deployment Manager (wadm) API is exposed entirely as a NATS service using a subject-per-operation model. All API requests and responses are JSON-encoded and published on subj
  name: wasmCloud wadm Application Deployment Manager API
  slug: wasmcloud-wadm-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wasmcloud-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wasmcloud
- group: company
  title: ''
  type: Website
  url: https://wasmcloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://wasmcloud.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://wasmcloud.com/docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://wasmcloud.com/blog/
- group: operate
  title: ''
  type: Community
  url: https://wasmcloud.com/community/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wasmCloud
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/wasmCloud/wasmCloud
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/wasmcloud/wasmcloud/releases
- group: operate
  title: ''
  type: Slack
  url: https://slack.wasmcloud.com/
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wasmcloud-control-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wasmcloud-wadm-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wasmcloud-lattice-events-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/wasmcloud-manifest-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/wasmcloud-oam-manifest-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/wasmcloud-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/wasmcloud-oam-manifest-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wasmcloud-vocabulary.yml
- group: other
  title: ''
  type: KubernetesCRD
  url: crd/runtime.wasmcloud.dev_hosts.yaml
- group: other
  title: ''
  type: KubernetesCRD
  url: crd/runtime.wasmcloud.dev_artifacts.yaml
- group: other
  title: ''
  type: KubernetesCRD
  url: crd/runtime.wasmcloud.dev_workloads.yaml
- group: other
  title: ''
  type: KubernetesCRD
  url: crd/runtime.wasmcloud.dev_workloaddeployments.yaml
- group: other
  title: ''
  type: KubernetesCRD
  url: crd/runtime.wasmcloud.dev_workloadreplicasets.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://wasmcloud.com/llms.txt
crds:
- name: runtime.wasmcloud.dev artifacts
  url: https://raw.githubusercontent.com/api-evangelist/wasmcloud/refs/heads/main/crd/runtime.wasmcloud.dev_artifacts.yaml
- name: runtime.wasmcloud.dev hosts
  url: https://raw.githubusercontent.com/api-evangelist/wasmcloud/refs/heads/main/crd/runtime.wasmcloud.dev_hosts.yaml
- name: runtime.wasmcloud.dev workloaddeployments
  url: https://raw.githubusercontent.com/api-evangelist/wasmcloud/refs/heads/main/crd/runtime.wasmcloud.dev_workloaddeployments.yaml
- name: runtime.wasmcloud.dev workloadreplicasets
  url: https://raw.githubusercontent.com/api-evangelist/wasmcloud/refs/heads/main/crd/runtime.wasmcloud.dev_workloadreplicasets.yaml
- name: runtime.wasmcloud.dev workloads
  url: https://raw.githubusercontent.com/api-evangelist/wasmcloud/refs/heads/main/crd/runtime.wasmcloud.dev_workloads.yaml
created: '2026-03-16'
description: wasmCloud is a CNCF incubating platform for building, managing, and scaling distributed applications using WebAssembly components. It provides a runtime that manages the lifecycle of WebAssembly actors and capability providers, enabling developers to write portable business logic that connects to infrastructure capabilities like HTTP servers, messaging, key-value stores, and databases through a declarative linking model based on WebAssembly Interface Types (WIT).
examples:
- key_count: 4
  name: Wasmcloud Link Definition Example
  slug: wasmcloud-link-definition-example
- key_count: 3
  name: Wasmcloud Oam Manifest Example
  slug: wasmcloud-oam-manifest-example
- key_count: 4
  name: Wasmcloud Scale Component Example
  slug: wasmcloud-scale-component-example
finops:
- name: Wasmcloud Finops
  service_category: API
  slug: wasmcloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wasmcloud.png
json_schemas:
- name: wasmCloud OAM Application Manifest
  property_count: 4
  slug: wasmcloud-manifest
- name: wasmCloud OAM Application Manifest
  property_count: 4
  slug: wasmcloud-oam-manifest
json_structures:
- name: Wasmcloud Oam Manifest Structure
  property_count: 0
  slug: wasmcloud-oam-manifest-structure
jsonld:
- class_count: 8
  name: Wasmcloud Context
  property_count: 35
  slug: wasmcloud-context
layout: provider
modified: '2026-05-03'
name: wasmCloud
nav: Providers
network: true
overview: 'wasmCloud publishes 2 APIs on the [APIs.io](https://apis.io/) network: Control Interface API and Application Deployment Manager (wadm) API. Tagged areas include Cloud Native, CNCF, Distributed Systems, Incubating, and Runtime.


  The wasmCloud catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  wasmCloud''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 21 more developer resources.'
plans:
- name: Wasmcloud Plans Pricing
  plan_count: 3
  slug: wasmcloud-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Wasmcloud Rate Limits
  slug: wasmcloud-rate-limits
rules:
- name: wasmCloud API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 7
  slug: wasmcloud-asyncapi-spectral-rules
- name: wasmCloud API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: wasmcloud-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 78.4
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 62.5
    operational_transparency: 52.6
  previous_composite: 54.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wasmcloud/refs/heads/main/screenshots/wasmcloud-2026-06-20T201238.png
security:
- kind: domain-security
  name: Wasmcloud Domain Security
  slug: wasmcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wasmcloud
tags:
- Cloud Native
- CNCF
- Distributed Systems
- Incubating
- Runtime
- Wasm
- WebAssembly
- WIT
website: https://wasmcloud.com
---
