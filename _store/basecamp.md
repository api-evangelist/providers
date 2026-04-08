---
aid: basecamp
url: https://raw.githubusercontent.com/api-evangelist/basecamp/refs/heads/main/apis.yml
apis:
- aid: basecamp:basecamp-api
  name: Basecamp API
  tags:
  - Collaboration
  - Project Management
  - REST
  - Team Communication
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://3.basecampapi.com
  humanURL: https://github.com/basecamp/bc3-api
  properties:
  - url: https://github.com/basecamp/bc3-api
    type: Documentation
  - url: openapi/basecamp-api-openapi.yml
    type: OpenAPI
  description: The Basecamp API is a REST API that provides programmatic access to Basecamp's project management and team communication platform. It enables developers to manage projects, to-do lists, messages, documents, schedules, and team members across Basecamp accounts. The API uses OAuth 2.0 for authentication and returns JSON responses, with all requests scoped to an account ID in the base URL.
- aid: basecamp:basecamp-webhooks
  name: Basecamp Webhooks
  tags:
  - Events
  - Notifications
  - Project Management
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://3.basecampapi.com
  humanURL: https://github.com/basecamp/bc3-api/blob/master/sections/webhooks.md
  properties:
  - url: https://github.com/basecamp/bc3-api/blob/master/sections/webhooks.md
    type: Documentation
  - url: asyncapi/basecamp-webhooks-asyncapi.yml
    type: AsyncAPI
  description: Basecamp Webhooks allow developers to receive real-time HTTP notifications when events occur within a Basecamp project. Webhooks are configured per project with an HTTPS payload URL and a list of resource types that should trigger notifications. Basecamp will attempt delivery up to 10 times with exponential backoff before deactivating a webhook if the endpoint does not return a 2xx status code.
- aid: basecamp:basecamp-oauth
  name: Basecamp OAuth
  tags:
  - Authentication
  - Authorization
  - OAuth
  - Security
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://launchpad.37signals.com
  humanURL: https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md
  properties:
  - url: https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md
    type: Documentation
  - url: openapi/basecamp-oauth-openapi.yml
    type: OpenAPI
  description: Basecamp OAuth 2.0 is the required authentication mechanism for accessing all Basecamp APIs. Developers register their applications at launchpad.37signals.com to receive a client ID and client secret, then implement the OAuth authorization code flow to obtain access tokens on behalf of users. Access tokens expire after two weeks and can be refreshed using refresh tokens without requiring the user to re-authorize.
name: Basecamp
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API documentation for Basecamp 4. Contribute to basecamp/bc3-api development by creating an account on GitHub.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

