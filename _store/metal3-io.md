---
aid: metal3-io
name: Metal3
description: Metal3 (Metal Kubed) is a CNCF incubating project that provides bare metal host provisioning for Kubernetes. It leverages Ironic for hardware management and integrates with the Cluster API to enable Kubernetes-native lifecycle management of bare metal infrastructure. Metal3 automates server discovery, inspection, provisioning, and deprovisioning using Kubernetes custom resources.
url: https://metal3.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bare Metal
  - Cloud Native
  - Incubating
  - Infrastructure
  - Kubernetes
  - Provisioning
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: metal3-io:metal3-api
    name: Metal3 BareMetalHost API
    description: Metal3 extends Kubernetes with the BareMetalHost custom resource for managing physical servers. The API supports hardware inventory discovery, firmware configuration, BIOS settings, RAID configuration, and OS provisioning. Combined with Cluster API, it enables declarative management of bare metal Kubernetes clusters.
    humanURL: https://metal3.io/documentation.html
    properties:
      - type: Documentation
        url: https://metal3.io/documentation.html
    tags:
      - Bare Metal
      - Hardware Management
      - Provisioning
common:
  - type: Documentation
    name: Metal3 Documentation
    description: Official Metal3 documentation.
    url: https://metal3.io/documentation.html
  - type: GitHubOrg
    name: Metal3 GitHub
    description: Source code repositories.
    url: https://github.com/metal3-io
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
