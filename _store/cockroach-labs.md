---
aid: cockroach-labs
url: >-
  https://raw.githubusercontent.com/api-evangelist/cockroach-labs/refs/heads/main/apis.yml
apis:
  - aid: cockroach-labs:cockroach-labs-cloud-api
    name: CockroachDB Cloud API
    tags:
      - Databases
    humanURL: https://www.cockroachlabs.com/docs/api/cloud/v1#get-/api/scim/v2/Groups
    properties:
      - url: https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api
        type: Documentation
      - url: properties/cockroach-labs-cloud-api-openapi.yml
        type: OpenAPI
    description: An API for managing CockroachDB Cloud resources
  - aid: cockroach-labs:cockroach-labs-cluster-api
    name: Cockroach Labs Cluster API
    tags:
      - Databases
    humanURL: https://www.cockroachlabs.com/docs/api/cloud/v1#get-/api/scim/v2/Groups
    properties:
      - url: https://www.cockroachlabs.com/docs/api/cluster/v2
        type: Documentation
      - url: properties/cockroach-labs-cluster-api-openapi.yml
        type: OpenAPI
    description: >-
      REST API for querying information about CockroachDB cluster health, nodes,
      ranges, sessions, and other meta information. For additional details, see
      cockroachlabs.com/docs/stable/cluster-api.  
name: Cockroach Labs
tags:
  - Databases
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.cockroachlabs.com/docs/
    name: CockroachDB Docs
    type: Documentation
  - url: https://www.cockroachlabs.com/pricing/
    name: CockroachDB Pricing | Cockroach Labs
    type: Pricing
  - url: https://www.cockroachlabs.com/blog/
    name: Cockroach Labs Blog | Cockroach Labs
    type: Blog
  - url: https://www.cockroachlabs.com/docs/
    name: CockroachDB Docs
    type: FAQ
  - url: https://www.cockroachlabs.com/docs/stable/architecture/glossary
    name: Glossary
    type: Glossary
  - url: https://www.cockroachlabs.com/events/
    name: Events
    type: Events
  - url: https://www.cockroachlabs.com/support/
    name: CockroachDB support
    type: Support
  - url: https://www.cockroachlabs.com/partners/
    name: Cockroach Labs Partner Ecosystem
    type: Partners
  - url: https://www.cockroachlabs.com/privacy/
    name: >-
      Privacy Policy - CockroachDB Dedicated - Scalable distributed SQL now in a
      few clicks | Cockroach Labs
    type: PrivacyPolicy
  - url: https://www.cockroachlabs.com/security/
    name: >-
      CockroachDB - Scalable distributed SQL now in a few clicks | Cockroach
      Labs
    type: Security
created: '2024-11-24T00:00:00.000Z'
modified: '2024-11-25'
position: Consumer
description: >-
  The Cloud API is a REST interface that allows you programmatic access to
  manage the lifecycle of clusters within your organization.. This document
  pertains to the latest version of the APIs v1 endpoints, 2024-09-16.For more
  detailed coverage of API endpoints for this version and prior verisons, refer
  to the API reference documentation.. To manage clusters and other resources in
  CockroachDB ...
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---