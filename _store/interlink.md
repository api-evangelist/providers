---
aid: interlink
name: Interlink
description: interLink is an abstraction layer that extends the Kubernetes Virtual Kubelet interface, enabling pods to execute on remote resources such as HPC batch systems (SLURM, HTCondor), virtual machines, remote Kubernetes clusters, and serverless platforms. It comprises a Virtual Kubelet that converts pod execution requests into remote API calls and a modular interLink API Server with provider-specific sidecar plugins, with built-in OpenTelemetry observability, TLS/mTLS, and OAuth2 authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - HPC
  - Kubernetes
  - Multi-Cluster
  - Networking
  - Virtual Kubelet
url: https://raw.githubusercontent.com/api-evangelist/interlink/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://interlink-hq.github.io/interLink/
  - type: GitHub
    url: https://github.com/interlink-hq/interLink
  - type: Documentation
    url: https://interlink-hq.github.io/interLink/docs/intro
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
