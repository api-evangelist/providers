---
aid: kubernetes
url: https://raw.githubusercontent.com/api-evangelist/kubernetes/refs/heads/main/apis.yml
apis:
  - aid: kubernetes:kubernetes
    name: Kubernetes API
    tags:
      - Automation
      - Cloud Native
      - CNCF
      - Containers
      - Deployment
      - Orchestration
      - Scaling
    humanURL: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
    baseURL: https://kubernetes.default.svc
    properties:
      - url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
        type: Documentation
      - url: https://kubernetes.io/docs/reference/kubernetes-api/
        type: APIReference
      - url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
        type: OpenAPI
      - url: https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec
        type: OpenAPIRepository
      - url: https://kubernetes.io/docs/reference/access-authn-authz/
        type: Authentication
      - url: https://kubernetes.io/docs/reference/using-api/client-libraries/
        type: Client Libraries
      - url: https://kubernetes.io/docs/reference/using-api/deprecation-guide/
        type: Migration Guide
      - type: OpenAPI
        url: openapi/kubernetes-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/kubernetes-watch-asyncapi.yml
      - type: JSONSchema
        url: json-schema/kubernetes-resource-schema.json
    description: The Kubernetes API lets you query and manipulate the state of objects in Kubernetes. The core of Kubernetes control plane is the API server and the HTTP API that it exposes. Users, the different parts of your cluster, and external components all communicate with one another through the API server.
name: Kubernetes
tags:
  - Automation
  - Cloud Native
  - CNCF
  - Containers
  - Deployment
  - Open Source
  - Orchestration
  - Scaling
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/kubernetes
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/kubernetes/kubernetes
    name: GitHub Repository
    type: GitHubRepository
  - url: https://github.com/kubernetes/community
    name: Community Repository
    type: GitHubRepository
  - url: https://github.com/kubernetes/kube-openapi
    name: OpenAPI Generation Repository
    type: GitHubRepository
  - url: https://bsky.app/profile/kubernetes.io
    name: Bluesky
    type: Bluesky
  - url: https://x.com/kubernetesio
    name: X (Twitter)
    type: X
  - url: https://kubernetes.io/
    name: Website
    type: Website
    description: Official Kubernetes website with documentation, tutorials, and community resources.
  - url: https://kubernetes.io/docs/home/
    name: Documentation
    type: Documentation
    description: Comprehensive documentation covering Kubernetes concepts, tasks, tutorials, and reference information.
  - url: https://kubernetes.io/docs/reference/kubernetes-api/
    name: API Reference
    type: APIReference
    description: Complete reference documentation for the Kubernetes API including all resource types and operations.
  - url: https://kubernetes.io/blog/
    name: Blog
    type: Blog
    description: Official Kubernetes blog featuring release announcements, community updates, and technical articles.
  - url: https://kubernetes.io/training/
    name: Training
    type: Training
    description: Training resources and certification programs for Kubernetes including CKA, CKAD, and CKS.
  - url: https://kubernetes.io/partners/
    name: Partners
    type: Partners
    description: Directory of Kubernetes partners including cloud providers, vendors, and service providers.
  - url: https://kubernetes.io/releases/
    name: Releases
    type: ChangeLog
    description: Kubernetes release information including version history, release notes, and support timeline.
  - url: https://kubernetes.io/community/
    name: Community
    type: Community
    description: Information about the Kubernetes community including how to get involved and communication channels.
  - url: https://discuss.kubernetes.io/
    name: Discussion Forum
    type: Forum
    description: Official Kubernetes community forum for discussions, announcements, and user support.
  - url: https://kubernetes.slack.com
    name: Slack
    type: Slack
    description: Kubernetes Slack workspace with 170+ channels for real-time community communication.
  - url: https://slack.k8s.io
    name: Slack Signup
    type: Signup
    description: Invitation link to join the Kubernetes Slack workspace.
  - url: https://www.youtube.com/@KubernetesCommunity
    name: YouTube
    type: YouTube
    description: Official Kubernetes Community YouTube channel with SIG meetings, tutorials, and conference talks.
  - url: https://stackoverflow.com/questions/tagged/kubernetes
    name: Stack Overflow
    type: StackOverflow
    description: Kubernetes-related questions and answers on Stack Overflow.
  - url: https://github.com/kubernetes/kubernetes/blob/master/LICENSE
    name: License
    type: License
    description: Kubernetes is licensed under the Apache License 2.0.
  - url: https://kubernetes.io/docs/concepts/security/
    name: Security
    type: Security
    description: Kubernetes security concepts including pod security, network policies, and RBAC.
  - url: https://github.com/kubernetes/kubernetes/security/policy
    name: Security Policy
    type: SecurityPolicy
    description: Information about reporting security vulnerabilities in Kubernetes.
  - url: https://www.cncf.io/projects/kubernetes/
    name: CNCF Project Page
    type: Foundation
    description: Kubernetes graduated project page on the Cloud Native Computing Foundation website.
  - url: https://www.cncf.io/kubeweekly/
    name: KubeWeekly Newsletter
    type: Newsletter
    description: Weekly curated newsletter with Kubernetes news, articles, and community updates.
  - url: https://kubernetes.io/docs/setup/
    name: Getting Started
    type: GettingStarted
    description: Documentation for setting up and configuring Kubernetes clusters.
  - url: https://kubernetes.io/docs/tutorials/
    name: Tutorials
    type: Tutorials
    description: Hands-on tutorials covering various Kubernetes topics and use cases.
  - url: https://kubernetes.io/case-studies/
    name: Case Studies
    type: CaseStudies
    description: Real-world case studies of organizations using Kubernetes in production.
  - url: https://kubernetes.io/community/code-of-conduct/
    name: Code of Conduct
    type: CodeOfConduct
    description: Kubernetes community code of conduct based on the CNCF Code of Conduct, governing participation in Kubernetes project spaces.
  - url: https://kubernetes.io/docs/reference/using-api/deprecation-policy/
    name: Deprecation Policy
    type: DeprecationPolicy
    description: Kubernetes deprecation policy describing the rules for deprecating and removing APIs, features, and flags across versions.
  - type: JSONSchema
    url: json-schema/kubernetes-resource-schema.json
  - type: JSON-LD
    url: json-ld/kubernetes-context.jsonld
created: '2025-06-05'
modified: '2026-04-28'
position: Consuming
description: Kubernetes, also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications. It groups containers that make up an application into logical units for easy management and discovery. Kubernetes builds upon 15 years of experience of running production workloads at Google, combined with best-of-breed ideas and practices from the community.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
