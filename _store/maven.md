---
aid: maven
url: https://raw.githubusercontent.com/api-evangelist/maven/refs/heads/main/apis.yml
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
name: Maven
tags:
- Artifacts
- Build Tools
- Java
- Maven
- Package Management
- Repository
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Maven is a software project management and build automation tool used primarily for Java projects. Maven Central is the default artifact repository for Maven, and Sonatype provides REST APIs for searching and publishing artifacts to Maven Central.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

