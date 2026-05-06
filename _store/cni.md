---
aid: cni
name: Container Network Interface (CNI)
x-type: opensource
description: CNI (Container Network Interface) is a CNCF-incubating project that defines a specification and libraries for configuring network interfaces in Linux containers. It provides a simple exec/stdin interface between the container runtime and network implementation plugins, enabling pluggable networking for Kubernetes and other container orchestrators. The CNI spec defines four operations (ADD, DEL, CHECK, VERSION), a network configuration document format, and a plugin Result document. CNI also publishes a collection of reference plugins (bridge, ipvlan, macvlan, host-device, ptp, loopback) and meta-plugins (portmap, bandwidth, firewall, sbr).
url: https://www.cni.dev
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Containers
  - Incubating
  - Kubernetes
  - Networking
  - Plugins
created: '2026-03-16'
modified: '2026-04-23'
specificationVersion: '0.19'
type: Index
apis:
  - aid: cni:cni-spec
    name: CNI Specification
    description: The CNI specification defines the interface between container runtimes and network plugins. It specifies how runtimes invoke plugins via environment variables (CNI_COMMAND, CNI_CONTAINERID, CNI_NETNS, CNI_IFNAME, CNI_PATH, CNI_ARGS) and stdin configuration, and how plugins respond on stdout with network interface details. The spec covers ADD, DEL, CHECK, and VERSION operations for managing container network attachments, and defines the plugin chaining model used by meta-plugins.
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
      - type: JSONLDContext
        url: json-ld/cni-context.jsonld
      - type: NaftikoCapabilities
        url: capabilities/cni-spec-capabilities.yml
    tags:
      - Network Plugins
      - Specification
    x-features:
      - name: ADD operation
        description: Attach a container to a network and return a Result document with assigned interfaces, IPs, routes, and DNS.
      - name: DEL operation
        description: Detach a container from a network and tear down allocated resources.
      - name: CHECK operation
        description: Verify the container's current attachment matches the prior ADD result.
      - name: VERSION operation
        description: Report the CNI spec versions a plugin supports.
      - name: Plugin Chaining
        description: Meta-plugin chaining model where a chain shares previous Result via prevResult.
      - name: Network Config Schema
        description: Schema for the JSON document that describes a network and its plugin chain.
      - name: Result Schema
        description: Schema for the Result document that plugins emit on stdout.
    x-useCases:
      - name: Kubernetes CNI Plugin
        description: Implement a CNI plugin that integrates with Kubernetes / containerd / CRI-O.
      - name: Network Validation
        description: Validate network configurations and plugin Result documents against the spec.
      - name: Custom SDN
        description: Build custom software-defined networks for containers using a portable plugin contract.
  - aid: cni:cni-plugins
    name: CNI Reference Plugins
    description: A collection of reference and example networking plugins maintained by the containernetworking team that implement the CNI specification. Includes main plugins such as bridge, ipvlan, macvlan, ptp, host-device, and loopback, as well as meta plugins such as portmap, bandwidth, firewall, sbr, and tuning for additional networking functionality.
    humanURL: https://www.cni.dev/plugins/current/
    properties:
      - type: Documentation
        url: https://www.cni.dev/plugins/current/
      - type: GitHubRepository
        url: https://github.com/containernetworking/plugins
      - type: NaftikoCapabilities
        url: capabilities/cni-spec-capabilities.yml
    tags:
      - Containers
      - Kubernetes
      - Linux
      - Network Plugins
      - Networking
    x-features:
      - name: bridge
        description: Linux-bridge plugin attaching container veth pairs to a bridge.
      - name: ipvlan
        description: IPVLAN plugin for L2/L3 IPVLAN attachments.
      - name: macvlan
        description: MACVLAN plugin for MACVLAN attachments.
      - name: host-device
        description: Plugin that moves an existing host device into a container netns.
      - name: ptp
        description: Point-to-point veth-pair plugin.
      - name: loopback
        description: Loopback interface configuration.
      - name: portmap
        description: Meta-plugin that publishes container ports to the host via NAT.
      - name: bandwidth
        description: Meta-plugin that applies ingress/egress traffic shaping with tc.
      - name: firewall
        description: Meta-plugin that applies iptables/nftables rules for a container.
      - name: sbr
        description: Source-based routing meta-plugin.
    x-useCases:
      - name: Kubernetes Pod Networking
        description: Use bridge + portmap as a minimal Kubernetes pod networking stack.
      - name: Multi-Network Pods
        description: Combine reference plugins via Multus or chains for multi-NIC pods.
common:
  - type: Website
    url: https://www.cni.dev/
  - type: Documentation
    url: https://www.cni.dev/docs/
  - type: GitHubOrganization
    url: https://github.com/containernetworking
  - type: GitHubRepository
    url: https://github.com/containernetworking/cni
  - type: GitHubRepository
    url: https://github.com/containernetworking/plugins
  - type: JSONLDContext
    url: json-ld/cni-context.jsonld
  - type: JSONSchema
    url: json-schema/cni-network-config-schema.json
  - type: JSONSchema
    url: json-schema/cni-result-schema.json
  - type: NaftikoCapabilities
    url: capabilities/cni-spec-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
