---
aid: maven-central
name: Maven Central
description: Maven Central is the central repository for Java and other JVM-based artifacts, operated by Sonatype. It provides a REST API for searching artifact metadata and a publishing API for deploying open source libraries to the repository.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/maven-central/refs/heads/main/apis.yml
tags:
  - Artifacts
  - Java
  - JVM
  - Maven
  - Package Management
  - Repository
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: maven-central:maven-central-search-api
    name: Maven Central Search API
    description: REST API for searching and retrieving metadata about artifacts in Maven Central. Supports Solr-based queries for finding Java libraries, their versions, and download statistics.
    humanURL: https://central.sonatype.org/search/
    baseURL: https://search.maven.org/solrsearch
    tags:
      - Artifacts
      - Metadata
      - Search
    properties:
      - type: Documentation
        url: https://central.sonatype.org/search/rest-api-guide/
      - type: Authentication
        url: https://central.sonatype.org/publish/generate-token/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/maven-central/refs/heads/main/openapi/maven-central-search-openapi.yml
  - aid: maven-central:central-portal-api
    name: Central Portal Publishing API
    description: API for publishing artifacts to Maven Central through the Sonatype Central Portal, supporting automated deployment pipelines.
    humanURL: https://central.sonatype.com/
    baseURL: https://central.sonatype.com/api/v1
    tags:
      - Deployment
      - Publishing
      - Upload
    properties:
      - type: Documentation
        url: https://central.sonatype.org/publish/publish-portal-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/maven-central/refs/heads/main/openapi/maven-central-portal-openapi.yml
common:
  - type: Portal
    url: https://central.sonatype.com/
  - type: Getting Started
    url: https://central.sonatype.org/publish/publish-guide/
  - type: Blog
    url: https://blog.sonatype.com/
  - type: Status
    url: https://status.maven.org/
  - type: Terms of Service
    url: https://central.sonatype.org/publish/terms/
  - type: GitHub Organization
    url: https://github.com/sonatype
  - type: Support
    url: https://central.sonatype.org/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
