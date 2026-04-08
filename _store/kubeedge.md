---
aid: kubeedge
url: https://raw.githubusercontent.com/api-evangelist/kubeedge/refs/heads/main/apis.yml
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
name: KubeEdge
tags:
- Cloud Native
- Edge Computing
- Graduated
- IoT
- Kubernetes
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: KubeEdge is a CNCF graduated project that extends Kubernetes to edge computing. It provides infrastructure support for networking, application deployment, and metadata synchronization between cloud and edge. KubeEdge enables containerized application orchestration at the edge with offline autonomy, ensuring edge nodes continue functioning when disconnected from the cloud.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

