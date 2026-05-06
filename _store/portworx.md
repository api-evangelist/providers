---
aid: portworx
name: Portworx
description: Portworx by Pure Storage is a Kubernetes data services platform that provides persistent storage, data protection, disaster recovery, and security for containerized applications running in production.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Containers
  - Data Management
  - Kubernetes
  - Storage
url: https://raw.githubusercontent.com/api-evangelist/portworx/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: portworx:portworx
    name: Portworx
    description: Portworx by Pure Storage is a Kubernetes data services platform that provides persistent storage, data protection, disaster recovery, and security for containerized applications running in production. The OpenStorage SDK exposes a REST API for volume, cluster, snapshot, backup, and credential management.
    humanURL: https://portworx.com/
    baseURL: https://libopenstorage.github.io/
    tags:
      - Containers
      - Data Management
      - Kubernetes
      - Storage
    properties:
      - type: Documentation
        url: https://docs.portworx.com/
      - type: GettingStarted
        url: https://docs.portworx.com/portworx-enterprise/get-started
      - type: APIReference
        url: https://libopenstorage.github.io/
      - type: OpenAPI
        url: openapi/portworx-openapi.yml
common:
  - type: Website
    url: https://portworx.com/
  - type: Documentation
    url: https://docs.portworx.com/
  - type: Blog
    url: https://portworx.com/blog/
  - type: GitHub Organization
    url: https://github.com/portworx
  - type: Pricing
    url: https://portworx.com/pricing/
  - type: Sign Up
    url: https://central.portworx.com/
  - type: Support
    url: https://portworx.com/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
