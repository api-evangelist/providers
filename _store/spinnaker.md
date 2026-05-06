---
aid: spinnaker
name: Spinnaker
description: Spinnaker is an open source multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence. Originally developed at Netflix and Google, Spinnaker provides a deployment platform supporting AWS, GCP, Azure, Kubernetes, and other cloud providers. The Gate API is the primary REST interface for all Spinnaker operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Continuous Delivery
  - Containers
  - DevOps
  - Multi-Cloud
  - Pipelines
url: https://raw.githubusercontent.com/api-evangelist/spinnaker/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spinnaker:spinnaker-gate-api
    name: Spinnaker Gate API
    description: Gate is the Spinnaker API Gateway — the primary REST interface for all Spinnaker operations including application management, pipeline execution, cluster management, and infrastructure discovery. Gate runs on port 8084 and is used by the Spinnaker UI (Deck) as well as external automation scripts and integrations. Supports OAuth 2.0, SAML, LDAP, and X.509 certificate authentication.
    humanURL: https://spinnaker.io/docs/reference/api/
    tags:
      - Applications
      - Clusters
      - Continuous Delivery
      - Deployments
      - Pipelines
    properties:
      - type: Documentation
        url: https://spinnaker.io/docs/reference/api/
      - type: SwaggerUI
        url: https://spinnaker.io/docs/reference/api/docs.html
      - type: GitHubRepository
        url: https://github.com/spinnaker/gate
      - type: OpenAPI
        url: openapi/spinnaker-gate-openapi.yml
      - type: SpectralRules
        url: rules/spinnaker-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/continuous-delivery.yaml
common:
  - type: Website
    url: https://spinnaker.io/
  - type: Documentation
    url: https://spinnaker.io/docs/
  - type: GitHubOrganization
    url: https://github.com/spinnaker
  - type: GitHubRepository
    url: https://github.com/spinnaker/spinnaker
  - type: Community
    url: https://spinnaker.io/community/
  - type: Slack
    url: https://join.spinnaker.io/
  - type: Blog
    url: https://spinnaker.io/blog/
  - type: RoadMap
    url: https://github.com/spinnaker/governance/tree/master/rfc
  - type: ChangeLog
    url: https://spinnaker.io/changelogs/
  - type: OpenAPI
    url: openapi/spinnaker-gate-openapi.yml
  - type: SpectralRules
    url: rules/spinnaker-rules.yml
  - type: Vocabulary
    url: vocabulary/spinnaker-vocabulary.yml
  - type: NaftikoCapabilities
    url: capabilities/continuous-delivery.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
