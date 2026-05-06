---
aid: consul-connect
url: https://raw.githubusercontent.com/api-evangelist/consul-connect/refs/heads/main/apis.yml
name: Consul Connect
x-type: opensource
description: Consul Connect is the service mesh subsystem of HashiCorp Consul. Connect provides service identity, mTLS, traffic authorization via intentions, and L7 traffic management through Envoy sidecar proxies. Consul Connect ships with a built-in certificate authority that can also be backed by Vault or external PKI, supports mesh, terminating, ingress, and API gateways, and spans virtual machines, Kubernetes, AWS ECS, AWS Lambda, and Nomad runtimes. Operators interact with Connect through the consul CLI, the HTTP API, configuration entries, and Kubernetes Custom Resource Definitions.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
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
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: consul-connect:consul-connect-api
    name: Consul Connect HTTP API
    description: The HTTP API exposed by Consul agents under /v1/connect for managing intentions, the Connect certificate authority, and related mesh operations. Connect-related endpoints also exist in the Agent and Catalog APIs for sidecar proxy registration and CA leaf signing.
    humanURL: https://developer.hashicorp.com/consul/api-docs/connect
    baseURL: http://localhost:8500/v1
    tags:
      - HTTP API
      - Intentions
      - mTLS
      - Service Mesh
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/consul/api-docs/connect
      - type: Reference
        url: https://developer.hashicorp.com/consul/api-docs/connect/intentions
      - type: Reference
        url: https://developer.hashicorp.com/consul/api-docs/connect/ca
      - type: OpenAPI
        url: openapi/consul-connect-openapi.yml
      - type: JSONSchema
        url: json-schema/consul-connect-intention-schema.json
    x-features:
      - Manage intentions by source/destination or UUID (legacy)
      - Authorize connections via /connect/intentions/check
      - Match intentions for a given service via /connect/intentions/match
      - List and configure the Connect certificate authority
      - Pluggable CA providers (Consul, Vault, AWS PCA, external)
      - ACL token enforcement via X-Consul-Token header
    x-useCases:
      - GitOps-managed authorization across heterogeneous services
      - Automating CA rotation and provider migrations
      - Building admin dashboards over service mesh policy
      - Integrating Consul Connect with CI/CD release gates
  - aid: consul-connect:consul-connect-config-entries
    name: Consul Connect Configuration Entries
    description: Consul Connect configuration entries (service-defaults, service-resolver, service-router, service-splitter, service-intentions, mesh, proxy-defaults) that declaratively configure mesh behavior. Configuration entries are managed via the /v1/config API and via Kubernetes Custom Resource Definitions when running on Kubernetes.
    humanURL: https://developer.hashicorp.com/consul/docs/connect/config-entries
    baseURL: https://developer.hashicorp.com
    tags:
      - Configuration Entries
      - CRD
      - Kubernetes
      - L7 Routing
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/consul/docs/connect/config-entries
      - type: Reference
        url: https://developer.hashicorp.com/consul/docs/connect/config-entries/service-defaults
      - type: Reference
        url: https://developer.hashicorp.com/consul/docs/connect/config-entries/service-router
      - type: Reference
        url: https://developer.hashicorp.com/consul/docs/connect/config-entries/service-splitter
    x-features:
      - service-defaults to set protocol and timeouts
      - service-router for L7 path/header/method routing
      - service-splitter for canary and blue/green rollouts
      - service-resolver for failover and subsets
      - mesh-wide configuration via the mesh entry
      - Kubernetes CRDs for declarative mesh management
    x-useCases:
      - Implementing canary deployments via service-splitter
      - Routing traffic by header for tenant isolation
      - Centralizing TLS and protocol defaults
  - aid: consul-connect:consul-connect-gateways
    name: Consul Connect Gateways
    description: 'Consul Connect supports four gateway types for traffic flowing into and out of the mesh: mesh gateways for cross-datacenter and cross-partition traffic, ingress gateways for North-South entry, terminating gateways for access to non-mesh services, and the Consul API Gateway implementing the Kubernetes Gateway API.'
    humanURL: https://developer.hashicorp.com/consul/docs/connect/gateways
    baseURL: https://developer.hashicorp.com
    tags:
      - API Gateway
      - Gateways
      - Ingress
      - Mesh Gateway
      - Terminating Gateway
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/consul/docs/connect/gateways
      - type: Reference
        url: https://developer.hashicorp.com/consul/docs/connect/gateways/mesh-gateway
      - type: Reference
        url: https://developer.hashicorp.com/consul/docs/connect/gateways/ingress-gateway
      - type: Reference
        url: https://developer.hashicorp.com/consul/docs/connect/gateways/terminating-gateway
      - type: Reference
        url: https://developer.hashicorp.com/consul/docs/api-gateway
    x-features:
      - Mesh gateways for WAN federation and partition crossing
      - Ingress gateways for L4/L7 ingress with TLS
      - Terminating gateways for non-mesh service access
      - API Gateway implementing the Kubernetes Gateway API
    x-useCases:
      - Federate Consul across datacenters securely
      - Expose mesh services to external clients with TLS
      - Allow mesh services to call legacy non-mesh endpoints
common:
  - type: Website
    url: https://www.consul.io/
  - type: JSON-LD
    url: json-ld/consul-connect-context.jsonld
  - type: JSONSchema
    url: json-schema/consul-connect-intention-schema.json
  - type: Vocabulary
    url: vocabulary/consul-connect-vocabulary.yml
  - type: SpectralRules
    url: rules/consul-connect-rules.yml
  - type: Capability
    url: capabilities/manage-service-intentions.yml
  - type: Capability
    url: capabilities/rotate-mesh-ca.yml
  - type: Documentation
    url: https://developer.hashicorp.com/consul/docs/connect
  - type: Documentation
    url: https://developer.hashicorp.com/consul/api-docs/connect
  - type: GitHubRepository
    url: https://github.com/hashicorp/consul
  - type: GitHub Organization
    url: https://github.com/hashicorp
  - type: Issue Tracker
    url: https://github.com/hashicorp/consul/issues
  - type: Change Log
    url: https://github.com/hashicorp/consul/releases
  - type: License
    url: https://github.com/hashicorp/consul/blob/main/LICENSE
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
