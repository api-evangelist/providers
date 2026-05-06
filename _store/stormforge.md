---
aid: stormforge
name: StormForge
description: StormForge provides machine learning-based Kubernetes resource optimization (rightsizing) for reducing cloud infrastructure costs while maintaining application performance. The Optimize Live product deploys an agent to Kubernetes clusters that collects workload metrics, applies ML algorithms, and generates CPU and memory recommendations for containers. Recommendations can be applied automatically, on-demand, or exported as Kubernetes patches for GitOps workflows. StormForge supports Deployments, StatefulSets, DaemonSets, ReplicaSets, and custom workload types, and integrates with Karpenter, HPA, VPA, Argo CD, and APM tools.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Cost Optimization
  - DevOps
  - FinOps
  - Kubernetes
  - Machine Learning
  - Resource Management
  - Rightsizing
created: '2026-03-27'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/stormforge/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: stormforge:optimize-live
    name: StormForge Optimize Live
    description: StormForge Optimize Live is a Kubernetes resource rightsizing product that uses machine learning to automatically generate CPU and memory recommendations for container workloads. An agent deployed to the cluster collects observability metrics, which are processed by StormForge's ML platform to produce rightsizing recommendations. Recommendations can be applied automatically, previewed in the web UI, or exported as Kubernetes patches for GitOps. Supports Deployments, StatefulSets, DaemonSets, ReplicaSets, custom CRD workloads, and HPA-managed workloads.
    humanURL: https://www.stormforge.io/optimize-live/
    tags:
      - Cloud Cost Optimization
      - FinOps
      - Kubernetes
      - Machine Learning
      - Rightsizing
    properties:
      - type: Documentation
        url: https://docs.stormforge.io/docs/
      - type: GettingStarted
        url: https://docs.stormforge.io/docs/get-started/
      - type: Pricing
        url: https://www.stormforge.io/pricing/
      - type: Sign Up
        url: https://app.stormforge.io/
      - type: HelmChart
        url: https://github.com/thestormforge/helm-charts
  - aid: stormforge:stormforge-cli
    name: StormForge CLI
    description: Command-line interface for interacting with the StormForge platform to manage clusters, workloads, and optimization recommendations. Supports authentication, resource inspection, recommendation generation and application, GitOps patch export, Helm post-renderer integration, and an MCP server for AI integration. Available via Homebrew (macOS/Linux) and direct download.
    humanURL: https://docs.stormforge.io/docs/stormforge-cli/reference/
    tags:
      - CLI
      - DevOps
      - Kubernetes
      - FinOps
    properties:
      - type: Documentation
        url: https://docs.stormforge.io/docs/stormforge-cli/reference/
      - type: GitHubRepository
        url: https://github.com/thestormforge
      - type: Homebrew
        url: https://github.com/thestormforge/homebrew-tap
common:
  - type: Website
    url: https://www.stormforge.io/
  - type: Documentation
    url: https://docs.stormforge.io/
  - type: Pricing
    url: https://www.stormforge.io/pricing/
  - type: Blog
    url: https://www.stormforge.io/blog/
  - type: About
    url: https://www.stormforge.io/about/
  - type: Contact
    url: https://www.stormforge.io/contact/
  - type: GettingStarted
    url: https://docs.stormforge.io/docs/get-started/
  - type: Sign Up
    url: https://app.stormforge.io/
  - type: GitHubOrg
    url: https://github.com/thestormforge
  - type: Sandbox
    url: https://docs.stormforge.io/docs/sandbox/
  - type: FinOps
    url: https://www.finops.org/members/stormforge/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
