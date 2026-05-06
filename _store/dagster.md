---
aid: dagster
name: Dagster
segments:
  - Workflows
description: Dagster is a data orchestration platform centered on software-defined assets with strong observability and testing support. It exposes a GraphQL API for programmatic interaction with Dagster instances and a REST API for reporting external asset materializations, checks, and observations from outside pipelines.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Engineering
  - Data Orchestration
  - Data Pipelines
  - ETL
  - Workflows
  - Assets
  - GraphQL
created: '2026-03-03'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/dagster/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: dagster:graphql-api
    name: Dagster GraphQL API
    description: The Dagster GraphQL API allows clients to interact with Dagster programmatically. It can be used to query information about Dagster runs, retrieve metadata about repositories, jobs, and ops, and launch runs. The GraphQL endpoint is served by the webserver at the /graphql route.
    humanURL: https://docs.dagster.io/api/graphql
    tags:
      - Data Orchestration
      - GraphQL
      - Jobs
      - Runs
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.dagster.io/api/graphql
      - type: GraphQL Playground
        url: https://docs.dagster.io/api/graphql
  - aid: dagster:external-assets-rest-api
    name: Dagster External Assets REST API
    description: The Dagster External Assets REST API provides endpoints to report asset materializations, asset check evaluations, and asset observations for external assets back to Dagster. This allows you to notify Dagster that an external asset has been updated and include metadata about the event.
    humanURL: https://docs.dagster.io/api/rest-apis/external-assets-rest-api
    tags:
      - Assets
      - Data Orchestration
      - Materializations
      - Observations
      - REST API
    properties:
      - type: Documentation
        url: https://docs.dagster.io/api/rest-apis/external-assets-rest-api
      - type: OpenAPI
        url: openapi/dagster-external-assets-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/asset-materialization.json
      - type: JSONSchema
        url: json-schema/asset-check.json
      - type: JSONSchema
        url: json-schema/asset-observation.json
      - type: Rules
        url: rules/dagster-external-assets-rest-api-rules.yml
      - type: Capabilities
        url: capabilities/dagster-external-assets-rest-api-capabilities.yml
common:
  - type: Portal
    url: https://dagster.cloud/
  - type: Sign Up
    url: https://dagster.cloud/signup
  - type: Documentation
    url: https://docs.dagster.io/
  - type: API Reference
    url: https://docs.dagster.io/api
  - type: Getting Started
    url: https://docs.dagster.io/getting-started/quickstart
  - type: Blog
    url: https://dagster.io/blog
  - type: Change Log
    url: https://docs.dagster.io/about/changelog
  - type: Pricing
    url: https://dagster.io/pricing
  - type: Support
    url: https://dagster.io/support
  - type: Community
    url: https://dagster.io/community
  - type: Slack
    url: https://dagster.io/slack
  - type: GitHub Organization
    url: https://github.com/dagster-io
  - type: GitHub Repository
    url: https://github.com/dagster-io/dagster
  - type: Integrations
    url: https://docs.dagster.io/integrations/libraries
  - type: Python SDK
    url: https://pypi.org/project/dagster/
  - type: Privacy Policy
    url: https://dagster.io/privacy
  - type: Terms of Service
    url: https://dagster.io/terms
  - type: Security
    url: https://dagster.io/security
  - type: About
    url: https://dagster.io/company/about-us
  - type: Contact
    url: https://dagster.io/contact
  - type: JSON-LD
    url: json-ld/dagster-context.jsonld
  - type: Vocabulary
    url: vocabulary/dagster-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
xType: opensource
---
