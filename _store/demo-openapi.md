---
aid: demo-openapi
url: https://raw.githubusercontent.com/api-evangelist/demo-openapi/refs/heads/main/apis.yml
apis:
- aid: apis-io:search-api
  name: APIs.io Search
  tags:
  - Directory
  - Search Engine
  image: https://kinlane-productions2.s3.amazonaws.com/apis-io/apis-io-api-logo.jpg
  baseURL: https://search-api.apis.io
  contact:
  - FN: APIs.io
    email: info@apis.io
  humanURL: https://developer.apis.io/documentation
  properties:
  - url: https://github.com/api-evangelist/search-api/blob/main/team.yml
    type: Teams
  - url: https://github.com/api-evangelist/search-api
    type: GitHubRepository
  - url: https://github.com/api-evangelist/search-api/blob/main/.github/workflows/pipeline.yml
    type: GitHubActions
  - url: https://developer.apis.io/documentation/
    type: Documentation
  - url: https://github.com/api-evangelist/search-api/blob/main/openapi.yml
    type: OpenAPI
  - url: https://www.postman.com/api-evangelist/apis-io-api-evangelist-engine/collection/hn8xpmd/apis-io-search-api
    type: PostmanCollection
  - url: https://us-east-1.console.aws.amazon.com/apigateway/main/apis/ibmwu99rx3/stages
    type: Gateway
  - url: https://www.postman.com/api-evangelist/apis-io-api-evangelist-engine/environment/35240-f6035e55-e9f8-41b8-a2d8-b7ac4cd127bb/production
    type: StagingEnvironment
  - url: https://www.postman.com/api-evangelist/apis-io-api-evangelist-engine/environment/35240-f6035e55-e9f8-41b8-a2d8-b7ac4cd127bb/production
    type: GatewayEnvironment
  - url: https://github.com/api-evangelist/search-api/labels/change-log
    type: ChangeLog
  - url: https://github.com/api-evangelist/search-api/labels/road-map
    type: RoadMap
  - url: https://github.com/api-evangelist/search-api/blob/main/use-cases.yml
    type: UseCases
  - url: https://www.postman.com/api-evangelist/apis-io/monitor/APIs-io-Search---Status1ef6bc29-9da9-4040-b98b-cef03be1155e
    type: Status
  - url: https://www.postman.com/api-evangelist/apis-io/monitor/APIs-io-Search---Performance1ef6bc38-c969-4bd0-815b-25b7d1b1a503
    type: Performance
  description: This is the API to access APIs.io API search engine, from the product management perspective.
name: APIs.io Search
tags:
- Directory
- Search Engine
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-io/apis-io-api-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: This is the contract for the APIs.io search API, allowing for programmatic search of the APIs in the index.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

