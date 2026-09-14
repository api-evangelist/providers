---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.weave.works'', ''status'': 302, ''note'': ''declared website redirects to https://ambking1234.dev/?action=register&marketingRef=6788b227da9499f55f6ea745 — a different registrable domain (weave.works -> ambking1234.dev), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weaveworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.weave.works
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weaveworks
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitops.weaveworks.org
- group: build
  title: ''
  type: Packages
  url: packages/weaveworks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/weaveworks-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weaveworks-lifecycle.yml
created: '2026-07-17'
description: Weaveworks was the cloud-native company that coined the term "GitOps" and built the Weave family of open-source infrastructure tooling — Weave Net (multi-host container networking), Weave Scope (Docker/Kubernetes visualization and monitoring), Weave GitOps, and the widely used eksctl CLI for Amazon EKS. Backed by Accel and GV, the company ceased commercial operations in February 2024 after a planned acquisition fell through. It shipped no hosted REST API or client SDKs; its public surface was open-source Go tooling. Following the shutdown, Flux CD moved to the CNCF (graduated), eksctl transferred to the eksctl-io org jointly maintained with AWS, and the remaining Weave repositories became community-driven under the github.com/weaveworks organization. The former company website (weave.works) has lapsed and now redirects to a parked page.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weaveworks.png
layout: provider
modified: '2026-07-21'
name: Weaveworks
nav: Providers
network: true
overview: 'Weaveworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, GitOps, Kubernetes, and Container Networking.


  Weaveworks'' developer surface includes documentation, CLI, and 5 more developer resources.'
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/weaveworks/refs/heads/main/screenshots/weaveworks-2026-09-02T170526.png
security:
- kind: domain-security
  name: Weaveworks Domain Security
  slug: weaveworks-domain-security
  summary_line: TLSv1.3
slug: weaveworks
tags:
- Company
- Developer Tools
- GitOps
- Kubernetes
- Container Networking
- Cloud-Native
- Open-Source
- DevOps
website: http://www.weave.works
---
