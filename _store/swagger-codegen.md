---
aid: swagger-codegen
name: Swagger Codegen
description: Swagger Codegen is an open-source template-driven code generation tool that automatically generates client libraries, server stubs, and API documentation from OpenAPI Specification definitions. It supports 40+ client languages and 20+ server frameworks. Available as a CLI, Docker image, Maven/Gradle plugin, and online REST API at generator3.swagger.io.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Client Libraries
  - Code Generation
  - Open Source
  - OpenAPI
  - SDK
url: https://raw.githubusercontent.com/api-evangelist/swagger-codegen/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: swagger-codegen:swagger-generator-api
    name: Swagger Generator API
    description: The Swagger Generator online API at generator3.swagger.io provides REST endpoints for generating client SDKs, server stubs, and documentation artifacts from OpenAPI V2 and V3 specifications. Supports 40+ client and 20+ server generator targets with configurable options.
    humanURL: https://generator3.swagger.io/
    baseURL: https://generator3.swagger.io
    tags:
      - Client Libraries
      - Code Generation
      - Generator
      - OpenAPI
      - SDK
      - Server Stubs
    properties:
      - type: Documentation
        url: https://github.com/swagger-api/swagger-codegen/wiki
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/swagger-codegen/refs/heads/main/openapi/swagger-generator-openapi.yml
      - type: OpenAPI Source
        url: https://generator3.swagger.io/openapi.json
      - type: GitHub Repository
        url: https://github.com/swagger-api/swagger-codegen
  - aid: swagger-codegen:swagger-codegen-cli
    name: Swagger Codegen CLI
    description: The Swagger Codegen command-line interface for generating code artifacts locally. Available as a JAR file and Docker image. Supports the same generators as the online API with additional template customization.
    humanURL: https://github.com/swagger-api/swagger-codegen#getting-started
    tags:
      - CLI
      - Code Generation
      - Command Line
      - Docker
    properties:
      - type: Documentation
        url: https://github.com/swagger-api/swagger-codegen/wiki
      - type: Getting Started
        url: https://github.com/swagger-api/swagger-codegen#getting-started
      - type: Docker
        url: https://hub.docker.com/r/swaggerapi/swagger-codegen-cli-v3
      - type: Package
        url: https://mvnrepository.com/artifact/io.swagger.codegen.v3/swagger-codegen-cli
common:
  - type: Portal
    url: https://swagger.io/tools/swagger-codegen/
  - type: Documentation
    url: https://github.com/swagger-api/swagger-codegen/wiki
  - type: Website
    url: https://swagger.io/
  - type: GitHub Organization
    url: https://github.com/swagger-api
  - type: GitHub Repository
    url: https://github.com/swagger-api/swagger-codegen
  - type: Issues
    url: https://github.com/swagger-api/swagger-codegen/issues
  - type: Releases
    url: https://github.com/swagger-api/swagger-codegen/releases
  - type: License
    url: https://github.com/swagger-api/swagger-codegen/blob/master/LICENSE
  - type: Docker
    url: https://hub.docker.com/r/swaggerapi/swagger-codegen-cli-v3
  - type: Maven Plugin
    url: https://mvnrepository.com/artifact/io.swagger.codegen.v3/swagger-codegen-maven-plugin
  - type: Gradle Plugin
    url: https://plugins.gradle.org/plugin/org.hidetake.swagger.generator
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
