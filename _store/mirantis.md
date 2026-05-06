---
aid: mirantis
name: Mirantis
description: Mirantis provides enterprise Kubernetes and container platform solutions for multi-cloud, hybrid-cloud, and edge deployments. Its product line includes Mirantis Kubernetes Engine (MKE), k0rdent Enterprise, Mirantis OpenStack for Kubernetes (MOSK), Mirantis Container Runtime, Mirantis Secure Registry, Lens Desktop, and the open source k0s Kubernetes distribution and k0smotron orchestrator.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Kubernetes
  - Containers
  - Cloud
  - DevOps
  - OpenStack
url: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mirantis:mirantis
    name: Mirantis
    description: Mirantis enterprise Kubernetes and container platform overview, indexing product, documentation, and developer resources.
    humanURL: https://www.mirantis.com/
    tags:
      - Kubernetes
      - Containers
    properties:
      - type: Website
        url: https://www.mirantis.com/
      - type: Documentation
        url: https://docs.mirantis.com/
  - aid: mirantis:mke
    name: Mirantis Kubernetes Engine
    description: Mirantis Kubernetes Engine (MKE) is an enterprise container orchestration platform that delivers production-ready Kubernetes for hybrid and multi-cloud environments.
    humanURL: https://www.mirantis.com/software/mirantis-kubernetes-engine/
    tags:
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.mirantis.com/mke/
  - aid: mirantis:k0rdent
    name: Mirantis k0rdent
    description: k0rdent is a composable Kubernetes management platform for centrally provisioning, observing, and securing fleets of clusters across clouds and edge.
    humanURL: https://k0rdent.io/
    tags:
      - Kubernetes
      - Multi-Cloud
    properties:
      - type: Documentation
        url: https://docs.mirantis.com/k0rdent/
      - type: OpenSource
        url: https://github.com/k0rdent
  - aid: mirantis:k0s
    name: k0s
    description: k0s is a single-binary, lightweight, certified Kubernetes distribution that runs on any infrastructure from cloud to edge.
    humanURL: https://k0sproject.io/
    tags:
      - Kubernetes
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.k0sproject.io/
      - type: GitHub
        url: https://github.com/k0sproject/k0s
  - aid: mirantis:mosk
    name: Mirantis OpenStack for Kubernetes
    description: MOSK delivers OpenStack on top of Kubernetes for cloud and telco workloads.
    humanURL: https://www.mirantis.com/software/mirantis-openstack-for-kubernetes/
    tags:
      - OpenStack
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.mirantis.com/mosk/
  - aid: mirantis:lens
    name: Lens Desktop
    description: Lens is a Kubernetes IDE for managing, observing, and troubleshooting clusters.
    humanURL: https://k8slens.dev/
    tags:
      - Kubernetes
      - IDE
    properties:
      - type: Website
        url: https://k8slens.dev/
common:
  - type: Website
    url: https://www.mirantis.com/
  - type: Documentation
    url: https://docs.mirantis.com/
  - type: Blog
    url: https://www.mirantis.com/blog/
  - type: GitHub
    url: https://github.com/Mirantis
  - type: Support
    url: https://www.mirantis.com/support/
  - type: Pricing
    url: https://www.mirantis.com/contact/
  - type: Careers
    url: https://www.mirantis.com/company/careers/
  - type: Twitter
    url: https://twitter.com/MirantisIT
  - type: LinkedIn
    url: https://www.linkedin.com/company/mirantis
  - type: YouTube
    url: https://www.youtube.com/user/mirantisinc
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
