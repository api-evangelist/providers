---
aid: metal3-io
url: https://raw.githubusercontent.com/api-evangelist/metal3-io/refs/heads/main/apis.yml
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
name: Metal3
tags:
- Bare Metal
- Cloud Native
- Incubating
- Infrastructure
- Kubernetes
- Provisioning
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Metal3 (Metal Kubed) is a CNCF incubating project that provides bare metal host provisioning for Kubernetes. It leverages Ironic for hardware management and integrates with the Cluster API to enable Kubernetes-native lifecycle management of bare metal infrastructure. Metal3 automates server discovery, inspection, provisioning, and deprovisioning using Kubernetes custom resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

