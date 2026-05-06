---
aid: spacelift
name: Spacelift
description: Spacelift is an infrastructure-as-code (IaC) orchestration platform that combines AI-assisted deployments, GitOps pipelines, and policy-as-code governance. It supports Terraform, OpenTofu, Pulumi, CloudFormation, Kubernetes, and Ansible. Key features include drift detection, OPA-based policies, self-service blueprints, dynamic credentials, and multi-tenancy. Available as fully managed SaaS and FedRAMP-authorized self-hosted.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Infrastructure as Code
  - FinOps
  - DevOps
  - Platform Engineering
  - Terraform
  - GitOps
url: https://raw.githubusercontent.com/api-evangelist/spacelift/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: spacelift:spacelift-graphql
    name: Spacelift GraphQL API
    description: Spacelift exposes a GraphQL API for programmatic control of all platform resources including stacks, runs, policies, contexts, worker pools, modules, and blueprints. Authentication uses JWT tokens obtained by exchanging a Spacelift API key ID and secret via the apiKeyUser mutation. The endpoint is account-specific at https://{account}.app.spacelift.io/graphql.
    humanURL: https://spacelift.io/
    baseURL: https://{account}.app.spacelift.io/graphql
    tags:
      - Infrastructure as Code
      - DevOps
      - Platform Engineering
      - Terraform
      - GraphQL
    properties:
      - type: Documentation
        url: https://docs.spacelift.io/
      - type: GraphQL
        url: https://docs.spacelift.io/integrations/api
      - type: Getting Started
        url: https://docs.spacelift.io/
      - type: GitHubRepository
        url: https://github.com/spacelift-io/spacectl
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/spacelift/refs/heads/main/json-schema/spacelift-stack-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/spacelift/refs/heads/main/json-structure/spacelift-stack-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/spacelift/refs/heads/main/json-ld/spacelift-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/spacelift/refs/heads/main/vocabulary/spacelift-vocabulary.yml
common:
  - type: Website
    url: https://spacelift.io/
  - type: Documentation
    url: https://docs.spacelift.io/
  - type: GraphQL
    url: https://docs.spacelift.io/integrations/api
  - type: GitHub
    url: https://github.com/spacelift-io
  - type: Pricing
    url: https://spacelift.io/pricing
  - type: Blog
    url: https://spacelift.io/blog
  - type: Changelog
    url: https://spacelift.io/changelog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
