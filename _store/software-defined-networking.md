---
aid: software-defined-networking
name: Software-Defined Networking
description: Software-Defined Networking (SDN) is a network architecture approach that decouples the network control plane from the data forwarding plane, enabling dynamic, programmatically efficient network configuration. SDN controllers expose northbound REST APIs for network applications to define routing, load balancing, and security policies, while southbound APIs communicate with switches and routers. Key SDN controllers include OpenDaylight, ONOS, and Floodlight.
url: https://raw.githubusercontent.com/api-evangelist/software-defined-networking/refs/heads/main/apis.yml
tags:
  - Cloud Infrastructure
  - Network Architecture
  - Networking
  - Virtualization
  - SDN
  - OpenDaylight
  - ONOS
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: software-defined-networking:opendaylight-restconf
    name: OpenDaylight RESTCONF API
    description: OpenDaylight is an open-source SDN controller platform that exposes RESTCONF APIs for managing network devices, topology, flows, and configuration. It provides northbound REST interfaces for network applications and southbound interfaces for OpenFlow devices.
    humanURL: https://docs.opendaylight.org/en/latest/
    baseURL: http://localhost:8181/restconf
    tags:
      - SDN
      - OpenDaylight
      - RESTCONF
      - Network Management
      - Networking
    properties:
      - type: Documentation
        url: https://docs.opendaylight.org/en/latest/user-guide/opendaylight-controller-overview.html
      - type: Website
        url: https://www.opendaylight.org/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/software-defined-networking/refs/heads/main/json-schema/sdn-network-topology-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/software-defined-networking/refs/heads/main/json-structure/sdn-topology-structure.json
  - aid: software-defined-networking:onos-rest-api
    name: ONOS SDN Controller REST API
    description: ONOS (Open Network Operating System) is an open-source SDN controller that provides REST APIs for network management including topology discovery, flow rule management, host tracking, and device management.
    humanURL: https://wiki.onosproject.org/display/ONOS/REST+API
    baseURL: http://localhost:8181/onos/v1
    tags:
      - SDN
      - ONOS
      - Network Management
      - Topology
      - Flow Rules
    properties:
      - type: Documentation
        url: https://wiki.onosproject.org/display/ONOS/REST+API
      - type: Website
        url: https://onosproject.org/
common:
  - type: Website
    url: https://opennetworking.org/
  - type: Reference
    url: https://en.wikipedia.org/wiki/Software-defined_networking
  - type: Standard
    url: https://datatracker.ietf.org/doc/html/rfc7426
  - type: Reference
    url: https://www.ciena.com/insights/articles/5-key-APIs-to-enable-the-concept-of-SDN-based-virtual-networks.html
  - type: GitHubOrganization
    url: https://github.com/opendaylight
  - type: GitHubOrganization
    url: https://github.com/opennetworkinglab
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/software-defined-networking/refs/heads/main/json-ld/software-defined-networking-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/software-defined-networking/refs/heads/main/vocabulary/software-defined-networking-vocabulary.yml
---
