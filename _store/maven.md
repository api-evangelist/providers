---
aid: maven
name: Maven
description: Apache Maven is a software project management and build automation tool used primarily for Java projects. Maven Central is the default artifact repository for Maven, and Sonatype provides REST APIs for searching and publishing artifacts to Maven Central.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/maven/refs/heads/main/apis.yml
tags:
  - Artifacts
  - Build Tools
  - Java
  - Maven
  - Package Management
  - Repository
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: maven:maven-central-search-api
    name: Maven Central Search API
    description: REST API for searching and retrieving artifact metadata from Maven Central Repository. Supports Solr-based queries for finding Java libraries and their versions.
    humanURL: https://central.sonatype.com/
    baseURL: https://search.maven.org/solrsearch
    tags:
      - Artifacts
      - Java
      - Search
    properties:
      - type: Documentation
        url: https://central.sonatype.org/search/rest-api-guide/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/maven/refs/heads/main/openapi/maven-search-openapi.yml
  - aid: maven:maven-central-portal-api
    name: Maven Central Portal Publishing API
    description: API for publishing artifacts to Maven Central through the Sonatype Central Portal. Supports automated deployment of Java libraries and other JVM-based artifacts.
    humanURL: https://central.sonatype.com/
    baseURL: https://central.sonatype.com/api/v1
    tags:
      - Deployment
      - Publishing
      - Upload
    properties:
      - type: Documentation
        url: https://central.sonatype.org/publish/publish-portal-api/
      - type: Authentication
        url: https://central.sonatype.org/publish/generate-token/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/maven/refs/heads/main/openapi/maven-portal-openapi.yml
common:
  - type: Website
    url: https://maven.apache.org
  - type: Documentation
    url: https://maven.apache.org/guides/
  - type: GitHub Organization
    url: https://github.com/apache/maven
  - type: Support
    url: https://maven.apache.org/mailing-lists.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
