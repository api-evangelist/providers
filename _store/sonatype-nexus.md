---
aid: sonatype-nexus
name: Sonatype Nexus
description: Sonatype Nexus Repository Manager provides a comprehensive REST API for managing software artifacts, repositories, and components across the software development lifecycle. It supports popular formats including Maven, npm, Docker, PyPI, NuGet, RubyGems, Go, Helm, APT, Yum, Cargo, Terraform, R, Swift, and more. The API covers repository configuration, component and asset management, security, blob stores, search, tasks, cleanup policies, staging, and system administration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artifact Management
  - DevOps
  - Package Management
  - Repository
  - Maven
  - npm
  - Docker
  - Software Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/sonatype-nexus/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sonatype-nexus:nexus-repository-api
    name: Nexus Repository API
    description: REST API for Sonatype Nexus Repository Manager (v3.91.0) providing 238 endpoints for managing repositories across many formats (Maven, npm, Docker, PyPI, NuGet, RubyGems, Go, Cargo, Helm, Terraform, R, APT, Yum, Raw, Swift, and more), components, assets, blob stores (file, S3, Azure, GCS), security (users, roles, privileges, LDAP, SAML, Crowd), search, tasks, cleanup policies, staging, and system administration. Authentication uses HTTP Basic Auth or User Tokens.
    humanURL: https://help.sonatype.com/en/api-reference.html
    baseURL: https://{nexus-host}/service/rest
    tags:
      - Artifact Management
      - Components
      - Repository
      - Security
      - Search
      - Tasks
      - Blob Store
      - Maven
      - npm
      - Docker
    properties:
      - type: Documentation
        url: https://help.sonatype.com/en/api-reference.html
      - type: Reference
        url: https://help.sonatype.com/en/rest-and-integration-api.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sonatype-nexus/refs/heads/main/openapi/sonatype-nexus-repository-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/sonatype-nexus/refs/heads/main/json-schema/sonatype-nexus-component-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/sonatype-nexus/refs/heads/main/json-schema/sonatype-nexus-repository-schema.json
    contact:
      - FN: Sonatype Support
        url: https://support.sonatype.com/
common:
  - type: Portal
    url: https://www.sonatype.com/products/sonatype-nexus-repository
  - type: Documentation
    url: https://help.sonatype.com/en/sonatype-nexus-repository.html
  - type: Website
    url: https://www.sonatype.com/
  - type: GitHub
    url: https://github.com/sonatype-nexus-community
  - type: Blog
    url: https://www.sonatype.com/blog
  - type: Changelog
    url: https://help.sonatype.com/en/release-notes.html
  - type: Support
    url: https://support.sonatype.com/
  - type: Pricing
    url: https://www.sonatype.com/products/sonatype-nexus-repository/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
