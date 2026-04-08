---
aid: zulip
url: https://raw.githubusercontent.com/api-evangelist/zulip/refs/heads/main/apis.yml
apis:
- aid: zulip:rest-api
  name: Zulip REST API
  description: The Zulip REST API powers the Zulip web and mobile apps. It provides programmatic access to messages, streams, users, organizations, and all other Zulip functionality. Anything you can do in Zulip, you can do with the REST API.
  humanURL: https://zulip.com/api/rest
  tags:
  - Messaging
  - REST
  - Team Chat
  properties:
  - type: Documentation
    url: https://zulip.com/api/rest
  - type: Reference
    url: https://zulip.com/api/
- aid: zulip:webhooks
  name: Zulip Webhooks
  description: Zulip supports both incoming webhooks (allowing third-party services to push data to Zulip) and outgoing webhooks (allowing Zulip to send HTTP POST payloads to external services when messages are sent).
  humanURL: https://zulip.com/api/incoming-webhooks-overview
  tags:
  - Events
  - Integrations
  - Webhooks
  properties:
  - type: Documentation
    url: https://zulip.com/api/incoming-webhooks-overview
  - type: Reference
    url: https://zulip.com/api/outgoing-webhooks
name: Zulip
tags:
- Collaboration
- Messaging
- Team Chat
- Webhooks
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-07'
position: Consumer
description: Zulip is an open-source team chat application with a unique topic-based threading model. Zulip's APIs power the web and mobile apps and provide REST endpoints, incoming webhooks, outgoing webhooks, and event-driven integrations to connect Zulip with external services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

