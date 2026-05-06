---
aid: kubeedge
name: KubeEdge
description: KubeEdge is a CNCF graduated project that extends Kubernetes to edge computing. It provides infrastructure support for networking, application deployment, and metadata synchronization between cloud and edge. KubeEdge enables containerized application orchestration at the edge with offline autonomy, ensuring edge nodes continue functioning when disconnected from the cloud.
url: https://kubeedge.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Edge Computing
  - Graduated
  - IoT
  - Kubernetes
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: kubeedge:kubeedge-api
    name: KubeEdge Edge API
    description: KubeEdge extends the Kubernetes API to manage edge nodes and devices. It includes custom resources for device management, edge application deployment, and node grouping. The EdgeController and DeviceController synchronize metadata between the cloud and edge components, enabling Kubernetes-native management of edge workloads and IoT devices.
    humanURL: https://kubeedge.io/docs/
    properties:
      - type: Documentation
        url: https://kubeedge.io/docs/
    tags:
      - Device Management
      - Edge
      - IoT
common:
  - type: Documentation
    name: KubeEdge Documentation
    description: Official KubeEdge documentation.
    url: https://kubeedge.io/docs/
  - type: GitHubOrg
    name: KubeEdge GitHub
    description: Source code repository.
    url: https://github.com/kubeedge/kubeedge
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
