---
aid: openinfra-foundation
name: OpenInfra Foundation
description: The OpenInfra Foundation, which recently joined the Linux Foundation, is home to open infrastructure projects including OpenStack, Kata Containers, StarlingX, and Zuul. It supports the development and adoption of open infrastructure for cloud computing, edge computing, and container technology.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Computing
  - Infrastructure
  - Linux Foundation
  - OpenStack
  - Kata Containers
  - StarlingX
  - Zuul
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openinfra-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openinfra-foundation:openstack
    name: OpenStack
    description: OpenStack is a programmable infrastructure platform for managing virtual machines, containers, and bare metal at cloud scale, with a broad set of REST APIs across compute, networking, storage, identity, and image services.
    humanURL: https://www.openstack.org/
    tags:
      - Cloud Computing
      - Infrastructure
      - VMs
      - Containers
      - Bare Metal
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/
      - type: GitHubOrg
        url: https://github.com/openstack
  - aid: openinfra-foundation:kata-containers
    name: Kata Containers
    description: Kata Containers provides secure, lightweight, CRI-compatible virtualized containers, combining the speed of containers with the isolation of virtual machines.
    humanURL: https://katacontainers.io/
    tags:
      - Containers
      - Virtualization
      - Security
    properties:
      - type: Documentation
        url: https://katacontainers.io/docs/
      - type: GitHubOrg
        url: https://github.com/kata-containers
  - aid: openinfra-foundation:starlingx
    name: StarlingX
    description: StarlingX is an edge cloud computing infrastructure platform optimized for high performance, ultra-low latency applications, integrating OpenStack, Kubernetes, and supporting services.
    humanURL: https://www.starlingx.io/
    tags:
      - Edge Computing
      - Cloud Native
      - Low Latency
    properties:
      - type: Documentation
        url: https://docs.starlingx.io/
      - type: GitHubOrg
        url: https://opendev.org/starlingx
  - aid: openinfra-foundation:zuul
    name: Zuul
    description: Zuul is a CI/CD platform that gates changes across multiple systems and repositories, providing project gating, cross-project dependency management, and pipeline-driven automation.
    humanURL: https://zuul-ci.org/
    tags:
      - CI/CD
      - Automation
      - Gating
    properties:
      - type: Documentation
        url: https://zuul-ci.org/docs/
      - type: GitHubOrg
        url: https://opendev.org/zuul
common:
  - type: Website
    name: OpenInfra Foundation
    url: https://openinfra.org/
  - type: Documentation
    name: OpenInfra Projects
    url: https://openinfra.org/projects/
  - type: GitHubOrg
    name: OpenInfra GitHub
    url: https://github.com/openinfra
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
