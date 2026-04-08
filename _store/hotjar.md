---
aid: hotjar
url: https://raw.githubusercontent.com/api-evangelist/hotjar/refs/heads/main/apis.yml
apis:
- aid: hotjar:rest-api
  name: Hotjar REST API
  tags:
  - Analytics
  - Behavior
  - Heatmaps
  - Surveys
  - User Feedback
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.hotjar.com
  humanURL: https://help.hotjar.com/hc/en-us/articles/36820005914001-Hotjar-API-Reference
  properties:
  - url: https://help.hotjar.com/hc/en-us/articles/36820005914001-Hotjar-API-Reference
    type: Documentation
  - url: openapi/hotjar-rest-api-openapi.yml
    type: OpenAPI
  description: The Hotjar REST API provides programmatic access to Hotjar data and functionality. It allows developers to export survey responses, automate user lookup and deletion requests, and integrate Hotjar data into external tools and workflows. The API uses OAuth client credentials authentication, returns JSON responses, supports cursor-based pagination, and is rate limited to 3000 requests per minute. It is available on Observe and Ask Scale plans.
- aid: hotjar:events-api
  name: Hotjar Events API
  tags:
  - Analytics
  - Events
  - Heatmaps
  - Recordings
  - Surveys
  - Tracking
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://help.hotjar.com/hc/en-us/articles/36819965075473-Events-API-Reference
  properties:
  - url: https://help.hotjar.com/hc/en-us/articles/36819965075473-Events-API-Reference
    type: Documentation
  description: The Hotjar Events API is a client-side JavaScript API that allows developers to send custom events to Hotjar when specific actions take place on a website. These events can be used to filter collected Recordings and Heatmap data, trigger session capture, and target Surveys to appear based on user behavior. Events are sent using the Hotjar tracking code and are available on all pages where the tracking snippet is installed.
- aid: hotjar:identify-api
  name: Hotjar Identify API
  tags:
  - Analytics
  - Attributes
  - Personalization
  - Segmentation
  - Users
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://help.hotjar.com/hc/en-us/articles/36820006120721-Identify-API-Reference
  properties:
  - url: https://help.hotjar.com/hc/en-us/articles/36820006120721-Identify-API-Reference
    type: Documentation
  description: The Hotjar Identify API is a client-side JavaScript API that allows developers to pass user data to Hotjar, saving it as User Attributes. These attributes enable advanced filtering and segmentation of Hotjar data such as Recordings, Heatmaps, and Surveys. The Identify API must be called before the Events API in the execution order. It is used via the Hotjar tracking code on pages where the JavaScript snippet is installed.
- aid: hotjar:javascript-sdk
  name: Hotjar JavaScript SDK
  tags:
  - Analytics
  - Browser
  - JavaScript
  - SDK
  - Tracking
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://github.com/hotjar/hotjar-js
  properties:
  - url: https://github.com/hotjar/hotjar-js
    type: Documentation
  description: The Hotjar JavaScript SDK (@hotjar/browser) is an npm package that provides a programmatic interface for integrating Hotjar directly into JavaScript applications. It allows developers to initialize Hotjar with a site ID, identify users, and send custom events without manually embedding the tracking script. The SDK supports modern JavaScript frameworks including React, Vue, and Angular, and provides methods for all Hotjar client-side APIs including identify and event tracking.
name: Hotjar
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Hotjar is a behavior analytics and user feedback platform that helps businesses understand how users interact with their website through heatmaps, session recordings, surveys, and feedback widgets.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

