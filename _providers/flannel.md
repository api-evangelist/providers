---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: Flannel is a simple overlay network that satisfies the Kubernetes networking requirements. It allocates subnet leases to each host and provides a layer 3 IPv4 network between multiple nodes in a clust
  name: Flannel
  slug: flannel
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/flannel-io/flannel
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/flannel-io/flannel/blob/master/Documentation/kubernetes.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/flannel-io/flannel/blob/master/Documentation/running.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flannel-io
- group: other
  title: ''
  type: Helm Chart
  url: https://flannel-io.github.io/flannel/
created: '2026-03-26'
description: Flannel is a simple overlay network that satisfies the Kubernetes networking requirements. It runs a small single binary agent called flanneld on each host and is responsible for allocating a subnet lease to each host out of a larger preconfigured address space. Flannel does not expose its own HTTP/REST API; it stores network configuration in either the Kubernetes API or etcd directly and is managed via configuration files, kubectl, and Helm.
finops:
- name: Flannel Finops
  service_category: API
  slug: flannel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flannel.png
layout: provider
modified: '2026-04-28'
name: Flannel
nav: Providers
network: true
overview: 'Flannel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CNI, Cloud-Native, Containers, Kubernetes, and Networking.


  Flannel''s developer surface includes documentation, getting-started guide, and 3 more developer resources.'
plans:
- name: Flannel Plans Pricing
  plan_count: 3
  slug: flannel-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Flannel Rate Limits
  slug: flannel-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/flannel/refs/heads/main/screenshots/flannel-2026-06-20T181303.png
slug: flannel
tags:
- CNI
- Cloud-Native
- Containers
- Kubernetes
- Networking
- Open-Source
- Overlay Network
---
