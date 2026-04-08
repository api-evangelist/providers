---
aid: medium
url: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/apis.yml
apis:
- aid: medium:rest-api
  name: Medium REST API
  tags:
  - Blogging
  - Content
  - Posts
  - Publications
  - Publishing
  - Social Media
  - Writing
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.medium.com/v1
  humanURL: https://github.com/Medium/medium-api-docs
  properties:
  - url: https://github.com/Medium/medium-api-docs
    type: Documentation
  - type: OpenAPI
    url: openapi/medium-rest-api-openapi.yml
  description: The Medium REST API provides programmatic access to the Medium online publishing platform. Developers can authenticate users via OAuth2, retrieve user profile details, list publications a user is associated with, create posts on a user's profile or within a publication, and upload images. The API is JSON-based with all requests made over HTTPS to endpoints under api.medium.com/v1, enabling integrations that automate content publishing workflows on Medium.
- aid: medium:oauth2
  name: Medium OAuth2 API
  tags:
  - Authentication
  - Authorization
  - Identity
  - OAuth
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://medium.com/m/oauth
  humanURL: https://github.com/Medium/medium-api-docs#2-authentication
  properties:
  - url: https://github.com/Medium/medium-api-docs#2-authentication
    type: Documentation
  - type: OpenAPI
    url: openapi/medium-oauth2-openapi.yml
  description: The Medium OAuth2 API enables third-party applications to authenticate and authorize users to act on their behalf on the Medium platform. Applications redirect users to Medium's authorization endpoint to obtain an authorization code, which is then exchanged for an access token and refresh token. The OAuth2 flow supports scoped permissions including basicProfile, publishPost, and listPublications, allowing developers to request only the level of access their application requires.
name: Medium
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Documentation for Medium's OAuth2 API. Contribute to Medium/medium-api-docs development by creating an account on GitHub.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

