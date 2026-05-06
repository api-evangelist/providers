---
aid: lf-broadband
name: LF Broadband
description: LF Broadband is a Linux Foundation Directed Fund established in late 2023 that supports open source broadband networking projects, including reference designs and virtualization tools for broadband access networks. Its flagship projects, SEBA and VOLTHA, virtualize multi-vendor Passive Optical Network (PON) systems and are deployed by major operators such as Deutsche Telekom and Turk Telekom.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Broadband
  - Linux Foundation
  - Networking
  - Telecom
  - PON
  - Open Source
  - SDN
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/lf-broadband/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: lf-broadband:voltha
    name: VOLTHA
    description: VOLTHA (Virtual Optical Line Termination Hardware Abstraction) is an open source platform that virtualizes multi-vendor Passive Optical Network (PON) hardware, exposing a vendor-agnostic gRPC API for network operators to manage PON access networks programmatically.
    humanURL: https://docs.voltha.org/
    tags:
      - PON
      - Network Virtualization
      - Access Networks
      - gRPC
    properties:
      - type: Documentation
        url: https://docs.voltha.org/
      - type: GitHubRepo
        url: https://github.com/opencord/voltha
  - aid: lf-broadband:seba
    name: SEBA
    description: SEBA (SDN-Enabled Broadband Access) is a reference design for constructing open broadband networks, providing a thin platform for access-network workloads and integrating VOLTHA, ONOS, and other open source components.
    humanURL: https://opennetworking.org/seba/
    tags:
      - SDN
      - Broadband Access
      - Reference Design
    properties:
      - type: Documentation
        url: https://docs.opennetworking.org/seba/
      - type: GitHubOrg
        url: https://github.com/opencord
common:
  - type: Documentation
    name: LF Broadband Documentation
    description: Official documentation for LF Broadband.
    url: https://lfbroadband.org/
  - type: GitHubOrg
    name: LF Broadband GitHub
    description: Source code and repositories for LF Broadband (OpenCORD).
    url: https://github.com/opencord
  - type: Website
    name: LF Broadband Website
    description: Official LF Broadband website.
    url: https://lfbroadband.org/
  - type: Support
    name: LF Broadband Support
    description: LF Broadband support contact.
    url: mailto:support@lfbroadband.org
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
