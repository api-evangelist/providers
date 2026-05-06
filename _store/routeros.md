---
aid: routeros
name: RouterOS
description: RouterOS is MikroTik's powerful network operating system designed for managing routers, switches, access points, and other network devices. It provides a comprehensive REST API (v7.1+) and a TCP-based binary API for programmatic management of IP addresses, interfaces, firewall rules, routing, VPN configurations, DHCP, DNS, and system resources. RouterOS powers MikroTik hardware and can also be deployed as a virtual machine (CHR).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Networking
  - Routers
  - Network Management
  - Firewall
  - MikroTik
url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/apis.yml
created: '2024-11-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: routeros:routeros-rest-api
    name: RouterOS REST API
    description: The RouterOS REST API is a JSON wrapper over the RouterOS console API, available from RouterOS v7.1beta4+. It enables create, read, update, and delete operations on all RouterOS configuration menus via standard HTTP methods (GET, PUT, PATCH, DELETE, POST). Authentication uses HTTP Basic Auth with console credentials. Supports filtering, property selection (.proplist), and complex queries. Accessible at https://{router-ip}/rest.
    humanURL: https://help.mikrotik.com/docs/spaces/ROS/pages/47579162/REST+API
    baseURL: https://{router-ip}/rest
    version: 7.1+
    tags:
      - Networking
      - Router Management
      - REST API
      - Network Configuration
      - Firewall
      - DHCP
      - DNS
    properties:
      - url: https://help.mikrotik.com/docs/spaces/ROS/pages/47579162/REST+API
        type: Documentation
      - url: https://help.mikrotik.com/docs/spaces/ROS/pages/47579160/API
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/openapi/routeros-rest-api-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/rules/routeros-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/capabilities/network-management.yaml
        type: NaftikoCapabilities
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/capabilities/shared/routeros-rest.yaml
        type: NaftikoCapabilities
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/json-schema/routeros-ip-address-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/json-schema/routeros-interface-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/json-schema/routeros-firewall-filter-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/json-structure/routeros-ip-address-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/json-ld/routeros-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/examples/routeros-list-ip-addresses-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/examples/routeros-list-firewall-filters-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/examples/routeros-get-system-resource-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/vocabulary/routeros-vocabulary.yml
        type: Vocabulary
    contact:
      - FN: MikroTik Support
        url: https://mikrotik.com/support
  - aid: routeros:routeros-tcp-api
    name: RouterOS TCP API
    description: The RouterOS TCP API is the native binary protocol for RouterOS, running on TCP port 8728 (standard) and TCP port 8729 (SSL/TLS). It uses a sentence-based word protocol with variable-length encoding, supporting tagged concurrent commands, streaming changes via /listen, and cancellation. Used by most RouterOS client libraries (Python, PHP, Java, Go, etc.).
    humanURL: https://help.mikrotik.com/docs/spaces/ROS/pages/47579160/API
    baseURL: tcp://{router-ip}:8728
    version: 6.43+
    tags:
      - Networking
      - Router Management
      - TCP API
      - Binary Protocol
    properties:
      - url: https://help.mikrotik.com/docs/spaces/ROS/pages/47579160/API
        type: Documentation
      - url: https://wiki.mikrotik.com/wiki/Manual:API
        type: Documentation
common:
  - type: Website
    url: https://mikrotik.com
  - type: Documentation
    url: https://help.mikrotik.com/docs/spaces/ROS
  - type: GitHubOrg
    url: https://github.com/mikrotik
  - type: Forum
    url: https://forum.mikrotik.com
  - type: Wiki
    url: https://wiki.mikrotik.com
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/vocabulary/routeros-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/routeros/refs/heads/main/json-ld/routeros-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
