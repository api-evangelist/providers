---
aid: calendly
url: https://raw.githubusercontent.com/api-evangelist/calendly/refs/heads/main/apis.yml
apis:
- aid: calendly:scheduling-api
  name: Calendly Scheduling API
  tags:
  - Appointments
  - Automation
  - Booking
  - Calendars
  - Meetings
  - Scheduling
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.calendly.com
  humanURL: https://developer.calendly.com/api-docs
  properties:
  - url: https://developer.calendly.com/api-docs
    type: Documentation
  - url: openapi/calendly-scheduling-api-openapi.yml
    type: OpenAPI
  description: The Calendly Scheduling API (v2) is a RESTful API that allows developers to programmatically manage scheduling workflows. It provides endpoints for managing users, organizations, event types, scheduled events, invitees, and routing forms. The API uses JSON for request and response bodies, standard HTTP methods, and supports authentication via personal access tokens and OAuth 2.1.
- aid: calendly:webhook-api
  name: Calendly Webhook API
  tags:
  - Events
  - Notifications
  - Scheduling
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.calendly.com
  humanURL: https://developer.calendly.com/api-docs
  properties:
  - url: https://developer.calendly.com/api-docs
    type: Documentation
  - url: asyncapi/calendly-webhook-api-asyncapi.yml
    type: AsyncAPI
  description: The Calendly Webhook API enables developers to receive real-time notifications when scheduling events occur in Calendly. By creating webhook subscriptions, applications can automatically receive data whenever invitees schedule, cancel, or reschedule meetings. This eliminates the need for polling the API and allows for event-driven integrations that respond immediately to changes in scheduling activity.
- aid: calendly:embed-api
  name: Calendly Embed API
  tags:
  - Embedding
  - Scheduling
  - Web Components
  - Widgets
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.calendly.com/
  properties:
  - url: https://developer.calendly.com/
    type: Documentation
  description: The Calendly Embed API allows developers to integrate Calendly scheduling pages directly into their websites and applications. It supports inline embeds, popup widgets, and popup text options, giving developers flexibility in how they present scheduling interfaces to users. The Embed API enables customization of the embedded experience and provides JavaScript callbacks for tracking when events are scheduled, allowing seamless integration of Calendly booking flows within third-party applications.
name: Calendly
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Calendly is a scheduling automation platform that helps individuals, teams, and organizations automate the meeting lifecycle by removing the back-and-forth of scheduling.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

