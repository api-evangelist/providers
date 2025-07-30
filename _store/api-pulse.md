---
---
aid: api-pulse
name: API Pulse
type: Contract
description: |-
  This is the APIs.json for the API Pulse, defining the business and technical details for the proposed API.
tags:
- Application Programming Interface
- API
- Pulse

created: '2025-02-10'
modified: '2025-02-17'

url: https://github.com/api-evangelist/api-pulse/blob/main/apis.yml
specificationVersion: '0.19'
apis:

  - aid: api-pulse:api-pulse-publish
    name: API Pulse - Publish
    description: This is the  API for publishing to the API Pulse.
    humanURL: https://github.com/api-evangelist/api-pulse
    tags:
      - Pulse
      - Publish
    properties:
      - type: OpenAPI
        url: openapi/api-pulse-publish-openapi.yml
      - type: GitHubRepository
        url: https://github.com/api-evangelist/api-pulse     
    contact:
      - FN: API Evangelist
        email: info@apievangelist.com            

common:

  - type: Website
    url: http://apievangelist.com

maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com---