---
aid: npr
url: https://raw.githubusercontent.com/api-search/news/main/_apis/npr/apis.md
apis:
  - aid: npr:listening
    name: NPR Listening
    tags: []
    contact:
      - FN: ''
        url: ''
        email: ''
    overlays:
      - url: >-

          overlays/https://listening.api.npr.org/v2/swagger.json-openapi-search.yml
        type: APIs.io Search
    description: Audio recommendations tailored to a user's preferences.
  - aid: npr:station
    name: NPR Station
    tags: []
    contact:
      - FN: ''
        url: ''
        email: ''
    overlays: []
    description: NPR Station information.
  - aid: npr:identity
    name: NPR Identity
    tags: []
    contact:
      - FN: ''
        url: ''
        email: ''
    overlays: []
    description: User management API.
  - aid: npr:authorization
    name: NPR Authorization
    tags: []
    contact:
      - FN: ''
        url: ''
        email: ''
    overlays:
      - url: >-

          overlays/https://authorization.api.npr.org/v2/swagger.json-openapi-search.yml
        type: APIs.io Search
    description: API Authorization.
name: NPR
tags:
  - News
  - Radio
type: Contract
access: 3rd-Party
created: 2024/04/14
modified: '2025-01-02'
position: Consuming
description: |-

  National Public Radio (NPR) APIs. The APIs support station finding,
  authentication, user management and listening.
maintainers:
  - FN: Steven Willmott
    url: http://timewarp.com
    email: steve@timewarp.io
specificationVersion: '0.18'

---