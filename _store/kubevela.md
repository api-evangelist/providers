---
aid: kubevela
name: KubeVela
description: KubeVela is a CNCF incubating application delivery and management platform that makes deploying and operating applications across hybrid and multi-cloud environments easier. Built on the Open Application Model (OAM), it provides a higher-level abstraction for defining applications with components, traits, and policies. KubeVela supports workflow-based delivery pipelines and multi-cluster deployment.
url: https://kubevela.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Delivery
  - Cloud Native
  - Incubating
  - Kubernetes
  - Multi-Cloud
  - OAM
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
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
common:
  - type: Documentation
    name: KubeVela Documentation
    description: Official KubeVela documentation.
    url: https://kubevela.io/docs/
  - type: GitHubOrg
    name: KubeVela GitHub
    description: Source code repository.
    url: https://github.com/kubevela/kubevela
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
