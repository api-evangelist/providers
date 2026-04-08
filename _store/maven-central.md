---
aid: maven-central
url: https://raw.githubusercontent.com/api-evangelist/maven-central/refs/heads/main/apis.yml
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
name: Maven Central
tags:
- Artifacts
- Java
- JVM
- Maven
- Package Management
- Repository
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Maven Central is the central repository for Java and other JVM-based artifacts, operated by Sonatype. It provides a REST API for searching artifact metadata and a publishing API for deploying open source libraries to the repository.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

