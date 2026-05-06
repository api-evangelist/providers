---
aid: kata-containers
name: Kata Containers
description: Kata Containers is an open source project that builds lightweight virtual machines that seamlessly plug into the container ecosystem. It combines the speed of containers with the security isolation of virtual machines, providing a hardware-level isolation boundary for each container or pod.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Isolation
  - Kubernetes
  - Open Source
  - Security
  - Virtual Machines
url: https://raw.githubusercontent.com/api-evangelist/kata-containers/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kata-containers:kata-containers
    name: Kata Containers
    description: Kata Containers is an open source container runtime that uses lightweight virtual machines to provide the speed of containers with the security of traditional VMs. It is compatible with the OCI runtime specification and integrates with Kubernetes through the CRI-O and containerd runtime interfaces.
    humanURL: https://katacontainers.io/
    tags:
      - Containers
      - Isolation
      - Kubernetes
      - Open Source
      - Security
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://katacontainers.io/docs/
      - type: Getting Started
        url: https://github.com/kata-containers/kata-containers/tree/main/docs/install
common:
  - type: Website
    url: https://katacontainers.io/
  - type: GitHub Organization
    url: https://github.com/kata-containers
  - type: GitHub Repository
    url: https://github.com/kata-containers/kata-containers
  - type: Documentation
    url: https://katacontainers.io/docs/
  - type: Blog
    url: https://katacontainers.io/blog/
  - type: Slack
    url: https://katacontainers.slack.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
