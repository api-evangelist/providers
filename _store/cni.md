---
aid: cni
url: https://raw.githubusercontent.com/api-evangelist/cni/refs/heads/main/apis.yml
apis:
- aid: cni:cni-spec
  name: CNI Specification
  description: The CNI specification defines the interface between container runtimes and network plugins. It specifies how runtimes invoke plugins via environment variables and stdin configuration, and how plugins respond with network interface details. The spec covers ADD, DEL, CHECK, and VERSION operations for managing container network attachments.
  humanURL: https://www.cni.dev/docs/spec/
  properties:
  - type: Documentation
    url: https://www.cni.dev/docs/spec/
  - type: GitHubRepository
    url: https://github.com/containernetworking/cni
  - type: JSONSchema
    url: json-schema/cni-network-config-schema.json
  - type: JSONSchema
    url: json-schema/cni-result-schema.json
  tags:
  - Network Plugins
  - Specification
- aid: cni:cni-plugins
  name: CNI Reference Plugins
  description: A collection of reference and example networking plugins maintained by the CNI team that implement the CNI specification. Includes main plugins such as bridge, ipvlan, macvlan, ptp, host-device, and loopback, as well as meta plugins such as portmap, bandwidth, firewall, and sbr for additional networking functionality.
  humanURL: https://www.cni.dev/plugins/current/
  properties:
  - type: Documentation
    url: https://www.cni.dev/plugins/current/
  - type: GitHubRepository
    url: https://github.com/containernetworking/plugins
  tags:
  - Containers
  - Kubernetes
  - Linux
  - Network Plugins
  - Networking
name: Container Network Interface (CNI)
tags:
- Cloud Native
- Containers
- Incubating
- Kubernetes
- Networking
- Plugins
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CNI (Container Network Interface) is a CNCF incubating project that defines a specification and libraries for configuring network interfaces in Linux containers. It provides a simple interface between the container runtime and network implementation plugins, enabling pluggable networking for Kubernetes and other container orchestrators. CNI includes reference plugins for bridge, IPVLAN, MACVLAN, loopback, and other network types.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

