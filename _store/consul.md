---
aid: consul
name: HashiCorp Consul
url: https://raw.githubusercontent.com/api-evangelist/consul/refs/heads/main/apis.yml
description: HashiCorp Consul is a distributed, highly available service-networking control plane that automates network configuration, discovers services, enables secure service-to-service communication, and exposes a strongly consistent key/value store. The Consul HTTP API is a REST + JSON service exposed by every Consul agent and server at /v1, gated by the X-Consul-Token header (apiKey) and ACL policies, supporting blocking queries via X-Consul-Index for streaming-style change detection.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - ACL
  - Configuration
  - Health Checking
  - Key/Value Store
  - Multi-Datacenter
  - Open Source
  - Service Discovery
  - Service Mesh
created: '2024-01-01'
modified: '2026-04-29'
position: Provider
specificationVersion: '0.19'
x-type: opensource
apis:
  - aid: consul:http-api
    name: Consul HTTP API
    description: The main HTTP API for interacting with Consul agents and servers. Endpoints are grouped under /agent (local agent state and registration), /catalog (cluster-wide service and node catalog), /health (health-checked service queries), /kv (key/value store), /acl (token, policy, and role management), /connect (service mesh CA, intentions), /config (central configuration entries), /event (user events), /session (locks and leadership), and /operator (Raft, autopilot, license).
    image: https://www.consul.io/img/logo-hashicorp.svg
    humanURL: https://developer.hashicorp.com/consul/api-docs
    baseURL: http://localhost:8500/v1
    tags:
      - ACL
      - Catalog
      - Connect
      - Health
      - Key/Value
      - Service Discovery
      - Service Mesh
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/consul/api-docs
      - type: OpenAPI
        url: openapi/consul-http-api.yml
      - type: Authentication
        url: https://developer.hashicorp.com/consul/api-docs/api-structure
      - type: ACL Documentation
        url: https://developer.hashicorp.com/consul/docs/security/acl
      - type: GitHub Repository
        url: https://github.com/hashicorp/consul
common:
  - type: Website
    url: https://www.consul.io
  - type: Documentation
    url: https://developer.hashicorp.com/consul
  - type: Getting Started
    url: https://developer.hashicorp.com/consul/tutorials/get-started-vms
  - type: Tutorials
    url: https://developer.hashicorp.com/consul/tutorials
  - type: GitHub Organization
    url: https://github.com/hashicorp
  - type: GitHub Repository
    url: https://github.com/hashicorp/consul
  - type: Change Log
    url: https://github.com/hashicorp/consul/releases
  - type: Blog
    url: https://www.hashicorp.com/blog/products/consul
  - type: Community
    url: https://discuss.hashicorp.com/c/consul
  - type: Twitter
    url: https://twitter.com/HashiCorp
  - type: Terms of Service
    url: https://www.hashicorp.com/terms-of-service
  - type: Privacy Policy
    url: https://www.hashicorp.com/privacy
  - type: JSON-LD
    url: json-ld/consul-context.jsonld
  - type: JSONSchema
    url: json-schema/consul-service-schema.json
  - type: JSONSchema
    url: json-schema/consul-kv-schema.json
  - type: Spectral
    url: rules/consul-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/consul-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
