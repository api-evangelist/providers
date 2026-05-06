---
aid: openbmc
name: OpenBMC
description: OpenBMC is a Linux Foundation project producing an open source implementation of baseboard management controller firmware. Founded by Microsoft, Intel, IBM, Google, and Facebook, it provides a Linux-based firmware stack for managing and monitoring server hardware systems.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Firmware
  - Hardware
  - Linux Foundation
  - Server
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openbmc/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openbmc:openbmc-api
    name: OpenBMC API
    description: API for interacting with OpenBMC baseboard management controller firmware, providing programmatic access to server hardware management and monitoring capabilities.
    humanURL: https://github.com/openbmc/docs
    tags:
      - Firmware
      - Hardware
    properties:
      - type: Documentation
        url: https://github.com/openbmc/docs
common:
  - type: Documentation
    name: OpenBMC Documentation
    description: Official documentation for OpenBMC.
    url: https://github.com/openbmc/docs
  - type: GitHubOrg
    name: OpenBMC GitHub
    description: Source code and repositories for OpenBMC.
    url: https://github.com/openbmc
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
