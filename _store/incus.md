---
aid: incus
name: Incus
description: Incus is a modern open source system container and virtual machine manager maintained by LinuxContainers.org as a community-led fork of Canonical's LXD. It provides a unified experience for running and managing system containers and VMs across single hosts and clusters, with image-based deployment, live migration, snapshots, projects, and a comprehensive RESTful API for automation and tooling integration.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Virtual Machines
  - Virtualization
  - Linux
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/incus/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: incus:incus-rest-api
    name: Incus REST API
    description: The Incus REST API is the canonical interface to the Incus container and virtual machine manager. All communication between Incus and its clients happens over HTTP, using TLS for remote access or a Unix socket for local access. The API covers the complete lifecycle of instances, images, networks, storage pools, projects, profiles, certificates, and cluster members, with support for asynchronous operations and WebSocket-based event streams.
    humanURL: https://linuxcontainers.org/incus/docs/main/rest-api/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Containers
      - Virtual Machines
      - Cluster Management
      - REST API
    properties:
      - type: Documentation
        url: https://linuxcontainers.org/incus/docs/main/rest-api/
      - type: Authentication
        url: https://linuxcontainers.org/incus/docs/main/authentication/
      - type: GitHubRepository
        url: https://github.com/lxc/incus
      - type: OpenAPI
        url: openapi/incus-openapi.yml
      - type: Rules
        url: rules/incus-rules.yml
common:
  - type: Website
    url: https://linuxcontainers.org/incus/
  - type: Documentation
    url: https://linuxcontainers.org/incus/docs/main/
  - type: Getting Started
    url: https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/
  - type: GitHubRepository
    url: https://github.com/lxc/incus
  - type: Forum
    url: https://discuss.linuxcontainers.org/
  - type: Issues
    url: https://github.com/lxc/incus/issues
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
