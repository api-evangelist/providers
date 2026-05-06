---
aid: microsoft-yammer
name: Microsoft Yammer
description: APIs for Yammer (now Viva Engage) enterprise social networking platform providing access to messages, groups, users, and networks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise Social
  - Microsoft
  - Social Networking
  - Viva Engage
  - Yammer
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/microsoft-yammer/refs/heads/main/apis.yml
apis:
  - aid: microsoft-yammer:rest-api
    name: Yammer REST API
    tags:
      - Enterprise Social
      - Social Networking
      - Viva Engage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.yammer.com/api/v1/
    humanURL: https://learn.microsoft.com/en-us/rest/api/yammer/rest-api-rate-limits
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/yammer/rest-api-rate-limits
        type: Documentation
    description: The Yammer REST API (now Viva Engage) provides access to enterprise social networking features including messages, groups, users, and networks. Developers can post messages, manage group memberships, search content, and integrate Yammer's social collaboration features into custom applications.
common:
  - type: Portal
    url: https://engage.cloud.microsoft/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/rest/api/yammer/oauth-2
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
