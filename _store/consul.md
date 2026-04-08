---
aid: consul
url: https://raw.githubusercontent.com/api-evangelist/consul/refs/heads/main/apis.yml
apis:
- name: Consul HTTP API
  description: The main HTTP API for interacting with Consul, including service discovery, health checking, key/value storage, and datacenter management.
  image: https://www.consul.io/img/logo-hashicorp.svg
  humanUrl: https://www.consul.io/api-docs
  baseUrl: http://localhost:8500/v1
  tags:
  - Catalog
  - Health Checks
  - Key/Value
  - Service Discovery
  properties:
  - type: Documentation
    url: https://www.consul.io/api-docs
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/consul/refs/heads/main/openapi/consul-http-api.yml
  - type: Authentication
    url: https://www.consul.io/api-docs#authentication
  contact:
  - type: Support
    url: https://support.hashicorp.com
  - type: GitHub
    url: https://github.com/hashicorp/consul
  - type: Community
    url: https://discuss.hashicorp.com/c/consul
  endpoints:
  - name: Agent
    path: /agent
    description: Interact with the local Consul agent
  - name: Catalog
    path: /catalog
    description: Register and query services and nodes
  - name: Health
    path: /health
    description: Query health information
  - name: KV Store
    path: /kv
    description: Key/Value store operations
  - name: Services
    path: /catalog/services
    description: List and query registered services
  - name: ACL
    path: /acl
    description: Manage Access Control Lists
  - name: Coordinates
    path: /coordinate
    description: Network coordinate information
  - name: Events
    path: /event
    description: Fire and query events
  - name: Namespaces
    path: /namespace
    description: Manage Consul Enterprise namespaces
  - name: Sessions
    path: /session
    description: Create and manage sessions
name: HashiCorp Consul
tags:
- Health Checking
- Key/Value Store
- Multi-Datacenter
- Service Discovery
- Service Mesh
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Consul is a service networking solution to automate network configurations, discover services, and enable secure connectivity across any cloud or runtime.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

