---
aid: nexus
url: https://raw.githubusercontent.com/api-evangelist/nexus/refs/heads/main/apis.yml
apis:
- aid: nexus:nexus-rest-api
  name: Nexus Repository Manager REST API
  description: Comprehensive REST API for managing repositories, components, assets, and configurations.
  humanURL: https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api
  baseURL: https://your-nexus-instance.com/service/rest
  tags:
  - Components
  - Repositories
  - REST
  - Security
  properties:
  - type: Documentation
    url: https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api
  - type: Authentication
    url: https://help.sonatype.com/repomanager3/integrations/rest-and-integration-api/authentication
name: Nexus Repository Manager
tags:
- Artifact Management
- DevOps
- Docker
- Maven
- Npm
- Package Management
- Repository Manager
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Nexus Repository Manager by Sonatype is an enterprise-grade artifact repository manager supporting multiple formats including Maven, npm, Docker, PyPI, and more. It provides a central hub for managing software supply chain components.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

