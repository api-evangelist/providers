---
aid: buoyant
name: Buoyant
description: Buoyant is the creator of Linkerd, the CNCF-graduated service mesh for Kubernetes. Linkerd provides zero-trust security via mutual TLS, ultra-high availability with automated failover, and observability for microservices including AI/LLM workloads. Buoyant Enterprise Linkerd adds enterprise features including FIPS 140-2/140-3 validated encryption and multi-cluster support.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Observability
  - Kubernetes
  - Linkerd
  - mTLS
  - Observability
  - Service Mesh
  - Zero Trust
created: '2026-01-02'
modified: '2026-04-21'
url: https://raw.githubusercontent.com/api-evangelist/buoyant/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: buoyant:linkerd
    name: Linkerd Service Mesh
    description: Linkerd is a CNCF-graduated service mesh for Kubernetes that transparently adds mutual TLS encryption, latency-aware load balancing, retries, timeouts, circuit breaking, and observability to any Kubernetes workload without code changes. Supports HTTP, HTTP/2, gRPC, and TCP traffic.
    humanURL: https://linkerd.io/
    tags:
      - Kubernetes
      - mTLS
      - Observability
      - Service Mesh
      - Zero Trust
    properties:
      - type: Documentation
        url: https://linkerd.io/2.x/overview/
      - type: Website
        url: https://linkerd.io/
      - type: Reference
        url: https://linkerd.io/2.x/reference/
      - type: GitHub Repository
        url: https://github.com/linkerd/linkerd2
    x-features:
      - Mutual TLS for transparent encryption and authentication
      - Cryptographic workload identity
      - Latency-aware load balancing
      - Automated retries, timeouts, and circuit breaking
      - Zone-aware routing (HAZL) to reduce cross-zone costs
      - Canary and blue-green deployment support
      - AI/LLM observability for resource, tool, and prompt usage metrics
      - Multi-cluster failover
      - FIPS 140-2/140-3 validated encryption (Enterprise)
    x-use-cases:
      - Zero-trust Kubernetes networking
      - Service-to-service mutual TLS without code changes
      - Observability for microservices and AI workloads
      - Multi-cluster Kubernetes deployments
      - Migration between cloud providers
  - aid: buoyant:buoyant-enterprise-linkerd
    name: Buoyant Enterprise Linkerd (BEL)
    description: Buoyant Enterprise Linkerd is the enterprise-supported distribution of Linkerd with additional features including FIPS-validated cryptography, lifecycle automation, multi-cluster networking, and enterprise SLA support.
    humanURL: https://buoyant.io/linkerd-enterprise
    tags:
      - Enterprise
      - FIPS
      - Kubernetes
      - Service Mesh
    properties:
      - type: Documentation
        url: https://docs.buoyant.io/buoyant-enterprise-linkerd/latest/overview/
      - type: Website
        url: https://buoyant.io/linkerd-enterprise
common:
  - type: Portal
    url: https://buoyant.io/
  - type: Documentation
    url: https://linkerd.io/2.x/overview/
  - type: GitHub Organization
    url: https://github.com/linkerd
  - type: Blog
    url: https://buoyant.io/blog/
  - type: Pricing
    url: https://buoyant.io/pricing/
  - type: Slack
    url: https://slack.linkerd.io/
  - type: Community
    url: https://linkerd.io/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
