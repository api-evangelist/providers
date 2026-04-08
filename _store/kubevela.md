---
aid: kubevela
url: https://raw.githubusercontent.com/api-evangelist/kubevela/refs/heads/main/apis.yml
apis:
- aid: kubevela:kubevela-api
  name: KubeVela Application API
  description: KubeVela uses Kubernetes CRDs to define applications using the Open Application Model. The Application resource combines components (workload definitions), traits (operational capabilities like scaling and rollout), and policies (deployment strategies). VelaQL provides a query interface for application status across clusters.
  humanURL: https://kubevela.io/docs/
  properties:
  - type: Documentation
    url: https://kubevela.io/docs/
  tags:
  - Application Model
  - Delivery
  - OAM
name: KubeVela
tags:
- Application Delivery
- Cloud Native
- Incubating
- Kubernetes
- Multi-Cloud
- OAM
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: KubeVela is a CNCF incubating application delivery and management platform that makes deploying and operating applications across hybrid and multi-cloud environments easier. Built on the Open Application Model (OAM), it provides a higher-level abstraction for defining applications with components, traits, and policies. KubeVela supports workflow-based delivery pipelines and multi-cluster deployment.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

