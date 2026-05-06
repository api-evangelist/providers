---
aid: nexus
name: Nexus Repository Manager
description: Nexus Repository Manager by Sonatype is an enterprise-grade artifact repository manager supporting multiple package formats including Maven, npm, Docker, PyPI, NuGet, RubyGems, Helm, Go, and more. It provides a central hub for managing software supply chain components, proxying remote repositories, hosting private artifacts, and grouping repositories. Nexus exposes a comprehensive REST API documented via an OpenAPI/Swagger specification served at `<nexus_url>/service/rest/swagger.json` on each instance.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artifact Management
  - DevOps
  - Docker
  - Maven
  - Npm
  - Package Management
  - Repository Manager
  - Software Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/nexus/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nexus:nexus-rest-api
    name: Nexus Repository Manager REST API
    description: Comprehensive REST API for managing repositories, components, assets, search, security, blob stores, capabilities, tasks, tags, staging, and scripts in Sonatype Nexus Repository Manager 3. The full OpenAPI specification is available from each Nexus instance at `/service/rest/swagger.json` and is explorable via the built-in Swagger UI under System Settings > API.
    humanURL: https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api
    baseURL: https://your-nexus-instance.example.com/service/rest
    tags:
      - Assets
      - Blob Stores
      - Capabilities
      - Components
      - Repositories
      - REST
      - Search
      - Security
      - Staging
      - Tags
      - Tasks
    properties:
      - type: Documentation
        url: https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api
      - type: Authentication
        url: https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api/authentication
      - type: SwaggerUI
        url: https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api/api-reference-documentation
common:
  - type: Website
    url: https://www.sonatype.com/products/nexus-repository
  - type: Documentation
    url: https://help.sonatype.com/repomanager3
  - type: Support
    url: https://support.sonatype.com
  - type: GettingStarted
    url: https://help.sonatype.com/repomanager3/getting-started
  - type: GitHub
    url: https://github.com/sonatype/nexus-public
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
