---
aid: bitbucket
url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/apis.yml
apis:
- aid: bitbucket:bitbucket-cloud-rest-api
  name: Bitbucket Cloud REST API
  description: The REST API for Bitbucket Cloud allows you to build apps using any language exposing operations on repositories, changesets, pull requests, and users.
  humanURL: https://developer.atlassian.com/bitbucket/api/2/reference/
  baseURL: https://api.bitbucket.org/2.0
  tags:
  - Pull Requests
  - Repositories
  - REST
  - Webhooks
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/bitbucket/api/2/reference/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/bitbucket/rest/intro/#authentication
  - type: OpenAPI
    url: openapi/bitbucket-cloud-rest-api-openapi.json
- aid: bitbucket:bitbucket-pipelines-api
  name: Bitbucket Pipelines API
  description: API for managing Bitbucket Pipelines, Atlassian's integrated CI/CD service.
  humanURL: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/
  baseURL: https://api.bitbucket.org/2.0
  tags:
  - Automation
  - CI/CD
  - Deployments
  - Pipelines
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/
name: Bitbucket
tags:
- CI/CD
- Code Collaboration
- DevOps
- Git
- Repository Hosting
- Version Control
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bitbucket is a Git-based source code repository hosting service owned by Atlassian offering both commercial plans and free accounts with unlimited private repositories, along with CI/CD pipelines and code collaboration tools.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

