---
aid: atlassian-confluence
url: https://raw.githubusercontent.com/api-evangelist/atlassian-confluence/refs/heads/main/apis.yml
apis:
- aid: atlassian-confluence:confluence-cloud-rest-api
  name: Confluence Cloud REST API
  description: The primary REST API for Confluence Cloud, providing access to content, spaces, users, and more.
  humanURL: https://developer.atlassian.com/cloud/confluence/rest/
  baseURL: https://your-domain.atlassian.net/wiki/rest/api
  tags:
  - Content
  - Pages
  - REST
  - Spaces
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/
  - type: OpenAPI
    url: https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json
  - type: Authentication
    url: https://developer.atlassian.com/cloud/confluence/authentication/
  - type: Getting Started
    url: https://developer.atlassian.com/cloud/confluence/getting-started/
- aid: atlassian-confluence:confluence-cloud-rest-api-v2
  name: Confluence Cloud REST API V2
  description: The next generation REST API for Confluence Cloud with improved performance and new capabilities.
  humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
  baseURL: https://your-domain.atlassian.net/wiki/api/v2
  tags:
  - Content
  - Pages
  - REST
  - Spaces
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
  - type: OpenAPI
    url: https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json
name: Atlassian Confluence
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Management
- Wiki
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Atlassian Confluence is a team collaboration and wiki platform for creating, organizing, and discussing work with your team. It provides APIs for managing content, spaces, pages, users, and search across Confluence Cloud deployments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

