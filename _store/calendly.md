---
aid: calendly
name: Calendly
url: https://raw.githubusercontent.com/api-evangelist/calendly/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Appointments
  - Automation
  - Booking
  - Calendars
  - Meetings
  - Scheduling
created: '2026-03-20'
modified: '2026-04-23'
specificationVersion: '0.19'
description: Calendly is a scheduling automation platform that helps individuals, teams, and organizations automate the meeting lifecycle by removing the back-and-forth of scheduling. Their developer platform provides APIs for programmatically managing scheduling workflows, receiving real-time event notifications via webhooks, and embedding scheduling interfaces directly into third-party applications.
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
common:
  - type: Portal
    url: https://developer.calendly.com/
  - type: Documentation
    url: https://developer.calendly.com/api-docs
  - type: Website
    url: https://calendly.com/
  - type: Privacy Policy
    url: https://calendly.com/privacy
  - type: Terms of Service
    url: https://calendly.com/terms
  - type: Blog
    url: https://calendly.com/blog
  - type: Login
    url: https://calendly.com/login
  - type: JSON-LD
    url: json-ld/calendly-context.jsonld
  - type: JSONSchema
    url: json-schema/calendly-event-type-schema.json
  - type: JSONSchema
    url: json-schema/calendly-scheduled-event-schema.json
  - type: JSONSchema
    url: json-schema/calendly-invitee-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
