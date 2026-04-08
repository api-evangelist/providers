---
aid: flatcar-container-linux
url: https://raw.githubusercontent.com/api-evangelist/flatcar-container-linux/refs/heads/main/apis.yml
apis:
- aid: flatcar-container-linux:nebraska-update-api
  name: Flatcar Nebraska Update API
  description: Nebraska is the update management server for Flatcar Container Linux. It provides an API for managing update channels, groups, and packages. Flatcar instances poll Nebraska for available updates using the Omaha protocol, enabling controlled rollouts, version pinning, and update monitoring across fleets of Flatcar nodes.
  humanURL: https://www.flatcar.org/docs/latest/Nebraska/
  properties:
  - type: Documentation
    url: https://www.flatcar.org/docs/latest/Nebraska/
  tags:
  - Fleet Management
  - Updates
name: Flatcar Container Linux
tags:
- Cloud Native
- Containers
- Immutable Infrastructure
- Incubating
- Linux
- Operating System
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Flatcar Container Linux is a CNCF incubating minimal, immutable Linux distribution designed for running containers. It provides automatic atomic updates through the Nebraska update server, ensuring nodes stay secure and consistent. Flatcar supports Kubernetes deployments on bare metal, cloud, and virtual environments with a focus on security and operational simplicity.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

