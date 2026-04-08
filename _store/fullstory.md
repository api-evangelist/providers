---
aid: fullstory
url: https://raw.githubusercontent.com/api-evangelist/fullstory/refs/heads/main/apis.yml
apis:
- aid: fullstory:server-api
  name: FullStory Server API
  tags:
  - Analytics
  - Digital Experience
  - Events
  - Session Replay
  - Users
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fullstory.com
  humanURL: https://developer.fullstory.com/server/getting-started/
  properties:
  - url: https://developer.fullstory.com/server/getting-started/
    type: Documentation
  - url: openapi/fullstory-server-api-openapi.yml
    type: OpenAPI
  description: The FullStory Server API is a RESTful API that enables developers to programmatically send user and event data to FullStory. It supports creating and updating individual users, batch importing users, sending server-side events, and batch importing events. The API uses JSON for request and response bodies and authenticates via API keys. Developers can use it to enrich FullStory session data with server-side context that is not available in the browser or mobile app.
- aid: fullstory:segments-export-api
  name: FullStory Segments Export API
  tags:
  - Analytics
  - Data Export
  - Digital Experience
  - Segments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fullstory.com
  humanURL: https://developer.fullstory.com/server/v1/segments/create-segment-export/
  properties:
  - url: https://developer.fullstory.com/server/v1/segments/create-segment-export/
    type: Documentation
  - url: openapi/fullstory-segments-export-api-openapi.yml
    type: OpenAPI
  description: 'The FullStory Segments Export API provides an asynchronous workflow for downloading captured event data from FullStory. Developers can initiate export jobs to aggregate segment data, query for the status of running jobs, and retrieve download URLs for completed exports. Two types of segment data are available for export: individuals matching a segment and events performed by those individuals.'
- aid: fullstory:sessions-api
  name: FullStory Sessions API
  tags:
  - Analytics
  - Digital Experience
  - Session Replay
  - Sessions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fullstory.com
  humanURL: https://developer.fullstory.com/server/getting-started/
  properties:
  - url: https://developer.fullstory.com/server/getting-started/
    type: Documentation
  - url: openapi/fullstory-sessions-api-openapi.yml
    type: OpenAPI
  description: The FullStory Sessions API allows developers to retrieve session replay URLs for specific users. By querying with a user email address or user ID, the API returns a list of session URLs that can be used to view recorded sessions in the FullStory platform. This is particularly useful for building integrations that link customer support tickets, CRM records, or other tools directly to relevant FullStory session replays.
- aid: fullstory:webhooks-api
  name: FullStory Webhooks API
  tags:
  - Events
  - Notifications
  - Segments
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fullstory.com
  humanURL: https://developer.fullstory.com/destinations/v1/webhooks/getting-started/
  properties:
  - url: https://developer.fullstory.com/destinations/v1/webhooks/getting-started/
    type: Documentation
  - url: openapi/fullstory-webhooks-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/fullstory-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The FullStory Webhooks API enables developers to create, update, retrieve, and manage webhook endpoints that receive real-time notifications from FullStory. Supported event types include segment creation, segment threshold alerts, and custom event notifications. Webhooks allow event-driven integrations that respond immediately to behavioral signals detected by FullStory, eliminating the need for polling and enabling automated workflows based on user activity patterns.
- aid: fullstory:browser-sdk
  name: FullStory Browser SDK
  tags:
  - Browser
  - Custom Events
  - Data Capture
  - JavaScript
  - Session Replay
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.fullstory.com/
  properties:
  - url: https://developer.fullstory.com/
    type: Documentation
  description: The FullStory Browser SDK is a JavaScript library that enables developers to manage FullStory data capture on websites, retrieve deep links to session replays, and send custom events. It provides functions for identifying users, setting user properties, tracking custom events with the FS.event API, and generating session replay URLs for integration with other platforms.
name: Fullstory
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Once you've created an API Key, you're ready to start sending data to Fullstory.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

