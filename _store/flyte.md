---
aid: flyte
name: Flyte
description: Flyte is a Kubernetes-native, open-source workflow orchestration platform for machine learning, data, and analytics pipelines. It provides reproducibility, type safety, strong versioning of tasks and workflows, and a multi-tenant control plane with native first-class scheduling on Kubernetes. Flyte is a Cloud Native Computing Foundation (CNCF) incubating project. Beyond the Python and Go SDKs, Flyte exposes a JSON-over-HTTP REST control-plane API (the Flyte Admin API) generated from the flyteidl protocol buffer definitions via gRPC-Gateway, which is used to register and manage projects, tasks, workflows, and launch plans, to create and inspect executions, to receive lifecycle events, and to read and write matchable attribute overrides.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/flyte/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - CNCF
  - Data Orchestration
  - Kubernetes
  - Machine Learning
  - Workflow Automation
apis:
  - aid: flyte:flyte-admin-api
    name: Flyte Admin API
    description: The Flyte Admin API is the control-plane REST API exposed by the flyteadmin service. It is generated from the flyteidl protocol buffer definitions via gRPC-Gateway and provides JSON over HTTP access to the same operations exposed via gRPC. The API is used to register and manage projects, tasks, workflows, and launch plans, to create and inspect workflow, node, and task executions, to receive lifecycle events, to proxy data to and from upstream object stores, and to read and write matchable attribute overrides at the project, domain, and workflow levels. The same REST API powers the Flyte Console UI and is the primary programmatic interface for operating a Flyte cluster.
    humanURL: https://docs.flyte.org
    baseURL: http://localhost:30080
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Workflow Orchestration
      - Control Plane
      - Executions
      - Launch Plans
      - Projects
      - Tasks
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.flyte.org
      - type: OpenAPI
        url: openapi/flyte-admin-api-openapi.yml
      - type: GitHubRepository
        url: https://github.com/flyteorg/flyte
      - type: SourceSwagger
        url: https://raw.githubusercontent.com/flyteorg/flyteidl/master/gen/pb-go/flyteidl/service/admin.swagger.json
common:
  - type: Website
    url: https://flyte.org
  - type: Documentation
    url: https://docs.flyte.org
  - type: GitHubRepository
    url: https://github.com/flyteorg/flyte
  - type: GitHubOrganization
    url: https://github.com/flyteorg
  - type: Blog
    url: https://flyte.org/blog
  - type: Community
    url: https://flyte.org/community
  - type: Slack
    url: https://slack.flyte.org
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
