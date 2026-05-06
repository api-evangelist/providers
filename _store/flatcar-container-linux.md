---
aid: flatcar-container-linux
name: Flatcar Container Linux
description: Flatcar Container Linux is a CNCF incubating minimal, immutable Linux distribution designed for running containers. It provides automatic atomic updates through the Nebraska update server, ensuring nodes stay secure and consistent. Flatcar supports Kubernetes deployments on bare metal, cloud, and virtual environments with a focus on security and operational simplicity.
url: https://raw.githubusercontent.com/api-evangelist/flatcar-container-linux/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Containers
  - Immutable Infrastructure
  - Incubating
  - Linux
  - Operating System
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
access: Open Source
position: Producer
apis:
  - aid: flatcar-container-linux:nebraska-update-api
    name: Flatcar Nebraska Update API
    description: Nebraska is the update management server for Flatcar Container Linux. It exposes a REST API for managing update applications, packages, channels, groups, instances, and activity. Flatcar instances poll Nebraska using the Omaha protocol for controlled rollouts, version pinning, and update monitoring across fleets of Flatcar nodes.
    humanURL: https://www.flatcar.org/docs/latest/nebraska/
    baseURL: https://nebraska.flatcar-linux.org/api
    tags:
      - Activity
      - Applications
      - Channels
      - Fleet Management
      - Groups
      - Instances
      - Omaha Protocol
      - Packages
      - Updates
    properties:
      - type: Documentation
        url: https://www.flatcar.org/docs/latest/nebraska/
      - type: OpenAPI
        url: openapi/nebraska-update-api-openapi.yml
      - type: SourceCode
        url: https://github.com/flatcar/nebraska
common:
  - type: Website
    url: https://www.flatcar.org
  - type: Documentation
    url: https://www.flatcar.org/docs/latest/
  - type: GitHubOrganization
    url: https://github.com/flatcar
  - type: SourceCode
    url: https://github.com/flatcar/flatcar
  - type: NebraskaSource
    url: https://github.com/flatcar/nebraska
  - type: Releases
    url: https://www.flatcar.org/releases/
  - type: Community
    url: https://www.flatcar.org/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
