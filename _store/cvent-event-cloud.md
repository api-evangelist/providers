---
aid: cvent-event-cloud
url: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/apis.yml
apis:
- name: Cvent REST API
  description: RESTful API for managing events, registrations, attendees, and event data.
  image: https://www.cvent.com/sites/default/files/cvent-logo.png
  humanURL: https://api.cvent.com
  baseURL: https://api.cvent.com/ea
  tags:
  - Attendees
  - Events
  - Registration
  - REST
  properties:
  - type: Documentation
    url: https://api.cvent.com/docs
  - type: Authentication
    url: https://api.cvent.com/docs/authentication
  - type: OpenAPI
    url: https://api.cvent.com/swagger
- name: Cvent Registration API
  description: API for managing event registrations, attendee information, and registration forms.
  image: https://www.cvent.com/sites/default/files/cvent-logo.png
  humanURL: https://api.cvent.com/registration
  baseURL: https://api.cvent.com/ea/registration
  tags:
  - Attendees
  - Forms
  - Registration
  properties:
  - type: Documentation
    url: https://api.cvent.com/docs/registration
  - type: Swagger
    url: https://api.cvent.com/swagger/registration
- name: Cvent Event API
  description: API for creating and managing events, sessions, speakers, and event details.
  image: https://www.cvent.com/sites/default/files/cvent-logo.png
  humanURL: https://api.cvent.com/events
  baseURL: https://api.cvent.com/ea/events
  tags:
  - Events
  - Sessions
  - Speakers
  properties:
  - type: Documentation
    url: https://api.cvent.com/docs/events
  - type: Rate Limits
    url: https://api.cvent.com/docs/rate-limits
- name: Cvent Webhook API
  description: Webhook system for real-time event notifications and data synchronization.
  image: https://www.cvent.com/sites/default/files/cvent-logo.png
  humanURL: https://api.cvent.com/webhooks
  baseURL: https://api.cvent.com/webhooks
  tags:
  - Notifications
  - Real-Time
  - Webhooks
  properties:
  - type: Documentation
    url: https://api.cvent.com/docs/webhooks
  - type: Webhook Events
    url: https://api.cvent.com/docs/webhook-events
name: Cvent Event Cloud
tags:
- Event Management
- Event Marketing
- Events
- Hybrid Events
- Registration
- Venue Selection
- Virtual Events
type: Contract
image: https://www.cvent.com/sites/default/files/cvent-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Cvent Event Cloud provides comprehensive event management solutions including registration, venue selection, mobile apps, onsite solutions, and virtual/hybrid event capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

