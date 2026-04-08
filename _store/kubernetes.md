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
  type: GitHubRepositories
- url: https://bsky.app/profile/kubernetes.io
  name: Bluesky
  type: Bluesky
- url: https://kubernetes.io/
  name: Kubernetes
  type: Website
  description: 'null'
- url: https://kubernetes.io/docs/home/
  name: Kubernetes Documentation | Kubernetes
  type: Documentation
  description: 'null'
- url: https://kubernetes.io/blog/
  name: Kubernetes Blog | Kubernetes
  type: Blog
  description: 'null'
- url: https://kubernetes.io/training/
  name: Training | Kubernetes
  type: Training
  description: 'null'
- url: https://kubernetes.io/partners/
  name: Partners | Kubernetes
  type: Partners
  description: 'null'
- url: https://kubernetes.io/releases/
  name: Releases | Kubernetes
  type: ChangeLog
  description: 'null'
created: '2025-06-05'
modified: '2026-04-07'
position: Consuming
description: Kubernetes, also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications. It groups containers that make up an application into logical units for easy management and discovery. Kubernetes builds upon 15 years of experience of running production workloads at Google, combined with best-of-breed ideas and practices from the community.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

