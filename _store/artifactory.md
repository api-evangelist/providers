---
aid: artifactory
url: https://raw.githubusercontent.com/api-evangelist/artifactory/refs/heads/main/apis.yml
apis:
- name: Artifactory REST API
  description: Comprehensive REST API for managing artifacts, repositories, security, and system configuration.
  image: https://jfrog.com/images/artifactory-api-logo.png
  baseURL: https://artifactory.example.com/artifactory/api
  humanURL: https://jfrog.com/help/r/jfrog-rest-apis/artifactory-rest-apis
  version: v1
  tags:
  - Artifacts
  - Repositories
  - Rest
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-rest-apis/artifactory-rest-apis
  - type: OpenAPI
    url: openapi/artifactory-rest-api-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-rest-apis/authentication
  - type: JSONSchema
    url: json-schema/artifactory-repository-configuration.json
  - type: JSONSchema
    url: json-schema/artifactory-file-info.json
  - type: JSONSchema
    url: json-schema/artifactory-permission-target.json
  contact:
  - type: Support
    url: https://jfrog.com/support/
  - type: Email
    url: mailto:support@jfrog.com
- name: Artifactory Query Language (AQL) API
  description: Advanced search API using a SQL-like query language for finding artifacts.
  baseURL: https://artifactory.example.com/artifactory/api/search/aql
  humanURL: https://jfrog.com/help/r/jfrog-artifactory-documentation/artifactory-query-language
  version: v1
  tags:
  - Aql
  - Query
  - Search
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-artifactory-documentation/artifactory-query-language
  - type: OpenAPI
    url: openapi/artifactory-aql-api-openapi.yml
  - type: Examples
    url: https://jfrog.com/help/r/jfrog-artifactory-documentation/aql-examples
- name: Artifactory Docker Registry API
  description: Docker Registry v2 API for managing Docker images.
  baseURL: https://artifactory.example.com/artifactory/api/docker
  humanURL: https://jfrog.com/help/r/jfrog-artifactory-documentation/docker-registry
  version: v2
  tags:
  - Containers
  - Docker
  - Registry
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-artifactory-documentation/docker-registry
  - type: OpenAPI
    url: openapi/artifactory-docker-registry-api-openapi.yml
- name: Artifactory Build Integration API
  description: API for publishing and managing build information from CI/CD systems.
  baseURL: https://artifactory.example.com/artifactory/api/build
  humanURL: https://jfrog.com/help/r/jfrog-rest-apis/builds
  version: v1
  tags:
  - Builds
  - Ci/Cd
  - Integration
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-rest-apis/builds
  - type: OpenAPI
    url: openapi/artifactory-build-integration-api-openapi.yml
  - type: JSONSchema
    url: json-schema/artifactory-build-info.json
name: JFrog Artifactory
tags:
- Artifacts
- Ci/Cd
- Devops
- Docker Registry
- Maven
- Npm
- Package Management
- Repository
type: Contract
image: https://jfrog.com/images/artifactory-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Universal artifact repository manager supporting all major package formats and build tools.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

